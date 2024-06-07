# Maintainer: Ren Tatsumoto <tatsu at autistici dot org>
# Contributor: eshrh <esrh at gatech dot edu>

pkgname=mpv-mpvacious
pkgver=0.35
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
sha512sums=('b3dd902b7275597e7323e7a0d01b52a20e155a58eb504bc3689e038936b44a4f93c0dbf81f8d10258dd182bd88e2b2b2a950c4196ae7ec402ea5997712092a9c')
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
