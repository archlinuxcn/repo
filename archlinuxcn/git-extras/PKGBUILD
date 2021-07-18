# Maintainer: Eli Schwartz <eschwartz@archlinux.org>
# Contributor: Stefan Tatschner <stefan.tatschner@gmail.com>

# All my PKGBUILDs are managed at https://github.com/eli-schwartz/pkgbuilds

pkgname=git-extras
pkgver=6.2.0
pkgrel=1
pkgdesc="GIT utilities -- repo summary, commit counting, repl, changelog population and more"
arch=('any')
url="https://github.com/tj/${pkgname}"
license=('MIT')
depends=('git')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz")
sha256sums=('151bc129f717179c1f7b6c83faf1d4829eeddef8b7c501dac05dc38c28270c3e')
b2sums=('71e3be3f56ca049d2060c79b8dd52aacf613d9157fc5d6fa76c827b59e9355f16903cce94e09dcf73e0c7c4f81b422a37234dbc8f9eb146ca9925da8778ea2dc')

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
