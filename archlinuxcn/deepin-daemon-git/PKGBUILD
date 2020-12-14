# Maintainer: justforlxz <justforlxz@gmail.com>

pkgname=deepin-daemon-git
pkgver=5.12.0.25.r42.g7f9b4e75
pkgrel=1
pkgdesc='Daemon handling the DDE session settings'
arch=('x86_64')
url="https://github.com/linuxdeepin/dde-daemon"
license=('GPL3')
depends=('deepin-desktop-schemas-git' 'ddcutil' 'deepin-api-git' 'gvfs' 'iso-codes' 'lsb-release'
         'mobile-broadband-provider-info' 'deepin-polkit-agent-git'
         'deepin-polkit-agent-ext-gnomekeyring' 'udisks2' 'upower'
         'libxkbfile' 'accountsservice' 'deepin-desktop-base-git' 'bamf' 'pulseaudio'
         'org.freedesktop.secrets' 'noto-fonts' 'imwheel')
makedepends=('golang-github-linuxdeepin-go-dbus-factory-git' 'golang-deepin-gir-git' 'golang-deepin-lib-git'
             'deepin-api-git' 'golang-github-nfnt-resize' 'golang-gopkg-yaml.v2' 'sqlite' 'deepin-gettext-tools-git'
             'git' 'mercurial' 'python-gobject' 'networkmanager' 'bluez' 'go')
optdepends=('networkmanager: for network management support'
            'bluez: for bluetooth support'
            'iw: for miracast module'
            'proxychains-ng: for proxy configuration module')
conflicts=('deepin-daemon')
provides=('deepin-daemon')
groups=('deepin-git')
install="$pkgname.install"
source=("$pkgname::git://github.com/linuxdeepin/dde-daemon"
        dde-daemon.patch
        'deepin-daemon.sysusers')
sha512sums=('SKIP'
            'SKIP'
            '808c02d4fec4cbbb01119bbb10499090199e738b7dd72c28a57dde098eef6132723f3434c151f79e21d9f788c7f7bae8046573ac93ba917afe0e803fbffa6d5a')

pkgver() {
    cd $pkgname
    git describe --long --tags | sed 's/\([^-]*-g\)/r\1/;s/-/./g'
}

prepare() {
  cd $pkgname
  mkdir build
  patch -p1 -i ../dde-daemon.patch

  export GOPATH="$srcdir/build:/usr/share/gocode"

  # golang-deepin-lib's dependency, remove when go packaging resumes
  go get -v github.com/cryptix/wav

  go get -v github.com/axgle/mahonia github.com/msteinert/pam github.com/gosexy/gettext github.com/rickb777/date \
         github.com/jinzhu/gorm github.com/kelvins/sunrisesunset github.com/mozillazg/go-pinyin github.com/teambition/rrule-go \
         golang.org/x/xerrors github.com/mattn/go-sqlite3 github.com/fsnotify/fsnotify
  go get -v github.com/godbus/dbus
  go get -v github.com/godbus/dbus/introspect
  go get -v github.com/godbus/dbus/prop
  sed -i 's#/usr/share/backgrounds/default_background.jpg#/usr/share/backgrounds/deepin/desktop.jpg#' accounts/user.go
}

build() {
  export CGO_CPPFLAGS="${CPPFLAGS}"
  export CGO_CFLAGS="${CFLAGS}"
  export CGO_CXXFLAGS="${CXXFLAGS}"
  export CGO_LDFLAGS="${LDFLAGS}"
  export GOFLAGS="-buildmode=pie -trimpath -mod=readonly -modcacherw"

  cd $pkgname
  make -C network/nm_generator gen-nm-code
  make
}

package() {
  cd $pkgname
  make DESTDIR="$pkgdir" PAM_MODULE_DIR=usr/lib/security install

  mv "$pkgdir"{,/usr}/lib/systemd
  mv "$pkgdir"{,/usr}/lib/udev
  rmdir "$pkgdir"/lib

  install -Dm644 ../deepin-daemon.sysusers "$pkgdir/usr/lib/sysusers.d/deepin-daemon.conf"
}
