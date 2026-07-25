# Maintainer: Jax Young <jaxvanyang@gmail.com>
pkgname=pokerth-bin
_pkgname="${pkgname%-bin}"
pkgver=2.1.4
pkgrel=1
pkgdesc="Poker game written in C++/Qt"
arch=('x86_64')
url="https://github.com/pokerth/pokerth"
license=('AGPL-3.0-or-later' 'LicenseRef-custom')
depends=('glibc')
provides=("$_pkgname")
conflicts=("$_pkgname")
source=(
	"$_pkgname-$pkgver.zip::$url/releases/download/v$pkgver/pokerth-$pkgver-linux-x86_64.zip"
	"pokerth.png"
	"pokerth.svg"
)
sha256sums=('c979314859fca5ff46baadd983ef494225bd8eefa587408b834a53dab50e808a'
            'f35bacd011dce3258b8394b82e28ef605f491c6fac6c2dfc743d403b23fd5eb2'
            '72ff070b9626661a051cc0582a69cd95b41809b6f4f2d8738245d92f3c417bb4')
_pkgsrc="pokerth-linux-binary"

prepare() {
	cd "$_pkgsrc"
	sed -i "s|^Exec=.*|Exec=/opt/$pkgname/pokerth|" share/pokerth.desktop
	sed -i 's|^SCRIPT_DIR=.*|SCRIPT_DIR="/opt/pokerth-bin"|' pokerth
}

package() {
	install -Dm644 -t "$pkgdir/usr/share/pixmaps" pokerth.png
	install -Dm644 -t "$pkgdir/usr/share/icons/hicolor/128x128/apps" pokerth.png
	install -Dm644 -t "$pkgdir/usr/share/icons/hicolor/scalable/apps" pokerth.svg

	cd "$_pkgsrc"
	install -d "$pkgdir/opt"
	cp -r . "$pkgdir/opt/$pkgname"
	install -Dm644 -t "$pkgdir/usr/share/applications" share/pokerth.desktop
	install -Dm644 -t "$pkgdir/usr/share/licenses/$pkgname" data/data-copyright.txt
	install -Dm755 -t "$pkgdir/usr/bin" pokerth
}
