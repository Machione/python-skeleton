from click.testing import CliRunner

from python_skeleton.cli import *


def test_hello() -> None:
    runner = CliRunner()
    result = runner.invoke(cli, ["hello"])
    assert result.exit_code == 0
    assert result.output == "Hello from python-skeleton!\n"
