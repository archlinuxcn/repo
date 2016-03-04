# Maintainer: Christian Hesse <mail@eworm.de>

pkgname=opera-beta
pkgver=36.0.2130.26
pkgrel=1
pkgdesc='A fast and secure web browser and Internet suite - beta stream'
arch=('x86_64' 'i686')
url='http://www.opera.com/browser/'
license=('custom:opera')
depends=('alsa-lib' 'nss' 'gtk2' 'gconf' 'libxss' 'libxtst' 'desktop-file-utils')
makedepends=('patchelf')
optdepends=('curl: opera crash reporter and autoupdate checker'
	'libnotify: native desktop notifications'
	"${pkgname}-ffmpeg-codecs: support h.264 and mp3 codecs")
install=opera.install
options=(!strip)
backup=("etc/${pkgname}/default")
source=('opera'
	'default')
source_x86_64=("http://get.geo.opera.com/pub/${pkgname}/${pkgver}/linux/${pkgname}_${pkgver}_amd64.deb")
source_i686=("http://get.geo.opera.com/pub/${pkgname}/${pkgver}/linux/${pkgname}_${pkgver}_i386.deb")
sha256sums=('508512464e24126fddfb2c41a1e2e86624bdb0c0748084b6a922573b6cf6b9c5'
	'99fc0d2822edd14e234d451995db47148125e4580221a292598959421d131231')
sha256sums_x86_64=('b1c90473be797a9f4e9f949555537f926cc4019376e2b5e5b82324e17b5b8b5b')
sha256sums_i686=('33b0471daa6f33524b1948beab5cffe3c3d2b78d0adc35df25f3541dcca4afc6')
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

	# patch rpath in opera-beta binary
	patchelf --set-rpath \$ORIGIN/lib_extra:\$ORIGIN/. \
		"$pkgdir/usr/lib/$pkgname/$pkgname"

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

