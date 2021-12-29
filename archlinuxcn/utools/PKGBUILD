# Maintainer: Jack Chen <redchenjs@live.com>

pkgname=utools
pkgver=2.5.2
pkgrel=1
pkgdesc="uTools Utilities"
arch=('x86_64')
url="https://u.tools/"
license=('custom')
depends=('gtk3' 'nss' 'libxss')
source=("https://publish.u-tools.cn/version2/utools_${pkgver}_amd64.deb")
sha512sums=('6f6a86f9af7b6f4a3d438ea771a1f58b51ba94b7911b6e7d5eec9741745366f779f7647ca92a704e786d133221f2ad8a24b07af3e0d7c2a2cb1d25f03c8acedc')

package() {
  tar -xf "$srcdir/data.tar.xz" -C "$pkgdir/"

  install -dm755 "$pkgdir/usr/bin"
  ln -s /opt/uTools/utools "$pkgdir/usr/bin/utools"
}
