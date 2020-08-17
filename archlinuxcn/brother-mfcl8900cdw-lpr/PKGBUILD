# Maintainer: Colin Keenan <colinnkeenan at gmail dot com>

pkgname=brother-mfcl8900cdw-lpr
pkgver=1.5.0
pkgrel=1
pkgdesc="CUPS LPR driver:Brother MFC-L8900CDW:laser print copy scan fax"
arch=("i686" "x86_64")
url="https://support.brother.com/g/b/producttop.aspx?c=us&lang=en&prod=mfcl8900cdw_all"
license=("EULA")
groups=("base-devel")
source=("https://download.brother.com/welcome/dlf103242/mfcl8900cdwlpr-1.5.0-0.i386.deb")
md5sums=('61d8770c4289ffe61222fc5dec12e65c')

package() {
	tar -xf data.tar.gz -C "${pkgdir}"
}
