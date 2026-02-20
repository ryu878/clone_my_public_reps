#!/usr/bin/env python3
"""
Clone all public repositories of GitHub user ryu878 into the current directory.
Uses clone URL format: https://github.com:ryu878/REPO_NAME.git
"""

import subprocess
import sys
from pathlib import Path

try:
    import requests
except ImportError:
    print("Required: pip install requests", file=sys.stderr)
    sys.exit(1)

GITHUB_USER = "ryu878"
BASE_URL = "https://api.github.com"
CLONE_PREFIX = "https://github.com:ryu878"
PER_PAGE = 100


def get_all_repos():
    """Fetch all repository names for the user via GitHub API."""
    repos = []
    page = 1
    while True:
        url = f"{BASE_URL}/users/{GITHUB_USER}/repos?per_page={PER_PAGE}&page={page}"
        resp = requests.get(url, timeout=30)
        if resp.status_code != 200:
            print(f"API error {resp.status_code}: {resp.text}", file=sys.stderr)
            sys.exit(1)
        data = resp.json()
        if not data:
            break
        for r in data:
            name = r.get("name")
            if name:
                repos.append(name)
        if len(data) < PER_PAGE:
            break
        page += 1
    return repos


def clone_repo(name: str, cwd: Path) -> bool:
    """Clone a single repo; return True on success."""
    url = f"{CLONE_PREFIX}/{name}.git"
    try:
        subprocess.run(
            ["git", "clone", url],
            cwd=cwd,
            check=True,
            capture_output=True,
            text=True,
        )
        print(f"Cloned: {name}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Failed to clone {name}: {e.stderr or e}", file=sys.stderr)
        return False


def main():
    cwd = Path.cwd()
    print(f"Fetching repos for {GITHUB_USER}...")
    names = get_all_repos()
    print(f"Found {len(names)} repositories. Cloning into: {cwd}")

    ok = 0
    for name in names:
        if clone_repo(name, cwd):
            ok += 1

    print(f"Done. Cloned {ok}/{len(names)} repositories.")


if __name__ == "__main__":
    main()
