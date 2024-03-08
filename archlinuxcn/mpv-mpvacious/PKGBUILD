# Maintainer: Ren Tatsumoto <tatsu at autistici dot org>
# Contributor: eshrh <esrh at gatech dot edu>

pkgname=mpv-mpvacious
pkgver=0.27
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
sha512sums=('e982fd94c6ee989d1bb64042779a87513c97f164a3f944ccc4ad7eea24c6894359e56341f171575278071238c0cbb1b0dcb0bb15b9343b406ed908bc82bd2772')
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
