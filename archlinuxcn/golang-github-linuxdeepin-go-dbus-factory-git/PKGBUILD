# Maintainer: DingYuan <justforlxz@gmail.com>

pkgname=golang-github-linuxdeepin-go-dbus-factory-git
pkgver=1.9.3.r13.gb4a21c8
pkgrel=1
pkgdesc='GO DBus factory for DDE'
arch=('any')
url="https://github.com/linuxdeepin/go-dbus-factory"
license=('GPL3')
depends=('golang-deepin-lib-git')
makedepends=('git' 'go')
provides=('golang-github-linuxdeepin-go-dbus-factory')
conflicts=('golang-github-linuxdeepin-go-dbus-factory')
groups=('deepin-git')
source=("$pkgname::git://github.com/linuxdeepin/go-dbus-factory")
sha512sums=('SKIP')

pkgver() {
    cd $pkgname
    git describe --long --tags | sed 's/\([^-]*-g\)/r\1/;s/-/./g'
}

prepare() {
  export GOPATH="$srcdir/build:/usr/share/gocode"
  export GO111MODULE=off
  mkdir -p "$srcdir"/build/src/github.com/linuxdeepin
  cp -a "$srcdir/$pkgname" "$srcdir"/build/src/github.com/linuxdeepin/go-dbus-factory
  go get -v github.com/fsnotify/fsnotify
  go get -v github.com/godbus/dbus
  go get -v github.com/godbus/dbus/introspect
  go get -v github.com/godbus/dbus/prop
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
