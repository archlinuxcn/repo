# Maintainer: brent s. <bts[at]square-r00t[dot]net>
validpgpkeys=('748231EBCBD808A14F5E85D28C004C2F93481F6B')
# Bug reports can be filed at https://bugs.square-r00t.net/index.php?project=3
# News updates for packages can be followed at https://devblog.square-r00t.net
# Past maintainer: Joris Steyn <jorissteyn@gmail.com>
# Contributor: TDY <tdy@gmx.com>
pkgname=iozone
pkgver=3_471
pkgrel=1
pkgdesc="A filesystem benchmark tool"
arch=('i686' 'x86_64')
url="http://www.iozone.org/"
license=('custom')
depends=('sh')
optdepends=('gnuplot: for generating graph reports')
install=$pkgname.install
source=("http://www.${pkgname}.org/src/current/${pkgname}${pkgver}.tar"
	"${pkgname}${pkgver}.tar.sig")
sha512sums=('c61b2b8b5af3dccdb99b26aef8a0a4f2f5f467fc3985ac72ed4bb4fb36e4b7684ca6dbaa5bbc05ae0a4e73852e048e9fd2495eda9313f5abc4e631499d683aec'
	    'SKIP')

build() {
	cd "${srcdir}/${pkgname}${pkgver}/src/current"

	[[ "${CARCH}" == 'x86_64' ]] && TARGET='-AMD64'
	make linux${TARGET} CFLAGS="${CFLAGS}"
}

package() {
	cd "${srcdir}/${pkgname}${pkgver}/src/current"

	_examples=/usr/share/doc/iozone3/examples

	install -Dm755 iozone ${pkgdir}/usr/bin/iozone
	install -Dm755 fileop ${pkgdir}/usr/bin/fileop
	install -Dm755 pit_server ${pkgdir}/usr/bin/pit_server
	install -Dm644 ../../docs/$pkgname.1 ${pkgdir}/usr/share/man/man1/$pkgname.1

	for i in gnuplotps.dem gnu3d.dem gnuplot.dem Gnuplot.txt client_list; do
		install -Dm644 $i ${pkgdir}/$_examples/$i
	done

	for i in Generate_Graphs iozone_visualizer.pl gengnuplot.sh report.pl; do
		install -Dm755 $i ${pkgdir}/$_examples/$i
	done
}
