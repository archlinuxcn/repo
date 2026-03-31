# Maintainer: Heddxh <g311571057 at gmail dot com>
# Contributor: BryanLiang <liangrui.ch@gmail.com>
# Contributor: meanlint <meanlint@outlook.com>

pkgname=metacubexd-bin
_pkgname=metacubexd
pkgver=1.244.0
pkgrel=1
pkgdesc='Clash.Meta Dashboard, The Official One, XD (Precompiled version)'
arch=('any')
url="https://github.com/MetaCubeX/metacubexd"
license=('MIT')
optdepends=('clash: A rule-based tunnel in Go'
            'sing-box: The universal proxy platform'
            'clash-meta: Another Clash Kernel by MetaCubeX, deprecated name'
            'mihomo: Another Clash Kernel by MetaCubeX')
provides=("${_pkgname}")
conflicts=("${_pkgname}")
source=("${pkgname}-${pkgver}.tgz::${url}/releases/download/v${pkgver}/compressed-dist.tgz"
        "${url}/raw/main/LICENSE")
sha256sums=('94c8a9778f1f1f8e7924db57217b26eb6a16760b77bb15f9c4f27f2e67ad89cb'
            'cd0735ba06f26a0008bbca399890c7ca87fe129aacc302c2e33fb03e60a4e8c3')

package() {
    install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${_pkgname}/LICENSE"

    cd "${srcdir}"
    find . -type f -exec install -Dm 644 {} "${pkgdir}/usr/share/${_pkgname}/"{} \;
}
