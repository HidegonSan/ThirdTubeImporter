# ThirdTubeImporter
A program to convert YouTube channel registration information into Json files for ThirdTube.


# Usage
**Japanese**  
https://takeout.google.com/ にアクセスします。  
新しいエクスポートの作成で、一旦全部解除します。  
YouTubeを選択し、登録チャンネルにのみチェックを入れます。  
形式をJSONに設定します。(ダウンロードしたらcsvになります)  
次のステップをクリックします。一回エクスポートを選択し、作成します。  
ダウンロードします。  
takeout-\*.zipを展開します。  
takeout-\*.zip/TakeOut/YouTube と YouTube Music/登録チャンネル/登録チャンネル.csv  
をThirdTibeImporter.pyがあるディレクトリにコピーします。  
Python ThirdTibeImporter.py  
出力された subscription.json を /3ds/ThirdTube/ にコピーします。  

**English**  
Go to https://takeout.google.com/.  
In Create New Export, deactivate all of them once.  
Select YouTube and check only the registered channels.  
Set the format to JSON. (It will be a csv when you download it).  
Click Next Step. Select Export once and create.  
Download the file.  
Extract takeout-\*.zip.  
takeout-\*.zip/TakeOut/YouTube and YouTube Music/Subscribed Channels/Subscribed Channels.csv  
to the directory containing ThirdTibeImporter.py.  
Python ThirdTibeImporter.py  
Copy the output subscription.json to /3ds/ThirdTube/  
Note: Translated from Japanese by DeepL. Some parts may be different. Good luck with that. (sry)  


# Note
Use at your own risk.  
The producer assumes no responsibility whatsoever for anything that occurs with the use of the product.


# Author
* Hidegon


# License
"BetterMiraiseed" is under [MIT license](https://en.wikipedia.org/wiki/MIT_License).  
"BetterMiraiseed" is Confidential.
