#!/bin/bash

PROJ="$(cd "$(dirname "$0")/.." && pwd)"
cd "$PROJ"

[ -d .venv ] || python3 -m venv .venv

.venv/bin/python -m pip install -r tools/requirements.txt
.venv/bin/python -m pip install ipykernel
.venv/bin/python -m ipykernel install --user --name chess \
    --display-name "Python (chess)"
