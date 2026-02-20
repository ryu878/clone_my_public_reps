#!/usr/bin/env bash

set -e

GITHUB_USER="ryu878"
PER_PAGE=100
PAGE=1

echo "Fetching public repositories for $GITHUB_USER..."

while : ; do
    REPOS=$(curl -s "https://api.github.com/users/${GITHUB_USER}/repos?per_page=${PER_PAGE}&page=${PAGE}" \
        | grep -o '"name": *"[^"]*"' \
        | cut -d '"' -f4)

    if [ -z "$REPOS" ]; then
        break
    fi

    for REPO in $REPOS; do
        if [ -d "$REPO" ]; then
            echo "Skipping $REPO (already exists)"
        else
            echo "Cloning $REPO..."
            git clone "https://github.com/${GITHUB_USER}/${REPO}.git"
        fi
    done

    PAGE=$((PAGE+1))
done

echo "Done. All public repos cloned."
