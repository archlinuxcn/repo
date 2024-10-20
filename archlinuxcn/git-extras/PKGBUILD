# Maintainer: Zhanibek Adilbekov <zhanibek.adilbekov@pm.me>
# Maintainer: Caleb Macalennan <caleb@alerque.com>
# Contributor: Eli Schwartz <eschwartz@archlinux.org>
# Contributor: Stefan Tatschner <stefan.tatschner@gmail.com>

pkgname=git-extras
pkgver=7.3.0
pkgrel=1
pkgdesc="GIT utilities -- repo summary, commit counting, repl, changelog population and more"
arch=('any')
url="https://github.com/tj/${pkgname}"
license=('MIT')
depends=('git')
install=$pkgname.install
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz")
b2sums=('f9f32688fa286be67f6e64c4d061c9587bb664c60f1af2042130b6b18b04500f44cb9991a86c458cf5b613eebf3de6c119da0738b9425dff80a7036089ad4337')

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
