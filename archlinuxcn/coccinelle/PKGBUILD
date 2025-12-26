# Maintainer: Manuel Wiesinger <m {you know what belongs here} mmap {and here} at>
# Contributor: Omar Sandoval <osandov at osandov dot com>
# Contributor: Roger Zanoni <rogerzanoni@gmail.com>
# Contributor: Sylvain Henry <hsyl20@gmail.com>
# Contributor: Marti Raudsepp <marti@juffo.org>
# Contributor: Dan McGee <dpmcgee@gmail.com>
# Contributor: LeCrayonVert <sunrider@laposte.net>
# Contributor: Lukas Fleischer <archlinux@cryptocrack.de>
# Contributor: Vladimir Kirillov <proger@wilab.org.ua>

pkgname=coccinelle
pkgver=1.3.1
pkgrel=2
pkgdesc="C source code matching and transformation engine"
arch=('x86_64')
url="https://coccinelle.gitlabpages.inria.fr/website/"
license=('GPL-2.0-or-later')
makedepends=(
    'ocaml'
    'ocaml-findlib'
    'ocaml-menhir'
    'ocaml-num'
    'ocaml-parmap'
    'ocaml-pcre'
    'ocaml-pyml'
    'ocaml-stdcompat'
)
depends=(
    'glibc'
    'pcre'
    'python'
    'zstd'
)
checkdepends=(
    'ocaml'
)
optdepends=(
    'ocaml-findlib: OCaml scripting feature'
    'ocaml: OCaml scripting feature'
    'python-psycopg2: PostgreSQL support for Python bindings'
)
source=(
    "$pkgname-$pkgver.tar.gz::https://github.com/coccinelle/${pkgname}/archive/${pkgver}.tar.gz"
)
b2sums=('4dfde0bee9f9c1b555a061e712f0f2c6026c3072ed1bd3e046339f46fd3e8a699b32de3abb00f07312143b9db7d8fa4cc9c6c32c406414380b64f1d43d30a146')
options=('!strip')

build() {
    cd "$pkgname-$pkgver"

    ./autogen

    ./configure \
	--enable-bytes \
	--enable-dynlink \
	--enable-menihr \
	--enable-ocaml \
	--enable-opt \
	--enable-opt \
	--enable-pcre \
	--enable-pcre-syntax \
	--enable-pyml \
	--enable-python \
	--enable-stdcompat \
	--enable-parmap \
	\
	--prefix=/usr \
	--docdir=/usr/share/doc \
	--libdir=/usr/lib/ocaml \
	--mandir=/usr/share/man

    make
}

check() {
    cd "$pkgname-$pkgver"
    make check
}

package() {
    cd "$pkgname-$pkgver"

    make DESTDIR="$pkgdir/" MANDIR="/usr/share/man" install

    # Emacs modes
    install -Dm644 editors/emacs/cocci.el -t $pkgdir/usr/share/emacs/site-lisp
    install -Dm644 editors/emacs/cocci-ediff.el -t $pkgdir/usr/share/emacs/site-lisp

    # vim
    install -Dm644 editors/vim/ftdetect/cocci.vim -t $pkgdir/usr/share/vim/vimfiles/ftdetect
    install -Dm644 editors/vim/syntax/cocci.vim -t $pkgdir/usr/share/vim/vimfiles/syntax

    strip \
	$pkgdir/usr/bin/spatch \
	$pkgdir/usr/bin/spgen
}
