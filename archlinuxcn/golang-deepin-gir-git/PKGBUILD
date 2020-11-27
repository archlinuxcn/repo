# Maintainer: justforlxz <justforlxz@gmail.com>

pkgname=golang-deepin-gir-git
pkgver=2.0.2.r1.gd9225a1
pkgrel=2
pkgdesc='Generate static golang bindings for GObject'
arch=('any')
url="https://github.com/linuxdeepin/go-gir-generator"
license=('GPL3')
depends=('gtk3' 'libgudev')
makedepends=('git' 'go' 'gobject-introspection')
checkdepends=('golang-gopkg-check.v1')
provides=('golang-deepin-gir')
conflicts=('golang-deepin-gir')
groups=('deepin-git')
source=("$pkgname::git://github.com/linuxdeepin/go-gir-generator"
        SettingsBackendLike.patch glib-2.63.patch)
sha512sums=('SKIP'
            '1ac5c868d764753d3da04370019725134ef4b0c7eb5b5032c9aa06e405d5ca713c920c3ff680ccf7c063078838509d28b8d687fae1bfeef9f7e946ac5a618357'
            'f39080fe660de5bf9e8d8fd7db5c9449866594c7286c013392768eeb4af9f459c0fff2956c9a07d4df772a7facd249d890930796dd7692a3a401832b4160bef6')

pkgver() {
    cd $pkgname
    git describe --long --tags | sed 's/\([^-]*-g\)/r\1/;s/-/./g'
}

prepare() {
  cd $pkgname
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
  export GOFLAGS="-buildmode=pie -trimpath -mod=readonly -modcacherw"

  cd $pkgname
  rm -r gogtk-demo
  make

  mv out/src/pkg.deepin.io/gir "$srcdir"/build/src/pkg.deepin.io/
}

check() {
  # https://github.com/linuxdeepin/developer-center/issues/955
  export GOPATH="$srcdir/build:/usr/share/gocode"
  cd "$srcdir"/build/src/pkg.deepin.io/gir
  go test -v $(go list ./...)

  cd "$srcdir/$pkgname"
  go run test/memory.go
}

package() {
  mkdir -p "$pkgdir"/usr/share/gocode/src/pkg.deepin.io
  cp -a "$srcdir"/build/src/pkg.deepin.io/gir "$pkgdir"/usr/share/gocode/src/pkg.deepin.io/
}
