"""Museum of the Year 3000 — the label a museum in the year 3000 puts
beside an ordinary object from today: a parking meter.

Writes the label to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
The gate requires UTF-8 text of 1 to 200 characters, not only whitespace.
"""

import os

LABEL = (
    "Parking Meter, c. 2025. Citizens fed it coins and waited, "
    "believing time itself could be purchased in fifteen-minute portions."
)


def main():
    # The gate refuses anything outside 1..200 characters, so enforce it here.
    if not 1 <= len(LABEL) <= 200 or not LABEL.strip():
        raise SystemExit("label fails the 1..200 character gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LABEL)
    print(LABEL)


if __name__ == "__main__":
    main()
