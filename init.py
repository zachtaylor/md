#!/usr/bin/env python3
print("initalize git submodule dependencies")
from subprocess import run
run(['git', 'submodule', 'init'])
run(['git', 'submodule', 'update'])
