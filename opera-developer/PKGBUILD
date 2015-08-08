# Maintainer: Christian Hesse <mail@eworm.de>

pkgname=opera-developer
pkgver=32.0.1933.0
pkgrel=3
pkgdesc='A fast and secure web browser and Internet suite - developer stream'
arch=('x86_64' 'i686')
url='http://www.opera.com/browser/'
license=('custom:opera')
depends=('alsa-lib' 'nss' 'gtk2' 'gconf' 'libxss' 'libxtst' 'desktop-file-utils')
optdepends=('curl: opera crash reporter and autoupdate checker'
	'libnotify: native desktop notifications'
	'opera-ffmpeg-codecs: support h.264 and mp3 codecs')
install=opera.install
options=(!strip)
backup=("etc/${pkgname}/default")
source=('opera'
	'default')
source_x86_64=("http://get.geo.opera.com/pub/${pkgname}/${pkgver}/linux/${pkgname}_${pkgver}_amd64.deb")
source_i686=("http://get.geo.opera.com/pub/${pkgname}/${pkgver}/linux/${pkgname}_${pkgver}_i386.deb")
sha256sums=('508512464e24126fddfb2c41a1e2e86624bdb0c0748084b6a922573b6cf6b9c5'
	'c3c7e5ae35d897b0cca91c07d55cdca4ea30b3c1ba89d428807454a6257bd1be')
sha256sums_x86_64=('36e153c3778ab543ea0b0921534f42dd689aaadd1fe0aac43d5e5fcb832a8a58')
sha256sums_i686=('be60c87212307a06d7628761b9bb16e15c2bc7d711957467b4c55e2f7f868b32')
# alternative download
#source=("ftp://ftp.opera.com/pub/${pkgname}/${pkgver}/linux/${pkgname}_${pkgver}_amd64.deb")
#source=("http://deb.opera.com/${pkgname}/pool/non-free/o/${pkgname}/${pkgname}_${pkgver}_amd64.deb")

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

