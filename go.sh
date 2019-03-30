#!/usr/bin/env bash

set -e
pip install -r "./requirement.txt"
pytest -n 5