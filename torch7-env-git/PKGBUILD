# Maintainer: Stephen Zhang <zsrkmyn at gmail dot com>
pkgdesc='Sets up default torch environment'
pkgname='torch7-env-git'
pkgver=r11.d28424a
pkgrel=1
makedepends=('cmake' 'git')
depends=('torch7-git>=r819')
conflicts=('torch7-env')
provides=('torch7-env')
arch=('any')
url='https://github.com/torch/env'
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

package () {
	cd "${pkgname}"
	install -dm755 "$pkgdir/usr/share/lua/5.1/env"
	install -Dm755 init.lua "$pkgdir/usr/share/lua/5.1/env"
}
