#!/usr/bin/env python3
"""hello-flair.py
A juicy Hello World: colorful, animated, and slightly opinionated CLI.

Usage:
  python3 /tmp/hello-flair.py
  python3 /tmp/hello-flair.py --name Alice
  python3 /tmp/hello-flair.py --fast

No external dependencies required.
"""

import sys
import time
import argparse
import random

# ANSI color codes (bright variants)
COLORS = [
    "\033[95m",  # magenta
    "\033[94m",  # blue
    "\033[96m",  # cyan
    "\033[92m",  # green
    "\033[93m",  # yellow
    "\033[91m",  # red
]
RESET = "\033[0m"
BOLD = "\033[1m"

EMOJIS = ["🌟", "✨", "🔥", "💫", "🎉", "👋", "😄", "🚀"]


def color_cycle(text):
    """Apply a cycling color effect across the characters of `text`."""
    out = []
    colors = COLORS
    for i, ch in enumerate(text):
        if ch.isspace():
            out.append(ch)
        else:
            out.append(colors[i % len(colors)] + ch + RESET)
    return "".join(out)


def typing_print(text, delay=0.03):
    """Print text with a typewriter effect."""
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")


def spinner(duration=1.6, label="Processing"):
    """Simple terminal spinner for `duration` seconds."""
    frames = "|/-\\"
    end = time.time() + duration
    i = 0
    while time.time() < end:
        frame = frames[i % len(frames)]
        sys.stdout.write(f"\r{label} {frame}")
        sys.stdout.flush()
        time.sleep(0.08)
        i += 1
    sys.stdout.write("\r" + " " * (len(label) + 3) + "\r")


def progress_bar(total=20, label="Squeezing juice"):
    for i in range(total + 1):
        filled = int((i / total) * 30)
        bar = "█" * filled + "─" * (30 - filled)
        perc = int((i / total) * 100)
        sys.stdout.write(f"\r{label}: |{bar}| {perc}%")
        sys.stdout.flush()
        time.sleep(0.05)
    sys.stdout.write("\n")


def banner(name, emoji):
    text = f"Hello, {name}! {emoji}"
    line = "=" * len(text)
    print(BOLD + color_cycle(line) + RESET)
    print(color_cycle(text))
    print(BOLD + color_cycle(line) + RESET)


def little_facts(name):
    facts = [
        f"Did you know, {name}? The Python snake emoji is a distant cousin. 🐍",
        "Tiny programs can make big smiles.",
        "Made with standard library, zero external deps.",
        "Tip: Try `--fast` to skip animations for CI-friendly runs.",
    ]
    chosen = random.sample(facts, 2)
    for f in chosen:
        print("  - " + f)


def parse_args():
    p = argparse.ArgumentParser(description="Juicy Hello World: a little flair for your terminal")
    p.add_argument("--name", "-n", default="World", help="Name to greet")
    p.add_argument("--fast", "-f", action="store_true", help="Skip animations for fast output")
    return p.parse_args()


def main():
    args = parse_args()
    name = args.name
    fast = args.fast

    emoji = random.choice(EMOJIS)

    print()  # leading space

    if fast:
        # Quick path: colorful one-liner
        print(BOLD + color_cycle(f"Hello, {name}! {emoji}") + RESET)
        print()
        little_facts(name)
        return

    # Animated path
    banner(name, emoji)

    msg = f"Pleased to meet you, {name}. Pouring some digital citrus..."
    typing_print(msg, delay=0.04)

    spinner(1.4, label="Warming up the juicer")
    progress_bar(20, label="Concentrating flavor")

    final = f"Here's your fresh greeting, {name}: {emoji}"
    print()
    print(BOLD + color_cycle(final) + RESET)
    print()

    little_facts(name)
    print()
    print("Stay juicy! 🍊")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.stderr.write("\nInterrupted. Bye!\n")
        sys.exit(1)
