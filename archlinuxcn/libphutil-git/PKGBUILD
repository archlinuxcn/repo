# Maintainer: Doug Newgard <scimmia at archlinux dot info>
# Contributor: Sergio Correia <sergio@correia.cc>
# Contributor: Nicolas Vivet <nizzox@gmail.com>

_pkgname=libphutil
pkgname=$_pkgname-git
pkgver=5.r937.gadb8a9c
pkgrel=2
pkgdesc='Library system which organizes PHP classes and functions into modules'
arch=('any')
url="http://phabricator.com"
license=('Apache')
depends=('php')
makedepends=('git')
provides=("$_pkgname=$pkgver")
conflicts=("$_pkgname")
source=("git+https://secure.phabricator.com/diffusion/PHU/libphutil.git")
sha256sums=('SKIP')

pkgver() {
  cd $_pkgname
  git describe --tags --always | sed 's/^conduit-//;s/-/.r/;s/-/./'
}

prepare() {
# Don't override user option, doesn't work right anyway
  sed -i "s|^\s*'error_log'|//&|" $_pkgname/scripts/__init_script__.php
}

package() {
  install -d "$pkgdir/usr/share/php/$_pkgname"
# do not copy hidden directories
  cp -a $_pkgname/* "$pkgdir/usr/share/php/$_pkgname/"
}
