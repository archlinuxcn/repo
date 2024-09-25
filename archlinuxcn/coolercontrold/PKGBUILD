# Maintainer: Eren Simsek <18117384-caferen@users.noreply.gitlab.com>
# Maintainer: Guy Boldon <gb@guyboldon.com>

pkgname=coolercontrold
pkgver=1.4.1
pkgrel=1
pkgdesc="A program to monitor and control your cooling devices. This package contains the CoolerControl service daemon."
arch=('x86_64')
url="https://gitlab.com/coolercontrol/coolercontrol"
license=('GPL-3.0-or-later')
depends=(
  'libdrm'
  'gcc-libs'
  'glibc'
  'coolercontrol-liqctld'
)
makedepends=(
  'cargo'
  'nodejs>=18'
  'npm'
)
optdepends=(
  'nvidia-utils: NVIDIA GPU support'
)
provides=(
  "$pkgname"
)
conflicts=(
  "$pkgname"
)
# lto is handled by cargo and can conflict with makepkg settings
options=(
  !lto
)
source=(
  "https://gitlab.com/coolercontrol/coolercontrol/-/archive/$pkgver/${pkgname%d}-$pkgver.tar.gz"
)
sha256sums=(
  '378ca7d9bb4ffc5caa5fe08c17e4a2986397a59c7305fb1511140e52b7950098'
)

build() {
  cd "${srcdir}/${pkgname%d}-$pkgver/coolercontrol-ui"
  npm ci
  npm run build
  cp -r dist/* "${srcdir}/${pkgname%d}-$pkgver/$pkgname/resources/app/"
  cd "${srcdir}/${pkgname%d}-$pkgver/$pkgname"
  export RUSTUP_TOOLCHAIN=stable
  export CARGO_TARGET_DIR=target
  cargo build --release --locked
}

check() {
  cd "${srcdir}/${pkgname%d}-$pkgver/$pkgname/target/release"
  ./coolercontrold --version
}

package() {
  cd "${srcdir}/${pkgname%d}-$pkgver/$pkgname"
  install -Dm755 "target/release/$pkgname" -t "$pkgdir/usr/bin"

  cd "${srcdir}/${pkgname%d}-$pkgver"
  # systemd service files
  install -Dm644 "packaging/systemd/${pkgname}.service" -t "$pkgdir/usr/lib/systemd/system/"

  install -Dm644 README.md -t "$pkgdir/usr/share/doc/$pkgname"
  install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname"
}
