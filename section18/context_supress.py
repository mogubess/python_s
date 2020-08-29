import contextlib
import os

# try:
#     os.remove('somefile.tmp')
# except FileNotFoundError:
#     pass

# 例外の抑圧に使える
with contextlib.suppress(FileNotFoundError):
    os.remove('somefile.tmp')
