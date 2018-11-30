# Maintainer: Hideaki Takahashi (mymelo+aur@gmail.com)
# based on PKGBUILD for MeCab https://aur.archlinux.org/packages/mecab/
pkgname=mecab-git
_pkgname=mecab
pkgrel=1
pkgver=r144.32041d9
pkgdesc="Yet another part-of-speech and morphological analyzer."
arch=('i686' 'x86_64')
url="https://taku910.github.io/mecab"
makedepends=('git')
conflicts=('mecab')
provides=('mecab')
license=('GPL2')
source=("git+https://github.com/taku910/mecab.git")
sha512sums=('SKIP')

pkgver() {
	cd "${_pkgname}"
	printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

build() {
	cd "${_pkgname}/mecab"
	./configure --prefix=/usr --sysconfdir=/etc --libexecdir=/usr/lib --with-charset=utf-8
	make
}

check() {
	cd "${_pkgname}/mecab"
	make -k check
}

package() {
	cd "${_pkgname}/mecab"
	make DESTDIR="$pkgdir/" install
}
