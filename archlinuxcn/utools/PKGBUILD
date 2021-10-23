# Maintainer: Jack Chen <redchenjs@live.com>

pkgname=utools
pkgver=2.4.1
pkgrel=1
pkgdesc="uTools Utilities"
arch=('x86_64')
url="https://u.tools/"
license=('custom')
depends=('gtk3' 'nss' 'libxss')
source=("https://publish.u-tools.cn/version2/utools_${pkgver}_amd64.deb")
sha512sums=('71c7d4dc5898557931c4485e395b2a4fe2a7737eac5beaae0a2ee81ed2934d1e42c77aae7f8f5b4dd1a6b8c8c3147eaf3d3283abcf63050e5b31b84831ab87c9')

package() {
  tar -xf "$srcdir/data.tar.xz" -C "$pkgdir/"

  install -dm755 "$pkgdir/usr/bin"
  ln -s /opt/uTools/utools "$pkgdir/usr/bin/utools"
}
