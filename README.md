# INF1002 C Programming Labs

This repository contains C programming lab assignments and exercises.

## Setup

The project is configured with:
- GCC compiler (w64devkit)
- VS Code C/C++ development environment
- F5 quick compile shortcut

## How to Use

### Method 1: F5 Shortcut (Fastest)
1. Open any `.c` file in VS Code
2. Press **F5** to compile
3. Run the generated `.exe` file

### Method 2: Batch Script
```bash
.\compile.bat yourfile.c
.\yourfile.exe
```

### Method 3: Manual Compilation
```bash
C:\w64devkit\w64devkit\bin\gcc.exe yourfile.c -o yourfile.exe
.\yourfile.exe
```

## Files

- `*.c` - C source files
- `compile.bat` - Compilation helper script
- `.vscode/` - VS Code configuration (tasks and keybindings)
- `*.pdf` - Lab instructions and documentation

## Note

Compiled `.exe` files are automatically ignored by git to keep the repository clean.