# Maintainer: Dct Mei <dctxmei@yandex.com>
# Maintainer: Daniel M. Capella <polyzen@archlinux.org>

pkgname=firefox-esr-decentraleyes
_pkgname=decentraleyes
pkgver=2.0.16
pkgrel=1
pkgdesc='Local emulation of Content Delivery Networks'
arch=('any')
url="https://git.synz.io/Synzvato/decentraleyes"
license=('MPL2')
#groups=('firefox-addons')
depends=('firefox-esr')
depends=('git' 'nodejs' 'strip-nondeterminism' 'yarn' 'zip')
source=("git+${url}.git#tag=v${pkgver}")
b2sums=('SKIP')
validpgpkeys=('A6B7BA10893FE67EE17A9F8FCECC45E1E979013C') # Thomas Rientjes <synzvato@protonmail.com>

build() {
    cd "${srcdir}"/"${_pkgname}"/audit/
    yarn install
    node run
}

package() {
    cd "${srcdir}"/"${_pkgname}"/
    install -d "${pkgdir}"/usr/lib/firefox-esr/browser/extensions
    zip -r \
        "${pkgdir}"/usr/lib/firefox-esr/browser/extensions/jid1-BoFifL9Vbdl2zQ@jetpack.xpi \
        * -x '.git*' 'audit/*' crowdin.yaml
    strip-nondeterminism -t zip "${pkgdir}"/usr/lib/firefox-esr/browser/extensions/*.xpi
}
