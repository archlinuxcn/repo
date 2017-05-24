# Author: Syed Adnan Kamili <adnan.kamili AT gmail D0T com>
# Maintainer: Marc Rozanc <marc AT rozanc D0T fr>

pkgname=flareget
_rel=4.4
_subrel=100
pkgver=${_rel}.${_subrel}
pkgrel=3
pkgdesc="A full featured, advanced, multi-threaded, multisegment download manager and accelerator."
arch=('i686' 'x86_64')
url="http://flareget.com"
license=('custom')
depends=('glibc>=2.13' 'qt4>=4.8.1' 'libmetalink')
install=${pkgname}.install
backup=('etc/opt/chrome/native-messaging-hosts/com.flareget.flareget.json'
        'etc/chromium/native-messaging-hosts/com.flareget.flareget.json')

if  [ "${CARCH}" = "i686" ]; then
    _arch1="i386"
elif [ "${CARCH}" = "x86_64" ]; then
    _arch1="x86_64"
fi

source_i686=("https://www.flareget.com/downloads/files/flareget/rpm/i386/${pkgname}-${_rel}-${_subrel}.i386.rpm")
source_x86_64=("https://www.flareget.com/downloads/files/flareget/rpm/amd64/${pkgname}-${_rel}-${_subrel}.x86_64.rpm")
sha256sums_i686=("9b4b514ac46001adb379db2c82b1afad06c534541d3e18653e1fc617737c841a")
sha256sums_x86_64=("413ce9161e5d17f71cc8d4524d76dfeaaa80a2033d4f7a893583dd3cf8137602")

package() {
    cd $srcdir
    cp -ra usr $pkgdir/usr
    cp -ra etc $pkgdir/etc
    
    # License
    install -Dm644 $pkgdir/usr/share/doc/$pkgname/COPYING $pkgdir/usr/share/licenses/$pkgname/LICENSE
    rm $pkgdir/usr/share/doc/$pkgname/COPYING
}

