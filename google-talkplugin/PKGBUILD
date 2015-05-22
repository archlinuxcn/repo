# Maintainer: Dominik Mayer <dominik.mayer@gmail.com>
# Maintainer: ava1ar <mail(at)ava1ar(dot)info>

pkgname=google-talkplugin
pkgver=5.41.0.0
pkgrel=3
pkgdesc="Video chat browser plug-in for Google Talk"
arch=('i686' 'x86_64')
url="http://www.google.com/chat/video"
license=('custom:google')
depends=('gtk2>=2.12.0' 'alsa-lib' 'mesa' 'lsb-release')
optdepends=('libnotify' 'pulseaudio')
source=(${pkgname}-license.html::https://www.google.com/intl/en/policies/terms/index.html)
sha1sums=('SKIP')
sha1sums_i686=('f6f5555cd2e48c41d2a438896ddf0df07a70781a')
sha1sums_x86_64=('b89fdc66ad728db5d564c4619ed480166e5be82c')
source_i686+=("https://dl.google.com/linux/talkplugin/rpm/stable/i386/${pkgname}-${pkgver}-1.i386.rpm")
source_x86_64+=("https://dl.google.com/linux/talkplugin/rpm/stable/x86_64/${pkgname}-${pkgver}-1.x86_64.rpm")

package() {
	cp -R "${srcdir}"/opt "${pkgdir}"
	install -d "${pkgdir}"/usr/lib
	cp -R "${srcdir}"/usr/lib*/* "${pkgdir}"/usr/lib
    
	# makeing it compatible with chromium and chromium-dev for Arch
	cp -R "${pkgdir}"/usr/lib/chromium-browser "${pkgdir}"/usr/lib/chromium
	cp -R "${pkgdir}"/usr/lib/chromium-browser "${pkgdir}"/usr/lib/chromium-dev
    
	# cleaning up cron update script
	rm -rf "${pkgdir}"/opt/google/talkplugin/cron
    
	# install license file
	install -Dm644 "${srcdir}"/${pkgname}-license.html "${pkgdir}"/usr/share/licenses/${pkgname}/license.html
}
