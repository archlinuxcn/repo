# Maintainer: Brad Erhart <brae dot 04 plus aur at gmail dot com>

pkgname=docker-machine-driver-kvm2
pkgver=1.8.2
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
sha256sums=(c29caec9024bb5cdc6a10a05878cee0ada34e275280941dc5d67183980a489f3)

package() {
	install -Dm 755 "$pkgname"-"$pkgver" "$pkgdir"/usr/bin/"$pkgname"
}
