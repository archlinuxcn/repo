# Maintainer: Mark Wagie <mark dot wagie at proton dot me>
pkgname=mission-center
pkgver=0.3.2
pkgrel=1
pkgdesc="Monitor your CPU, Memory, Disk, Network and GPU usage"
arch=('x86_64')
url="https://gitlab.com/mission-center-devs/mission-center"
license=('GPL3')
depends=('dmidecode' 'libadwaita')
makedepends=('blueprint-compiler' 'cargo' 'meson')
checkdepends=('appstream-glib')
options=('!lto')
_commit=be47f8c560487efc6e6a419d59c69bfbdb819324
source=("$url/-/archive/v$pkgver/$pkgname-v$pkgver.tar.gz"
        "nvtop-$_commit.tar.gz::https://github.com/Syllo/nvtop/archive/$_commit.tar.gz")
sha256sums=('4518988508a06890c3bf89652e833912bf750c23161dc75cf393cece021d2360'
            '47c963deb1d22c75e92ca2cc7fcd1e1552cfa6da70e9d51be6a80da45249035f')

prepare() {
  cd "$pkgname-v$pkgver"
  export CARGO_HOME="$srcdir/cargo-home"
  export RUSTUP_TOOLCHAIN=stable
  cargo fetch --target "$CARCH-unknown-linux-gnu"

  cp -rf "$srcdir/nvtop-$_commit" subprojects/
  cd "subprojects/nvtop-$_commit"
  find ../packagefiles -type f -name 'nvtop-*' -exec sh -c 'patch -p1 < {}' \;
}

build() {
  export CARGO_HOME="$srcdir/cargo-home"
  export RUSTUP_TOOLCHAIN=stable
  arch-meson "$pkgname-v$pkgver" build
  meson compile -C build
}

check() {
  meson test -C build --print-errorlogs || :
}

package() {
  meson install -C build --no-rebuild --destdir "$pkgdir"
}
