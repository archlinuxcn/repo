# Maintainer: Bin Jin <bjin@ctrl-d.org>
# Contributor: Whyme Lyu <callme5long@gmail.com>

pkgname=dnsproxy
pkgver=0.73.4
pkgrel=1
pkgdesc="Simple DNS proxy with DoH, DoT, DoQ and DNSCrypt support"
arch=('x86_64')
url="https://github.com/AdguardTeam/dnsproxy"
license=('Apache')
source=("dnsproxy.service"
        "https://github.com/AdguardTeam/dnsproxy/archive/v${pkgver}.tar.gz")
makedepends=("go")
sha256sums=('002deb38e7d69beb8848c57a7ba0d00437c542589baccc6dab074767ffa64b75'
            '8a7779900d2449cdc7e9bf1b311a3317c04d78db24efde4186c169cc8a501a5f')

_conf=etc/dnsproxy/dnsproxy.yaml
backup=($_conf)

build() {
    cd "${srcdir}/${pkgname}-${pkgver}"
    version_pkg='github.com/AdguardTeam/dnsproxy/internal/version'
    go build --ldflags "-linkmode=external -s -w -X ${version_pkg}.version=${pkgver}" -mod=readonly -v -trimpath -buildmode=pie
}

package() {
    cd "${srcdir}/${pkgname}-${pkgver}"
    install -Dm755 dnsproxy "${pkgdir}/usr/bin/dnsproxy"
    install -Dm644 LICENSE "$pkgdir"/usr/share/licenses/dnsproxy/LICENSE
    install -Dm644 README.md "$pkgdir"/usr/share/doc/dnsproxy/README.md
    install -Dm644 config.yaml.dist "$pkgdir/$_conf"

    install -Dm644 "${srcdir}/dnsproxy.service" "${pkgdir}/usr/lib/systemd/system/dnsproxy.service"
}
