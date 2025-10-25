@echo off
set PATH=C:\msys64\ucrt64\bin;%PATH%
gcc.exe %1 -o %~n1.exe
if errorlevel 1 (
    echo Compilation failed!
) else (
    echo Compilation successful! Run %~n1.exe to execute.
)