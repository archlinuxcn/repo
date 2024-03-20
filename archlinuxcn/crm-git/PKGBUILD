# Maintainer: taotieren <admin@taotieren.com>

pkgname=crm-git
pkgver=0.2.0.r1.gcb4f0ce
pkgrel=1
pkgdesc="crm (Cargo registry manager)"
arch=('any')
url="https://github.com/wtklbm/crm"
license=('MIT' 'Apache-2.0')
provides=(${pkgname%-git})
conflicts=(${pkgname%-git})
replaces=()
depends=('cargo')
makedepends=('git' 'rust')
backup=()
options=('!strip' '!lto')
install=
source=("${pkgname%-git}::git+${url}.git")
sha256sums=('SKIP')

pkgver() {
    cd "${srcdir}/${pkgname%-git}/"
    git describe --long --tags | sed 's/v//g;s/\([^-]*-g\)/r\1/;s/-/./g'
}

build() {
    cd "${srcdir}/${pkgname%-git}/"

    export RUSTUP_TOOLCHAIN=stable
    export CARGO_TARGET_DIR=target
    cargo build --release --all-features
}

check() {
    cd "${srcdir}/${pkgname%-git}/"

    export RUSTUP_TOOLCHAIN=stable
    cargo test --all-features
}

package() {
    cd "${srcdir}/${pkgname%-git}/"

    export RUSTUP_TOOLCHAIN=stable
    cargo install --no-track --all-features --root "$pkgdir/usr/" --path .
}
