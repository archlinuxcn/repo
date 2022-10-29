# Contributor: taotieren <admin@taotieren.com>

pkgname=opengnb
pkgver=1.3.0.c
pkgrel=1
pkgdesc="GNB is open source de-centralized VPN to achieve layer3 network via p2p with the ultimate capability of NAT Traversal."
arch=('any')
url="https://github.com/gnbdev/opengnb"
license=('GPLv3')
provides=(${pkgname})
conflicts=(${pkgname})
replaces=()
depends=('miniupnpc')
optdepends=()
makedepends=()
backup=()
options=('!strip')
install=
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/refs/tags/v${pkgver}.tar.gz")
sha256sums=('1f45a3a625bcfaf69cb55ec8fb24307e19bcebdb4ab223d5fe5056188bb691b0')

prepare() {
    cd "${srcdir}/${pkgname}-${pkgver}"
    sed -i 's|-I./libs/miniupnpc|-I/usr/include/miniupnpc/|g'  Makefile.linux
}

build() {
    cd "${srcdir}/${pkgname}-${pkgver}"
    make -f Makefile.linux
}

package() {
    cd "${srcdir}/${pkgname}-${pkgver}"
    make -f Makefile.linux install
    install -dm0755 "${pkgdir}/usr" \
                    "${pkgdir}/usr/lib/systemd/system/" \
                    "${pkgdir}/usr/share/${pkgname}/"
    cp -rv bin "${pkgdir}/usr"
    cp -rv scripts/${pkgname}@.service "${pkgdir}/usr/lib/systemd/system/"
    cp -rv examples/* "${pkgdir}/usr/share/${pkgname}/"
    install -Dm0644 "${srcdir}/${pkgname}-${pkgver}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
