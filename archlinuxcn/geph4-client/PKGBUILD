# Maintainer: Dct Mei <dctxmei@yandex.com>

pkgname=geph4-client
pkgver=4.5.2.alpha.2
pkgrel=1
pkgdesc="A command-line Geph4 toolset"
arch=('x86_64')
url="https://github.com/geph-official/geph4"
license=('GPL3')
groups=('geph4')
depends=('gcc-libs')
makedepends=('rust')
conflicts=('geph4-client-git')
backup=('etc/default/geph4-client')
source=("geph4-client.default"
        "geph4-client.service")
sha256sums=('fe10aa9e8ecc58e3b01487cb60c6fe970dd80343d1b715744e734077b1e14f66'
            '2aef927e466ce22796bbaec6d618f6178d0251e6d0ba1df3c526d3374dd903da'
            'a5e1765549c7f25d2578d05de302fcf6bcddc375863433ad315d1cc2ce15db42')

_prepare() {
    if [[ "${pkgver}" =~ '.alpha' ]]; then
        _pkgver="${pkgver%%.alpha*}"
        _alpha="${pkgver#*.alpha}"
        source+=("${pkgname}-${pkgver}.tar.gz::${url}/archive/v${_pkgver}-alpha${_alpha}.tar.gz")
        _pkgver="${_pkgver}-alpha${_alpha}"
    elif [[ "${pkgver}" =~ '.beta' ]]; then
        _pkgver="${pkgver%%.beta*}"
        _beta="${pkgver#*.beta}"
        source+=("${pkgname}-${pkgver}.tar.gz::${url}/archive/v${_pkgver}-beta${_beta}.tar.gz")
        _pkgver="${_pkgver}-beta${_beta}"
    fi
}

_prepare

build() {
    cd "${srcdir}"/"${groups}-${_pkgver}"/
    cargo build --release --manifest-path=Cargo.toml
}

package() {
    cd "${srcdir}"/"${groups}-${_pkgver}"/
    install -Dm 644 LICENSE.md "${pkgdir}"/usr/share/licenses/geph4-client/LICENSE
    install -Dm 755 target/release/geph4-client -t "${pkgdir}"/usr/bin/
    install -Dm 644 "${srcdir}"/geph4-client.default "${pkgdir}"/etc/default/geph4-client
    install -Dm 644 "${srcdir}"/geph4-client.service -t "${pkgdir}"/usr/lib/systemd/system/
}
