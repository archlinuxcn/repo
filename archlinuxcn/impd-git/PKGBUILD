# Maintainer: Ren Tatsumoto <tatsu at autistici dot org>

pkgname=impd-git
conflicts=('impd')
provides=('impd')
pkgver=0.8.r1.g0ec9ab5
pkgrel=1
pkgdesc="Manage passive immersion and create condensed audio."
arch=(any)
url="https://github.com/Ajatt-Tools/impd"
license=("GPL3")
source=("${pkgname}::git+${url}")
depends=('bash' 'gawk' 'ffmpeg' 'mpd' 'xdg-user-dirs')
makedepends=('git')
optdepends=(
	'mpc: interaction with mpd'
	'libnotify: desktop notifications'
	'youtube-dl: adding audio from youtube'
	'yt-dlp: adding audio from youtube'
)
sha256sums=('SKIP')

pkgver() {
	cd -- "${pkgname}"
	git describe --long --tags | sed 's/^v//;s/\([^-]*-g\)/r\1/;s/-/./g'
}

package() {
	cd -- "${pkgname}"
	make DESTDIR="${pkgdir}" install
	install -Dm0644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname%-git}/LICENSE"
	install -Dm0644 README.md "${pkgdir}/usr/share/doc/${pkgname%-git}/README"
}
