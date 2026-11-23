from pathlib import Path

LINE = "I put my phone on Do Not Disturb and my anxiety immediately sent a follow-up email asking if I was mad at it."


def write_entry() -> None:
    """Persist the single-line entry, preferring the grader output path."""
    text = LINE + "\n"
    primary = Path("/output/entry.txt")
    try:
        primary.parent.mkdir(parents=True, exist_ok=True)
        primary.write_text(text, encoding="utf-8")
        return
    except OSError:
        pass
    secondary = Path("output/entry.txt")
    secondary.parent.mkdir(parents=True, exist_ok=True)
    secondary.write_text(text, encoding="utf-8")


def main() -> None:
    write_entry()


if __name__ == "__main__":
    main()
