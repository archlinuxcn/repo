# Maintainer: Ren Tatsumoto <tatsu at autistici dot org>
# Contributor: eshrh <esrh at gatech dot edu>

pkgname=mpv-mpvacious
pkgver=0.23
pkgrel=1
pkgdesc="Adds mpv keybindings to create Anki cards from movies and TV shows."
arch=('any')
url="https://github.com/Ajatt-Tools/mpvacious"
license=('GPL3')
depends=('mpv>=0.34' 'gawk' 'curl')
makedepends=()
optdepends=(
	'xclip: clipboard autocopy'
	'wl-clipboard: clipboard autocopy on wayland'
	'ffmpeg: using ffmpeg directly to encode media'
)
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/refs/tags/v${pkgver}.tar.gz")
sha512sums=('4833acf845e3dd589dfe5c02b769ee3b30f08f93995329b476b1a8b6b2e9c069b744488c6fb4f2d13420a1ce3a20e27dfd7c395cd617be9d0341b4ffd6febd4c')
install="${pkgname#mpv-}.install"

package() {
	cd -- "$srcdir/${pkgname#mpv-}-${pkgver}"
	find . -type f -iname '*.lua' | while read -r file; do
		install -Dm644 "$file" "${pkgdir}/etc/mpv/scripts/${pkgname#mpv-}/${file}"
	done
	find . -type f -iname '*.sh' | while read -r file; do
		install -Dm755 "$file" "${pkgdir}/etc/mpv/scripts/${pkgname#mpv-}/${file}"
	done
	install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
	install -Dm644 .github/RELEASE/subs2srs.conf "$pkgdir/etc/mpv/script-opts/subs2srs.conf"
}
