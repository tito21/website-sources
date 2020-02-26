#!/bin/sh

# Script from the hogo docs with modificationts by Alberto Di Biase (Feb 2020)
# https://gohugo.io/hosting-and-deployment/hosting-on-github/



# If a command fails then the deploy stops
set -e

printf "\033[0;32mDeploying updates to GitHub...\033[0m\n"

# Build the project.
./yassg.py

# Go To Public folder
cd public

# Add changes to git.
git add .

# Commit changes.
msg="rebuilding site $(date)"
if [ -n "$*" ]; then
	msg="$*"
fi
git commit -m "$msg"

# Push source and build repos.
git push origin master