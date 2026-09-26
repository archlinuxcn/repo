# Maintainer: fabse
# Contributor: repsac

pkgname=llama-swap
pkgver=v259 # renovate: datasource=github-releases depName=mostlygeek/llama-swap
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
sha256sums=('b2cea9386923e99cc7fdb765c3f0f96044bf232d0823b1b65ef584aa42e6b405'
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
