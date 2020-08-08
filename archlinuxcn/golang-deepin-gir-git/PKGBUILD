# Maintainer: DingYuan Zhang <justforlxz@gmail.com>

pkgname=golang-deepin-gir-git
pkgver=2.0.2.r0.g095577f
pkgrel=1
pkgdesc='Generate static golang bindings for GObject'
arch=('any')
url="https://github.com/linuxdeepin/go-gir-generator"
license=('GPL3')
depends=('gtk3' 'libgudev')
makedepends=('git' 'go' 'gobject-introspection')
checkdepends=('golang-gopkg-check.v1')
provides=('golang-deepin-gir')
conflicts=('golang-deepin-gir')
replaces=('golang-deepin-gir')
groups=('deepin-git')
source=('git://github.com/linuxdeepin/go-gir-generator'
        SettingsBackendLike.patch glib-2.63.patch)
sha512sums=('SKIP'
            'bd97770e2a345bc1fe4248238f13bd741c157629c5e097c56039326fe7fa4d550c8030272c18c2adc1c0dce35dd72c8d4e6fc394bf4d659076794e6a375d045a'
            '0cdf4e2251eb6c88f37cea12af8db9e2e7465bebb4636ce90c86cce994b5b9a82ff332964735ae8349d8a67e5146ff26a42802ce46f33def5c9452fe6eda92f3')

pkgver() {
    cd go-gir-generator
    git describe --long --tags | sed 's/\([^-]*-g\)/r\1/;s/-/./g'
}

prepare() {
  cd go-gir-generator
  mkdir -p "$srcdir"/build/src/pkg.deepin.io

  # Should be fixed upstream
  mkdir -p out/src/pkg.deepin.io/gir/{glib-2.0,gobject-2.0,gio-2.0,gudev-1.0}

  # Our gobject-introspection is too new
  # https://cr.deepin.io/#/c/16880/
  patch -p1 -i ../SettingsBackendLike.patch

  patch -p0 -i ../glib-2.63.patch

  # https://github.com/linuxdeepin/developer-center/issues/955
  sed -i "s/'Can'tFind'/“Can'tFind”/" lib.in/glib-2.0/keyfile_test.go
}

build() {
  export GOPATH="$srcdir/build:/usr/share/gocode"
  export CGO_CPPFLAGS="${CPPFLAGS}"
  export CGO_CFLAGS="${CFLAGS}"
  export CGO_CXXFLAGS="${CXXFLAGS}"
  export CGO_LDFLAGS="${LDFLAGS}"
  export GOFLAGS="-buildmode=pie -trimpath -mod=readonly -modcacherw"

  cd go-gir-generator
  rm -r gogtk-demo
  make

  mv out/src/pkg.deepin.io/gir "$srcdir"/build/src/pkg.deepin.io/
}

check() {
  # https://github.com/linuxdeepin/developer-center/issues/955
  export GOPATH="$srcdir/build:/usr/share/gocode"
  cd "$srcdir"/build/src/pkg.deepin.io/gir
  go test -v $(go list ./...)

  cd "$srcdir"/go-gir-generator
  go run test/memory.go
}

package() {
  mkdir -p "$pkgdir"/usr/share/gocode/src/pkg.deepin.io
  cp -a "$srcdir"/build/src/pkg.deepin.io/gir "$pkgdir"/usr/share/gocode/src/pkg.deepin.io/
}
