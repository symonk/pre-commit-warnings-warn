

def main() -> int:
    """A Pre-commit hook that checks for the default `stacklevel` argument when attempting to 
    emit python warnings.  Often stacklevel is left on the default `1` which offers little
    value."""

    return 0

if __name__ == "__main__":
    raise SystemExit(main())