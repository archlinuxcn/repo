# Maintainer: Vimsucks <dev@vimsucks.com>
# Contributor: Metal A-wing <1 at 233 dot email>

pkgbase='frp'
pkgname=('frpc' 'frps')
pkgver=0.46.1
pkgrel=1
pkgdesc="A fast reverse proxy to help you expose a local server behind a NAT or firewall to the internet."
arch=('x86_64' 'i686' 'arm' 'armv6h' 'armv7h' 'aarch64')
license=('Apache')
url="https://github.com/fatedier/frp"
depends=('glibc')
makedepends=('go')

source=(
  "${pkgbase}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz"
  "frpc.service"
  "frpc@.service"
  "frps.service"
  "frps@.service"
)

sha512sums=('16ad01540a7771d9690a5e7c3963bb14f17597cbb63fdd17b7f9fb5857276128677f94f3a431e06cd912dbc65ad2e17e42de208cc6f0148923f56d821e5e78bc'
            '2c96df7eeb6bd36163fb2b389a434f21db3f9c4baca36751e0979a74e8f456714259d4756d77f6733e5a6097f8d6b16d6fdacd94ea66135b05b5502c12a69902'
            '7ccfd7a67b62e76de099c8dd394e40566b67175b0d9b6195433ffc2051c89a83b91c108866b99c8b4266c6c39ff2b5be7e048ce4386aeb3f65568e22dfdd1073'
            'af822dd76ddb5dd07af0947d90c2415788a229b923d444aa955100e593b654fe6b89c564afb001a3f52db888a1fbd68d5b3bffa805a39c7435634633b137115a'
            '9d26d00d3959bf509d691ecf7656f93cd154ea6990f4479e03067d0b4ccc42200fb17928e33cd27454d4e17b9ae3cac27bce0a13af244a420a8c1f1df01bf461')

build() {
  cd "${pkgbase}-${pkgver}"
  make build
}

check() {
  cd "${pkgbase}-${pkgver}"
  make test
}

packaging() {
  install -Dm755  ${srcdir}/${pkgbase}-${pkgver}/bin/${1} ${pkgdir}/usr/bin/${1}

  install -Dm644 ${srcdir}/${pkgbase}-${pkgver}/conf/${1}.ini ${pkgdir}/etc/frp/${1}.ini
  install -Dm644 ${srcdir}/${pkgbase}-${pkgver}/conf/${1}_full.ini ${pkgdir}/etc/frp/${1}_full.ini

  install -Dm644 ${srcdir}/${1}.service  ${pkgdir}/usr/lib/systemd/system/${1}.service
  install -Dm644 ${srcdir}/${1}@.service  ${pkgdir}/usr/lib/systemd/system/${1}@.service
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

