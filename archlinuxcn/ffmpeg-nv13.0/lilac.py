from types import SimpleNamespace

from lilaclib import *

g = SimpleNamespace()


def pre_build():
    g.files = download_official_pkgbuild('ffmpeg')

    state = 'out'
    for line in edit_file('PKGBUILD'):
        if line.startswith('pkgname='):
            line = 'pkgname=ffmpeg-nv13.0'
        elif line.startswith('pkgdesc='):
            line = line[:-1] + " (with Nvidias codec APIs version 13.0)'"

        elif line.startswith('makedepends=('):
            state = 'makedepends'
        elif state == 'makedepends' and line == '  ffnvcodec-headers':
            line = '  ffnvcodec-headers13.0'
        elif state == 'makedepends' and line == ')':
            state = 'out'

        elif line.startswith('provides=('):
            state = 'provides'
        elif state == 'provides' and line == ')':
            line = '''  ffmpeg=$epoch:$pkgver\n''' + \
                line + '\nconflicts=(ffmpeg)'
            state = 'out'

        print(line)


def post_build():
    git_add_files(g.files)
    git_commit()
