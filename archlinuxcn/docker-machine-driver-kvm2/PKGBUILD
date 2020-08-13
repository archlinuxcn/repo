# Maintainer: Brad Erhart <brae dot 04 plus aur at gmail dot com>

pkgname=docker-machine-driver-kvm2
pkgver=1.12.3
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
sha256sums=(884904475d406a7aa06dbf8bbf44962c0d1c2f1fe4c7b3ae44314f6e2933dc24)

package() {
	install -Dm 755 "$pkgname-$pkgver" "$pkgdir/usr/bin/$pkgname"
}
