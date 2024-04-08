# Maintainer: Dct Mei <dctxmei@yandex.com>
# Maintainer: Daniel M. Capella <polyzen@archlinux.org>

pkgname=firefox-esr-ublock-origin
_pkgname=uBlock
pkgver=1.57.2
pkgrel=1
pkgdesc='Efficient blocker add-on for various browsers. Fast, potent, and lean'
arch=('any')
url="https://github.com/gorhill/uBlock"
license=('GPL3')
#groups=('firefox-addons')
depends=('firefox-esr')
makedepends=('git' 'npm' 'python' 'strip-nondeterminism' 'zip')
source=("git+$url.git#commit=$pkgver?signed"
        "git+https://github.com/uBlockOrigin/uAssets.git")
b2sums=('4d9815c11807e280ee43f255c7f97ac40e2657d7022a4107ff8f9989a2a0896c465d3503470de41a85cc9d05ea2f5cfd2169619beb17b0aca7419395dfd4a062'
        'SKIP')
validpgpkeys=('603B28AA5D6CD687A554347425E1490B761470C2') # Raymond Hill <rhill@raymondhill.net>

prepare() {
    cd "${srcdir}"/"${_pkgname}"/
    git submodule init
    git config submodule.submodules/uAssets.url ../uAssets
    git submodule update
}

build() {
    cd "${srcdir}"/"${_pkgname}"/
    make
    strip-nondeterminism -t zip dist/build/uBlock0.firefox.xpi
}

check() {
    cd "${srcdir}"/"${_pkgname}"/
    make test
}

package() {
    cd "${srcdir}"/"${_pkgname}"/dist/build/
    install -Dm 644 uBlock0.firefox.xpi \
            "$pkgdir"/usr/lib/firefox-esr/browser/extensions/uBlock0@raymondhill.net.xpi
}
