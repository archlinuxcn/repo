# Maintainer: FzerorubigD <Fzerorubigd {AT} GMail {DOT} com>
pkgname=protobuf-go
pkgver=652.d3c38a4
pkgrel=1
pkgdesc="Go support for Google's protocol buffers"
arch=('i686' 'x86_64' 'armv5tel' 'armv6l' 'armv71')
url="https://github.com/golang/protobuf"
license=('BSD')
depends=('protobuf')
makedepends=('go' 'git')
source=('git://github.com/golang/protobuf.git')

sha1sums=('SKIP')

_gitname=protobuf

pkgver() {
        cd "${srcdir}/${_gitname}"
        echo "$(git rev-list --count HEAD).$(git rev-parse --short HEAD)"
}

build() {
	mkdir -p ${srcdir}/src/github.com/golang/protobuf
        cd "${srcdir}/${_gitname}"
	git --work-tree=${srcdir}/src/github.com/golang/protobuf checkout -f master
	cd ${srcdir}/src/github.com/golang/protobuf
	 GOPATH=${srcdir} go get -v ./...
}

package() {
  mkdir -p $pkgdir/usr/bin
  install -m755 $srcdir/bin/protoc-gen-go $pkgdir/usr/bin/protoc-gen-go
}
