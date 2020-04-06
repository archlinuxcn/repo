# Maintainer: Brad Erhart <brae dot 04 plus aur at gmail dot com>

pkgname=docker-machine-driver-kvm2
pkgver=1.9.2
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
sha256sums=(4f75e89a915160e74b2b5ed681468b887af8fe40c3da121a41682bfab152d35f)

package() {
	install -Dm 755 "$pkgname"-"$pkgver" "$pkgdir"/usr/bin/"$pkgname"
}
