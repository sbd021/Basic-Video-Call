cd %~1
echo "build azure pipeline bat"
echo %VS2017_BUILD%

set QTDIR=C:\Qt\Qt5.12.7\5.12.7\msvc2017
echo %QTDIR%
echo "==================================="
call build_release.bat "%VS2017_BUILD%" "%QTDIR%" x86