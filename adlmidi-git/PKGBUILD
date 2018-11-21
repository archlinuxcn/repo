# Maintainer: Stephen Gregoratto <themanhimself at sgregoratto dot me>
pkgname=adlmidi-git
pkgver=1.2.6.1.r0.8aa85de
pkgrel=2
pkgdesc="CLI MIDI player using OPL3 emulation"
url="https://bisqwit.iki.fi/source/adlmidi.html"
license=('GPL3' 'GPL2+')
arch=('i686' 'x86_64')
depends=('sdl2')
makedepends=('git')
optdepends=('ffmpeg: recording output to video file')
conflicts=(adlmidi)
source=("git://bisqwit.iki.fi/adlmidi.git")
sha256sums=('SKIP')

pkgver() {
	cd "${pkgname/-git}"
	git describe --long --tags origin/release | sed 's/\([^-]*-\)g/r\1/;s/-/./g'
}

build() {
	cd "${pkgname/-git}"
	make 
}

package() {
	cd "${pkgname/-git}"
	install -D ./adlmidi "${pkgdir}"/usr/bin/adlmidi
}
