# Maintainer: Brad Erhart <brae dot 04 plus aur at gmail dot com>

pkgname=docker-machine-driver-kvm2
pkgver=1.9.0
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
sha256sums=(5e399ab8849e00e60918eb4d9fa40b000eb649f614d6fcc066efbba8d7f2c39d)

package() {
	install -Dm 755 "$pkgname"-"$pkgver" "$pkgdir"/usr/bin/"$pkgname"
}
