pkgname=kdocker
pkgver=5.0
pkgrel=2
pkgdesc="An application to help you dock any application into the system tray"
arch=('i686' 'x86_64')
url="https://github.com/user-none/KDocker"
license=('GPL2')
depends=('qt5-base' 'qt5-x11extras' 'libxpm' 'libxmu')
source=(https://github.com/user-none/KDocker/archive/${pkgver}.tar.gz)
sha256sums=('711c3a07d36d278eca47fa56db34fcb0f20f30210d9a1e86a9d0243b834e357a')

build() {
    cd "$srcdir/KDocker-$pkgver"

    # Fix building with Qt 5.5
    sed -i '/<QCoreApplication>/ a\#include <QDataStream>' 3rdparty/qtsingleapplication/src/qtlocalpeer.cpp

    # Make sure to restore docked applications on exit
    sed -i '/delete m_trayItemManager;/ i\m_trayItemManager->undockAll();' src/kdocker.cpp

    qmake-qt5
    make
}

package() {
    cd "$srcdir/KDocker-$pkgver"

    install -Dm755 "kdocker"                             "$pkgdir/usr/bin/kdocker"
    install -Dm644 "helpers/appdata/kdocker.appdata.xml" "$pkgdir/usr/share/appdata/kdocker.appdata.xml"
    strip "$pkgdir/usr/bin/kdocker"
    install -Dm644 "resources/images/kdocker.png"        "$pkgdir/usr/share/pixmaps/kdocker.png"
    install -Dm644 "helpers/kdocker.desktop"             "$pkgdir/usr/share/applications/kdocker.desktop"
    install -Dm644 "helpers/kdocker"                     "$pkgdir/etc/bash_completion.d/kdocker"
    install -Dm644 "helpers/kdocker.1"                   "$pkgdir/usr/share/man/man1/kdocker.1"
}
