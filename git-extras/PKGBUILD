# Maintainer: Eli Schwartz <eschwartz@archlinux.org>
# Contributor: Stefan Tatschner <stefan.tatschner@gmail.com>

# All my PKGBUILDs are managed at https://github.com/eli-schwartz/pkgbuilds

pkgname=git-extras
pkgver=4.6.0
pkgrel=1
pkgdesc="GIT utilities -- repo summary, commit counting, repl, changelog population and more"
arch=('any')
url="https://github.com/tj/${pkgname}"
license=('MIT')
depends=('git')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz")
sha256sums=('e3baa3a54cb3d8f2e09409e9dec22c76c0e4802e44e108b6cc0b4b0245e4e5ca')

package() {
    cd "${srcdir}/${pkgname}-${pkgver}"
    make DESTDIR="${pkgdir}" PREFIX=/usr SYSCONFDIR=/etc install
    install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
