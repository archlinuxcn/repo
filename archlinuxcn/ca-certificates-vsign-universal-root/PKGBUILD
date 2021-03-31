# Maintainer: DuckSoft <realducksoft@gmail.com>
# WARNING: Used to workaround m1kr0$h1t nuget certificate problem.
# DO NOT INSTALL UNLESS YOU ARE CLEAR WHAT YOU ARE DOING.
pkgname=ca-certificates-vsign-universal-root
pkgver=114514
pkgrel=1
pkgdesc="VeriSign Universal Root Certification Authority"
arch=(any)
url=https://symantec.tbs-certificats.com/vsign-universal-root.crt
license=(GPL)
makedepends=(p11-kit)
provides=(ca-certificates-verisign-root)
conflicts=(ca-certificates-verisign-root)
source=($url)
b2sums=('a81094c32af2b9c9740fb3d8bdc18a4ddca277be8ff218d1cee82891bbf172b4cecb126303589a8bb4a19d0f86dcecd5584f07bbab4182e50f47036bd0dc26b6')

package() {
  cd "$srcdir"
  install -Dm644 -t "${pkgdir}/usr/share/ca-certificates/trust-source/anchors" vsign-universal-root.crt
}
