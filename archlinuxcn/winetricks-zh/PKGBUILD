# Maintainer: Bruce Zhang <zttt183525594@gmail.com>

pkgname=winetricks-zh
pkgver=20190912.1
pkgrel=1
pkgdesc='A windows applications setup wizard for Chinese wine users'
url='https://github.com/hillwoodroc/winetricks-zh'
license=('LGPL')
arch=('any')
depends=('wine' 'cabextract' 'unzip' 'xorg-xmessage')
optdepends=('zenity: GUI for GNOME desktop'
            'kdialog: GUI for KDE desktop')
source=("https://github.com/hillwoodroc/winetricks-zh/archive/${pkgver}.tar.gz")
sha256sums=('efdc6df8dc70085994962ea692728c01d15ca89a8befcb92670a51b3429e2220')

package() {
    cd "$pkgname-$pkgver"
    install -D -m755 "$srcdir/${pkgname}-${pkgver}/winetricks-zh" "$pkgdir/usr/bin/winetricks-zh"
    install -D -m644 "$srcdir/${pkgname}-${pkgver}/winetricks-zh.desktop" "$pkgdir/usr/share/applications/winetricks-zh.desktop"
}
