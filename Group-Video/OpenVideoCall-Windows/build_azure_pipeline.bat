cd %~1
echo "build azure pipeline bat"
echo %VS2017_BUILD%

set Machine=%~2

if %Machine% == x86 (
  set QTDIR=C:\Qt\Qt5.12.7\5.12.7\msvc2017
) else (
  set QTDIR=C:\Qt\Qt5.12.7\5.12.7\msvc2017_64
)
echo %QTDIR%
echo "==================================="
call build_release.bat "%VS2017_BUILD%" "%QTDIR%" %~2