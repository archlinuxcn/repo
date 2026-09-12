# Maintainer: Rafael Dominiquini <rafaeldominiquini at gmail dot com>
# Contributor: David Birks <david@birks.dev>

_pkgauthor=theopfr
_pkgname=somo
pkgname=${_pkgname}
pkgver=1.4.0
pkgrel=1
pkgdesc='A human-friendly alternative to netstat for socket and port monitoring'

url="https://github.com/${_pkgauthor}/${_pkgname}"
license=('MIT')
arch=('x86_64')

provides=("${pkgname}")
conflicts=("${pkgname}"{-git,-bin})

makedepends=('cargo')
depends=('glibc' 'libgcc')

options=('!debug' '!lto' '!strip')

source=("${_pkgname}-${pkgver}.tgz::${url}/archive/v${pkgver}.tar.gz")
sha256sums=('b084d1617055f39f17e3ae08fe1fdba023b43f8f928c8edf53af0f8ce8a2b14a')

_target="target"
_toolchain="stable"
_bin="${_target}/release/${_pkgname}"

prepare() {
    cd "${pkgname}-${pkgver}" || exit

    export RUSTUP_TOOLCHAIN=${_toolchain}
    cargo fetch --locked --target "$(rustc -vV | sed -n 's/host: //p')"
}

build() {
    cd "${pkgname}-${pkgver}" || exit

    export CARGO_TARGET_DIR=${_target}
    export RUSTUP_TOOLCHAIN=${_toolchain}
    cargo build --frozen --release --all-features

    mkdir -p completions
    ./"${_bin}" generate-completions bash > "completions/${_pkgname}.bash"
    ./"${_bin}" generate-completions zsh > "completions/${_pkgname}.zsh"
    ./"${_bin}" generate-completions fish > "completions/${_pkgname}.fish"
}

check() {
    cd "${pkgname}-${pkgver}" || exit

    export RUSTUP_TOOLCHAIN=stable
    cargo test --frozen --all-features
}

package() {
    cd "${pkgname}-${pkgver}" || exit

    install -Dm0755 "${_bin}" "${pkgdir}/usr/bin/${_pkgname}"

    install -D -m644 "completions/${_pkgname}.bash" "${pkgdir}/usr/share/bash-completion/completions/${_pkgname}"
    install -D -m644 "completions/${_pkgname}.zsh" "${pkgdir}/usr/share/zsh/site-functions/_${_pkgname}"
    install -D -m644 "completions/${_pkgname}.fish" "${pkgdir}/usr/share/fish/vendor_completions.d/${_pkgname}.fish"

    install -Dm644 "README.md" "${pkgdir}/usr/share/doc/${pkgname}/README.md"

    install -Dm644 "LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
