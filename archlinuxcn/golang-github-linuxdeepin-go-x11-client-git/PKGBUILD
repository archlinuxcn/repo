# Maintainer: DingYuan Zhang <justforlxz@gmail.com>

pkgname=golang-github-linuxdeepin-go-x11-client-git
pkgver=0.6.0.r1.gace6660
pkgrel=1
pkgdesc='X11 protocol go language binding'
arch=('any')
url="https://github.com/linuxdeepin/go-x11-client"
license=('GPL')
conflicts=('golang-github-linuxdeepin-go-x11-client')
replaces=('golang-github-linuxdeepin-go-x11-client')
provides=('golang-github-linuxdeepin-go-x11-client')
groups=('deepin-git')
depends=('go' 'golang-deepin-lib-git' 'golang-golang-x-text')
makedepends=('git')
checkdepends=('xorg-server-xvfb' 'golang-github-stretchr-testify' 'golang-gopkg-check.v1' 'golang-gopkg-yaml.v2' 'git')
source=('git://github.com/linuxdeepin/go-x11-client')
sha512sums=('SKIP')

pkgver() {
    cd go-x11-client
    git describe --long --tags | sed 's/\([^-]*-g\)/r\1/;s/-/./g'
}

check() {
  export GOPATH="$srcdir/build:/usr/share/gocode"
  mkdir -p "$srcdir"/build/src/github.com/linuxdeepin
  cp -a "$srcdir"/go-x11-client "$srcdir"/build/src/github.com/linuxdeepin/go-x11-client
  cd "$srcdir"/build/src/github.com/linuxdeepin/go-x11-client
  go get gopkg.in/yaml.v3
  xvfb-run go test -v $(go list ./...)
}

package() {
  mkdir -p "$pkgdir"/usr/share/gocode/src/github.com/linuxdeepin
  cp -a "$srcdir"/go-x11-client "$pkgdir"/usr/share/gocode/src/github.com/linuxdeepin/go-x11-client

  rm -r "$pkgdir"/usr/share/gocode/src/github.com/linuxdeepin/go-x11-client/debian
}
