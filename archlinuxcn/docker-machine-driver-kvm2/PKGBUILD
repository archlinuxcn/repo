# Maintainer: Brad Erhart <brae dot 04 plus aur at gmail dot com>

pkgname=docker-machine-driver-kvm2
pkgver=1.13.0
pkgrel=1
pkgdesc='Minikube-maintained KVM driver for docker-machine'
url='https://minikube.sigs.k8s.io'
license=('Apache')
arch=('x86_64')
depends=(
	'dnsmasq'
	'docker-machine'
	'iptables'
	'libvirt'
)
optdepends=('docker: to manage the containers in the machine')
source=("$pkgname-$pkgver::https://storage.googleapis.com/minikube/releases/v$pkgver/$pkgname-amd64")
sha256sums=(4dfbf54160f389464fc778a64ce596014433db52b0c649f51a2ba4b9285ee307)

package() {
	install -Dm 755 "$pkgname-$pkgver" "$pkgdir/usr/bin/$pkgname"
}
