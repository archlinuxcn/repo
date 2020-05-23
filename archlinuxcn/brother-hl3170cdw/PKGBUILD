# Maintainer: David Pflug <david@pflug.email>
# Based on package from Phil Martella <philmartella@live.com>
# Based on brother-hl3150cdw by MCMic <come.bernigaud@laposte.net>
pkgname="brother-hl3170cdw"
pkgver="1.1.4"
pkgrel=1
pkgdesc="LPR and CUPS driver for the Brother HL3170CDW"
arch=('i686' 'x86_64')
url="http://solutions.brother.com/linux/en_us/"
license=('custom:brother commercial license')
depends=('cups')
install='brother-hl3170cdw.install'
source=(
	"http://www.brother.com/pub/bsc/linux/dlf/hl3170cdwlpr-1.1.2-$pkgrel.i386.rpm"
  "http://download.brother.com/welcome/dlf007057/hl3170cdwcupswrapper-${pkgver}-0.i386.rpm"
	'cupswrapper-license.txt'
	'lpr-license.txt'
)
sha512sums=('e21417ff2d44ae1d6c0af2254b29921acd029acaf2df45568e5a2722e2575b924d5260c706b03a3e4f97045e0009d3aa70d07a67c7bdebe697225dabf905ad68'
            'b05a5969f27e0340d0be794c54a87c5b09dcf399438c3380634dc60b27ec7b895e528c3bee3ea4504ea500ce71b4aadd5ab11b27b42f5ca8aedb4a0099d3b9ee'
            'bd035acc69734d954c132df67e80476094044d2c929e97bd6e0467aacfeefa9883da7474af8d8ff7fa65c3043ec6e1d8e0386e032c3f2121c36b0f6bfd079c86'
            'bf555e3622b68cc8a4d89f9fbb26ca09f29acf66c07d517be8aa7b58d985e1408d0d1bde408ba3b0e0aa842a69d6ebf0b4a1d194673203f42a3cbcecdcfaca06')
if test "$CARCH" == x86_64; then
	depends+=('lib32-glibc')
fi
prepare() {
	# setup cups-directories
	install -d $srcdir/usr/share/cups/model
	install -d $srcdir/usr/lib/cups/filter
	#  go to the cupswrapper directory and find the source file from wich to generate a ppd- and wrapper-file
	cd `find . -type d -name 'cupswrapper'`
	if [ -f cupswrapper* ]; then
		_wrapper_source=`ls cupswrapper*`
		sed -i '/^\/etc\/init.d\/cups/d' $_wrapper_source
		sed -i '/^sleep/d' $_wrapper_source
		sed -i '/^lpadmin/d' $_wrapper_source
		sed -i 's|/usr|$srcdir/usr|g' $_wrapper_source
		sed -i 's|/opt|$srcdir/opt|g' $_wrapper_source
		sed -i 's|/model/Brother|/model|g' $_wrapper_source
		sed -i 's|lpinfo|echo|g' $_wrapper_source
		export srcdir=$srcdir
		./$_wrapper_source
		sed -i 's|$srcdir||' $srcdir/usr/lib/cups/filter/*lpdwrapper*
		sed -i "s|$srcdir||" $srcdir/usr/lib/cups/filter/*lpdwrapper*
		rm $_wrapper_source
	fi
	#  /etc/printcap is managed by cups
	rm `find $srcdir -type f -name 'setupPrintcap*'`
}
package() {
	cp -R $srcdir/usr $pkgdir
	if [ -d $srcdir/opt ]; then cp -R $srcdir/opt $pkgdir; fi
	install -m 644 -D cupswrapper-license.txt $pkgdir/usr/share/licenses/${pkgname}/cupswrapper-licence.txt
	install -m 644 -D lpr-license.txt $pkgdir/usr/share/licenses/${pkgname}/lpr-licence.txt
}
