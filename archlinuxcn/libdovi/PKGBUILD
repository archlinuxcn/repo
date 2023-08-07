# Maintainer: quietvoid <tcChlisop0@gmail.com>

pkgname=libdovi
pkgver=3.2.0
pkgrel=1
pkgdesc='Library to read and write Dolby Vision metadata (C-API)'
_pkgtag="libdovi-${pkgver}"
arch=('x86_64')
url='https://github.com/quietvoid/dovi_tool/tree/main/dolby_vision'
license=('MIT')
depends=('gcc-libs' 'glibc')
makedepends=('cargo' 'cargo-c')
conflicts=('libdovi.so')
provides=('libdovi.so')
source=("https://github.com/quietvoid/dovi_tool/archive/refs/tags/${_pkgtag}.tar.gz")
sha256sums=('23c339b08bf32b66144b8fe17bf9a39f2dc810a37f081e5bc50207af9ae99922')
_rootdir="dovi_tool-${_pkgtag}"

prepare() {
  cargo fetch \
    --manifest-path ${_rootdir}/dolby_vision/Cargo.toml
}

build() {
  cargo cbuild \
    --release \
    --frozen \
    --prefix=/usr \
    --manifest-path ${_rootdir}/dolby_vision/Cargo.toml
}

check() {
  cargo test \
    --release \
    --frozen \
    --all-features \
    --manifest-path ${_rootdir}/dolby_vision/Cargo.toml
}

package() {
  cd ${_rootdir}/dolby_vision

  cargo cinstall \
    --release \
    --frozen \
    --prefix /usr \
    --destdir "${pkgdir}"

  install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/libdovi/LICENSE"
}
