from __future__ import annotations

import argparse
import sys
from collections.abc import Sequence

import task1
import task2
from scripting_program_2_final.shared.student import (
    GROUP_NAME,
    STUDENT_NAME,
    VARIANT_NUMBER,
)

EXIT_INTERRUPTED = 130
COMMAND_ALL = "all"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="python -m labs.lab02.main",
        description=(
            f"Лабораторна робота №2 (варіант {VARIANT_NUMBER}) — "
            f"{STUDENT_NAME}, {GROUP_NAME}"
        ),
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("demo", help="Завдання 1: демонстрація ООП-моделі")

    analyze = subparsers.add_parser(
        "analyze",
        help="Завдання 2 (варіант 1): аналізатор журналів веб-сервера (access.log)",
    )
    task2.add_arguments(analyze)

    run_all = subparsers.add_parser(
        COMMAND_ALL,
        help="обидва завдання підряд (параметри такі самі, як у analyze)",
    )
    task2.add_arguments(run_all)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    raw_args = list(sys.argv[1:] if argv is None else argv)
    if not raw_args:
        raw_args = [COMMAND_ALL]
    args = build_parser().parse_args(raw_args)
    try:
        if args.command == "demo":
            task1.run_demo()
            return 0
        if args.command == "analyze":
            return task2.run(args)
        task1.run_demo()
        print("\nЗавдання 2 (варіант 1)")
        return task2.run(args)
    except KeyboardInterrupt:
        print("\n[WARNING] Interrupted by user", file=sys.stderr)
        return EXIT_INTERRUPTED


if __name__ == "__main__":
    sys.exit(main())
