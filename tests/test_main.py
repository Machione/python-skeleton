import pytest

from python_skeleton.main import *


def test_project_name() -> None:
    actual = project_name()
    assert actual == "python-skeleton"


@pytest.mark.parametrize(
    "a,b,expected",
    [(0, 0, False), (1, 0, True), (0, 1, False), (-100, 100, False), (100, -100, True)],
)
def test_function_with_args(a: int, b: int, expected: bool) -> None:
    actual = function_with_args(a, b)
    assert actual == expected


def test_main(capsys: pytest.CaptureFixture[str]) -> None:
    main()
    my_name = project_name()
    captured = capsys.readouterr()
    assert captured.out == f"Hello from {my_name}!\n"
    assert captured.err == ""
