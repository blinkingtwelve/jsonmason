#!/usr/bin/env python3

from sys import argv as sysargv, stdin, stderr
from pathlib import Path
from json import load as jsonload

from . import deconstruct


def main():
    invocation_map = {
        'jsonmason-nodedump': lambda n: n,
        'jsonmason-jsdump': lambda n: n.assignment
    }
    try:
        stringgetter = invocation_map[Path(sysargv[0]).name]
        try:
            for n in deconstruct(jsonload(stdin)):
                print(stringgetter(n), flush=True)
        except (BrokenPipeError, KeyboardInterrupt):
            stderr.close()
    except (KeyError, TypeError):
        import doctest
        import libjsonmason
        failed, total = doctest.testmod(libjsonmason)
        if failed:
            exit(f"Failed {failed} out of {total} tests.")
        else:
            print(f"Passed {total} tests.", file=stderr)


if __name__ == "__main__":
    main()
