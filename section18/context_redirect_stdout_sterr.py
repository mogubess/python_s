import contextlib
import logging

with open('stdout.log', 'w') as f:
    with contextlib.redirect_stdout(f):
        print('hello')

with open('stderr.log', 'w') as f:
    with contextlib.redirect_stderr(f):
        logging.error('Error!')

print('hello2')
