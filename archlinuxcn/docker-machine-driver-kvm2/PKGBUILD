# Maintainer: Brad Erhart <brae.04+aur@gmail.com> 

pkgname=docker-machine-driver-kvm2
pkgver=1.6.2
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
sha256sums=('97991c877d5da217462f885b6976ee0fd60d427a42f560adf300f3f379d4308e')

package() {
	install -Dm755 "${pkgname}_${pkgver}" "$pkgdir/usr/bin/$pkgname"
}
