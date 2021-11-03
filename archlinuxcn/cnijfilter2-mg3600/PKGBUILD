# Maintainer: crazyboycjr <crazyboycjr@gmail.com>
# Based on the PKGBUILD for 3500 series by yaroslav <proninyaroslav@mail.ru>

pkgname=cnijfilter2-mg3600
pkgver=5.20
pkgrel=3
pkgdesc="Canon InkJet Printer Driver mg3600"
arch=('i686' 'x86_64')
url="http://www.canon-printerdrivers.com/2015/12/canon-pixma-mg3600-driver-download-mac.html"
license=('custom')
depends=('popt')
conflicts=('cnijfilter-common' 'cnijfilter2')
source=("http://gdlp01.c-wss.com/gds/2/0100006902/01/cnijfilter2-5.20-1-deb.tar.gz")
md5sums=('1bd481e5c2b539bc29ad34b346f4b04f')

package() {
    local _pkgarch=$(echo -n "${CARCH}" | sed 's/x86_/amd/' | sed 's/i6/i3/')
    local _debdir="${srcdir}/cnijfilter2-${pkgver}-1-deb/packages"

    cd $pkgdir
    ar -x "${_debdir}/cnijfilter2_${pkgver}-1_${_pkgarch}.deb" "data.tar.gz"
    tar -xzf data.tar.gz && rm -f data.tar.gz

    mkdir -p usr/share/licenses/${pkgname}
    mv usr/share/doc/cnijfilter2/* usr/share/licenses/${pkgname}
    rmdir usr/share/doc/cnijfilter2
    rmdir usr/share/doc

    # Weird permissions error from namcap
    chown root usr/lib/bjlib2/cnnet.ini
    chgrp root usr/lib/bjlib2/cnnet.ini

    chmod 0755 $(find usr/bin -type f)
    chmod 0755 $(find usr/lib -type f)
    chmod 0644 $(find usr/share -type f)
}
