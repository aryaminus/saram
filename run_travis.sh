#!/usr/bin/env bash
python run.py > /dev/null &
nosetests --with-coverage