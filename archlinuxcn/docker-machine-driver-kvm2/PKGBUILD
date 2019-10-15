# Maintainer: Brad Erhart <brae.04+aur@gmail.com> 

pkgname=docker-machine-driver-kvm2
pkgver=1.4.0
pkgrel=1
pkgdesc="Minikube-maintained KVM driver for docker-machine"
url="https://github.com/kubernetes/minikube"
license=('Apache')
arch=('x86_64')
depends=(
  'docker-machine'
  'libvirt'
  'iptables'
  'dnsmasq'
)
optdepends=(
  'docker: to manage the containers in the machine'
)
makedepends=()

source=($pkgname_$pkgver::https://github.com/kubernetes/minikube/releases/download/v$pkgver/$pkgname)
sha256sums=('e9f3c84413beeebe1b4e082193c960efe2f0f80d06672fc87d14bfce8e62aa2f')

package() {
  cd "$srcdir"
  install -d "$pkgdir/usr/bin"
  install -m755 $pkgname_$pkgver "$pkgdir/usr/bin/$pkgname"
}
