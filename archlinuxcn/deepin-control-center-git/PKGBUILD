# Maintainer: justforlxz <justforlxz@gmail.com>

pkgname=deepin-control-center-git
_pkgname=deepin-control-center
pkgver=5.3.0.68.r83.g4f8555dfd
pkgrel=1
pkgdesc='New control center for linux deepin'
arch=('x86_64')
url="https://github.com/linuxdeepin/dde-control-center"
license=('GPL3')
depends=('dtkwidget-git' 'deepin-account-faces' 'libpwquality' 'startdde-git'
         'deepin-daemon-git' 'startdde-git' 'networkmanager-qt'
         'deepin-qt-dbus-factory-git' 'deepin-network-utils-git')
makedepends=('git' 'cmake' 'ninja' 'qt5-tools' 'qt5-base' 'qt5-x11extras' 'qt5-multimedia' 'qt5-svg' 'dtkcore-git' 'dtkwidget-git' 'dtkgui-git' 'networkmanager-qt' 'deepin-network-utils-git' 'deepin-qt-dbus-factory-git' 'gtest')
optdepends=('redshift: automatic color temperature support'
            'networkmanager-openconnect: for OpenConnect support'
            'networkmanager-openvpn: for OpenVPN support'
            'networkmanager-pptp: for PPTP support'
            'networkmanager-strongswan: for StrongSwan support'
            'networkmanager-vpnc: for VPNC support'
            'network-manager-sstp: for SSTP support')
# Not packaged: network-manager-l2tp
conflicts=('deepin-control-center')
provides=('deepin-control-center')
groups=('deepin-git')
source=("$pkgname::git://github.com/linuxdeepin/dde-control-center/"
        $_pkgname-systeminfo-deepin-icon.patch)
sha512sums=('SKIP'
            '74fd63391e923ca37f4559f30da967ba7f33d4426b60d58d1ece8cd9a154578e8184b1a376a8d7ff3ef81ffce530915f79d0845a2612ae4e06522b96855ab3dd')

pkgver() {
    cd $pkgname
    git describe --long --tags | sed 's/\([^-]*-g\)/r\1/;s/-/./g'
}

prepare() {
  rm $pkgname/src/frame/window/icons/icons/dcc_nav_systeminfo_{42,84}px.svg
  patch -d $pkgname -Np1 < $_pkgname-systeminfo-deepin-icon.patch

  cd $pkgname
  sed -i '/#include <QPainter>/a #include <QPainterPath>' src/frame/widgets/basiclistdelegate.cpp src/frame/window/modules/update/updatehistorybutton.cpp \
                                                          src/frame/window/modules/commoninfo/commonbackgrounditem.cpp src/frame/modules/accounts/useroptionitem.cpp \
                                                          src/frame/window/modules/sync/pages/avatarwidget.cpp src/frame/window/modules/accounts/avataritemdelegate.cpp \
                                                          src/frame/modules/accounts/avatarwidget.cpp src/frame/window/modules/accounts/accountswidget.cpp \
                                                          src/frame/modules/datetime/timezone_dialog/popup_menu.cpp src/frame/modules/display/recognizedialog.cpp \
                                                          src/frame/window/modules/personalization/roundcolorwidget.cpp src/frame/window/modules/unionid/pages/avatarwidget.cpp
  sed -i '/#include <QRect>/a #include <QPainterPath>' src/frame/window/modules/personalization/personalizationgeneral.cpp

  sed -i 's|/bin/deepin-recovery-tool|/usr/bin/deepin-recovery-tool|' src/frame/window/modules/systeminfo/backupandrestoreworker.cpp

  # remove after they obey -DDISABLE_SYS_UPDATE properly
  sed -i '/new UpdateModule/d' src/frame/window/mainwindow.cpp
}

build() {
  mkdir -p $pkgname/build
  cd $pkgname/build
  cmake -GNinja -DDISABLE_SYS_UPDATE=YES -DDISABLE_RECOVERY=YES -DDISABLE_ACTIVATOR=YES -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_INSTALL_LIBDIR=/usr/lib \
    ../
  ninja
}

package() {
  cd $pkgname/build
  DESTDIR="$pkgdir" ninja install
}
