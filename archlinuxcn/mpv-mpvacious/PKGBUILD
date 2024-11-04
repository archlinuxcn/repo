# Maintainer: Ren Tatsumoto <tatsu at autistici dot org>
# Contributor: eshrh <esrh at gatech dot edu>

pkgname=mpv-mpvacious
pkgver=0.37
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
sha512sums=('ec01f6398e937ac1e4c7736a91eb2d550f233720f1fb744732e8ce0d0dc9fcfcbd06c24acb5423bdee3b7af7b3d903e8bbbc65f218b822e9dbc3f1607cc7fbde')
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
