# Maintainer: Eli Schwartz <eschwartz@archlinux.org>
# Contributor: Stefan Tatschner <stefan.tatschner@gmail.com>

# All my PKGBUILDs are managed at https://github.com/eli-schwartz/pkgbuilds

pkgname=git-extras
pkgver=5.1.0
pkgrel=2
pkgdesc="GIT utilities -- repo summary, commit counting, repl, changelog population and more"
arch=('any')
url="https://github.com/tj/${pkgname}"
license=('MIT')
depends=('git')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz")
sha256sums=('432f73f178345b69d98fb48ccdc04839bafb605f2f8cc3e5bb8f87d497ef3e7d')
b2sums=('279f0476c2ec6f30531d77d5c348bc6c0a823a622f7ec96ae65b1b2861a7c3ab1bf66eb246d031d0cfb4e1cc5fd3c2bfbf1418bc619dc3b81c6f0d7ffdcccd0a')

prepare() {
    cd "${srcdir}/${pkgname}-${pkgver}"

    # remove conflicting namespace with well-known projects
    # https://github.com/tj/git-extras/issues/842
    for i in bug chore refactor; do
        rm -v bin/git-$i man/git-$i.*
    done
}

package() {
    cd "${srcdir}/${pkgname}-${pkgver}"

    # avoid annoying interactive prompts if an alias is in your gitconfig
    export GIT_CONFIG=/dev/null
    make DESTDIR="${pkgdir}" PREFIX=/usr SYSCONFDIR=/etc install
    install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
