#!C:\Users\Kevin\Documents\Python\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'pyprof2calltree==1.4.3','console_scripts','pyprof2calltree'
__requires__ = 'pyprof2calltree==1.4.3'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('pyprof2calltree==1.4.3', 'console_scripts', 'pyprof2calltree')()
    )
