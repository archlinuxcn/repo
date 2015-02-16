# Maintainer: lilydjwg <lilydjwg@gmail.com>
pkgname=systemtap-git
pkgver=2.3.1539.g00b943a
pkgrel=1
pkgdesc="SystemTap provides free software (GPL) infrastructure to simplify the gathering of information about the running Linux system."
url="http://sourceware.org/systemtap/"
arch=('i686' 'x86_64')
license=('GPL')
depends=('elfutils' 'nss' 'python2' 'avahi')
makedepends=('git')
optdepends=('sqlite3' 'linux-fedora: for debug enabled kernel' 'linux-lily-debug: for debug enabled kernel')
provides=(systemtap=2.3)
conflicts=(systemtap)
_gitroot=git://github.com/fche/systemtap.git
_gitname=systemtap
source=("git+$_gitroot")
md5sums=(SKIP)

pkgver() {
  cd "$srcdir/$_gitname"
  git describe | sed 's/release-//;s/-/./g'
}

build() {
  cd "$srcdir/$_gitname"
  msg "Starting make..."

  ./configure --prefix=/usr --sysconfdir=/etc \
    --localstatedir=/var --libexecdir=/usr/lib
  make
}

package() {
  cd "$srcdir/$_gitname"
  make DESTDIR="${pkgdir}" install
  mv "${pkgdir}"/var/run "${pkgdir}"
  sed -i 's=#!/usr/bin/python.*=#!/usr/bin/python2=' "${pkgdir}/usr/bin/dtrace"
}
