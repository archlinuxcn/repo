# Maintainer: Brad Erhart <brae.04+aur@gmail.com> 

pkgname=docker-machine-driver-kvm2
pkgver=1.7.2
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
sha256sums=('ed034d5a6cb7b2023316d8fae77f45a6f384aec130434630640c421641dd0292')

package() {
	install -Dm755 "${pkgname}_${pkgver}" "$pkgdir/usr/bin/$pkgname"
}
