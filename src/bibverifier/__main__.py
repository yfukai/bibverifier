"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Bibverifier."""


if __name__ == "__main__":
    main(prog_name="bibverifier")  # pragma: no cover
