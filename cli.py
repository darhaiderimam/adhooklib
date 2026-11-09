import argparse
import json
import random
import sys
from pathlib import Path

DATA_FILE = Path(__file__).parent / "data" / "hooks.json"

def load_hooks():
    if not DATA_FILE.exists():
        sys.stderr.write(f"Error: Hooks data file not found at {DATA_FILE}\n")
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def main():
    parser = argparse.ArgumentParser(
        prog="adhooklib",
        description="Queryable open corpus of high-performing ad hooks and angles."
    )
    subparsers = parser.add_subparsers(dest="command", help="Commands")

    search_p = subparsers.add_parser("search", help="Search hooks by vertical, angle, or keyword")
    search_p.add_argument("--vertical", "-v", help="Filter by vertical (ecommerce, b2b_saas, fintech, b2b_services)")
    search_p.add_argument("--angle", "-a", help="Filter by angle type (contrarian, curiosity_gap, us_vs_them, etc.)")
    search_p.add_argument("--query", "-q", help="Search text within hook")
    search_p.add_argument("--limit", "-n", type=int, default=5, help="Number of hooks to return")

    random_p = subparsers.add_parser("random", help="Get a random inspiration hook")
    random_p.add_argument("--vertical", "-v", help="Optional vertical filter")

    list_p = subparsers.add_parser("list-angles", help="List all available angle types and verticals")

    args = parser.parse_args()
    hooks = load_hooks()

    if args.command == "search":
        filtered = hooks
        if args.vertical:
            filtered = [h for h in filtered if h.get("vertical", "").lower() == args.vertical.lower()]
        if args.angle:
            filtered = [h for h in filtered if h.get("angle_type", "").lower() == args.angle.lower()]
        if args.query:
            q = args.query.lower()
            filtered = [h for h in filtered if q in h.get("hook_text", "").lower()]

        print(f"\n[+] Found {len(filtered)} matching hooks (Showing top {min(args.limit, len(filtered))}):\n")
        for h in filtered[:args.limit]:
            print(f"- [{h['id']}] \"{h['hook_text']}\"")
            print(f"  Vertical: {h['vertical']} | Angle: {h['angle_type']} | Format: {h['format']}")
            print(f"  Visual Direction: {h.get('visual_cue', 'N/A')}")
            print(f"  Benchmark: {h.get('synthetic_benchmark', 'N/A')}\n")

    elif args.command == "random":
        candidates = hooks
        if args.vertical:
            candidates = [h for h in candidates if h.get("vertical", "").lower() == args.vertical.lower()]
        if not candidates:
            print("No hooks found matching criteria.")
            return
        h = random.choice(candidates)
        print(f"\n[🎲 Random Hook Inspiration]")
        print(f"\"{h['hook_text']}\"")
        print(f"Angle: {h['angle_type']} | Vertical: {h['vertical']} | Format: {h['format']}")
        print(f"Visual Action: {h.get('visual_cue', 'N/A')}\n")

    elif args.command == "list-angles":
        verticals = sorted(list(set(h.get("vertical") for h in hooks if h.get("vertical"))))
        angles = sorted(list(set(h.get("angle_type") for h in hooks if h.get("angle_type"))))
        print("\nAvailable Verticals:")
        for v in verticals:
            print(f"  - {v}")
        print("\nAvailable Angle Types:")
        for a in angles:
            print(f"  - {a}")
        print()

    else:
        parser.print_help()

if __name__ == "__main__":
    main()
