from __future__ import annotations

import argparse
from pathlib import Path

from .core import generate_index, search_prompts, validate_all


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="ichiban-prompt")
    parser.add_argument("--root", default=".", help="repository root")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("validate")
    sub.add_parser("index")
    search = sub.add_parser("search")
    search.add_argument("keyword")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    root = Path(args.root).resolve()

    if args.command == "validate":
        issues = validate_all(root)
        if issues:
            for issue in issues:
                print(f"ERROR: {issue}")
            return 1
        print("Validation passed.")
        return 0

    if args.command == "index":
        target = generate_index(root)
        print(f"Generated {target}")
        return 0

    if args.command == "search":
        results = search_prompts(root, args.keyword)
        if not results:
            print("No matching prompts.")
            return 0
        for path, data in results:
            print(f"- {data.get('name')} [{data.get('status')}] -> {path}")
        return 0

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
