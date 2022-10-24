# Maintainer: Jingbei Li <i@jingbei.li>
# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: kastik <kastik69420@gmail.com>
# Contributor: Ismaël Bouya <ismael.bouya@normalesup.org>
# Contributor: Martin Wimpress <code@flexion.org>
pkgname=anaconda
pkgver=2022.10
pkgrel=1
pkgdesc="Simplifies package management and deployment of Anaconda"
arch=(x86_64)
url="https://${pkgname}.com"
license=('custom')
provides=('conda')
optdepends=('libxau: for Anaconda Navigator support'
	'libxi: for Anaconda Navigator support'
	'libxss: for Anaconda Navigator support'
	'libxtst: for Anaconda Navigator support'
	'libxcursor: for Anaconda Navigator support'
	'libxcomposite: for Anaconda Navigator support'
	'libxdamage: for Anaconda Navigator support'
	'libxfixes: for Anaconda Navigator support'
	'libxrandr: for Anaconda Navigator support'
	'libxrender: for Anaconda Navigator support'
	'mesa-libgl: for Anaconda Navigator support'
	'alsa-lib: for Anaconda Navigator support'
	'libglvnd: for Anaconda Navigator support')
source=(https://repo.${pkgname}.com/archive/Anaconda3-${pkgver}-Linux-x86_64.sh)
options=(!strip libtool staticlibs)
sha512sums=('a0f17c8bbdcb05397da831af513a027738033844e7f9cdeb6e8b192d9c8f917109e72326e449f74bf3ee2a0da3789e0864c3d51ef2bdc816c62cc85f3395d226')
install="${pkgname}.install"

package() {
	prefix="${pkgdir}"/opt/${pkgname}
	LD_PRELOAD="/usr/lib/libfakeroot/libfakeroot.so"

	# Packaging anaconda for installation to /opt/anaconda
	bash "${srcdir}"/Anaconda3-${pkgver}-Linux-${CARCH}.sh -b -p $prefix -f
	[ "$BREAK_EARLY" = 1 ] && exit 1
	cd $prefix

	# Correcting permissions
	chmod a+r -R pkgs

	# Stripping $pkgdir
	sed -e "s|${pkgdir}||g" -i $(grep "${pkgdir}" . -rIl 2>/dev/null)

	# Installing license
	install -D -m644 LICENSE.txt "${pkgdir}"/usr/share/licenses/${pkgname}/LICENSE
}
