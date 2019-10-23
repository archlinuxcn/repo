# Maintainer: Jiachen YANG <farseerfc@gmail.com>
_pkgname=conoha-iso
pkgname=${_pkgname}-git
pkgver=0.4.3.r78.g94c2ee6
pkgrel=1
pkgdesc="ISO image management tool for ConoHa"
arch=(x86_64)
url="https://github.com/hironobu-s/conoha-iso"
license=('MIT')
makedepends=(go git dep)
source=("git+https://github.com/hironobu-s/conoha-iso.git")
md5sums=('SKIP')

pkgver() {
	cd "$_pkgname"
	git describe --long --tags | sed 's/\([^-]*-g\)/r\1/;s/-/./g' | sed "s/current/$(grep -oP 'APP_VERSION.*"\K([.0-9]*)(?=")' app.go)/g"
#	printf "0.4.3.r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

prepare() {
	mkdir -p gopath/src/github.com/$_pkgname
	ln -rTsf $_pkgname gopath/src/github.com/$_pkgname/$_pkgname
	export GOPATH="$srcdir"/gopath
	cd gopath/src/github.com/$_pkgname/$_pkgname
        dep init
	dep ensure
}

build() {
	export GOPATH="$srcdir"/gopath
	cd gopath/src/github.com/$_pkgname/$_pkgname
	make linux
}

package() {
	cd gopath/src/github.com/$_pkgname/$_pkgname
	install -Dm755 bin/linux/conoha-iso $pkgdir/usr/bin/conoha-iso
	install -Dm644 LICENSE $pkgdir/usr/share/licenses/$pkgname/LICENSE
}
