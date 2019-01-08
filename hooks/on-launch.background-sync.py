#!/usr/bin/env python

# Author: Srikanth Sastry (sastry@csail.mit.edu)
#
# Description:
# This hook runs `task sync` in the background at the start of each task command, except
# `task sync` itself.
#
# Usage: simply copy this file to ~/.tasks/hooks, or whatever your hooks directory is
# as specified in you taskrc file.
#
# Compatibility: This hook uses the Hooks V2 API (https://taskwarrior.org/docs/hooks2.html)
# So, it works with TaskWarrior 2.4.3+

import sys
import json

from subprocess import Popen, PIPE

args = sys.argv
arg_map = {}
for arg in args:
    arg_pair = arg.split(':')
    if len(arg_pair) != 2:
        continue
    arg_map[arg_pair[0]] = arg_pair[1]
process = None
if arg_map.get('command', '') == 'synchronize':
    sys.exit(0)
else:
    process = Popen(['task', 'synchronize', 'rc.hooks=off'], stdout=PIPE, stderr=PIPE)
    print("Synchronizing in the background")

sys.exit(0)
