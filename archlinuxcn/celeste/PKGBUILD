# Maintainer: Mark Wagie <mark dot wagie at proton dot me>
pkgname=celeste
pkgver=0.8.2
pkgrel=1
pkgdesc="GUI file synchronization client that can sync with any cloud provider"
arch=('x86_64')
url="https://github.com/hwittenborn/celeste"
license=('GPL-3.0-or-later')
depends=('libadwaita' 'rclone')
makedepends=('cargo-nightly' 'clang' 'go' 'just')
source=("$pkgname-$pkgver.tar.gz::$url/archive/refs/tags/v$pkgver.tar.gz")
sha256sums=('a79bffb746e75c58773f55eda4c422d7b06d57d57ad813f353a56f017aeea690')

prepare() {
  cd "$pkgname-$pkgver"
  export CARGO_HOME="$srcdir/cargo-home"
  export RUSTUP_TOOLCHAIN=nightly
  cargo fetch --target "$CARCH-unknown-linux-gnu"
}

build() {
  cd "$pkgname-$pkgver"
  CFLAGS+=" -ffat-lto-objects"
  export CARGO_HOME="$srcdir/cargo-home"
  export RUSTUP_TOOLCHAIN=nightly
  export GOPATH="$srcdir/gopath"
  export CGO_CPPFLAGS="${CPPFLAGS}"
  export CGO_CFLAGS="${CFLAGS}"
  export CGO_CXXFLAGS="${CXXFLAGS}"
  export CGO_LDFLAGS="${LDFLAGS}"
  export GOFLAGS="-buildmode=pie -trimpath -ldflags=-linkmode=external -mod=readonly -modcacherw"
  just build

  # Clean module cache for makepkg -C
  go clean -modcache
}

package() {
  cd "$pkgname-$pkgver"
  DESTDIR="$pkgdir" just install
}
