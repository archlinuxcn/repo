# Maintainer: Zhanibek Adilbekov <zhanibek.adilbekov@pm.me>
# Maintainer: Caleb Macalennan <caleb@alerque.com>
# Contributor: Eli Schwartz <eschwartz@archlinux.org>
# Contributor: Stefan Tatschner <stefan.tatschner@gmail.com>

pkgname=git-extras
pkgver=7.0.0
pkgrel=1
pkgdesc="GIT utilities -- repo summary, commit counting, repl, changelog population and more"
arch=('any')
url="https://github.com/tj/${pkgname}"
license=('MIT')
depends=('git')
install=$pkgname.install
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz")
b2sums=('8b6ae331b761729d5f92cd350bf21f4f5ebb5098092e224f49db9fe5ef2cbdcd3fc2783af2fb74a8d22008d35675d9a753e753d5fa60e586dbbde919dab7ff80')

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
