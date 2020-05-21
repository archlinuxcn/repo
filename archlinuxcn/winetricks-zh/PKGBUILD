# Maintainer: Bruce Zhang <zttt183525594@gmail.com>

pkgname=winetricks-zh
pkgver=20200421.3
pkgrel=1
pkgdesc='A windows applications setup wizard for Chinese wine users'
url='https://github.com/hillwoodroc/winetricks-zh'
license=('LGPL')
arch=('any')
depends=('wine' 'cabextract' 'unzip' 'xorg-xmessage')
optdepends=('zenity: GUI for GNOME desktop'
            'kdialog: GUI for KDE desktop')
source=("https://github.com/hillwoodroc/winetricks-zh/archive/${pkgver}.tar.gz")
sha256sums=('4a30e135875808e13042f503911d442723b9fa5f1930790b870214e9a2a23958')

package() {
    cd "$pkgname-$pkgver"
    install -D -m755 "$srcdir/${pkgname}-${pkgver}/winetricks-zh" "$pkgdir/usr/bin/winetricks-zh"
    install -D -m644 "$srcdir/${pkgname}-${pkgver}/winetricks-zh.desktop" "$pkgdir/usr/share/applications/winetricks-zh.desktop"
}
