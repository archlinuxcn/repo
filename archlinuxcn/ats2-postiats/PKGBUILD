# Maintainer: Mario Rodas <marsam@users.noreply.github.com>
# Contributor: Jonathon Fernyhough <jonathon_at_manjaro_dot_org>

pkgname=ats2-postiats
_pkgname=ATS2-Postiats-gmp
pkgver=0.4.0
pkgrel=1
pkgdesc="Statically typed programming language"
arch=('i686' 'x86_64')
url="http://www.ats-lang.org/"
license=('GPL3')
depends=('bash' 'gmp')
options=('staticlibs' '!emptydirs' '!makeflags')
install="${pkgname}.install"
source=("https://downloads.sourceforge.net/project/ats2-lang/ats2-lang/ats2-postiats-${pkgver}/${_pkgname}-${pkgver}.tgz")

sha256sums=('1cdf6dca3d1a481d1ae7c0400c7da9f040d7542cc210b2de51a4d3fd61c091c1')

build() {
	cd "${srcdir}/${_pkgname}-${pkgver}"
	# NOTE: Before update a version check if has been correctly packaged
	# sed -i "s/0.2.11/${pkgver}/g" VERSION
	# sed -i "49s/0.3.9/${pkgver}/g" configure.ac
	autoconf
	./configure --prefix=/usr
	make all
}

package() {
	cd "${srcdir}/${_pkgname}-${pkgver}"
	make DESTDIR="${pkgdir}" install

	local profiled="${pkgdir}/etc/profile.d"
	local patshome="/usr/lib/${pkgname}-${pkgver}"
	mkdir -p "${profiled}"

	echo "export PATSHOME=${patshome}" > "${profiled}/${pkgname}.sh"
	echo "setenv PATSHOME ${patshome}" > "${profiled}/${pkgname}.csh"

	chmod 0755 "${profiled}/${pkgname}.sh" "${profiled}/${pkgname}.csh"
}

# Local Variables:
# compile-command: "makepkg -sm && mksrcinfo"
# End:
