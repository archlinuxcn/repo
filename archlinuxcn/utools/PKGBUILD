# Maintainer: Jack Chen <redchenjs@live.com>

pkgname=utools
pkgver=3.0.1
pkgrel=1
pkgdesc="uTools Utilities"
arch=('x86_64')
url="https://u.tools/"
license=('custom')
depends=('gtk3' 'nss' 'libxss')
source=("https://publish.u-tools.cn/version2/utools_${pkgver}_amd64.deb")
sha512sums=('382cf86783c149b3d345abbaf8f21a2bb7691a2ab20d33478d35c26edfbf2eaf2a7f00fea69ce86297c609662c4cdceebe29256eca1e159a3cf2a48a9c0e7042')

package() {
  tar -xf "$srcdir/data.tar.xz" -C "$pkgdir/"

  install -dm755 "$pkgdir/usr/bin"
  ln -s /opt/uTools/utools "$pkgdir/usr/bin/utools"
}
