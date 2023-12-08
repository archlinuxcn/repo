# Maintainer: Jack Chen <redchenjs@live.com>

pkgname=utools
pkgver=4.4.1
pkgrel=1
pkgdesc="uTools Utilities"
arch=('x86_64')
url="https://u.tools/"
license=('custom')
depends=('gtk3' 'nss' 'alsa-lib' 'openssl-1.1')
source=("https://publish.u-tools.cn/version2/utools_${pkgver}_amd64.deb")
sha512sums=('b78ab6bbb956faa8f9701d0ad97e62956f534e4a2056edad6c4c6556e00964226e76a8582b3798044b2eb9769913e09ac34eb05aede74127f9b188f6f699b3e6')

package() {
  tar -xf "$srcdir/data.tar.xz" -C "$pkgdir/"

  install -dm755 "$pkgdir/usr/bin"
  ln -s /opt/uTools/utools "$pkgdir/usr/bin/utools"
}
