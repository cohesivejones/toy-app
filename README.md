# Hello World App

A simple Python CLI application that prints "Hello World" and includes a `--version` flag using the Typer library.

[![Build Windows Binary](https://github.com/username/hello-world-app/actions/workflows/build.yml/badge.svg)](https://github.com/username/hello-world-app/actions/workflows/build.yml)

## Installation

1. Clone this repository or download the files.
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Run the application

```bash
python main.py hello
```

This will output:
```
Hello World!
```

### Check the version

```bash
python main.py --version
```

This will output:
```
Hello World App v0.1.0
```

## Making the script executable (Unix/Linux/macOS)

You can make the script directly executable:

```bash
chmod +x main.py
./main.py hello
./main.py --version
```

## Requirements

- Python 3.6+
- Typer library

## Windows Binary

This repository includes a GitHub Actions workflow that automatically builds a Windows executable (.exe) file for this application. This allows Windows users to run the application without needing to install Python or any dependencies.

### Downloading the Windows Binary

1. Go to the [Actions tab](https://github.com/username/hello-world-app/actions) in the GitHub repository
2. Click on the most recent successful workflow run
3. Scroll down to the "Artifacts" section
4. Download the "hello_world_app" artifact
5. Extract the ZIP file to get the hello_world_app.exe file

### Using the Windows Binary

Once you have downloaded and extracted the hello_world_app.exe file, you can run it from the command prompt:

```
hello_world_app.exe hello
```

To check the version:

```
hello_world_app.exe --version
```

Note: When running the executable for the first time, Windows may show a security warning. This is normal for executables downloaded from the internet.
