#!/bin/bash
LOG=dynip.log
PYTHON=python

$PYTHON dynip/server/dynip.py >$LOG 2>&1 &
