# Maintainer: Fabio 'Lolix' Loli <fabio.loli@disroot.org> -> https://github.com/FabioLolix
# Maintainer: Sean E. Russell <ser@ser1.net> -> also the program developer
# Contributor: Caleb Bassi <calebjbassi@gmail.com>

pkgname=gotop
pkgver=4.2.0
pkgrel=3
pkgdesc="A terminal based graphical activity monitor inspired by gtop and vtop"
arch=(x86_64 i686 arm armv6h armv7h aarch64)
url="https://github.com/xxxserxxx/gotop"
license=(MIT)
changelog=Changelog
depends=(glibc)
makedepends=(go)
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz")

build() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  CGO_ENABLED=0

  go build \
    -gcflags "all=-trimpath=${PWD}" \
    -asmflags "all=-trimpath=${PWD}" \
    -ldflags "-X main.Version=v${pkgver} -extldflags '-s -w'" \
    -buildmode=pie \
    ./cmd/gotop
  go run ./cmd/gotop --create-manpage > gotop.1
  gzip gotop.1
}

package() {
  install -Dm755 "${srcdir}"/${pkgname}-${pkgver}/gotop "${pkgdir}"/usr/bin/gotop
  install -Dm644 "${srcdir}"/${pkgname}-${pkgver}/gotop.1.gz "${pkgdir}"/usr/share/man/man1/gotop.1.gz
  install -Dm644 "${srcdir}"/${pkgname}-${pkgver}/README.md -t "${pkgdir}"/usr/share/doc/gotop/
  install -Dm644 "${srcdir}"/${pkgname}-${pkgver}/CHANGELOG.md -t "${pkgdir}"/usr/share/doc/gotop/
  install -Dm644 "${srcdir}"/${pkgname}-${pkgver}/layouts/htop "${pkgdir}"/etc/gotop/htop
  install -Dm644 "${srcdir}"/${pkgname}-${pkgver}/LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
sha256sums=('e9d9041903acb6bd3ffe94e0a02e69eea53f1128274da1bfe00fe44331ccceb1')
