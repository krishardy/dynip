#!/bin/bash
LOG=dynip.log
PYTHON=python

$PYTHON dynip/server.py >$LOG 2>&1 &
