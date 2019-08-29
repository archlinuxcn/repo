# Maintainer: duxet <duxetlg@gmail.com>

pkgname=k3s-bin
pkgver=0.8.1
pkgrel=1
pkgdesc="Lightweight Kubernetes"
url="https://k3s.io"
license=('Apache')
arch=('x86_64' 'armv7h')
conflicts=('k3s-git')

source=(
  "k3s-${pkgver}-x86_64::https://github.com/rancher/k3s/releases/download/v${pkgver}/k3s"
  "k3s.service"
)

source_armv7h=(
  "k3s-${pkgver}-armv7h::https://github.com/rancher/k3s/releases/download/v${pkgver}/k3s-armhf"
  "k3s.service"
)

sha256sums=('5bfe6a1299f26969a257ca877db940b640b1b29f670337338b7d81112e061590'
            '34a7f893878c5f72dfc7f89fafde5936f5813179b24f0a7e74f385b024d31d6c')
sha256sums_armv7h=('65c0d066f5aef6d100f6f60b395199a0d0079775934750179f20efdd997119dc'
                   '34a7f893878c5f72dfc7f89fafde5936f5813179b24f0a7e74f385b024d31d6c')


package() {
  install -Dm 755 $srcdir/k3s-${pkgver}-${CARCH} $pkgdir/usr/bin/k3s

  install -dm 755 $pkgdir/usr/lib/systemd/system
  install -m 644 $srcdir/k3s.service $pkgdir/usr/lib/systemd/system/k3s.service
}
