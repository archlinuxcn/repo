# Maintainer: Jiachen YANG <farseerfc@gmail.com>
_pkgname=zograscope
_commit=5a0a0754478e7ae5bd76509d082821202bb5ddf0
pkgname=$_pkgname-git
pkgver=r932.5a0a075
pkgrel=1
pkgdesc="syntax-aware diff that also provides a number of additional tools (zs-diff, zs-find, zs-gdiff, zs-hi, zs-stats)"
arch=(x86_64)
url="https://github.com/xaizek/zograscope"
license=('AGPL')
depends=('qt5-base' 'libgit2' 'boost-libs')
makedepends=('git' 'boost' 'srcml')
optdepends=('srcml: srcML related diff features')
provides=("${pkgname%-git}")
conflicts=("${pkgname%-git}")
source=("zograscope::git+$url.git#commit=$_commit")
md5sums=('SKIP')

# Please refer to the 'USING VCS SOURCES' section of the PKGBUILD man page for
# a description of each element in the source array.

pkgver() {
	cd "$srcdir/${_pkgname}"
	printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

prepare() {
	cd "$srcdir/${_pkgname}"
	echo 'QT5_PROG := qmake-qt5' >> config.mk
	echo 'HAVE_LIBGIT2 := yes'   >> config.mk
}

build() {
	cd "$srcdir/${_pkgname}"
	#make LDFLAGS="$LDFLAGS" release
	make release
}

check() {
	cd "$srcdir/${_pkgname}"
	make check
}

package() {
	cd "$srcdir/${_pkgname}"
	make DESTDIR="$pkgdir/" install
}
