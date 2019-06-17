#!/bin/bash
# Usage: ./run_tests.sh
# Detects and runs all Python unit tests in project

if [ ! -d venv ] || [ ! -d markup ]
then
    >2 echo "Run from project root directory!"
    exit 1
fi

(. ./venv/bin/activate || exit 1
python -m unittest discover -s markup -p 'test_*.py')
