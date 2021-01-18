# Maintainer: justforlxz <justforlxz@gmail.com>

pkgname=deepin-control-center-git
_pkgname=deepin-control-center
pkgver=5.3.0.82+c6.r50.gf5f741414
pkgrel=1
pkgdesc='New control center for linux deepin'
arch=('x86_64')
url="https://github.com/linuxdeepin/dde-control-center"
license=('GPL3')
depends=('dtkwidget-git' 'deepin-account-faces' 'libpwquality' 'startdde-git'
         'deepin-daemon-git' 'startdde-git' 'networkmanager-qt'
         'deepin-qt-dbus-factory-git' 'deepin-network-utils-git')
makedepends=('git' 'cmake' 'ninja' 'qt5-tools' 'qt5-base' 'qt5-x11extras' 'qt5-multimedia' 'qt5-svg' 'dtkcore-git' 'dtkwidget-git' 'dtkgui-git' 'networkmanager-qt' 'deepin-network-utils-git' 'deepin-qt-dbus-factory-git' 'gtest' 'polkit-qt5')
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
