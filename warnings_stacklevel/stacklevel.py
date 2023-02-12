import argparse
import dataclasses
import typing


@dataclasses.dataclass
class FileContainer:
    """A Container for the command line file paths."""

    files: typing.Sequence[str]


def main() -> int:
    """A Pre-commit hook that checks for the default `stacklevel` argument when attempting to
    emit python warnings.  Often stacklevel is left on the default `1` which offers little
    value."""
    files = parse_argv()
    print(files)
    return 0


def parse_argv() -> FileContainer:
    """Convert the command line options into a FileContainer instance."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "filenames",
        action="store",
        nargs="*",
        default=[],
        help="The sequence of tracked staged files",
    )
    return FileContainer(files=parser.parse_args().filenames)


if __name__ == "__main__":
    raise SystemExit(main())
