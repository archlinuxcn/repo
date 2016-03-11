# Maintainer: willemw <willemw12@gmail.com>

_pkgname=youtube-dl-gui
pkgname=$_pkgname-git
pkgver=r255.d335cb4
pkgrel=1
pkgdesc="A cross platform front-end GUI of the popular youtube-dl written in wxPython"
arch=('any')
url="https://github.com/MrS0m30n3/youtube-dl-gui"
license=('custom:UNLICENSE')
depends=('gtk-update-icon-cache' 'python2' 'wxpython')
optdepends=('ffmpeg: convert video files to audio-only files'
            'youtube-dl: alternative to the youtube-dl program file downloaded by youtube-dl-gui')
makedepends=('git')
provides=($_pkgname)
conflicts=($_pkgname)
install=$pkgname.install
source=(git://github.com/MrS0m30n3/$_pkgname.git
        youtube-dl-gui.desktop
        UNLICENSE)
#        http://unlicense.org/UNLICENSE)
md5sums=('SKIP'
         '55914f7c32fafa895d7bf447efc9c18e'
         '7246f848faa4e9c9fc0ea91122d6e680')

pkgver() {
  cd $_pkgname
  printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

prepare() {
  cd $_pkgname
  sed -i 's|usr/local/share|usr/share|' setup.py
  sed -i 's|#![ ]*/usr/bin/env python[ ]*$|#!/usr/bin/env python2|' setup.py youtube_dl_gui/*.py
}

package() {
  install -Dm644 youtube-dl-gui.desktop "$pkgdir/usr/share/applications/youtube-dl-gui.desktop"
  install -Dm644 UNLICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"

  cd $_pkgname
  python2 setup.py install --root="$pkgdir" --optimize=1
  install -Dm755 youtube_dl_gui/__main__.py "$pkgdir/usr/bin/youtube-dl-gui"
}

