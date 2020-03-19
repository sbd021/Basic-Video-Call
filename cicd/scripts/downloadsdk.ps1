param($SDKURL)
Invoke-WebRequest -Uri "$SDKURL" -OutFile .\AgoraSDK.zip -TimeoutSec 10;

Invoke-WebRequest -Uri "http://download.qt.io/archive/qt/5.12/5.12.7/qt-opensource-windows-x86-5.12.7.exe" -OutFile .\qt-5.12.7.exe -TimeoutSec 10;