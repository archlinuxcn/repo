# Maintainer: Zhanibek Adilbekov <zhanibek.adilbekov@pm.me>
# Maintainer: Caleb Macalennan <caleb@alerque.com>
# Contributor: Eli Schwartz <eschwartz@archlinux.org>
# Contributor: Stefan Tatschner <stefan.tatschner@gmail.com>

pkgname=git-extras
pkgver=6.4.0
pkgrel=1
pkgdesc="GIT utilities -- repo summary, commit counting, repl, changelog population and more"
arch=('any')
url="https://github.com/tj/${pkgname}"
license=('MIT')
depends=('git')
install=$pkgname.install
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz")
b2sums=('bffbc8efcf1cf030bceb20b953e1cbbc067c8383ced38b786c21eb9bd9b7d3febd3d8aae652c0dd731de688d3cfa225c3aec91d6b9c590459b576db113ca0af0')

package() {
    cd "${srcdir}/${pkgname}-${pkgver}"

    # avoid annoying interactive prompts if an alias is in your gitconfig
    export GIT_CONFIG=/dev/null
    make DESTDIR="${pkgdir}" PREFIX=/usr SYSCONFDIR=/etc install
    install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"

    # add documentation for completions, which do not work when autoloaded
    mkdir -p "${pkgdir}"/usr/share/doc/git-extras/
    cp etc/*.zsh etc/*.fish "${pkgdir}"/usr/share/doc/git-extras/
}
