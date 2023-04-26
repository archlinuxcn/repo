# Maintainer: Wenxuan <wenxuangm@gmail.com>
pkgname=mmv-go
_binname=mmv
pkgver=0.1.6
pkgrel=1
pkgdesc="Rename multiple files with editor"
arch=(i686 x86_64)
url='https://github.com/itchyny/mmv'
license=("MIT")
depends=()
makedepends=('go' 'make')
conflicts=('mmv' 'mmv-go-git' 'mmv-go-bin-git')
provides=('mmv')

source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz")
sha256sums=('18d181e6a53437ad18c4409f3c423bc23687152a17b53a605dde13dfffb0d215')

build() {
	cd "$srcdir/${_binname}-${pkgver}"
	make build
}

check() {
	cd "$srcdir/${_binname}-${pkgver}"
	make test
}

package() {
	cd "$srcdir/${_binname}-${pkgver}"
	install -Dm755 "${_binname}" "$pkgdir/usr/bin/${_binname}"
	install -Dm644 "README.md"   "$pkgdir/usr/share/doc/${_binname}/README.md"
	install -Dm644 "LICENSE"     "$pkgdir/usr/share/licenses/${_binname}/LICENSE"
}

# vim:set noet sts=0 sw=4 ts=4 ft=PKGBUILD:
