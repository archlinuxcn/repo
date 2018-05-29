# Maintainer: Felix Yan <felixonmars@archlinux.org>

_pkgname=chnroutes2
pkgname=$_pkgname-git
pkgver=0.6.7a131eb
pkgrel=1
pkgdesc="Better aggregated chnroutes"
arch=('any')
url="https://github.com/ym/chnroutes2"
license=('unknown') 
depends=()
makedepends=('git')
source=("git+https://github.com/ym/${_pkgname}.git")
md5sums=('SKIP')

pkgver() {
  cd "$srcdir/$_pkgname"
  echo 0.$(git rev-list --count HEAD).$(git rev-parse --short HEAD)
}

package() {
  install -Dm644 "$srcdir"/$_pkgname/chnroutes.txt "$pkgdir"/usr/share/chnroutes2/chnroutes.txt
}

# vim:set ts=2 sw=2 et:
