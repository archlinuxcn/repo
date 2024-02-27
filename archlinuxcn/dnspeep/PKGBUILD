# Maintainer: Jah Way <jahway603 at protonmail dot com>

pkgname=dnspeep
pkgver=0.1.3
pkgrel=2
pkgdesc='Spy on the DNS queries your computer is making'
url='https://github.com/jvns/dnspeep'
arch=('x86_64')
license=('MIT')
depends=('libpcap')
makedepends=('rust')
provides=('dnspeep')
conflicts=('dnspeep-bin')
source=("$url/archive/v$pkgver.tar.gz")
sha512sums=('82dafdf415678eeff1112a0114806e9e2edb8fea6fd2b7642df2384fcb995a69c80a9674745fcd7fc1baed7a72ecf27756f3a7f0cdf494e6ff9a7e4812e24bc9')

# per https://wiki.archlinux.org/title/Rust_package_guidelines#Prepare
prepare() {
  cd "$pkgname-$pkgver"
  export RUSTUP_TOOLCHAIN=stable
  cargo fetch --locked --target "$(rustc -vV | sed -n 's/host: //p')"
}

build() {
  cd "$pkgname-$pkgver"
  export RUSTUP_TOOLCHAIN=stable
  export CARGO_TARGET_DIR=target
  cargo build --frozen --release --all-features
}

package() {
  install -Dm644 "${srcdir}/$pkgname-$pkgver/License.md" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
  install -Dm755 "${srcdir}/$pkgname-$pkgver/target/release/dnspeep" "${pkgdir}/opt/$pkgname/dnspeep"
  install -Dm755 "${srcdir}/$pkgname-$pkgver/README.md" "${pkgdir}/opt/$pkgname/README.md"

  # link to /usr/bin
  install -d "${pkgdir}/usr/bin"
  ln -s /opt/${pkgname}/dnspeep "${pkgdir}/usr/bin"
}
