# Maintainer: Colin Keenan <colinnkeenan at gmail dot com>

pkgname=brother-mfcl8900cdw-cups
pkgver=1.4.0
pkgrel=1
pkgdesc="CUPS wrapper:Brother MFC-L8900CDW:laser print copy scan fax"
arch=("i686" "x86_64")
url="https://support.brother.com/g/b/producttop.aspx?c=us&lang=en&prod=mfcl8900cdw_all"
license=("EULA")
groups=("base-devel")
source=("https://download.brother.com/welcome/dlf103251/mfcl8900cdwcupswrapper-1.4.0-0.i386.deb")
md5sums=('e170a674c30d25e0e18bbe86b2c04855')
install=brother-mfcl8900cdw-cups.install

package() {
	tar -xf data.tar.gz -C "${pkgdir}"
  mkdir -p -m 755 "${pkgdir}"/usr/share/cups/model
  mkdir -p -m 755 "${pkgdir}"/usr/lib/cups/filter
  ln -s /opt/brother/Printers/mfcl8900cdw/cupswrapper/brother_mfcl8900cdw_printer_en.ppd "${pkgdir}"/usr/share/cups/model
  ln -s /opt/brother/Printers/mfcl8900cdw/cupswrapper/brother_lpdwrapper_mfcl8900cdw "${pkgdir}"/usr/lib/cups/filter
}
