# Maintainer: Jack Chen <redchenjs@live.com>

pkgname=utools
pkgver=4.1.0
pkgrel=1
pkgdesc="uTools Utilities"
arch=('x86_64')
url="https://u.tools/"
license=('custom')
depends=('gtk3' 'nss' 'alsa-lib' 'openssl-1.1')
source=("https://publish.u-tools.cn/version2/utools_${pkgver}_amd64.deb")
sha512sums=('0819f9cb143b29ce3f2d4c29e5b956e459e926704e49ee33ea89bc51fa6061cad172824b0787123db9fa15b5d2814b1597db34ccaf2bc7d8fd46c44b75960fba')

package() {
  tar -xf "$srcdir/data.tar.xz" -C "$pkgdir/"

  install -dm755 "$pkgdir/usr/bin"
  ln -s /opt/uTools/utools "$pkgdir/usr/bin/utools"
}
