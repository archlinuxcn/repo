# Maintainer: Sherlock Holo <sherlockya(at)gmail.com>

pkgname=gnome-shell-extension-kimpanel-git
pkgver=20170329
pkgrel=4
pkgdesc="KDE's kimpanel implementation for GNOME Shell, now support fcitx"
arch=("i686" "x86_64")
license=('GPL')
url="http://code.google.com/p/fcitx"
depends=('fcitx' 'gnome-shell' 'zip' 'unzip')
makedepends=('cmake' 'git')

_extensionname="kimpanel@kde.org"
_gitname="kimpanel-for-gnome-shell"
_gitroot="https://github.com/wengxt/kimpanel-for-gnome-shell.git"

build() {
  cd "$srcdir"
  msg "Connecting to the GIT server...."

  if [[ -d $srcdir/$_gitname ]] ; then
    cd $_gitname
    git pull origin
    msg "The local files are updated."
  else
    git clone $_gitroot $_gitname
    cd $_gitname
  fi

  rm -rf build
  mkdir build
  cd build
  CMAKE=`which cmake`
  cmake  -DCMAKE_INSTALL_PREFIX=/usr .. || return 1
  make clean || return 1
  make || return 1
}

package(){
  cd ${srcdir}/$_gitname/build
  make DESTDIR=${pkgdir} install
}

