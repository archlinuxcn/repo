# Maintainer: Vimsucks <dev@vimsucks.com>
# Contributor: Metal A-wing <1 at 233 dot email>

pkgbase='frp'
pkgname=('frpc' 'frps')
pkgver=0.53.2
pkgrel=5
pkgdesc="A fast reverse proxy to help you expose a local server behind a NAT or firewall to the internet."
arch=('x86_64' 'i686' 'arm' 'armv6h' 'armv7h' 'aarch64')
license=('Apache-2.0')
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

sha512sums=('c1f0acff002dbdef001d04c3dcd5ca138c33a36b8e5ad119a555f0dd05f4e6200c915e1481eab58c02e650a058f0b3f75310b9a50ad4756087f69f9fe74377b4'
            'c9d7c4b24faf7c086a6fd1ca96e345c43fece1dbebe33c8c1bcd8fb12d11c57274d33ad0d197ff874498605ab23d46453890054a643cfa9fec8d8b19e5b0121c'
            'b90edfeeed262472a09fb39beb9c51894ab4b7d61979e878607b201f8ee9463c5ce656e62713cf2108a1bd1d9cf12146d26e1f97760b3d8a07c5be8bed7e693a'
            '90d326d7103301c518f84673ea80650adeb18a154c64bc8daf487bdfa6936525fc42fcc8e0db70cc50df9bae6d3dfdeebec79333bf62e3d079aa8453483db395'
            'b8f9c75893bede053d9d6b1e9e9c596168006d4c92edffa7b2824e7c865e508705c66e879984375e59348b7c83e8438aedff4fab624e06c4e3b25e7ebc5add52')

build() {
  cd "${pkgbase}-${pkgver}"
  make build
}

check() {
  cd "${pkgbase}-${pkgver}"
  make test
}

_packaging() {
  install -Dm755 ${srcdir}/${pkgbase}-${pkgver}/bin/${1} ${pkgdir}/usr/bin/${1}

  install -Dm644 ${srcdir}/${pkgbase}-${pkgver}/conf/${1}.toml ${pkgdir}/etc/frp/${1}.toml
  install -Dm644 ${srcdir}/${pkgbase}-${pkgver}/conf/${1}_full_example.toml ${pkgdir}/etc/frp/${1}_full_example.toml

  install -Dm644 ${srcdir}/${1}.service  ${pkgdir}/usr/lib/systemd/system/${1}.service
  install -Dm644 ${srcdir}/${1}@.service  ${pkgdir}/usr/lib/systemd/system/${1}@.service
}

package_frpc() {
  _name=`echo ${FUNCNAME} | cut -d _ -f 2`
  conflicts=('frp')
  backup=("etc/frp/${_name}.toml" "etc/frp/${_name}_full_example.toml")

  _packaging ${_name}
}

package_frps() {
  _name=`echo ${FUNCNAME} | cut -d _ -f 2`
  conflicts=('frp')
  backup=("etc/frp/${_name}.toml" "etc/frp/${_name}_full_example.toml")

  _packaging ${_name}
}
