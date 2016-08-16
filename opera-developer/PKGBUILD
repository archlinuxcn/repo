# Maintainer: Christian Hesse <mail@eworm.de>

pkgname=opera-developer
pkgver=41.0.2323.0
pkgrel=1
pkgdesc='A fast and secure web browser and Internet suite - developer stream'
arch=('x86_64' 'i686')
url='http://www.opera.com/browser/'
license=('custom:opera')
depends=('alsa-lib' 'nss' 'gtk2' 'gconf' 'libxss' 'libxtst' 'desktop-file-utils')
optdepends=('curl: opera crash reporter and autoupdate checker'
	'libnotify: native desktop notifications'
	"${pkgname}-ffmpeg-codecs: support h.264 and mp3 codecs")
options=(!strip)
backup=("etc/${pkgname}/default")
source=('opera'
	'default')
_source='https://get.geo.opera.com/pub/'
# alternative downloads:
# http://get.geo.opera.com/pub/
# https://ftp.opera.com/pub/
# http://ftp.opera.com/pub/
# ftp://ftp.opera.com/pub/
source_x86_64=("${_source}/${pkgname}/${pkgver}/linux/${pkgname}_${pkgver}_amd64.deb")
source_i686=("${_source}/${pkgname}/${pkgver}/linux/${pkgname}_${pkgver}_i386.deb")
sha256sums=('508512464e24126fddfb2c41a1e2e86624bdb0c0748084b6a922573b6cf6b9c5'
	'99fc0d2822edd14e234d451995db47148125e4580221a292598959421d131231')
sha256sums_x86_64=('0f9d43762764e01c25c17c5c050f9eb136d0a5e28ea4dd3303660cfccba1440a')
sha256sums_i686=('2ba8991f782416759412cd8e95b5c5a2684da7863b01ca39a7a2a7abe29f3af5')

prepare() {
	cd ${srcdir}/

	sed -i -e "s/%pkgname%/${pkgname}/g" \
		-e "s/%operabin%/${pkgname}\/${pkgname}/g" \
		opera default
}

package() {
	cd ${srcdir}/

	# this is nested archive with final directory structure,
	# so extract the inner tarball to ${pkgdir}
	tar xJf data.tar.xz -C "${pkgdir}/"

	# get rid of the extra subfolder {i386,x86_64}-linux-gnu
	(
		cd "${pkgdir}/usr/lib/"*-linux-gnu/
		mv "${pkgname}" ../
	)
	rm -rf "${pkgdir}/usr/lib/"*-linux-gnu

	# set suid bit for Opera sandbox
	chmod 4755 "${pkgdir}/usr/lib/${pkgname}/opera_sandbox"

	# install default options
	install -Dm644 "default" "${pkgdir}/etc/${pkgname}/default"

	# install opera wrapper
	rm "${pkgdir}/usr/bin/${pkgname}"
	install -Dm755 "opera" "${pkgdir}/usr/bin/${pkgname}"

	# license
	install -Dm644 \
		"${pkgdir}/usr/share/doc/${pkgname}/copyright" \
		"${pkgdir}/usr/share/licenses/${pkgname}/copyright"
}

