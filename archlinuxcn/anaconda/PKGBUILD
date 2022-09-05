# Maintainer: Jingbei Li <i@jingbei.li>
# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: kastik <kastik69420@gmail.com>
# Contributor: Ismaël Bouya <ismael.bouya@normalesup.org>
# Contributor: Martin Wimpress <code@flexion.org>
pkgname=anaconda
pkgver=2022.05
pkgrel=1
pkgdesc="Completely free enterprise-ready Python distribution for large-scale data processing, predictive analytics, and scientific computing."
arch=(x86_64)
url="https://www.${pkgname}.com"
license=('custom')
source=(https://repo.${pkgname}.com/archive/Anaconda3-${pkgver}-Linux-x86_64.sh)
options=(!strip libtool staticlibs)
sha512sums=('45b7fd085cb4edabb388ab64cd1d5e1bb62aeb4c906d371552fa71b6fae341b10d30c4acb54af43d63f027180d6a16095443668f36954cbc2f362e295c8e2c47')
install="${pkgname}.install"

package() {
	prefix=${pkgdir}/opt/${pkgname}
	LD_PRELOAD="/usr/lib/libfakeroot/libfakeroot.so"

	# Packaging anaconda for installation to /opt/anaconda
	bash ${srcdir}/Anaconda3-${pkgver}-Linux-${CARCH}.sh -b -p $prefix -f
	[ "$BREAK_EARLY" = 1 ] && exit 1
	cd $prefix

	# Correcting permissions
	chmod a+r -R pkgs

	# Stripping $pkgdir
	sed -e "s|${pkgdir}||g" -i $(grep "${pkgdir}" . -rIl 2>/dev/null)

	# Installing license
	install -D -m644 LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
