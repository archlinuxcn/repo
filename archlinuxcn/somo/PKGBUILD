# Maintainer: Rafael Dominiquini <rafaeldominiquini at gmail dot com>
# Contributor: David Birks <david@birks.dev>

_pkgauthor=theopfr
_pkgname=somo
pkgname=${_pkgname}
pkgver=1.3.2
pkgrel=1
pkgdesc='A human-friendly alternative to netstat for socket and port monitoring'

url="https://github.com/${_pkgauthor}/${_pkgname}"
license=('MIT')
arch=('x86_64')

provides=("${pkgname}")
conflicts=("${pkgname}"{-git,-bin})

makedepends=('cargo')
depends=('glibc' 'libgcc')

options=('!debug' '!strip')

source=("${_pkgname}-${pkgver}.tgz::${url}/archive/v${pkgver}.tar.gz")
sha256sums=('d9c413f302ee59b7fc831180429aabb8f9f62992b1905af5908a12cd7b808974')

prepare() {
    cd "${pkgname}-${pkgver}" || exit

    export RUSTUP_TOOLCHAIN=stable
    cargo fetch --locked --target "$(rustc -vV | sed -n 's/host: //p')"
}

build() {
    cd "${pkgname}-${pkgver}" || exit

    export RUSTUP_TOOLCHAIN=stable
    export CARGO_TARGET_DIR=target
    cargo build --frozen --release --all-features

    mkdir -p completions
    ./"target/release/${_pkgname}" generate-completions bash > "completions/${_pkgname}.bash"
    ./"target/release/${_pkgname}" generate-completions zsh > "completions/${_pkgname}.zsh"
    ./"target/release/${_pkgname}" generate-completions fish > "completions/${_pkgname}.fish"
}

check() {
    cd "${pkgname}-${pkgver}" || exit

    export RUSTUP_TOOLCHAIN=stable
    cargo test --frozen --all-features
}

package() {
    cd "${pkgname}-${pkgver}" || exit

    install -Dm0755 "target/release/${_pkgname}" "${pkgdir}/usr/bin/${_pkgname}"

    install -D -m644 "completions/${_pkgname}.bash" "${pkgdir}/usr/share/bash-completion/completions/${_pkgname}"
    install -D -m644 "completions/${_pkgname}.zsh" "${pkgdir}/usr/share/zsh/site-functions/_${_pkgname}"
    install -D -m644 "completions/${_pkgname}.fish" "${pkgdir}/usr/share/fish/vendor_completions.d/${_pkgname}.fish"

    install -Dm644 "README.md" "${pkgdir}/usr/share/doc/${pkgname}/README.md"

    install -Dm644 "LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
