#Contributor: Jekyll Wu <adaptee [at] gmail [dot] com>
#Maintainer:xgdgsc <xgdgsc [at] gmail [dot]com>
pkgname=synaptiks-git
pkgver=20130226
pkgrel=1
pkgdesc="Touchpad configuration and management tool for KDE"
arch=('i686' 'x86_64')
url="http://synaptiks.readthedocs.org/en/latest/"
license=('BSD')
depends=('kdebase-workspace' 'kdebindings-python2' 'python2-distribute' 'python2-udev' 'xf86-input-synaptics')
makedepends=('git')
provides=('synaptiks')
conflicts=('synaptiks')
install=synaptiks.install

_gitroot="git://github.com/lunaryorn/synaptiks.git"
_gitname="synaptiks"

build() {
  cd "$srcdir"
  msg "Connecting to GIT server...."

  if [ -d $_gitname ] ; then
    cd $_gitname && git pull origin
    msg "The local files are updated."
  else
    git clone --recursive $_gitroot $_gitname
  fi

  msg "GIT checkout done"
  msg "Starting make..."

  rm -rf "$srcdir/$_gitname-build"
  git clone "$srcdir/$_gitname" "$srcdir/$_gitname-build"
  cd "$srcdir/$_gitname-build"

}

package() {
  cd "$srcdir/$_gitname-build"
  python2 setup.py install  --root="${pkgdir}" --single-version-externally-managed
  install -Dm644 COPYING "$pkgdir/usr/share/licenses/${pkgname}/LICENSE"
}
