# Maintainer: Jack Chen <redchenjs@live.com>

pkgname=utools
pkgver=3.3.0
pkgrel=1
pkgdesc="uTools Utilities"
arch=('x86_64')
url="https://u.tools/"
license=('custom')
depends=('gtk3' 'nss' 'libxss')
source=("https://publish.u-tools.cn/version2/utools_${pkgver}_amd64.deb")
sha512sums=('aeee77bd434b326ecd9f0dec2db3fced736e3adb844c233112f119a9b6dc08a5ac28c82bb8dd6fd6a427fca39d667a31c5e66bce52965c77a77aae131bd63ae6')

package() {
  tar -xf "$srcdir/data.tar.xz" -C "$pkgdir/"

  install -dm755 "$pkgdir/usr/bin"
  ln -s /opt/uTools/utools "$pkgdir/usr/bin/utools"
}
