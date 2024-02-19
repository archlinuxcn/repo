# Maintainer: stefanwimmer128 <info at stefanwimmer128 dot eu>

_pkgname=shellspec
pkgname=$_pkgname-bin
_pkgver=0.28.1-2
pkgver=${_pkgver//-/.r}
pkgrel=2
pkgdesc="BDD style unit testing framework for POSIX compliant shell script"
_arch=any
arch=($_arch)
license=(MIT)
url=https://shellspec.info
depends=('sh')
provides=($_pkgname)
conflicts=($_pkgname)
source=("https://git.stefanwimmer128.io/api/v4/projects/151/packages/generic/$_pkgname/$_pkgver/$_pkgname-$_pkgver-$_arch.pkg.tar.zst")
sha256sums=('7f5cd4f8702b48750a6e03ed51af3ab6c898e51234f9786ed811ad60557a4f30')

build() {
  rm "$_pkgname-$_pkgver-$_arch.pkg.tar.zst"
  rm .BUILDINFO .MTREE .PKGINFO
}

package() {
    cp -r . "$pkgdir"
}
