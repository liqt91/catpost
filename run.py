from __init__ import make_app
import sys

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'debug':
        debug = True
    else:
        debug = False
    app = make_app('config.py',debug)
    app.run()
