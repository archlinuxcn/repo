# Maintainer: DingYuan Zhang <justforlxz@gmail.com>

pkgname=golang-deepin-lib-git
pkgver=5.5.0.1.r4.g67f7719
pkgrel=1
pkgdesc='A library containing many useful go routines for things such as glib, gettext, archive, graphic,etc.'
arch=('any')
url="https://github.com/linuxdeepin/go-lib"
license=('GPL3')
depends=('dbus' 'go' 'libpulse' 'gdk-pixbuf2' 'mobile-broadband-provider-info' 'libx11'
         'golang-gopkg-alecthomas-kingpin.v2' 'golang-deepin-gir-git'
         'golang-github-linuxdeepin-go-x11-client' 'golang-golang-x-net' 'golang-golang-x-image')
         # 'golang-github-cryptix-wav' not packaged yet, paused until our go packaging standards formed
checkdepends=('iso-codes' 'golang-gopkg-check.v1' 'git') # git needed only for go get
replaces=('golang-deepin-lib')
conflicts=('golang-deepin-lib')
provides=('golang-deepin-lib')
groups=('deepin-git')
source=("git://github.com/linuxdeepin/go-lib/")
sha512sums=('SKIP')

pkgver() {
    cd go-lib
    git describe --long --tags | sed 's/\([^-]*-g\)/r\1/;s/-/./g'
}

prepare() {
  cd go-lib
  sed -i 's/int connect_timeout;/extern int connect_timeout;/' pulse/dde-pulse.h
}

check() {
  export GOPATH="$srcdir/build:/usr/share/gocode"
  mkdir -p "$srcdir"/build/src/pkg.deepin.io
  cp -a "$srcdir"/go-lib "$srcdir"/build/src/pkg.deepin.io/lib
  cd "$srcdir"/build/src/pkg.deepin.io/lib
  # TODO: make packages for them
  go get github.com/cryptix/wav github.com/smartystreets/goconvey/convey github.com/mozillazg/go-pinyin gopkg.in/yaml.v3
  # TODO: figure out why pulse tests hang
  # passwd: test needs to access /etc/passwd
  # group & timer & log & dbus: build failed
  # shell: TestEncode failed
  go test -v $(go list ./... | grep -v -e lib/pulse -e lib/users/passwd -e lib/users/group -e lib/timer -e lib/log -e lib/dbus -e lib/shell)
}

package() {
  mkdir -p "$pkgdir"/usr/share/gocode/src/pkg.deepin.io
  cp -a "$srcdir"/go-lib "$pkgdir"/usr/share/gocode/src/pkg.deepin.io/lib

  rm -r "$pkgdir"/usr/share/gocode/src/pkg.deepin.io/lib/debian
}
