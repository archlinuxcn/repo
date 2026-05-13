# Maintainer: Zhanibek Adilbekov <zhanibek.adilbekov@pm.me>
# Maintainer: Caleb Macalennan <caleb@alerque.com>
# Contributor: Eli Schwartz <eschwartz@archlinux.org>
# Contributor: Stefan Tatschner <stefan.tatschner@gmail.com>

pkgname=git-extras
pkgver=7.5.0
pkgrel=1
pkgdesc="GIT utilities -- repo summary, commit counting, repl, changelog population and more"
arch=('any')
url="https://github.com/tj/${pkgname}"
license=('MIT')
depends=('git')
install=$pkgname.install
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz")
b2sums=('85336939515959cab1b3398f62220ac5e20a895e1e40e7539ce9dd92cba13a183cfaebb7626c07200395bf7bd0bc651400f4a86e91138e052e4a18a8fdcbd55d')

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
