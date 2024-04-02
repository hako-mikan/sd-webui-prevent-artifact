# Prevent Artifact
This is an auxiliary script for the Stable Diffusion Web-UI. It prevents image corruption that occurs in the SDXL series.
Stable Diffusion Web-UI用の補助スクリプトです。SDXL系統で発生する画像の破綻を防ぎます。

# Overview/概要
This script prevents the corruption of generated images that started being reported around the time animagine-V3 became popular. For more details, please refer [here](https://civitai.com/articles/4044).  
Animagine XL V3が流行りだした頃から報告され始めた生成画像の破綻を防ぐスクリプトです。詳しくは[こちら](https://note.com/hakomikan/n/nb6dd68a1bd9e)を参照して下さい。  

# Same function in Web-UI/Web-Ui本体の対応について
In Web-UI version 1.8.0 and the latest version of Forge, the same functionality is implemented in the core system, so it's recommended to use that instead. If the core settings include options like the following, it means the core supports it:
- Enable emphasis (for AUTOMATIC1111)
- Emphasis mode (for Forge)
Setting these to "No norm" will achieve the same effect as activating this extension.

Web-UI 1.8.0及び最新バージョンのforgeでは本体に同じ機能が実装されているので、そちらを使うことを推奨します。
本体の設定に以下のような設定が存在する場合、本体が対応しています。
Enable emphasis （AUTOMATIC1111）
Emphasis mode（Forge）
これらにおいて、No normと設定することが、この拡張を有効化したときと同じ設定になります。

# Install/インストール
`https://github.com/hako-mikan/sd-webui-prevent-artifact`  
After installing from Install from URL of Web-UI, please restart.  
Web-UIのInstall from URLからインストールした後、再起動して下さい。  

# How to Use/使い方
After installing and restarting, an option called Prevent Artifact will appear in Settings. By checking the box for Disable taking the average value when calculating cond/uncond and saving, it will be activated.  
インストールして再起動すると、SettingsにPrevent Artifactという項目が現れます。Disable taking the average value when calculating cond/uncondにチェックを入れ保存すると有効化します。
