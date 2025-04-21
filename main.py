#!/usr/bin/env python3
import typer
from typing import Optional

# Define the app version
APP_VERSION = "0.1.0"
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
