# Maintainer: Bruce Zhang <zttt183525594@gmail.com>

pkgname=winetricks-zh
pkgver=20190615.1
pkgrel=1
pkgdesc='A windows applications setup wizard for Chinese wine users'
url='https://github.com/hillwoodroc/winetricks-zh'
license=('LGPL')
arch=('any')
depends=('wine' 'cabextract' 'unzip' 'xorg-xmessage')
optdepends=('zenity: GUI for GNOME desktop'
            'kdialog: GUI for KDE desktop')
source=("https://github.com/hillwoodroc/winetricks-zh/archive/${pkgver}.tar.gz")
sha256sums=('baff83200f08068808bc4ed6ea104a7cb53be28eee962bb21ecc8cfd0b34e0b4')

package() {
    cd "$pkgname-$pkgver"
    install -D -m755 "$srcdir/${pkgname}-${pkgver}/winetricks-zh" "$pkgdir/usr/bin/winetricks-zh"
    install -D -m644 "$srcdir/${pkgname}-${pkgver}/winetricks-zh.desktop" "$pkgdir/usr/share/applications/winetricks-zh.desktop"
}
