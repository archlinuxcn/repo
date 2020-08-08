# Maintainer: DingYuan Zhang <justforlxz@gmail.com>

pkgname=startdde-git
pkgver=5.5.0.8.r1.g3e984a3
pkgrel=1
pkgdesc="starter of deepin desktop environment"
arch=('x86_64')
url="https://github.com/linuxdeepin/startdde"
license=('GPL3')
depends=('deepin-daemon' 'deepin-dock-git' 'deepin-polkit-agent-git' 'deepin-file-manager-git'
         'deepin-session-shell-git' 'deepin-session-ui-git' 'libgnome-keyring')
makedepends=('cmake' 'coffeescript' 'golang-github-linuxdeepin-go-dbus-factory-git' 'golang-deepin-gir-git'
             'golang-deepin-lib-git' 'deepin-api-git' 'go' 'git' 'jq'
             'golang-golang-x-net' 'golang-github-linuxdeepin-go-x11-client-git')
optdepends=('deepin-wm: Legacy 3D window manager'
            'deepin-metacity: Legacy 2D window manager'
            'deepin-kwin: Preferred window manager')
replaces=('deepin-wm-switcher' 'startdde')
provides=('startdde')
conflicts=('startdde')
groups=('deepin-git')
source=("git://github.com/linuxdeepin/startdde")
sha512sums=('SKIP')

pkgver() {
    cd startdde
    git describe --long --tags | sed 's/\([^-]*-g\)/r\1/;s/-/./g'
}

prepare() {
  export GOPATH="$srcdir/build:/usr/share/gocode"
  go get github.com/cryptix/wav golang.org/x/xerrors

  sed -i 's/sbin/bin/' startdde/Makefile
}

build() {
  export CGO_CPPFLAGS="${CPPFLAGS}"
  export CGO_CFLAGS="${CFLAGS}"
  export CGO_CXXFLAGS="${CXXFLAGS}"
  export CGO_LDFLAGS="${LDFLAGS}"
  export GOFLAGS="-buildmode=pie -trimpath -mod=readonly -modcacherw"

  cd startdde
  make
}

package() {
  cd startdde
  make DESTDIR="$pkgdir" install

  # Fix env file permission
  chmod +x "$pkgdir"/etc/X11/Xsession.d/*

  # Don't rely on deepin-session's location
  install -dm755 "$pkgdir"/etc/X11/xinit/xinitrc.d
  mv "$pkgdir"/etc/X11/Xsession.d/* "$pkgdir"/etc/X11/xinit/xinitrc.d/
  rmdir "$pkgdir"/etc/X11/Xsession.d
}
