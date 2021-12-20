# Maintainer: Jack Chen <redchenjs@live.com>

pkgname=utools
pkgver=2.5.1
pkgrel=1
pkgdesc="uTools Utilities"
arch=('x86_64')
url="https://u.tools/"
license=('custom')
depends=('gtk3' 'nss' 'libxss')
source=("https://publish.u-tools.cn/version2/utools_${pkgver}_amd64.deb")
sha512sums=('deb2de05d05eb730b9e3996d3ea91e5d103d701c99a4b8848c066a4eb7142460df5e58c417c91c31f371d2085f64e3292c9ff9e252e3fd778492aff2ab59ce2e')

package() {
  tar -xf "$srcdir/data.tar.xz" -C "$pkgdir/"

  install -dm755 "$pkgdir/usr/bin"
  ln -s /opt/uTools/utools "$pkgdir/usr/bin/utools"
}
