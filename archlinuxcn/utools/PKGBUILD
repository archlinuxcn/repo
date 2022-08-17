# Maintainer: Jack Chen <redchenjs@live.com>

pkgname=utools
pkgver=3.0.2
pkgrel=1
pkgdesc="uTools Utilities"
arch=('x86_64')
url="https://u.tools/"
license=('custom')
depends=('gtk3' 'nss' 'libxss')
source=("https://publish.u-tools.cn/version2/utools_${pkgver}_amd64.deb")
sha512sums=('435887f42e2a2a1e368cc64023753e878e7913df6911ed7b503e5c13cec1ab79702ec151d938984e3dbcf2059ce4b10905cb086c262b0535478dbe9c53eaf54d')

package() {
  tar -xf "$srcdir/data.tar.xz" -C "$pkgdir/"

  install -dm755 "$pkgdir/usr/bin"
  ln -s /opt/uTools/utools "$pkgdir/usr/bin/utools"
}
