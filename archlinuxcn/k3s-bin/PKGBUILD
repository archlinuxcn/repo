# Maintainer: duxet <duxetlg@gmail.com>

pkgname=k3s-bin
pkgver=0.6.1
pkgrel=1
pkgdesc="Lightweight Kubernetes"
url="https://k3s.io"
license=('Apache')
arch=('x86_64')
conflicts=('k3s-git')

source=(
  "k3s-${pkgver}::https://github.com/rancher/k3s/releases/download/v${pkgver}/k3s"
  "k3s.service"
)
sha256sums=(
  'df7ff885145cf58a8c32e5c7b66eb2659708d433f360e36b59350c431bf81e46'
  '34a7f893878c5f72dfc7f89fafde5936f5813179b24f0a7e74f385b024d31d6c'
)

package() {
  install -Dm 755 $srcdir/k3s-${pkgver} $pkgdir/usr/bin/k3s

  install -dm 755 $pkgdir/usr/lib/systemd/system
  install -m 644 $srcdir/k3s.service $pkgdir/usr/lib/systemd/system/k3s.service
}
