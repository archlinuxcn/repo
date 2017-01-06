# Maintainer: Adrián Pérez de Castro <aperez@igalia.com>
pkgdesc='Tool to aid wrapping C functions to be used from Lua'
pkgname='torch7-cwrap-git'
pkgver=r35.dbd0a62
pkgrel=1
conflicts=('torch7-cwrap')
provides=('torch7-cwrap')
arch=('any')
url='https://github.com/torch/cwrap'
makedepends=('git')
license=('BSD')
source=("${pkgname}::git+${url}")
sha512sums=('SKIP')

pkgver () {
	cd "${pkgname}"
	(
		set -o pipefail
		git describe --long 2>/dev/null | sed 's/\([^-]*-g\)/r\1/;s/-/./g' ||
		printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
	)
}

build () {
	echo 'Nothing to build'
}

package () {
	cd "${pkgname}"
	for filename in *.lua ; do
		install -Dm644 "${filename}" \
			"${pkgdir}/usr/share/lua/5.1/cwrap/${filename}"
	done
}
