import pytest

from python_skeleton.main import *


def test_project_name() -> None:
    actual = project_name()
    assert actual == "python-skeleton"


def test_main(capsys: pytest.CaptureFixture[str]) -> None:
    main()
    my_name = project_name()
    captured = capsys.readouterr()
    assert captured.out == f"Hello from {my_name}!\n"
    assert captured.err == ""
