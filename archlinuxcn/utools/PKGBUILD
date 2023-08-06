# Maintainer: Jack Chen <redchenjs@live.com>

pkgname=utools
pkgver=4.0.0
pkgrel=1
pkgdesc="uTools Utilities"
arch=('x86_64')
url="https://u.tools/"
license=('custom')
depends=('gtk3' 'nss' 'alsa-lib' 'openssl-1.1')
source=("https://publish.u-tools.cn/version2/utools_${pkgver}_amd64.deb")
sha512sums=('8b848cc4ec79d74a289843f5fba53b5cd5ab6724ed530f5d083a505743f68ef0288c5f11b1ec895eebba0976a984138180d2dc57a5a4ce2a31bb7c15ef723781')

package() {
  tar -xf "$srcdir/data.tar.xz" -C "$pkgdir/"

  install -dm755 "$pkgdir/usr/bin"
  ln -s /opt/uTools/utools "$pkgdir/usr/bin/utools"
}
