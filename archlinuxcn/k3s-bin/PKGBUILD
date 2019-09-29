# Maintainer: duxet <duxetlg@gmail.com>

pkgname=k3s-bin
pkgver=0.9.1
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

sha256sums=('9f8bea3fa6f88066ca51cc896000aab2794e3f585d6fc982dd5aa7da8ee9fe85'
            '34a7f893878c5f72dfc7f89fafde5936f5813179b24f0a7e74f385b024d31d6c')
sha256sums_armv7h=('67fe371043b2ef23658e51fba8d7884e891ffee09419022161a411e4775d2afc'
                   '34a7f893878c5f72dfc7f89fafde5936f5813179b24f0a7e74f385b024d31d6c')


package() {
  install -Dm 755 $srcdir/k3s-${pkgver}-${CARCH} $pkgdir/usr/bin/k3s

  install -dm 755 $pkgdir/usr/lib/systemd/system
  install -m 644 $srcdir/k3s.service $pkgdir/usr/lib/systemd/system/k3s.service
}
