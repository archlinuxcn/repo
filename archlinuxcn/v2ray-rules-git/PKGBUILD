# Maintainer: Poscat <poscat@mail.poscat.moe>

pkgname=v2ray-rules-git
pkgver=r6.32b35fd
pkgrel=2
pkgdesc="A simple script for v2ray to set up a transparent proxy."
arch=('x86_64')
url="https://github.com/poscat0x04/v2ray-rules"
license=('MIT')
provides=("v2ray-rules")
conflicts=()
makedepends=('git')
depends=('nftables' 'python')
source=("${pkgname}::git://github.com/poscat0x04/v2ray-rules")
noextract=()
sha256sums=('SKIP')

pkgver() {
  cd "${srcdir}/${pkgname}"
  printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

prepare() {
    cd "${srcdir}/${pkgname}"
    git submodule update --init
}

build() {
    cd "${srcdir}/${pkgname}"
}

package() {
    cd "${srcdir}/${pkgname}"
    install -D -m 755 v2ray-rules "${pkgdir}/usr/bin/v2ray-rules"
    install -D -m 755 v2ray-rules-template "${pkgdir}/usr/share/v2ray-rules/v2ray-rules-template"
}
