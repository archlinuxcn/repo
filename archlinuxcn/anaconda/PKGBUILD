# Maintainer: Jingbei Li <i@jingbei.li>
# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: kastik <kastik69420@gmail.com>
# Contributor: Ismaël Bouya <ismael.bouya@normalesup.org>
# Contributor: Martin Wimpress <code@flexion.org>
pkgname=anaconda
pkgver=2023.03
pkgrel=2
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
	'libglvnd: for Anaconda Navigator support'
	'xdg-utils: for ')
source=(https://repo.${pkgname}.com/archive/Anaconda3-${pkgver}-Linux-x86_64.sh
	${pkgname}-navigator.desktop)
options=(!strip libtool staticlibs)
sha512sums=('27a44d1da6a6d0bce646e735510c3a16f30a74a310f86c6da09a6364d440717750bad96316ae978f66ed1801310e7d4cf0b5a410808a7c51522a484e636eb4ad'
	'16a4d08590c082dc6042a68783f5c6bfa03af6aa6e07baf489f7d698695d1e2659b0add6c123693da6516ebc031009f97368830f028e2c7af45db33f883aa26a')
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
	install -Dm 644 LICENSE.txt -t "${pkgdir}/usr/share/licenses/${pkgname}"

	# Installing .desktop for anaconda navigator
	install -Dm 644 "${srcdir}/${pkgname}-navigator.desktop" -t "${pkgdir}"/usr/share/applications/
}
