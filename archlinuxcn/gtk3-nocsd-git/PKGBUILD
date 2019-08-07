# Maintainer:  Callum Parsey <neoninteger@protonmail.com>
# Contributor: Sefa Eyeoglu <contact@scrumplex.net>
# Contributor: Kazutoshi Noguchi <noguchi.kazutosi+lGlcOenS [at] gmail [dot] com>
# Contributor: Marco Kundt <mrckndt [at] gmail [dot] com>

pkgname=gtk3-nocsd-git
pkgver=r63.3f91a6b
pkgrel=1
pkgdesc="A hack to disable gtk+ 3 client side decoration"
arch=("i686" "x86_64")
url="https://github.com/ZaWertun/gtk3-nocsd"
license=("LGPL")

conflicts=("gtk3-nocsd")
provides=("gtk3-nocsd")
depends=("gtk3")

makedepends=(
    "git"
    "gobject-introspection"
)

source=(
    "git+https://github.com/ZaWertun/gtk3-nocsd.git"
    "30-gtk3-nocsd.sh"
)

sha512sums=(
    "SKIP"
    "ef7a812887072a19b7b365fd393d808806d1bdb4beb2aa4e46af9cb690dc2a7abc8976a8e5875d91742f3029330ac9229feb6d50141e0c2d35f0d3d8a7400830"
)

install="$pkgname.install"

_gitname="gtk3-nocsd"

pkgver() {
    cd "$srcdir/$_gitname"
    printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

build() {
    cd "$srcdir/$_gitname"
    make
}

package() {
    cd "$srcdir/$_gitname"
    install -D -m 0755 gtk3-nocsd "${pkgdir}"/usr/bin/gtk3-nocsd
    install -D -m 0644 gtk3-nocsd.1 "${pkgdir}"/usr/share/man/man1/gtk3-nocsd.1
    install -D -m 0644 gtk3-nocsd.bash-completion "${pkgdir}"/usr/share/bash-completion/completions/gtk3-nocsd

    install -D -m 0644 libgtk3-nocsd.so.0 "${pkgdir}"/usr/lib/libgtk3-nocsd.so.0

    cd "$srcdir"
    install -D -m 0755 30-gtk3-nocsd.sh "${pkgdir}"/etc/X11/xinit/xinitrc.d/30-gtk3-nocsd.sh
}
