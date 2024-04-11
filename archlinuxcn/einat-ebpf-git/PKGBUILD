# Maintainer: edward-p <edward at edward-p dot xyz>

pkgname=einat-ebpf-git
_pkgname=einat-ebpf
_target=einat
pkgver=0.1.1.r23.g07eafd1
pkgrel=1
pkgdesc="eBPF-based Endpoint-Independent NAT"
arch=('x86_64')
url="https://github.com/EHfive/einat-ebpf"
license=('GPL-2.0-only')
depends=('glibc' 'gcc-libs' 'zlib' 'libelf')
provides=('einat')
conflicts=('einat')
makedepends=('git' 'cargo' 'clang')
source=("$_pkgname::git+https://github.com/EHfive/einat-ebpf.git"
        "einat.service")
sha512sums=('SKIP'
            '84948ad7dd40677eb723d8cc6820718e2f0b5bb5226871e5ded3d5bfc680a64af16dd72cd2ef5e36e1677d74505ec942c7ca1e4444fd7535d89214c5e730bd4f')
options=(!lto !debug)

pkgver(){
  cd "$_pkgname"
  git describe --long --tags --abbrev=7 | sed 's/^v//;s/\([^-]*-g\)/r\1/;s/-/./g'
}

prepare() {
  cd "$_pkgname"
  cargo fetch --locked --target "$(rustc -vV | sed -n 's/host: //p')"
}

build() {
  cd "$_pkgname"
  cargo build --release --features ipv6 --frozen
}

check() {
  cd "$_pkgname"
  cargo test --frozen
}

package() {
  cd "$_pkgname"
  install -Dm 755 "target/release/$_target" -t "$pkgdir/usr/bin"
  install -Dm 644 README.md -t "$pkgdir/usr/share/doc/$pkgname"
  install -Dm 644 config.sample.toml -t "$pkgdir/usr/share/doc/$pkgname"
  install -Dm 644 "$srcdir/einat.service" -t "$pkgdir/usr/lib/systemd/system"
}

# vim: ts=2 sw=2 et:

