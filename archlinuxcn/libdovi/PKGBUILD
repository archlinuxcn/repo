# Maintainer: quietvoid <tcChlisop0@gmail.com>

pkgname=libdovi
pkgver=3.1.1
pkgrel=1
pkgdesc='Library to read and write Dolby Vision metadata (C-API)'
arch=('any')
url='https://github.com/quietvoid/dovi_tool/tree/main/dolby_vision'
license=('MIT')
depends=('gcc-libs' 'glibc')
makedepends=('git' 'cargo' 'cargo-c')
conflicts=('libdovi.so')
provides=('libdovi.so')
source=("git+https://github.com/quietvoid/dovi_tool.git#tag=libdovi-${pkgver}")
sha256sums=(SKIP)

prepare() {
  cargo fetch \
    --locked \
    --manifest-path dovi_tool/dolby_vision/Cargo.toml
}

build() {
  cargo cbuild \
    --release \
    --frozen \
    --prefix=/usr \
    --manifest-path dovi_tool/dolby_vision/Cargo.toml
}

check() {
  cargo test \
    --release \
    --frozen \
    --all-features \
    --manifest-path dovi_tool/dolby_vision/Cargo.toml
}

package() {
  cd dovi_tool/dolby_vision

  cargo cinstall \
    --release \
    --frozen \
    --prefix /usr \
    --destdir "${pkgdir}"

  install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/libdovi/LICENSE"
}
