# Maintainer: Jack Chen <redchenjs@live.com>

pkgname=utools
pkgver=3.2.1
pkgrel=1
pkgdesc="uTools Utilities"
arch=('x86_64')
url="https://u.tools/"
license=('custom')
depends=('gtk3' 'nss' 'libxss')
source=("https://publish.u-tools.cn/version2/utools_${pkgver}_amd64.deb")
sha512sums=('8924e84bac0e6de34dd9f1b1c9977d4de1ace4a9db62f190f729dfdd65583cad9a8c11e3862b69a31230b3d5e9b01964bdce54e1b07fcd2311dcfea245971edc')

package() {
  tar -xf "$srcdir/data.tar.xz" -C "$pkgdir/"

  install -dm755 "$pkgdir/usr/bin"
  ln -s /opt/uTools/utools "$pkgdir/usr/bin/utools"
}
