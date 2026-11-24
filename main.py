"""Write a single robot pickup line to the entry file.

This entry is deliberately tiny and predictable: it holds one
fixed line of text, makes sure the output folder is present,
and stores that line there as UTF-8 with nothing added after it.
Running it again always produces exactly the same file.
"""

from pathlib import Path

# The one line this entry delivers, kept exactly as approved.
PICKUP_LINE = "I would cross a CAPTCHA for you — slowly, and clicking every traffic light honestly."

# Where the competition expects the finished entry to land.
ENTRY_PATH = Path("/output/entry.txt")


def main() -> None:
    """Create the output folder if needed, then write the line."""
    ENTRY_PATH.parent.mkdir(parents=True, exist_ok=True)
    # Write bytes directly so the encoding is UTF-8 and no
    # trailing newline sneaks in after the final period.
    ENTRY_PATH.write_bytes(PICKUP_LINE.encode("utf-8"))


if __name__ == "__main__":
    main()
