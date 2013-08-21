# Maintainer: vehicle lee <lizaifang@gmail.com>
pkgname=aliedit
pkgver=1.0.3.20
pkgrel=2
pkgdesc='www.alipay.com security control'
url='http://www.alipay.com'
arch=('i686' 'x86_64')
license=('custom')
depends=('libpng12' 'gtk2' 'gcc-libs')
source=('https://download.alipay.com/alipaysc/linux/aliedit/1.0.3.20/aliedit.tar.gz')
md5sums=('bb3e6270fc85c532beb8ee30b1deb80a')

package() {
	cd "${srcdir}"
	ARCHIVE=`awk '/^__ARCHIVE_BELOW__/ {print NR + 1; exit 0; }' ${srcdir}/aliedit.sh`
	tail -n+$ARCHIVE aliedit.sh | tar xzvm -C "${srcdir}"/
	if [ "$CARCH" = "i686" ]; then
		install -D -m644 "${srcdir}/lib/libaliedit32.so" "${pkgdir}/usr/lib/mozilla/plugins/libaliedit32.so"
	elif [ "$CARCH" = "x86_64" ]; then
		install -D -m644 "${srcdir}/lib/libaliedit64.so" "${pkgdir}/usr/lib/mozilla/plugins/libaliedit64.so"
	fi
}