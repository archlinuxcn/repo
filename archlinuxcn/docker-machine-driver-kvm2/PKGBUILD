# Maintainer: Brad Erhart <brae dot 04 plus aur at gmail dot com>

pkgname=docker-machine-driver-kvm2
pkgver=1.9.1
pkgrel=1
pkgdesc='Minikube-maintained KVM driver for docker-machine'
url=https://minikube.sigs.k8s.io
license=(Apache)
arch=(x86_64)
depends=(
	dnsmasq
	docker-machine
	iptables
	libvirt
)
optdepends=('docker: to manage the containers in the machine')
source=("$pkgname"-"$pkgver"::https://storage.googleapis.com/minikube/releases/v"$pkgver"/"$pkgname")
sha256sums=(126cacf0b29d3a4ec162cc9b7ae7dcaf9e890e4c03ce4d96387871728d16c8c8)

package() {
	install -Dm 755 "$pkgname"-"$pkgver" "$pkgdir"/usr/bin/"$pkgname"
}
