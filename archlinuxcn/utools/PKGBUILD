# Maintainer: Jack Chen <redchenjs@live.com>

pkgname=utools
pkgver=3.1.0
pkgrel=1
pkgdesc="uTools Utilities"
arch=('x86_64')
url="https://u.tools/"
license=('custom')
depends=('gtk3' 'nss' 'libxss')
source=("https://publish.u-tools.cn/version2/utools_${pkgver}_amd64.deb")
sha512sums=('54677fc20af15a41aaaf8e025633d30f83b964705ff23e065c5ac9fd96bafbe7be184cf3b3a28680d5d5d84bec7f13d176663e5b9f8b8586b932efbcbe3ea0da')

package() {
  tar -xf "$srcdir/data.tar.xz" -C "$pkgdir/"

  install -dm755 "$pkgdir/usr/bin"
  ln -s /opt/uTools/utools "$pkgdir/usr/bin/utools"
}
