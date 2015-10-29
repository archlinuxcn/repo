# Maintainer:  Giovanni Santini "ItachiSan" <giovannisantini93@yahoo.it>
# Previous maintainer:  agnotek <agnostic.sn [at]gmail.com>
# Contributor: agnotek <agnostic.sn [at]gmail.com>

pkgname=telegram-desktop-bin-dev
pkgver=0.9.8
pkgrel=1
_dev=1 # If it is a dev-only version, set this to 1
pkgdesc="Official desktop version of Telegram messaging app - Static binaries, developement version"
arch=('i686' 'x86_64')
url="https://desktop.telegram.org"
license=('GPL3')
depends=('libx11' 'libgcrypt' 'libasyncns' 'libsndfile' 'libsystemd' 'libdbus' 'openal' 'libogg' 'opus' 'opusfile' 'portaudio' 'openssl' 'zlib' 'libexif' 'xz')
optdepends=(
			'libappindicator-gtk2: to hide Telegram in the tray bar (GTK2-based desktop environment)'
			'libappindicator-gtk3: to hide Telegram in the tray bar (GTK3-based desktop environment)'
			'libappindicator-sharp: to hide Telegram in the tray bar (Unity-based desktop environment)'
			)
conflicts=('telegram-desktop' 'telegram-desktop-bin')
provides=('telegram-desktop')
replaces=('telegram-bin')
install="$pkgname.install"

# Sources
source=("$pkgname.sh" "$pkgname.desktop" "$pkgname.png")
# If this is a dev version
if [ $_dev == 1 ]
then
	_devsuffix=".dev"
else
	_devsuffix=""
fi
# Use this
source_i686=('https://updates.tdesktop.com/tlinux32/tsetup32.'${pkgver}${_devsuffix}'.tar.xz')
source_x86_64=('https://updates.tdesktop.com/tlinux/tsetup.'${pkgver}${_devsuffix}'.tar.xz')
# Checksums
sha256sums=('0f2a6e4c2b9b4ff5f4ddb628728be4cc5a419f79695c0151321a5f234099ee59'
            'e3e10fe8620bd4ed8fda41743ad844739757286eeecea5249cf1fcf21a8431bd'
            '4226167b476a75e844ddf0d429068e7e901bbde516810a7d4ca90f8405c01eef')
sha256sums_i686=('d9047ede64e75961fd7325778a18d623be17b0cb371b407e3f60244b0acf5cc0')
sha256sums_x86_64=('e93a372b3145fb988a04b9dee2d6cd583084373c56ecb7ab6790df9afffbabaf')

package() {

	cd "$srcdir/"

	# Creating needed directories
	install -dm755 "$pkgdir/opt/telegram/"
	install -dm755 "$pkgdir/usr/bin"
	install -dm755 "$pkgdir/usr/share/pixmaps/"
	install -dm755 "$pkgdir/usr/share/applications/"

	# Program
	install -Dm755 "$srcdir/Telegram/Telegram" "$pkgdir/opt/telegram/"
	install -Dm755 "$srcdir/Telegram/Updater" "$pkgdir/opt/telegram/"

	# Shell wrapper
	install -Dm755 "$srcdir/$pkgname.sh" "$pkgdir/usr/bin/telegram"

	# Desktop launcher
	install -Dm755 "$srcdir/$pkgname.png" "$pkgdir/usr/share/pixmaps/telegram.png"
	install -Dm755 "$srcdir/$pkgname.desktop" "$pkgdir/usr/share/applications/telegramdesktop.desktop"
}
