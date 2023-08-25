# Maintainer: Ren Tatsumoto <tatsu at autistici dot org>
# Contributor: eshrh <esrh at gatech dot edu>

pkgname=mpv-mpvacious
pkgver=0.24
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
sha512sums=('f060fc49989a6a62553838c506060dd13c0886334b0a587e65a424eac9caa50c6699c773a251b0784c089d85374dd8ece88b993890a988846d650b611e2d7790')
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
