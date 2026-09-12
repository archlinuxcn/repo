from types import SimpleNamespace

from lilaclib import *

g = SimpleNamespace()


def pre_build():
    g.files = download_official_pkgbuild('gpu-screen-recorder')

    state = 'out'
    ffmpeg_seen = False  # Original PKGBUILD contains more than one ffmpeg
    for line in edit_file('PKGBUILD'):
        if line.startswith('pkgname='):
            line = 'pkgname=gpu-screen-recorder-nv13.0'
        elif line.startswith('pkgdesc='):
            line = line[:-1] + " (with Nvidias codec APIs version 13.0)'"

        elif line.startswith('depends=('):
            state = 'depends'
        elif state == 'depends' and line == '  ffmpeg':
            if not ffmpeg_seen:
                line = '  ffmpeg-nv13.0'
                ffmpeg_seen = True
            else:
                continue
        elif state == 'depends' and line == ')':
            state = 'out'

        elif line.startswith('optdepends=('):
            state = 'optdepends'
        elif state == 'optdepends' and line == ')':
            line = line + \
                '\nprovides=(gpu-screen-recorder=$pkgver)\nconflicts=(gpu-screen-recorder)'
            state = 'out'

        elif line == 'build() {':
            line = '''prepare () {\n''' + \
                '''  cd "$srcdir"/$pkgname\ngit apply -3 ../0001-Skip-custom-nvenc-version-checks.patch\n''' + \
                ''')\n\n''' + line

        elif line.startswith('source=('):
            line = '''source=(\n''' + \
                '  $pkgname::' + line[8:-1] + '''\n''' + \
                '''  \'0001-Skip-custom-nvenc-version-checks.patch\'\n''' + \
                ''')\n'''

        elif line.startswith('sha512sums=('):
            line = '''sha512sums=(\n''' + \
                '  ' + line[13:-1] + '''\n''' + \
                '''  \'1bda2fb2b0aab4bd52d904db69b27ea2cd9be6686a8bc3a0975bc83f8213dfff5bfdc739baaf15d660f907a71732883a9589e1f060ba168a6ba10dbaa02828b3\'\n''' + \
                ''')\n'''

        print(line)


def post_build():
    git_add_files(g.files)
    git_commit()
