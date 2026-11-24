"""The Robot Pickup Line Championship — one-line entry.

A watchdog timer reboots a robot it thinks has frozen. The joke is the
misdiagnosis — the robot is not frozen, it is just watching you.
"""

import os

LINE = "My watchdog timer keeps rebooting me — it thinks I'm frozen, but I'm just watching you."


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
