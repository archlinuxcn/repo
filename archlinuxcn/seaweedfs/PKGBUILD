# Maintainer: Jonathon Fernyhough <jonathon+m2x.dev>
# Contributor: krevedko <helllamer-gmail.com>

pkgname=seaweedfs
pkgver=3.15
pkgrel=1
pkgdesc="SeaweedFS is a simple and highly scalable distributed file system"
arch=('i686' 'x86_64' 'aarch64' 'armv7h' 'armv6h' 'arm')
url="https://github.com/chrislusf/seaweedfs"
license=('APACHE')
makedepends=('git' 'go')
options=('!lto')
source=("$pkgname-$pkgver.tar.gz::$url/archive/$pkgver.tar.gz")
b2sums=('fb6ac9827b51b460aa42935ae1e55869969307bfcd2c37dad118b136564033bf0fe699de68b98ca3cc1e09cdbc93583c018ce4da61b21b8a7e14396dcb702ad8')
_shortcommit=5799a20

prepare() {
  cd $pkgname-$pkgver

  export GOPATH="${SRCDEST:-$srcdir}"
  go mod vendor
}

build() {
  export CGO_CPPFLAGS="$CPPFLAGS"
  export CGO_CFLAGS="$CFLAGS"
  export CGO_CXXFLAGS="$CXXFLAGS"
  export CGO_LDFLAGS="$LDFLAGS"
  export GOFLAGS="-buildmode=pie -trimpath -mod=vendor -modcacherw"
  export GOPATH="${SRCDEST:-$srcdir}"

  cd $pkgname-$pkgver/weed
  go build -v $GO_FLAGS -tags 5BytesOffset -ldflags "-X github.com/chrislusf/seaweedfs/weed/util.COMMIT=$_shortcommit -extldflags $LDFLAGS"
}

#check() {
#  cd $pkgname-$pkgver/weed
#  go test -v
#}

package() {
  cd $pkgname-$pkgver
  install -D     weed/weed "$pkgdir"/usr/bin/weed
  install -Dm644 README.md "$pkgdir"/usr/share/doc/$pkgname/README.md
  install -Dm644 LICENSE   "$pkgdir"/usr/share/licenses/$pkgname/LICENSE
}
