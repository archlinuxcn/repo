# Maintainer: Wenxuan <wenxuangm@gmail.com>
pkgname=mmv-go
_binname=mmv
pkgver=0.1.2
pkgrel=1
pkgdesc="Rename multiple files with editor"
arch=(i686 x86_64)
url='https://github.com/itchyny/mmv'
license=("MIT")
depends=()
makedepends=('go' 'make')
conflicts=('mmv' 'mmv-go-git' 'mmv-go-bin-git')
provides=('mmv')

source=("${url}/archive/v${pkgver}.tar.gz")
sha256sums=('d9841ed28a720ceb07aa894cc3f69643bab02c558fc1c566ff42562875a9c84d')

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
