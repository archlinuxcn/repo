# Maintainer: Vimsucks <dev@vimsucks.com>
# Contributor: Metal A-wing <1 at 233 dot email>

pkgbase='frp'
pkgname=('frpc' 'frps')
pkgver=0.29.0
pkgrel=1
pkgdesc="A fast reverse proxy to help you expose a local server behind a NAT or firewall to the internet."
arch=('x86_64' 'i686' 'arm' 'armv6h' 'armv7h' 'aarch64')
license=('Apache')
url="https://github.com/fatedier/frp"
depends=('glibc')
makedepends=('go')

source=("${pkgbase}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz")

sha256sums=('5d7980b81cfd055e3e5bb7a120098f94342656f647cb906ea075912f63568816')

prepare() {
  cd "${pkgbase}-${pkgver}"
  sed -i 's#go build -o bin/#go build -mod=vendor -o bin/#g' Makefile
}

build() {
  #make all
  #export GOPATH=`pwd`"/vendor"
  cd "${pkgbase}-${pkgver}"
  make build
}

check() {
  cd "${pkgbase}-${pkgver}"
  sed -i 's#go test -v#go test -mod=vendor -v#g' Makefile
  make test
}

packaging() {
  install -Dm755  ${srcdir}/${pkgbase}-${pkgver}/bin/${1} ${pkgdir}/usr/bin/${1}

  install -Dm644 ${srcdir}/${pkgbase}-${pkgver}/conf/${1}.ini ${pkgdir}/etc/frp/${1}.ini
  install -Dm644 ${srcdir}/${pkgbase}-${pkgver}/conf/${1}_full.ini ${pkgdir}/etc/frp/${1}_full.ini

  install -Dm644 ${srcdir}/${pkgbase}-${pkgver}/conf/systemd/${1}.service  ${pkgdir}/usr/lib/systemd/system/${1}.service
  install -Dm644 ${srcdir}/${pkgbase}-${pkgver}/conf/systemd/${1}@.service  ${pkgdir}/usr/lib/systemd/system/${1}@.service
}

package_frpc() {
  _name=`echo ${FUNCNAME} | cut -d _ -f 2`
  conflicts=('frp')
  backup=("etc/frp/${_name}.ini" "etc/frp/${_name}_full.ini")

  packaging ${_name}
}

package_frps() {
  _name=`echo ${FUNCNAME} | cut -d _ -f 2`
  conflicts=('frp')
  backup=("etc/frp/${_name}.ini" "etc/frp/${_name}_full.ini")

  packaging ${_name}
}

