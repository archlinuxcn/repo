# Maintainer: brent s. <bts[at]square-r00t[dot]net>
validpgpkeys=('748231EBCBD808A14F5E85D28C004C2F93481F6B')
# Bug reports can be filed at https://bugs.square-r00t.net/index.php?project=3
# News updates for packages can be followed at https://devblog.square-r00t.net
# Past maintainer: Joris Steyn <jorissteyn@gmail.com>
# Contributor: TDY <tdy@gmx.com>
pkgname=iozone
pkgver=3.484
_pkgver=${pkgver/./_}
pkgrel=1
pkgdesc="A filesystem benchmark tool"
arch=('i686' 'x86_64')
url="http://www.iozone.org/"
license=('custom')
depends=('sh')
optdepends=('gnuplot: for generating graph reports')
install=$pkgname.install
source=("http://www.${pkgname}.org/src/current/${pkgname}${_pkgver}.tar"
	"${pkgname}${_pkgver}.tar.sig")
sha512sums=('bb1ac0c1724a5d3c20e90c56c0b4a438b4aa50384cddc76f4b77f2c465f052fd3fae9217b77688a2c6caf5e90611123a97ea0cd8074b3678068a90e6dd7857b7'
	    'SKIP')

build() {
	cd "${srcdir}/${pkgname}${_pkgver}/src/current"

	[[ "${CARCH}" == 'x86_64' ]] && TARGET='-AMD64'
	make linux${TARGET} CFLAGS="${CFLAGS}"
}

package() {
	cd "${srcdir}/${pkgname}${_pkgver}/src/current"

	_examples=usr/share/doc/iozone3

	install -Dm755 iozone ${pkgdir}/usr/bin/iozone
	install -Dm755 fileop ${pkgdir}/usr/bin/fileop
	install -Dm755 pit_server ${pkgdir}/usr/bin/pit_server
	install -Dm644 ../../docs/$pkgname.1 ${pkgdir}/usr/share/man/man1/$pkgname.1

	#for i in gnuplotps.dem gnu3d.dem gnuplot.dem Gnuplot.txt client_list; do
	#	install -Dm644 $i ${pkgdir}/$_examples/$i
	#done

	#for i in Generate_Graphs iozone_visualizer.pl gengnuplot.sh report.pl; do
	#	install -Dm755 $i ${pkgdir}/$_examples/$i
	#done
	for i in $(find ${srcdir}/${pkgname}${_pkgver}/docs -type f);
	do
		mode=$(stat -c "%a %n" ${i} | awk '{print $1}')
		fname=$(basename ${i})
		install -Dm${mode} ${i} ${pkgdir}/usr/share/doc/${pkgname}/${fname}
	done

}
