# Maintainer: Adrián Pérez de Castro <aperez@igalia.com>
# Maintainer: Alexandre Macabies <web+oss@zopieux.com>
#
pkgname=gn-git
pkgdesc='Meta-build system which generates Ninja build files'
pkgver=r1523.377ad041
pkgrel=1
license=('BSD')
arch=('x86_64' 'i686')
conflicts=('gn-bin' 'gn')
provides=('gn')
depends=('gcc-libs')
makedepends=('python2' 'ninja' 'git')
url='https://gn.googlesource.com/gn'
source=("gn::git+${url}" gcc-support.patch)
sha512sums=('SKIP'
            '33b8f6da50dc4989ea2f5b13d638a24d89f6847ddb0fad8845575c6f490a25ff2772aee15d1d83e57a1554dee3cd19e88d69823664099714e551d3edd9c56aa7')

pkgver () {
	export GIT_DIR="${startdir}/gn"
	printf "r%s.%s" "$(git --bare rev-list --count HEAD)" "$(git --bare rev-parse --short HEAD)"
}

prepare () {
	cd gn
	patch -p1 < "${srcdir}/gcc-support.patch"
}

build () {
	cd gn
	CC=cc CXX=c++ AR=ar python2 build/gen.py --use-lto
	ninja -C out
}

package () {
	install -Dm755 gn/out/gn "${pkgdir}/usr/bin/gn"

	# Documentation
	install -Dm644 -t "${pkgdir}/usr/share/doc/${pkgname}" \
		gn/docs/*.md gn/README.md

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
