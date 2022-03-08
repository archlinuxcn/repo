# Trimmed lilac.py
#!/usr/bin/env python3
#
# This file is the most simple lilac.py file,
# and it suits for most packages in AUR.
#

from lilaclib import *

def pre_build():
    aur_pre_build(maintainers=['S13ntist'])
    checks = ''
    for line in edit_file('PKGBUILD'):
        if "git describe --long --tags" in line:
            line = '    printf "%s.%s" "$(git describe --tags --long | cut -d- -f1)" "$(git rev-list --count HEAD)"'
            checks = checks + '1'

        # use nodejs
        if line.startswith("depends="):
            line = 'depends=("nodejs")'
            checks = checks + '2'

        # remove .DS_Store
        command = 'find "${pkgdir}"/{usr,opt} -type d -exec chmod 755 {} +'
        if line.strip() == command:
            print('find "${pkgdir}" -type f -name .DS_Store -delete')
            checks = checks + '3'

        print(line)

    if len(checks) != 3:
        raise ValueError('PKGBUILD editing not completed. checks=' + checks)

#if __name__ == '__main__':
#  single_main()
