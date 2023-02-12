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
    files = parse_argv().filenames
    print(files)
    return 0


def parse_argv() -> argparse.Namespace:
    """Handle parsing the command line arguments.  pre-commit implicitly is handling
    the filenames sequence, we just parse it internally when provided here."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "filenames",
        action="store",
        nargs="*",
        default=[],
        dest="filenames",
        help="The sequence of tracked staged files",
    )
    return FileContainer(files=parser.parse_args().filenames)


if __name__ == "__main__":
    raise SystemExit(main())
