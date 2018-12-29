#!/usr/bin/env python
import sys

POETRY_DIR = '/usr/lib/poetry'
sys.path.insert(0, POETRY_DIR)

if __name__ == '__main__':
    from poetry.console import main
    sys.exit(main())
