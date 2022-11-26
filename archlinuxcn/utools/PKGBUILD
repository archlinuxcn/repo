# Maintainer: Jack Chen <redchenjs@live.com>

pkgname=utools
pkgver=3.2.0
pkgrel=1
pkgdesc="uTools Utilities"
arch=('x86_64')
url="https://u.tools/"
license=('custom')
depends=('gtk3' 'nss' 'libxss')
source=("https://publish.u-tools.cn/version2/utools_${pkgver}_amd64.deb")
sha512sums=('6ef8585385194c19128ab797016b8be53b59aa95df155b37191df91145fe07f750c397ce45744835fe6cadb653b55f073bdb6341808c62d690b5edb67b77d10d')

package() {
  tar -xf "$srcdir/data.tar.xz" -C "$pkgdir/"

  install -dm755 "$pkgdir/usr/bin"
  ln -s /opt/uTools/utools "$pkgdir/usr/bin/utools"
}
