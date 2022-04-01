# Maintainer: Jack Chen <redchenjs@live.com>

pkgname=utools
pkgver=2.6.2
pkgrel=1
pkgdesc="uTools Utilities"
arch=('x86_64')
url="https://u.tools/"
license=('custom')
depends=('gtk3' 'nss' 'libxss')
source=("https://publish.u-tools.cn/version2/utools_${pkgver}_amd64.deb")
sha512sums=('6023c7e7f7365bbd334a1e202e5b20cafc0b6f11da9c0952ef248cfcec08f173051e6a2b26a070671529531c3cede66c31ca61d8f0618290f6463dbd6205ce2a')

package() {
  tar -xf "$srcdir/data.tar.xz" -C "$pkgdir/"

  install -dm755 "$pkgdir/usr/bin"
  ln -s /opt/uTools/utools "$pkgdir/usr/bin/utools"
}
