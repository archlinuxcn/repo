# Maintainer: DingYuan Zhang <justforlxz@gmail.com>

pkgname=deepin-api-git
pkgver=5.3.0.3.r1.ga8e8112
pkgrel=1
pkgdesc='Golang bindings for dde-daemon'
arch=('x86_64')
url="https://github.com/linuxdeepin/dde-api"
license=('GPL3')
# alsa-utils: alsactl used in sound-theme-player
# bc: used in adjust-grub-theme
# fontconfig: fc-match used in adjust-grub-theme
# librsvg: rsvg-convert used in adjust-grub-theme
# util-linux: rfkill used in device
depends=('alsa-utils' 'bc' 'fontconfig' 'glib2' 'gdk-pixbuf2' 'gtk3' 'libcanberra-pulse' 'librsvg'
         'libxi' 'libxfixes' 'poppler-glib' 'util-linux' 'xcur2png' 'blur-effect')
makedepends=('git' 'deepin-gettext-tools' 'golang-deepin-gir-git' 'golang-deepin-lib-git'
             'golang-github-linuxdeepin-go-dbus-factory-git' 'golang-github-linuxdeepin-go-x11-client-git'
             'golang-github-nfnt-resize' 'bzr' 'go-pie')
provides=('deepin-api')
replaces=('deepin-api')
conflicts=('deepin-api')
groups=('deepin-git')
install=deepin-api.install
source=("git://github.com/linuxdeepin/dde-api/"
        deepin-api.sysusers)
sha512sums=('SKIP'
            'e894eb3928af9e244fa78010fdf16c8abb6ce18df114cf05327d02b18774d6ba5b023e4dfa0d07042f4e44a5c6e2ddb55b07f3e0db466a0e6169b52465fdefd6')

pkgver() {
    cd dde-api
    git describe --long --tags | sed 's/\([^-]*-g\)/r\1/;s/-/./g'
}

prepare() {
  export GOPATH="$srcdir/build:/usr/share/gocode"
  mkdir -p build/src/pkg.deepin.io/dde/api
  cp -a dde-api/* build/src/pkg.deepin.io/dde/api/

  # golang-deepin-lib's dependency, remove when go packaging resumes
  go get github.com/cryptix/wav

  go get github.com/disintegration/imaging github.com/fogleman/gg github.com/mattn/go-sqlite3 github.com/gosexy/gettext github.com/rickb777/date
}

build(){
  export CGO_CPPFLAGS="${CPPFLAGS}"
  export CGO_CFLAGS="${CFLAGS}"
  export CGO_CXXFLAGS="${CXXFLAGS}"
  export CGO_LDFLAGS="${LDFLAGS}"
  export GOFLAGS="-buildmode=pie -trimpath -mod=readonly -modcacherw"

  cd dde-api
  make
}

package() {
  cd dde-api
  make DESTDIR="$pkgdir" SYSTEMD_LIB_DIR=/usr/lib install

  install -Dm644 ../deepin-api.sysusers "$pkgdir"/usr/lib/sysusers.d/deepin-api.conf
}
