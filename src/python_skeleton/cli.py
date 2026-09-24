import click

from python_skeleton.main import main


@click.group()
def cli() -> None:
    """This is just an example."""


@cli.command()
def hello() -> None:
    """Greetings from the CLI!"""
    main()


if __name__ == "__main__":
    cli()
