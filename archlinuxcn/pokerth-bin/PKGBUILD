# Maintainer: Jax Young <jaxvanyang@gmail.com>
pkgname=pokerth-bin
_pkgname="${pkgname%-bin}"
pkgver=2.1.8
pkgrel=1
pkgdesc="Poker game written in C++/Qt"
arch=('x86_64')
url="https://github.com/pokerth/pokerth"
license=('AGPL-3.0-or-only' 'LicenseRef-custom')
depends=('glibc')
provides=("$_pkgname")
conflicts=("$_pkgname")
source=(
	"$_pkgname-$pkgver.zip::$url/releases/download/v$pkgver/pokerth-$pkgver-linux-x86_64.zip"
	"pokerth.png"
	"pokerth.svg"
	"pokerth.desktop"
)
sha256sums=('1aa588f7b7844cddc819fdbb006fd9bba531bccf5263e0c9f853380b51606298'
            'f35bacd011dce3258b8394b82e28ef605f491c6fac6c2dfc743d403b23fd5eb2'
            '72ff070b9626661a051cc0582a69cd95b41809b6f4f2d8738245d92f3c417bb4'
            '8bbfb9db5be8bca7ed20b703251afa336f4445bd79e7b049b028aff0e788bb57')
_pkgsrc="pokerth-linux-binary"

prepare() {
	cd "$_pkgsrc"
	# pokerth.desktop is not included in the release zip right now
	# sed -i "s|^Exec=.*|Exec=/opt/$pkgname/pokerth|" share/pokerth.desktop
	sed -i 's|^SCRIPT_DIR=.*|SCRIPT_DIR="/opt/pokerth-bin"|' pokerth
	# don't allow it to create a user desktop entry
	sed -i 's|^integrate_desktop_entry$||' pokerth
}

package() {
	install -Dm644 -t "$pkgdir/usr/share/pixmaps" pokerth.png
	install -Dm644 -t "$pkgdir/usr/share/icons/hicolor/128x128/apps" pokerth.png
	install -Dm644 -t "$pkgdir/usr/share/icons/hicolor/scalable/apps" pokerth.svg
	install -Dm644 -t "$pkgdir/usr/share/applications" pokerth.desktop

	cd "$_pkgsrc"
	install -d "$pkgdir/opt"
	cp -r . "$pkgdir/opt/$pkgname"
	install -Dm644 -t "$pkgdir/usr/share/licenses/$pkgname" data/data-copyright.txt
	install -Dm755 -t "$pkgdir/usr/bin" pokerth
}
