# Maintainer: duxet <duxetlg@gmail.com>
pkgname=k3s-bin
pkgver=1.18.4+k3s1
pkgrel=1
pkgdesc="Lightweight Kubernetes"
url="https://k3s.io"
license=('Apache')
arch=('x86_64' 'armv7h' 'aarch64')
conflicts=('k3s-git')

source=(
  "k3s.service"
  "k3s.service.env"
)

source_x86_64=(
  "k3s-${pkgver}-x86_64::https://github.com/rancher/k3s/releases/download/v${pkgver}/k3s"
)

source_armv7h=(
  "k3s-${pkgver}-armv7h::https://github.com/rancher/k3s/releases/download/v${pkgver}/k3s-armhf"
)

source_aarch64=(
  "k3s-${pkgver}-aarch64::https://github.com/rancher/k3s/releases/download/v${pkgver}/k3s-arm64"
)

sha256sums=('f4ae496b69b3dd376a28298df50297728a47761b041be522adf2537aa8a8c3d8'
            '667199fa6b811dde3aef3e626e2695a566ad64c9a03d19d0c94a1f104a7612d0')
sha256sums_x86_64=('0c19d64dde77c8bb3af1dfbac5aecea59ab4679d97dcfaa62419aaa795380490')
sha256sums_armv7h=('f2e3e393b1cf1c960d6e20165c76efab19ae0a72ae99e39eb24b3f77648a915d')
sha256sums_aarch64=('e81a9ee17e87a54197c30af761dc6f84bce7e4fece7382900c075670f3f73e3d')




package() {
  install -Dm 755 $srcdir/k3s-${pkgver}-${CARCH} $pkgdir/usr/bin/k3s

  install -dm 755 $pkgdir/usr/lib/systemd/system
  install -dm 755 $pkgdir/etc/systemd/system

  install -m 644 $srcdir/k3s.service $pkgdir/usr/lib/systemd/system/k3s.service
  install -m 400 $srcdir/k3s.service.env $pkgdir/etc/systemd/system/k3s.service.env
}
