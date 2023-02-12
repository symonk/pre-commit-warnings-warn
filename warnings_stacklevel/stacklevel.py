import argparse
import ast
import dataclasses
import typing


class Result(typing.NamedTuple):
    """Custom sequence for recording violations in files, including their line and column."""

    name: str
    line: int
    column: int


class WarningsWarnVisitor(ast.NodeVisitor):
    """A Custom visitor class that can parse python AST syntax looking for
    references to warning.warn."""

    def __init__(self) -> None:
        self.violations: typing.List[Result] = []

    def visit_Call(self, node: ast.Call) -> None:
        print(node)


def check_python_file(name: str) -> typing.List[Result]:
    """Given a file path, open and parse the AST of the file
    looking for warnings.warn calls that violate the hook.

    :param name: The absolute file path"""
    with open(name, mode="rb") as f:
        tree = ast.parse(f.read(), filename=name)
    custom_visitor = WarningsWarnVisitor()
    custom_visitor.visit(tree)
    return custom_visitor.violations


def main() -> int:
    """A Pre-commit hook that checks for the default `stacklevel` argument when attempting to
    emit python warnings.  Often stacklevel is left on the default `1` which offers little
    value."""
    exit_code = 0
    namespace = parse_argv()
    for file in namespace.filenames:
        results = check_python_file(file)
        if results:
            exit_code = 1
        for result in results:
            print(f"{file}:{result.line}:{result.column}: `warnings.warn(..., stacklevel=1)` detected.")
    return exit_code


def parse_argv() -> argparse.Namespace:
    """Convert the command line options into a FileContainer instance."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "filenames",
        action="store",
        nargs="*",
        default=[],
        help="The sequence of tracked staged files",
    )
    return parser.parse_args()


if __name__ == "__main__":
    raise SystemExit(main())
