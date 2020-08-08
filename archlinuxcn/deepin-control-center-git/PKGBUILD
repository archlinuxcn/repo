# Maintainer: DingYuan Zhang <justforlxz@gmail.com>

pkgname=deepin-control-center-git
_pkgname=deepin-control-center
pkgver=5.3.0.5.r0.g1ecf3e842
pkgrel=1
pkgdesc='New control center for linux deepin'
arch=('x86_64')
url="https://github.com/linuxdeepin/dde-control-center"
license=('GPL3')
depends=('desktop-file-utils' 'dtkwidget-git' 'deepin-account-faces' 'deepin-api-git' 'geoip' 'libpwquality'
         'geoip-database' 'geoip-database-extra' 'deepin-daemon-git' 'startdde-git' 'networkmanager-qt'
         'deepin-qt-dbus-factory-git' 'deepin-qt5integration-git' 'deepin-network-utils-git')
makedepends=('git' 'cmake' 'deepin-dock' 'ninja' 'qt5-tools')
optdepends=('redshift: automatic color temperature support'
            'networkmanager-openconnect: for OpenConnect support'
            'networkmanager-openvpn: for OpenVPN support'
            'networkmanager-pptp: for PPTP support'
            'networkmanager-strongswan: for StrongSwan support'
            'networkmanager-vpnc: for VPNC support'
            'network-manager-sstp: for SSTP support')
# Not packaged: network-manager-l2tp
conflicts=('deepin-control-center')
replaces=('deepin-control-center')
provides=('deepin-control-center')
groups=('deepin-git')
source=("git://github.com/linuxdeepin/dde-control-center/"
        $_pkgname-systeminfo-deepin-icon.patch
        $_pkgname-no-user-experience.patch)
sha512sums=('SKIP'
            '74fd63391e923ca37f4559f30da967ba7f33d4426b60d58d1ece8cd9a154578e8184b1a376a8d7ff3ef81ffce530915f79d0845a2612ae4e06522b96855ab3dd'
            '99fc7e369680f3a91cb30daaa9015fccf3f2b733522e917fbd94e69b48471dd739536e220d4a9c17a93834d51192832cabf355b633cca27c903f8dd3249f4c5d')

pkgver() {
    cd dde-control-center
    git describe --long --tags | sed 's/\([^-]*-g\)/r\1/;s/-/./g'
}

prepare() {
  rm dde-control-center/src/frame/window/icons/icons/dcc_nav_systeminfo_{42,84}px.svg
  patch -d dde-control-center -Np1 < $_pkgname-systeminfo-deepin-icon.patch
  patch -d dde-control-center -Np1 < $_pkgname-no-user-experience.patch
  mkdir -p build

  cd dde-control-center
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
  cd build
  cmake -GNinja -DDISABLE_SYS_UPDATE=YES -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_INSTALL_LIBDIR=/usr/lib \
    ../dde-control-center
  ninja
}

package() {
  cd build
  DESTDIR="$pkgdir" ninja install

  rm "$pkgdir"/etc/xdg/autostart/deepin-ab-recovery.desktop
  rmdir "$pkgdir"/etc/xdg/autostart "$pkgdir"/etc/xdg "$pkgdir"/etc
}
