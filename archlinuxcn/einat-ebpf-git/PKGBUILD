# Maintainer: edward-p <edward at edward-p dot xyz>

pkgname=einat-ebpf-git
_pkgname=einat-ebpf
_target=einat
pkgver=0.1.4.r8.gd9ce880
pkgrel=2
pkgdesc="eBPF-based Endpoint-Independent NAT"
arch=('x86_64')
url="https://github.com/EHfive/einat-ebpf"
license=('GPL-2.0-only')
depends=('glibc' 'gcc-libs' 'zlib' 'libelf' 'libbpf')
provides=('einat')
conflicts=('einat')
makedepends=('git' 'cargo' 'clang' 'llvm')
source=("$_pkgname::git+https://github.com/EHfive/einat-ebpf.git"
        "einat.service")
sha512sums=('SKIP'
            '52ce570ef64664cc9eb1180c9f98fbc00249db7ed28352835d4574383e399fd5b2f142515169e609344538680b4c949c5342a0607b31a16ae4857491da052b91')
options=(!lto)

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
  cargo build --release --features libbpf,pkg-config,ipv6 --frozen
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

