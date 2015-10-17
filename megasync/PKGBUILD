# Maintainer: Alfonso Saavedra "Son Link" <sonlink.dourden@gmail.com>
pkgname=megasync
pkgver=2.3.1
pkgrel=1
pkgdesc="Sync your files to your Mega account. Official app"
arch=('i686' 'x86_64')
url="https://mega.co.nz/#sync"
license=('custom:The Clarified Artistic License')
conflicts=('megatools')
depends=('openssl' 'c-ares' 'libgcrypt' 'crypto++' 'qt4' 'libpng' 'qtchooser' 'sqlite')
source_i686=("https://mega.co.nz/linux/MEGAsync/Debian_8.0/i386/${pkgname}_${pkgver}_i386.deb")
source_x86_64=("https://mega.co.nz/linux/MEGAsync/Debian_8.0/amd64/${pkgname}_${pkgver}_amd64.deb")
md5sums_i686=('562775fe7e0a8a785ce6215af6341401')
md5sums_x86_64=('1e925a593a99eebcc51722f4f485377e')
install="${pkgname}.install"
package (){
	cd "${srcdir}"
	pwd
	tar -xvf data.tar.xz -C ${pkgdir}
	rm -r ${pkgdir}/usr/share/doc
}
