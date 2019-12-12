# Maintainer: Eli Schwartz <eschwartz@archlinux.org>
# Contributor: Stefan Tatschner <stefan.tatschner@gmail.com>

# All my PKGBUILDs are managed at https://github.com/eli-schwartz/pkgbuilds

pkgname=git-extras
pkgver=5.0.0
pkgrel=1
pkgdesc="GIT utilities -- repo summary, commit counting, repl, changelog population and more"
arch=('any')
url="https://github.com/tj/${pkgname}"
license=('MIT')
depends=('git')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz")
sha256sums=('7fb70af14c12119d184fe33f5f86046b7ad175ee81fa89e75fb54a5b3aff609a')
b2sums=('10c607da5685ed40a4e535e2e72d3fa99a398a9cc25e2d49ee89345d299324fd7bd37e5e320e8d017cbaf0790b76b119a5fcf6588f7ba42062b1f4d00211e078')

package() {
    cd "${srcdir}/${pkgname}-${pkgver}"
    make DESTDIR="${pkgdir}" PREFIX=/usr SYSCONFDIR=/etc install
    install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
