"""CLI interface for PR Summarizer AI."""

import argparse
import os
import sys
import subprocess
import json
from pathlib import Path
from datetime import datetime, timezone


def main():
    parser = argparse.ArgumentParser(
        prog="pr-summarizer",
        description="AI-powered PR summarization for GitHub",
    )
    parser.add_argument("pr_url", help="GitHub PR URL")
    parser.add_argument("--model", default="google/gemini-2.5-flash",
                        help="OpenRouter model to use")
    parser.add_argument("--format", choices=["markdown", "json"], default="markdown",
                        help="Output format")
    parser.add_argument("--output", "-o", default=None,
                        help="Output file path")
    parser.add_argument("--api-key", default=None,
                        help="OpenRouter API key (default: OPENROUTER_API_KEY env)")

    args = parser.parse_args()

    print(f"Summarizing: {args.pr_url}", file=sys.stderr)
    
    # Placeholder - real implementation would fetch diff and summarize
    summary = f"## Summary\nPR summary for {args.pr_url}\n\n## Key Changes\n- See full diff for details\n"
    
    if args.format == "json":
        output = json.dumps({"pr_url": args.pr_url, "summary": summary}, indent=2)
    else:
        output = summary
    
    if args.output:
        with open(args.output, "w") as f:
            f.write(output)
        print(f"Written to {args.output}", file=sys.stderr)
    else:
        print(output)


if __name__ == "__main__":
    main()