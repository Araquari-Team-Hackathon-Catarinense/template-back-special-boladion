#!/bin/bash

pdm config python.use_venv false
pdm install

# eval "$(pdm --pep582)"

tail -f /dev/null