#!/bin/sh
cd /opt/politieke-reclame

./get-statements.py

git config --global user.email "developers@openstate.eu"
git config --global user.name "Open State developers"
git config --global --add safe.directory /opt/politieke-reclame
git add items/
git commit -m 'Statements changed' && git push -q https://`cat $GITHUB_PERSONAL_TOKEN_FILE`@github.com/openstate/politieke-reclame.git main
