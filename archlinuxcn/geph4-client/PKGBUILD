# Maintainer: Dct Mei <dctxmei@yandex.com>

pkgname=geph4-client
pkgver=4.7.0.beta.11
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
options=('!lto')
source=("geph4-client.default"
        "geph4-client.service")
sha256sums=('4e6ac4d3e31d7bf0fd4cb4b9269bbb124501a07a4701ce9728e857751773e4dd'
            'e3d7e3afb1b524e93e60a80a21773a16de17643865bdf6a1a1f2e17fc2cc8e2d'
            '10ad633ed8b7a30b5659f9780b2a04a344f0f44be66301e1e0ff83dee2f53c92')

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
    else
        source+=("${pkgname}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz")
        _pkgver="${pkgver}"
    fi
}

_prepare

build() {
    cd "${srcdir}"/"${pkgname}-${_pkgver}"/
    cargo build --release --manifest-path=Cargo.toml
}

package() {
    cd "${srcdir}"/"${pkgname}-${_pkgver}"/
    install -Dm 644 LICENSE.md "${pkgdir}"/usr/share/licenses/geph4-client/LICENSE
    install -Dm 755 target/release/geph4-client -t "${pkgdir}"/usr/bin/
    install -Dm 644 "${srcdir}"/geph4-client.default "${pkgdir}"/etc/default/geph4-client
    install -Dm 644 "${srcdir}"/geph4-client.service -t "${pkgdir}"/usr/lib/systemd/system/
}
