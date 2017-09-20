# Maintainer: carstene1ns <arch carsten-teibes de> - http://git.io/ctPKG

pkgname=raine-blend
pkgver=201501
pkgrel=2
pkgdesc="Transparency information files for CPS1, CPS2 and NeoGeo games in the Raine emulator"
arch=('any')
url="http://raine.1emulation.com/download/extras.html"
license=('unknown')
depends=('raine')
source=("http://raine.1emulation.com/archive/debian/dists/unstable/main/binary-i386/blend-raine_$pkgver-1_all.deb")
sha256sums=('ae86281a520e39a1ea08350079fc60419b0633a17b6ae5d0903d938531fcceab')

prepare() {
  bsdtar xf data.tar.xz
}

package() {
  install -d "$pkgdir"/usr/share/raine/blend
  install -m644 usr/share/games/raine/blend/*.bld "$pkgdir"/usr/share/raine/blend
}
