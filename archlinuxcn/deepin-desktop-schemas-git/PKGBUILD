# Maintainer: justforlxz <justforlxz@gmail.com>

pkgname=deepin-desktop-schemas-git
pkgver=5.9.8.r8.g801ed45
pkgrel=1
pkgdesc='GSettings deepin desktop-wide schemas'
arch=('any')
url="https://github.com/linuxdeepin/deepin-desktop-schemas"
license=('GPL3')
depends=('dconf' 'deepin-gtk-theme' 'deepin-icon-theme' 'deepin-sound-theme')
makedepends=('git' 'python' 'go' 'golang-deepin-lib')
conflicts=('deepin-artwork-themes' 'deepin-desktop-schemas')
provides=('deepin-desktop-schemas')
groups=('deepin-git')
source=("$pkgname::git://github.com/linuxdeepin/deepin-desktop-schemas")
sha512sums=('SKIP')

pkgver() {
    cd $pkgname
    git describe --long --tags | sed 's/\([^-]*-g\)/r\1/;s/-/./g'
}

prepare() {
  export GOPATH="$srcdir/build:/usr/share/gocode"
  cd $pkgname
  # fix default background url
  sed -i "s#/usr/share/backgrounds/default_background.jpg#/usr/share/backgrounds/deepin/desktop.jpg#" \
    overrides/common/com.deepin.wrap.gnome.desktop.override schemas/com.deepin.dde.appearance.gschema.xml
  # fix network checker url
  sed -i "s#'https://www.chinauos.com', 'https://www.uniontech.com'#'https://www.archlinux.org'#" schemas/com.deepin.dde.network-utils.gschema.xml
}

build() {
  export CGO_CPPFLAGS="${CPPFLAGS}"
  export CGO_CFLAGS="${CFLAGS}"
  export CGO_CXXFLAGS="${CXXFLAGS}"
  export CGO_LDFLAGS="${LDFLAGS}"
  export GOFLAGS="-buildmode=pie -trimpath -mod=readonly -modcacherw"

  cd $pkgname
  make ARCH=x86
}

check() {
  cd $pkgname
  make test
}

package() {
  cd $pkgname
  make DESTDIR="$pkgdir" install
}
