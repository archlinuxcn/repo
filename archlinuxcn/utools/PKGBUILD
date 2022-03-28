# Maintainer: Jack Chen <redchenjs@live.com>

pkgname=utools
pkgver=2.6.1
pkgrel=1
pkgdesc="uTools Utilities"
arch=('x86_64')
url="https://u.tools/"
license=('custom')
depends=('gtk3' 'nss' 'libxss')
source=("https://publish.u-tools.cn/version2/utools_${pkgver}_amd64.deb")
sha512sums=('823e83ff09f81b64ec43f38dc06744dec79472c46d94bd7bae7fdf6a961e78dcaf2d1d1c7b694e2c5af6f806b9c78c40ab4f39a2a4c8f4a3c65e29b528854659')

package() {
  tar -xf "$srcdir/data.tar.xz" -C "$pkgdir/"

  install -dm755 "$pkgdir/usr/bin"
  ln -s /opt/uTools/utools "$pkgdir/usr/bin/utools"
}
