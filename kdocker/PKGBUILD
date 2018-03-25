pkgname=kdocker
pkgver=5.1
pkgrel=1
pkgdesc="An application to help you dock any application into the system tray"
arch=('i686' 'x86_64')
url="https://github.com/user-none/KDocker"
license=('GPL2')
depends=('qt5-base' 'qt5-x11extras' 'libxpm' 'libxmu')
source=(https://github.com/user-none/KDocker/archive/${pkgver}.tar.gz)
sha256sums=('4d0e6e9d35d0afe3358f38cfab7e25fe12c0c60b97d14aaaa2f8572674879034')

build() {
    cd "$srcdir/KDocker-$pkgver"

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
