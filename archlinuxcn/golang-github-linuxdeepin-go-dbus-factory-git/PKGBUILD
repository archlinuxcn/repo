# Maintainer: DingYuan <justforlxz@gmail.com>

pkgname=golang-github-linuxdeepin-go-dbus-factory-git
pkgver=1.7.0.6.r13.g922bd1e
pkgrel=1
pkgdesc='GO DBus factory for DDE'
arch=('any')
url="https://github.com/linuxdeepin/go-dbus-factory"
license=('GPL3')
depends=('golang-deepin-lib-git')
makedepends=('go')
provides=('golang-github-linuxdeepin-go-dbus-factory')
conflicts=('golang-github-linuxdeepin-go-dbus-factory')
replaces=('golang-github-linuxdeepin-go-dbus-factory')
groups=('deepin-git')
source=('git://github.com/linuxdeepin/go-dbus-factory')
sha512sums=('SKIP')

pkgver() {
    cd go-dbus-factory
    git describe --long --tags | sed 's/\([^-]*-g\)/r\1/;s/-/./g'
}

prepare() {
  export GOPATH="$srcdir/build:/usr/share/gocode"
  mkdir -p "$srcdir"/build/src/github.com/linuxdeepin
  cp -a "$srcdir"/go-dbus-factory "$srcdir"/build/src/github.com/linuxdeepin/go-dbus-factory
}

build() {
  export CGO_CPPFLAGS="${CPPFLAGS}"
  export CGO_CFLAGS="${CFLAGS}"
  export CGO_CXXFLAGS="${CXXFLAGS}"
  export CGO_LDFLAGS="${LDFLAGS}"
  export GOFLAGS="-buildmode=pie -trimpath -mod=readonly -modcacherw"

  cd "$srcdir"/build/src/github.com/linuxdeepin/go-dbus-factory
  make bin

  # Suggested by upstream: don't run
  # ./gen.sh
}

check() {
  export GOPATH="$srcdir/build:/usr/share/gocode"
  cd "$srcdir"/build/src/github.com/linuxdeepin/go-dbus-factory
  go test -v $(go list ./...)
}

package() {
  cd "$srcdir"/build/src/github.com/linuxdeepin/go-dbus-factory
  install -dm755 "$pkgdir"/usr/share/gocode/src/github.com/linuxdeepin/go-dbus-factory
  cp -a com.* org.* net.* object_manager "$pkgdir"/usr/share/gocode/src/github.com/linuxdeepin/go-dbus-factory/
}
