# Maintainer: justforlxz <justforlxz@gmail.com>

pkgname=deepin-file-manager-git
pkgver=5.2.0.76.r107.g7ccae2357
pkgrel=1
pkgdesc='Deepin File Manager'
arch=('x86_64')
url="https://github.com/linuxdeepin/dde-file-manager"
license=('GPL3')
# startdde: for com.deepin.SessionManager
depends=('deepin-anything-git' 'disomaster' 'file' 'gio-qt' 'libmediainfo' 'avfs' 'polkit-qt5' 'poppler'
         'ffmpegthumbnailer' 'startdde-git' 'taglib' 'jemalloc' 'htmlcxx' 'mimetic' 'lucene++')
makedepends=('git' 'deepin-movie' 'lucene++' 'jemalloc' 'kcodecs' 'htmlcxx' 'libgsf' 'mimetic' 'boost' 'boost-libs' 'qt5-tools' 'deepin-dock-git' 'deepin-gettext-tools-git')
optdepends=('deepin-manual: for help menual'
            'deepin-shortcut-viewer: for shortcut display'
            'deepin-screensaver: for screensaver chooser'
            'deepin-movie: for video preview'
            'deepin-terminal: for opening in terminal'
            'deepin-compressor: for compress/decompress')
groups=('deepin-git')
provides=('deepin-file-manager')
conflicts=('deepin-file-manager')
source=("$pkgname::git://github.com/linuxdeepin/dde-file-manager")
sha512sums=('SKIP')

pkgver() {
    cd $pkgname
    git describe --long --tags | sed 's/\([^-]*-g\)/r\1/;s/-/./g'
}

prepare() {
    cd ${pkgname}
    sed -i '/#include <QException>/a #include <QPainterPath>' dialogs/dfmtaskwidget.cpp
    sed -i '/#include <QTimer>/a #include <QPainterPath>' dde-file-manager-lib/interfaces/dfmglobal.cpp
    sed -i '/#include <QPainter>/a #include <QPainterPath>' dde-file-manager-lib/interfaces/{dlistitemdelegate,dfmstyleditemdelegate,diconitemdelegate}.cpp dde-file-manager-lib/dialogs/openwithdialog.cpp
    sed -i 's|systembusconf.path = /etc/dbus-1/system.d|systembusconf.path = /usr/share/dbus-1/system.d|' dde-file-manager-daemon/dde-file-manager-daemon.pro
}

build() {
  cd ${pkgname}
  qmake-qt5 PREFIX=/usr filemanager.pro
  make
}

package() {
  cd ${pkgname}
  make INSTALL_ROOT="$pkgdir" install
}
