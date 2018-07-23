# Maintainer: Adrián Pérez de Castro <aperez@igalia.com>
# Maintainer: Alexandre Macabies <web+oss@zopieux.com>
#
pkgname=gn-git
pkgdesc='Meta-build system which generates Ninja build files'
pkgver=r1446.5d9a4e9a
pkgrel=1
license=('BSD')
arch=('x86_64' 'i686')
conflicts=('gn-bin')
provides=('gn')
depends=('gcc-libs')
makedepends=('python2' 'ninja')
url='https://gn.googlesource.com/gn'
source=("gn::git+${url}" gcc-support.patch)
sha512sums=('SKIP'
            '14f5a6236c09d1e11f6ce8984cbe1e635dc582a38ba801b719404bdaaf0b9f708262fdf13b5d6496e8af7fd50d411ab90747af1d816fa78a6a8b808ae88cb4f8')

pkgver () {
	export GIT_DIR="${startdir}/gn"
	printf "r%s.%s" "$(git --bare rev-list --count HEAD)" "$(git --bare rev-parse --short HEAD)"
}

prepare () {
	patch -p1 < gcc-support.patch
}

build () {
	cd gn
	CC=cc CXX=c++ AR=ar python2 build/gen.py --no-sysroot --use-lto
	ninja -C out
}

package () {
	install -Dm755 gn/out/gn "${pkgdir}/usr/bin/gn"

	# Documentation
	install -Dm644 -t "${pkgdir}/usr/share/doc/${pkgname}" \
		gn/tools/gn/docs/*.md

	install -Dm644 -t "${pkgdir}/usr/share/doc/${pkgname}/example" \
		gn/tools/gn/example/*.*
	install -Dm644 -t "${pkgdir}/usr/share/doc/${pkgname}/example/build" \
		gn/tools/gn/example/build/*.*

	# Vim support
	local item
	for item in autoload ftplugin ftdetect syntax ; do
		install -Dm 644 -t "${pkgdir}/usr/share/vim/vimfiles/${item}" \
			"gn/tools/gn/misc/vim/${item}"/*.vim
	done
		
	# License
	install -m 644 -D gn/LICENSE \
		"${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
