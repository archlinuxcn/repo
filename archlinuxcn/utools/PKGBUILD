# Maintainer: Jack Chen <redchenjs@live.com>

pkgname=utools
pkgver=4.0.1
pkgrel=1
pkgdesc="uTools Utilities"
arch=('x86_64')
url="https://u.tools/"
license=('custom')
depends=('gtk3' 'nss' 'alsa-lib' 'openssl-1.1')
source=("https://publish.u-tools.cn/version2/utools_${pkgver}_amd64.deb")
sha512sums=('fad4390b72e928efe43bf99e8998a8c1791956221136e555984ccc6ad1c167413eb0d313be1bf2014e17985f60ae473eb20fdbf58d204a0666fe508795ddf5c3')

package() {
  tar -xf "$srcdir/data.tar.xz" -C "$pkgdir/"

  install -dm755 "$pkgdir/usr/bin"
  ln -s /opt/uTools/utools "$pkgdir/usr/bin/utools"
}
