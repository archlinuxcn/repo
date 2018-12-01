# Maintainer: Gordian Edenhofer <gordian.edenhofer@gmail.com>

pkgname=zoom
pkgver=2.5.146186.1130
pkgrel=1
pkgdesc="Video Conferencing and Web Conferencing Service"
arch=('x86_64')
license=('custom')
url="https://zoom.us/"
depends=('fontconfig' 'glib2' 'libpulse' 'libsm' 'libx11' 'libxcb' 'libxcomposite' 'libxfixes' 'libxi'
	'libxrandr' 'libxrender' 'libxshmfence' 'libxslt' 'mesa' 'nss' 'pulseaudio-alsa' 'xcb-util-image' 'xcb-util-keysyms'
	'qt5-svg' 'qt5-webengine' 'qt5-quickcontrols2')
options=(!strip)
source=("${pkgname}-${pkgver}_orig_x86_64.pkg.tar.xz"::"https://zoom.us/client/${pkgver}/zoom_x86_64.pkg.tar.xz")
sha512sums=('6b606469972388743733a3540ea422401b7e24dc0456e7caf26971409a9151921a0b5b97f0391839f3309b3fc172976ed491855dd322eb3666a1b32a44ee8053')

package() {
	cp -dpr --no-preserve=ownership opt usr "${pkgdir}"
}
