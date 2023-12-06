# Maintainer: Jack Chen <redchenjs@live.com>

pkgname=utools
pkgver=4.4.0
pkgrel=1
pkgdesc="uTools Utilities"
arch=('x86_64')
url="https://u.tools/"
license=('custom')
depends=('gtk3' 'nss' 'alsa-lib' 'openssl-1.1')
source=("https://publish.u-tools.cn/version2/utools_${pkgver}_amd64.deb")
sha512sums=('85855e707ea7c43279917fedd42539598eec871c078ac6a6ea965ffe95e385433bd0f83c83e7465e542eefb9ac68e8a2c55c7906b0dc355813acb4897e70f736')

package() {
  tar -xf "$srcdir/data.tar.xz" -C "$pkgdir/"

  install -dm755 "$pkgdir/usr/bin"
  ln -s /opt/uTools/utools "$pkgdir/usr/bin/utools"
}
