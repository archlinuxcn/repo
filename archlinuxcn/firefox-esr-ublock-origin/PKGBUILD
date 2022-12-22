# Maintainer: Dct Mei <dctxmei@yandex.com>
# Maintainer: Daniel M. Capella <polyzen@archlinux.org>

pkgname=firefox-esr-ublock-origin
_pkgname=uBlock
pkgver=1.46.0
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
b2sums=('SKIP'
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
