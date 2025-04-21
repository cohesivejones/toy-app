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
Hello World App vdevelopment version
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

## Version Information

The application version is stored in `version.txt` at the root of the repository. This version is:

1. Used during the build process to embed version information into the Windows executable
2. Read directly from the executable's metadata when running the compiled binary
3. When running in development mode (not as a compiled executable), the application will display "development version"

## Windows Binary

This repository includes a GitHub Actions workflow that builds a Windows executable (.exe) file for this application. This allows Windows users to run the application without needing to install Python or any dependencies. The executable includes embedded version information that can be viewed in the file properties dialog on Windows.

The workflow can be triggered in three ways:
1. Automatically on push to the main branch
2. Automatically on pull requests to the main branch
3. Manually from the Actions tab in the GitHub repository

To manually trigger the workflow:
1. Go to the [Actions tab](https://github.com/username/hello-world-app/actions)
2. Select the "Build Windows Binary" workflow from the left sidebar
3. Click the "Run workflow" button
4. Select the branch you want to build from (usually main)
5. Click "Run workflow" to start the build process

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
