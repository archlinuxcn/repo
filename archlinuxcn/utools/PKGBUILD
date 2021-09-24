# Maintainer: Jack Chen <redchenjs@live.com>

pkgname=utools
pkgver=1.3.5
pkgrel=1
pkgdesc="uTools Utilities"
arch=('x86_64')
url="https://u.tools/"
license=('custom')
depends=('gtk3' 'nss' 'libxss')
source=("https://resource.u-tools.cn/currentversion/utools_${pkgver}_amd64.deb")
sha512sums=('8bdfc7d8164839a9722085157fdbfe3d3e0f7a223ee106dd607937e8db028f429b65b4326c557bfe244514cfdccfc5a76797cff135fecd1dc5c33c5f6dec6b31')

package() {
  tar -xf "$srcdir/data.tar.xz" -C "$pkgdir/"

  install -dm755 "$pkgdir/usr/bin"
  ln -s /opt/uTools/utools "$pkgdir/usr/bin/utools"
}
