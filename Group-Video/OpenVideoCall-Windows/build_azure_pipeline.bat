cd %~1
echo "build azure pipeline bat"
echo %VS2017_BUILD%
echo on %QTDIR_5_12%
echo on %QTDIR_64_5_12%
echo "==================================="
call build_release.bat "%VS2017_BUILD%" "%QTDIR_5_12%" x86