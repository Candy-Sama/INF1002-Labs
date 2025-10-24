@echo off
set PATH=C:\w64devkit\w64devkit\bin;%PATH%
gcc.exe %1 -o %~n1.exe
echo Compilation complete! Run %~n1.exe to execute.