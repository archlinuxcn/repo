# Maintainer: DingYuan Zhang <justforlxz@gmail.com>

pkgname=deepin-file-manager-git
pkgver=5.1.0.26.r213.g03f26b70
pkgrel=1
pkgdesc='Deepin File Manager'
arch=('x86_64')
url="https://github.com/linuxdeepin/dde-file-manager"
license=('GPL3')
# startdde: for com.deepin.SessionManager
depends=('deepin-qt5integration-git' 'deepin-anything' 'disomaster' 'file' 'gio-qt' 'libmediainfo' 'avfs' 'polkit-qt5' 'poppler'
         'ffmpegthumbnailer' 'jemalloc' 'kcodecs' 'startdde' 'taglib')
makedepends=('git' 'qt5-tools' 'deepin-dock-git' 'deepin-movie' 'deepin-gettext-tools')
optdepends=('deepin-manual: for help menual'
            'deepin-shortcut-viewer: for shortcut display'
            'deepin-screensaver: for screensaver chooser'
            'deepin-movie: for video preview'
            'deepin-terminal: for opening in terminal'
            'deepin-compressor: for compress/decompress')
groups=('deepin-git')
provides=('deepin-file-manager')
conflicts=('deepin-file-manager')
replaces=('deepin-file-manager')
source=("git://github.com/linuxdeepin/dde-file-manager"
        "deepin-file-manager-qt5.15.patch")
sha512sums=('SKIP'
            '2b58868fdaee9d42f8ba2029bcaa727c146c64b219faa52bd2df1c1483290e95a7cb6622227a24d35f7d7167061d264839bfeb47872d84519097b47af036daf7')

pkgver() {
    cd dde-file-manager
    git describe --long --tags | sed 's/\([^-]*-g\)/r\1/;s/-/./g'
}

prepare() {
  cd dde-file-manager
  sed -i 's|systembusconf.path = /etc/dbus-1/system.d|systembusconf.path = /usr/share/dbus-1/system.d|' dde-file-manager-daemon/dde-file-manager-daemon.pro

  patch -p1 -i ../deepin-file-manager-qt5.15.patch # Fix build with Qt 5.15
}

build() {
  cd dde-file-manager
  qmake-qt5 PREFIX=/usr
  make
}

package() {
  cd dde-file-manager
  make INSTALL_ROOT="$pkgdir" install
}
