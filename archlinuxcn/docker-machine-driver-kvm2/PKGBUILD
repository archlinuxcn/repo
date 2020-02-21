# Maintainer: Brad Erhart <brae dot 04 plus aur at gmail dot com>

pkgname=docker-machine-driver-kvm2
pkgver=1.7.3
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
sha256sums=(37d4998f855e97de1bb3903179c4e774ebdbc2e1b421c45bba2045834a87367f)

package() {
	install -Dm 755 "$pkgname"-"$pkgver" "$pkgdir"/usr/bin/"$pkgname"
}
