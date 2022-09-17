import os, platform
os.system('xdg-open https://www.facebook.com/X.R.404')
bit = platform.architecture()[0]
if bit == '64bit':
    import bxi
else:
    exit('\033[1;32m [Sorry Not Support Your Phone]')
exit()
