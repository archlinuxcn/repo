# Maintainer: Vimsucks <dev@vimsucks.com>
# Contributor: Metal A-wing <1 at 233 dot email>

pkgbase='frp'
pkgname=('frpc' 'frps')
pkgver=0.68.1
pkgrel=4
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

sha512sums=('714199ad4e9bfd917574fe4f3535caca430cca040b39ef39f32511356d9ec63b79e1bd97e57cdd0359e5019e64bdacc249d57943da80282b0ce1cfe5b6a8599c'
            '32f62f961f4f6c4fa192c511b5c5217b296a926e16b2da665c2164729fe0ec0ce3d0ed3c4e223469bbf85bc1d9592b2e1d934712cbbf8e2818fd82dd3f747c3b'
            'f1376736a8fa81d2a4dcf9252789ba34fb890a7df241148809b4f1fdc92f47db78397d49b61555f9bad6e5007422cc984c1713ef0604c52efb16d148476e182f'
            'd4e39337ec4cc5c53408f9d9c1a703f09a35a6011de16c289361843ca9d219ed8393c1c24b90fbbb5ad5c0df7eee7d3ac88f93d0be80e6a2e8bca55f5045dae4'
            '9bfed0ca61558cbe889e1a6d51bdac682f24ad8294b15cc2913706f09defa330aaaa78deec44375966e699a65f77951c706ee18186eddf189a20f8372222f6aa')

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

  install -Dm644 ${srcdir}/${1}.service ${pkgdir}/usr/lib/systemd/system/${1}.service
  install -Dm644 ${srcdir}/${1}@.service ${pkgdir}/usr/lib/systemd/system/${1}@.service

  # completions
  install -Dm644 <(${srcdir}/${pkgbase}-${pkgver}/bin/${1} completion zsh) ${pkgdir}/usr/share/zsh/site-functions/_${1}
  install -Dm644 <(${srcdir}/${pkgbase}-${pkgver}/bin/${1} completion bash) ${pkgdir}/usr/share/bash-completion/completions/${1}
  install -Dm644 <(${srcdir}/${pkgbase}-${pkgver}/bin/${1} completion fish) ${pkgdir}/usr/share/fish/vendor_completions.d/${1}.fish
}

package_frpc() {
  _name=$(echo ${FUNCNAME} | cut -d _ -f 2)
  conflicts=('frp')
  backup=("etc/frp/${_name}.toml" "etc/frp/${_name}_full_example.toml")

  _packaging ${_name}
}

package_frps() {
  _name=$(echo ${FUNCNAME} | cut -d _ -f 2)
  conflicts=('frp')
  backup=("etc/frp/${_name}.toml" "etc/frp/${_name}_full_example.toml")

  _packaging ${_name}
}
