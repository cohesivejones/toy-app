#!/usr/bin/env python3
import sys
import typer
from typing import Optional

def get_version():
    """
    Get application version:
    1. Try to read from the executable's version info (when running as exe)
    2. Return "development version" if not running as exe or if reading fails
    """
    # Check if running as compiled binary
    if getattr(sys, 'frozen', False):
        try:
            import win32api
            exe_path = sys.executable
            version_info = win32api.GetFileVersionInfo(exe_path, '\\')
            ms = version_info['FileVersionMS']
            ls = version_info['FileVersionLS']
            version = f"{win32api.HIWORD(ms)}.{win32api.LOWORD(ms)}.{win32api.HIWORD(ls)}.{win32api.LOWORD(ls)}"
            return version
        except (ImportError, Exception):
            pass  # Fall through to development version
    
    # Return development version if not running as exe or if reading fails
    return "development version"

# Get version and app name
APP_VERSION = get_version()
APP_NAME = "Hello World App"

# Create a Typer app instance
app = typer.Typer()

def version_callback(value: bool):
    """Callback function for the --version flag"""
    if value:
        typer.echo(f"{APP_NAME} v{APP_VERSION}")
        raise typer.Exit()

@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None, "--version", callback=version_callback, is_flag=True, help="Show the application version and exit."
    ),
):
    """
    A simple Hello World CLI application.
    """
    pass

@app.command()
def hello():
    """Print Hello World message"""
    typer.echo("Hello World!")

if __name__ == "__main__":
    app()
