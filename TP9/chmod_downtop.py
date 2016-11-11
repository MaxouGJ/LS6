#!/usr/bin/env python3

import os
import sys

if __name__ == "__main__":
    mode = int(sys.argv[2], 8)
    for root, dirs, files in os.walk(sys.argv[1], False):
        for f in files :
            os.chmod(os.path.join(root, f), mode)
        for r in dirs :
            os.chmod(os.path.join(root, r), mode)
