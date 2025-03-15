# Maintainer: Heddxh <g311571057 at gmail dot com>
# Contributor: BryanLiang <liangrui.ch@gmail.com>
# Contributor: meanlint <meanlint@outlook.com>

pkgname=metacubexd-bin
_pkgname=metacubexd
pkgver=1.184.0
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
sha256sums=('ed3bb3745f2d403e28446abcf1a04206199f110662612c1a6327cf9a443edd9a'
            'cd0735ba06f26a0008bbca399890c7ca87fe129aacc302c2e33fb03e60a4e8c3')

package() {
    install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${_pkgname}/LICENSE"

    cd "${srcdir}"
    find . -type f -exec install -Dm 644 {} "${pkgdir}/usr/share/${_pkgname}/"{} \;
}
