# Maintainer: Jack Chen <redchenjs@live.com>

pkgname=utools
pkgver=2.6.3
pkgrel=1
pkgdesc="uTools Utilities"
arch=('x86_64')
url="https://u.tools/"
license=('custom')
depends=('gtk3' 'nss' 'libxss')
source=("https://publish.u-tools.cn/version2/utools_${pkgver}_amd64.deb")
sha512sums=('d97391926da6a9bb2322fe1dd10264e508f157d2e102fc62b56047fad33679735e8f271e273c8fb83a97920a1e5693eff35033c5d95b9db75a1b84349833504f')

package() {
  tar -xf "$srcdir/data.tar.xz" -C "$pkgdir/"

  install -dm755 "$pkgdir/usr/bin"
  ln -s /opt/uTools/utools "$pkgdir/usr/bin/utools"
}
