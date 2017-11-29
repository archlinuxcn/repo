# Maintainer: Chad "crossroads1112" Sharp <crossroads1112@riseup.net>
pkgname=lumina-desktop
pkgver=1.2.0
pkgrel=1
my_pkgrel=p1
pkgfullname="${pkgname%-*}-${pkgver}-${my_pkgrel}"
pkgdesc="A Lightweight QT5 Desktop for FreeBSD"
arch=('x86_64' 'i686')
url="https://github.com/trueos/lumina"
license=('BSD')
depends=('qt5-base' 'qt5-svg' 'qt5-multimedia' 'qt5-x11extras' 'fluxbox' 'oxygen' 'oxygen-icons' 'xscreensaver' 'desktop-file-utils')
optdepends=('xorg-xbacklight: required for changing screen brightness' 'alsa-utils: required for adjusting audio volume' 'acpi: required for monitoring battery life' 'numlockx: required for changign state of numlock at login' 'pavucontrol: required for detatched audio mixer' 'fluxmod-styles: A good set of Fluxbox themes to improve the appearence of window decorations' 'network-manager-applet: Manage network connections from panel' 'xterm: Terminal emulator')
makedepends=('qt5-base' 'qt5-tools')
conflicts=("lumina-de-git" "lumina-desktop-git" "insight-fm")
provides=("${pkgname%-*}" "insight-fm")
install="${pkgname%-*}.install"
source=("https://github.com/trueos/lumina/archive/v${pkgver}-${my_pkgrel}.tar.gz")
sha512sums=('8490e2b0f2fa08b2d63ec688f9993771ea935129a2947ef7bfa1874424cbede6d8877083ce90658c283858e67397383b5bab536388e9222b440015ebdf8b2919')

build(){
    cd "$srcdir/${pkgfullname}"
    find $srcdir/${pkgfullname} -name *.desktop -exec sed -i 's/usr\/local/usr/' {} \;
    qmake-qt5 QMAKE_CFLAGS_ISYSTEM= PREFIX="/usr" QT5LIBDIR=/usr/lib/qt
    make
}

package() {
    cd "$srcdir/${pkgfullname}"
    make INSTALL_ROOT="${pkgdir}" install
    mv "${pkgdir}"/usr/etc "${pkgdir}"/etc
}
