#!/bin/bash

PROJ="$(cd "$(dirname "$0")/.." && pwd)"
cd "$PROJ"

[ -d .venv ] || python3 -m venv .venv
source .venv/bin/activate
    python -m pip install -r tools/requirements.txt
    python -m pip install ipykernel
    python -m ipykernel install --user --name chess \
        --display-name "Python (chess)"
deactivate
