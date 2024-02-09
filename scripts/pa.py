import torch
from modules import shared, devices, sd_hijack_clip
from modules.script_callbacks import on_ui_settings

OPT_NAME = "disable_mean_in_calclate_cond"
       
def ext_on_ui_settings():
    # [setting_name], [default], [label], [component(blank is checkbox)], [component_args]debug_level_choices = []
    negpip_options = [
        (OPT_NAME, False, "Disable taking the average value when calculating cond/uncond")
    ]
    section = ('Prevent Artifact', "Prevent Artifact")

    for cur_setting_name, *option_info in negpip_options:
        shared.opts.add_option(cur_setting_name, shared.OptionInfo(*option_info, section=section))

on_ui_settings(ext_on_ui_settings)

def process_tokens(self, remade_batch_tokens, batch_multipliers):
    """
    sends one single prompt chunk to be encoded by transformers neural network.
    remade_batch_tokens is a batch of tokens - a list, where every element is a list of tokens; usually
    there are exactly 77 tokens in the list. batch_multipliers is the same but for multipliers instead of tokens.
    Multipliers are used to give more or less weight to the outputs of transformers network. Each multiplier
    corresponds to one token.
    """
    tokens = torch.asarray(remade_batch_tokens).to(devices.device)

    # this is for SD2: SD1 uses the same token for padding and end of text, while SD2 uses different ones.
    if self.id_end != self.id_pad:
        for batch_pos in range(len(remade_batch_tokens)):
            index = remade_batch_tokens[batch_pos].index(self.id_end)
            tokens[batch_pos, index+1:tokens.shape[1]] = self.id_pad

    z = self.encode_with_transformers(tokens)

    pooled = getattr(z, 'pooled', None)

    # restoring original mean is likely not correct, but it seems to work well to prevent artifacts that happen otherwise
    batch_multipliers = torch.asarray(batch_multipliers).to(devices.device)
    original_mean = z.mean()
    z = z * batch_multipliers.reshape(batch_multipliers.shape + (1,)).expand(z.shape)
    new_mean = z.mean()
    if hasattr(shared.opts, OPT_NAME):
        if not getattr(shared.opts, OPT_NAME, False):
            z = z * (original_mean / new_mean)
    else:
        z = z * (original_mean / new_mean)

    if pooled is not None:
        z.pooled = pooled

    return z

sd_hijack_clip.FrozenCLIPEmbedderWithCustomWordsBase.process_tokens = process_tokens
