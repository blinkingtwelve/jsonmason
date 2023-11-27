#!/usr/bin/env python3


def mkdocs():
    from src.jsonmason import libjsonmason, attrdict
    for lib in (libjsonmason, attrdict):
        with open(f'doc/{lib.__name__.split(".")[-1]}.rst', 'w') as docfile:
            docfile.write(lib.__doc__)


if __name__ == "__main__":
    mkdocs()
