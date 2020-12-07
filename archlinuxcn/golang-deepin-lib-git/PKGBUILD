# Maintainer: justforlxz <justforlxz@gmail.com>

pkgname=golang-deepin-lib-git
pkgver=5.6.0.5.r15.g1954485
pkgrel=2
pkgdesc='A library containing many useful go routines for things such as glib, gettext, archive, graphic,etc.'
arch=('any')
url="https://github.com/linuxdeepin/go-lib"
license=('GPL3')
depends=('dbus' 'libpulse' 'gdk-pixbuf2' 'gdk-pixbuf-xlib' 'mobile-broadband-provider-info' 'libx11'
         'golang-gopkg-alecthomas-kingpin.v2' 'golang-deepin-gir-git'
         'golang-github-linuxdeepin-go-x11-client-git' 'golang-golang-x-net' 'golang-golang-x-image')
         # 'golang-github-cryptix-wav' not packaged yet, paused until our go packaging standards formed
makedepends=('iso-codes' 'golang-gopkg-check.v1' 'git' 'go') # git needed only for go get
conflicts=('golang-deepin-lib')
provides=('golang-deepin-lib')
groups=('deepin-git')
source=("$pkgname::git://github.com/linuxdeepin/go-lib/")
sha512sums=('SKIP')

pkgver() {
    cd $pkgname
    git describe --long --tags | sed 's/\([^-]*-g\)/r\1/;s/-/./g'
}

prepare() {
  cd $pkgname
  sed -i 's/int connect_timeout;/extern int connect_timeout;/' pulse/dde-pulse.h
  go get -v github.com/fsnotify/fsnotify
  go get -v github.com/godbus/dbus
  go get -v github.com/godbus/dbus/introspect
  go get -v github.com/godbus/dbus/prop
}

check() {
  export GOPATH="$srcdir/build:/usr/share/gocode"
  mkdir -p "$srcdir"/build/src/pkg.deepin.io
  cp -a "$srcdir/$pkgname" "$srcdir"/build/src/pkg.deepin.io/lib
  cd "$srcdir"/build/src/pkg.deepin.io/lib
  # TODO: make packages for them
  go get github.com/cryptix/wav github.com/smartystreets/goconvey/convey github.com/mozillazg/go-pinyin gopkg.in/yaml.v3
  # TODO: figure out why pulse tests hang
  # passwd: test needs to access /etc/passwd
  # group & timer & log & dbus: build failed
  # shell: TestEncode failed
  go get -v github.com/fsnotify/fsnotify
  go get -v github.com/godbus/dbus
  go get -v github.com/godbus/dbus/introspect
  go get -v github.com/godbus/dbus/prop
  go test -v $(go list ./... | grep -v -e lib/pulse -e lib/users/passwd -e lib/users/group -e lib/timer -e lib/log -e lib/dbus -e lib/shell)
}

package() {
  mkdir -p "$pkgdir"/usr/share/gocode/src/pkg.deepin.io
  cp -a "$srcdir/$pkgname" "$pkgdir"/usr/share/gocode/src/pkg.deepin.io/lib

  rm -r "$pkgdir"/usr/share/gocode/src/pkg.deepin.io/lib/debian
}
