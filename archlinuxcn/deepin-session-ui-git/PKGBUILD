# Maintainer: DingYuan Zhang <justforlxz>

pkgname=deepin-session-ui-git
pkgver=5.2.0.16.r1.gbc630c7d
pkgrel=1
pkgdesc='Deepin desktop-environment - Session UI module'
arch=('x86_64')
url="https://github.com/linuxdeepin/dde-session-ui"
license=('GPL3')
groups=('deepin')
depends=('gsettings-qt' 'deepin-qt5integration-git' 'liblightdm-qt5' 'qt5-svg' 'deepin-daemon'
         'deepin-wallpapers')
makedepends=('deepin-gettext-tools' 'qt5-tools')
provides=('deepin-notifications' 'deepin-session-ui')
conflicts=('dde-workspace' 'deepin-session-ui' 'deepin-notifications')
replaces=('dde-workspace' 'deepin-session-ui' 'deepin-notifications')
groups=('deepin-git')
source=("git://github.com/linuxdeepin/dde-session-ui"
         deepin-session-ui-qt5.15.patch)
sha512sums=('SKIP'
            '846726964cac5005b0ac3a5043e5df914ff83faff68f98d2513d86494a9718a85ae4268776fd08ffe852e28ac0ae5878353d3c65db84fbd1509b2325e70fe8d6')

pkgver() {
    cd dde-session-ui
    git describe --long --tags | sed 's/\([^-]*-g\)/r\1/;s/-/./g'
}

prepare() {
  cd dde-session-ui
  sed -i 's|/usr/share/backgrounds/default_background.jpg|/usr/share/backgrounds/deepin/desktop.jpg|' widgets/*.cpp

  sed -i '/include <QPainter>/a #include <QPainterPath>' dde-notification-plugin/notifications/notificationswidget.cpp

  patch -p1 -i ../deepin-session-ui-qt5.15.patch # Fix build with Qt 5.15
}

build() {
  cd dde-session-ui
  qmake-qt5 PREFIX=/usr
  make
}

package() {
  cd dde-session-ui
  make INSTALL_ROOT="$pkgdir" install
}
