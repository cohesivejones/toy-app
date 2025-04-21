# Hello World App

A simple Python CLI application that prints "Hello World" and includes a `--version` flag using the Typer library.

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
