# author: Arad HamidSamiee
# July 2020
# Quarantine DayZ

import platform
import subprocess

os_platform = platform.system()

if os_platform == 'Windows':
    subprocess.call('dir', shell=True)
else:
    subprocess.call('ls -l', shell=True)
print(os_platform)
