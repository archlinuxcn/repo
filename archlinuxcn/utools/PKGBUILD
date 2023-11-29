# Maintainer: Jack Chen <redchenjs@live.com>

pkgname=utools
pkgver=4.3.2
pkgrel=1
pkgdesc="uTools Utilities"
arch=('x86_64')
url="https://u.tools/"
license=('custom')
depends=('gtk3' 'nss' 'alsa-lib' 'openssl-1.1')
source=("https://publish.u-tools.cn/version2/utools_${pkgver}_amd64.deb")
sha512sums=('7672b3922348f05103ad681f2ebf81c81d373062617a5a8f8ef232a83fc93b0afa9812eb9785a175db86cddd2f431c643553393037823be9af555475a1f78319')

package() {
  tar -xf "$srcdir/data.tar.xz" -C "$pkgdir/"

  install -dm755 "$pkgdir/usr/bin"
  ln -s /opt/uTools/utools "$pkgdir/usr/bin/utools"
}
