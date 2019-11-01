# Maintainer: Bruce Zhang <zttt183525594@gmail.com>

pkgname=winetricks-zh
pkgver=20190615.3
pkgrel=1
pkgdesc='A windows applications setup wizard for Chinese wine users'
url='https://github.com/hillwoodroc/winetricks-zh'
license=('LGPL')
arch=('any')
depends=('wine' 'cabextract' 'unzip' 'xorg-xmessage')
optdepends=('zenity: GUI for GNOME desktop'
            'kdialog: GUI for KDE desktop')
source=("https://github.com/hillwoodroc/winetricks-zh/archive/${pkgver}.tar.gz")
sha256sums=('a07f09a02c5e29f2c05d8603c00a1c6c8a3dbb7f18b85dfedb7e654827486a4f')

package() {
    cd "$pkgname-$pkgver"
    install -D -m755 "$srcdir/${pkgname}-${pkgver}/winetricks-zh" "$pkgdir/usr/bin/winetricks-zh"
    install -D -m644 "$srcdir/${pkgname}-${pkgver}/winetricks-zh.desktop" "$pkgdir/usr/share/applications/winetricks-zh.desktop"
}
