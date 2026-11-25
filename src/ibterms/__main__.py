import sys
from .core import explain


def main(argv=None):
    a = sys.argv[1:] if argv is None else argv
    if not a:
        print("usage: python -m ibterms 'Find the roots of ... Hence sketch ...'")
        return 2
    print(explain(" ".join(a)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
