def project_name() -> str:
    """Just return the name of the project."""
    return "python-skeleton"


def function_with_args(a: int, b: int) -> bool:
    """Just an example function with two arguments to test type hint
    documentation of both the arguments and the return."""
    return a > b


def main() -> None:
    """Just an example for now.

    Examples:
        >>> main()
        Hello from python-skeleton!
    """
    this_name = project_name()
    print(f"Hello from {this_name}!")
