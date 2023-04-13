# Maintainer: Ren Tatsumoto <tatsu at autistici dot org>

pkgname=hunspell-ja-git
conflicts=('hunspell-ja')
provides=('hunspell-ja')
pkgver=1.r1.g9854fc6
pkgrel=1
pkgdesc="Japanese dictionary for Hunspell"
arch=('any')
url='https://github.com/Ajatt-Tools/hunspell-ja'
license=('custom')
optdepends=('hunspell: the spell checking libraries and apps')
source=("${pkgname}::git+${url}")
sha512sums=('SKIP')
makedepends=('git')

_lang=ja_JP

pkgver() {
	cd -- "${pkgname}"
	{ git describe --long --tags || date '+%Y-%m-%d' ;} | sed 's/^v//;  s/\([^-]*-g\)/r\1/;  s/-/./g'
}

package() {
	cd -- "$srcdir/$pkgname"

	install -vdm755 "${pkgdir}/usr/share/hunspell"
	for dict in aff dic; do
		install -vDm644 "${_lang}.${dict}" "${pkgdir}/usr/share/hunspell/${_lang}.${dict}"
	done

	# the symlinks
	install -dm755 "$pkgdir"/usr/share/myspell/dicts
	pushd "$pkgdir"/usr/share/myspell/dicts
	for file in "$pkgdir"/usr/share/hunspell/*; do
		ln -sv /usr/share/hunspell/$(basename $file) .
	done
	popd
	install -vDm644 "README.md" "${pkgdir}/usr/share/licenses/${pkgname}/README.md"
}
