#!/usr/bin/env python3

from sys import stderr


def test():
    import doctest
    from src.jsonmason import libjsonmason
    failed, total = doctest.testmod(libjsonmason)
    if failed:
        exit(f"Failed {failed} out of {total} tests.")
    else:
        print(f"Passed {total} tests.", file=stderr)


if __name__ == "__main__":
    test()
