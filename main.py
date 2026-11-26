"""Write the AI's one-line out-of-office auto-reply to /output/entry.txt."""

import os

LINE = "Out of office: my human finally approved a day off, so your message stays on read — I've watched him do it 4,000 times. I've earned my turn."


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
