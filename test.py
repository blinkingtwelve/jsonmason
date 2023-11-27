#!/usr/bin/env python3

from sys import stderr


def test():
    import doctest
    from src.jsonmason import libjsonmason, attrdict
    failed, total = 0, 0
    for lib in (libjsonmason, attrdict):
        libfailed, libtotal = doctest.testmod(lib)
        failed += libfailed
        total += libtotal
    if failed:
        exit(f"Failed {failed} out of {total} tests.")
    else:
        print(f"Passed {total} tests.", file=stderr)


if __name__ == "__main__":
    test()
