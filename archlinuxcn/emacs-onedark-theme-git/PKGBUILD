# Maintainer: Poscat <poscat@mail.poscat.moe>

pkgname=emacs-onedark-theme-git
pkgver=r154.623fc08
pkgrel=1
pkgdesc="An Emacs port of the Atom One Dark theme."
arch=('x86_64')
url="https://github.com/jonathanchu/atom-one-dark-theme"
license=('GPL3')
provides=('emacs-onedark-theme')
conflicts=()
makedepends=('git')
depends=('emacs')
source=("${pkgname}::git://github.com/jonathanchu/atom-one-dark-theme")
noextract=()
sha256sums=('SKIP')

pkgver() {
  cd "${srcdir}/${pkgname}"
  printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

prepare() {
    cd "${srcdir}/${pkgname}"
    git submodule update --init
}

build() {
    cd "${srcdir}/${pkgname}"
}

package() {
    cd "${srcdir}/${pkgname}"
    install -D -m 644 atom-one-dark-theme.el "${pkgdir}/usr/share/emacs/site-lisp/onedark-theme/atom-one-dark-theme.el"
}
