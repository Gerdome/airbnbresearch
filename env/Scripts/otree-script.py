#!c:\users\merzg\otree\env\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'otree==2.1.39','console_scripts','otree'
__requires__ = 'otree==2.1.39'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('otree==2.1.39', 'console_scripts', 'otree')()
    )
