import nose
import sys


if __name__ == '__main__':
    config = nose
    nose.run(argv=[sys.argv[0], "--verbosity=2"])
