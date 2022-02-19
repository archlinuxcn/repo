# Maintainer: Bryce Chidester <bryce@cobryce.com>

_pkgname=rescrobbled
pkgname="${_pkgname}-git"
pkgver=0.3.0.r0.g0aff874
pkgrel=1
pkgdesc="Music scrobbler daemon using the MPRIS D-Bus interface."
arch=('x86_64')
url="https://github.com/InputUsername/rescrobbled"
license=('GPL3')
depends=('dbus')
makedepends=('rust' 'cargo' 'git')
provides=("${_pkgname}")
conflicts=("${_pkgname}")
source=('git+https://github.com/InputUsername/rescrobbled.git'
        'rescrobbled.service')
sha256sums=('SKIP'
            'a5a9735c34c1851bfbcceddbbc3d5116fe12324281916dbb29dc7d68b89f6b74')

pkgver() {
  cd "${srcdir}/${_pkgname}"
  git describe --long --tags | sed 's/^v//;s/\([^-]*-g\)/r\1/;s/-/./g'
}

prepare() {
  cd "${srcdir}/${_pkgname}"
  cargo fetch --locked
}

build() {
  cd "${srcdir}/${_pkgname}"
  cargo build --release --locked --all-features --target-dir=target
}

check() {
  cd "${srcdir}/${_pkgname}"
  cargo test --release --locked --all-features
}

package() {
  cd "${srcdir}/${_pkgname}"
  install -Dm755 "target/release/${_pkgname}" "${pkgdir}/usr/bin/${_pkgname}"
  install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${_pkgname}/LICENSE"
  install -Dm644 "${srcdir}/rescrobbled.service" -t "${pkgdir}/usr/lib/systemd/user"
}

