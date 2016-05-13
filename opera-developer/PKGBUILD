# Maintainer: Christian Hesse <mail@eworm.de>

pkgname=opera-developer
pkgver=39.0.2226.0
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
sha256sums_x86_64=('289a090023f51d183de87bdaed72d4186f4b96dfafba704ccb238ff95ba31e43')
sha256sums_i686=('6a9cb8ff6e6975cee272312c54dc06a8f39ea691ffa19b090b25266e3cc4c4c9')

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

