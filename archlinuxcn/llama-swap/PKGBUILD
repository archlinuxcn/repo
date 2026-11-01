# Maintainer: fabse
# Contributor: repsac

pkgname=llama-swap
pkgver=v269 # renovate: datasource=github-releases depName=mostlygeek/llama-swap
pkgrel=1
pkgdesc="Model swapping for llama.cpp (or any local OpenAPI compatible server)"
arch=(x86_64 aarch64)
url="https://github.com/mostlygeek/llama-swap"
license=('MIT')
depends=(
  curl
  gcc-libs
  glibc
)
makedepends=(
  git
  go
  npm
)
provides=(${pkgname})
conflicts=(${pkgname}-bin)
options=(lto !debug)
source=(
  "git+$url.git#tag=$pkgver"
  llama-swap.service
)
sha256sums=('2fac593a86c5352950bf12fb962057bb37b5b29d944786467ac8d28fcc5f6845'
            '8f247fec3e347c212006415e23260a4851ccc435ea3fe0b2c7eaed12b49c406c')

build() {
  cd "$pkgname"
  
  case "$CARCH" in
    x86_64)
      make linux-amd64
      ;;
    aarch64)
      make linux-arm64
      ;;
  esac
}

package() {
  cd "$pkgname"
  
  _binary_name=""
  case "$CARCH" in
    x86_64) _binary_name="llama-swap-linux-amd64" ;;
    aarch64) _binary_name="llama-swap-linux-arm64" ;;
  esac
  
  install -Dm644 -t "$pkgdir/usr/share/licenses/$pkgname" LICENSE.md
  install -Dm644 -t "$pkgdir/etc/llama-swap" docs/config.example.yaml
  install -Dm644 -t "$pkgdir/usr/lib/systemd/system" ../llama-swap.service
  install -Dm755 "build/$_binary_name" "$pkgdir/usr/bin/llama-swap"
}
