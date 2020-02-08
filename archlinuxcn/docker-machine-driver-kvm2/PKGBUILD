# Maintainer: Brad Erhart <brae.04+aur@gmail.com> 

pkgname=docker-machine-driver-kvm2
pkgver=1.7.1
pkgrel=1
pkgdesc='Minikube-maintained KVM driver for docker-machine'
url='https://minikube.sigs.k8s.io'
license=('Apache')
arch=('x86_64')
depends=(
	'docker-machine'
	'libvirt'
	'iptables'
	'dnsmasq'
)
optdepends=('docker: to manage the containers in the machine')
source=("${pkgname}_${pkgver}::https://storage.googleapis.com/minikube/releases/v$pkgver/$pkgname")
sha256sums=('891b88e2768a6a735bcd6ae23ed34a188e45a078ad3c7e9b4388e771001b27b4')

package() {
	install -Dm755 "${pkgname}_${pkgver}" "$pkgdir/usr/bin/$pkgname"
}
