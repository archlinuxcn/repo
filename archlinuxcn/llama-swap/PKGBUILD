# Maintainer: fabse
# Contributor: repsac

pkgname=llama-swap
pkgver=v228 # renovate: datasource=github-releases depName=mostlygeek/llama-swap
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
  pnpm
)
provides=(${pkgname})
conflicts=(${pkgname}-bin)
options=(lto !debug)
source=(
  "git+$url.git#tag=$pkgver"
  llama-swap.service
)
sha256sums=('9fd29ebff4ad1b1482db2f7b2bb87b9cdaf17e329319ce252cfb5ff5d08d590b'
            '8f247fec3e347c212006415e23260a4851ccc435ea3fe0b2c7eaed12b49c406c')

prepare() {
  cd "$pkgname"
  go mod download
}
build() {
  cd "$pkgname"

  cd ui-svelte
  pnpm install
  pnpm run build
  cd ..

  local GIT_HASH=$(git rev-parse --short HEAD)
  local BUILD_DATE=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
  go build \
    -trimpath \
    -mod=readonly \
    -ldflags="-X main.commit=${GIT_HASH} -X main.version=${pkgver} -X main.date=${BUILD_DATE}" \
    -o llama-swap .
}
package() {
  cd "$pkgname"

  install -Dm644 -t "$pkgdir/usr/share/licenses/$pkgname" LICENSE.md
  install -Dm644 -t "$pkgdir/etc/llama-swap" config.example.yaml
  install -Dm644 -t "$pkgdir/usr/lib/systemd/system" ../llama-swap.service
  install -Dm755 -t "$pkgdir/usr/bin" llama-swap
}
