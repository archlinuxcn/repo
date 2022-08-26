# Maintainer: Jack Chen <redchenjs@live.com>

pkgname=utools
pkgver=3.0.3
pkgrel=1
pkgdesc="uTools Utilities"
arch=('x86_64')
url="https://u.tools/"
license=('custom')
depends=('gtk3' 'nss' 'libxss')
source=("https://publish.u-tools.cn/version2/utools_${pkgver}_amd64.deb")
sha512sums=('8b1a4a7ad364a5a388337326aa880551985e9f912067d30b5dd194d9fb4a5467c92cf13dc62c7de54ccdc80f0477be11c08f20400124c03c8c49e5ac531dc935')

package() {
  tar -xf "$srcdir/data.tar.xz" -C "$pkgdir/"

  install -dm755 "$pkgdir/usr/bin"
  ln -s /opt/uTools/utools "$pkgdir/usr/bin/utools"
}
