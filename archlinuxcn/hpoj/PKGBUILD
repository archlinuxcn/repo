# $Id: PKGBUILD 139136 2011-09-30 09:07:52Z eric $
# Contributer : Tobias Powalowski <tpowa@archlinux.org>
# Contributer : Wesley Merkel <ooesili@gmail.com>
# Maintainer : Sapphira Armageddos <shadowkyogre.public+aur@gmail.com>

pkgname=hpoj
pkgver=0.91
pkgrel=21
pkgdesc="Hewlett-Packard OfficeJet, PSC, LaserJet, and PhotoSmart printer multi-function peripherals (MFPs) drivers"
arch=('i686' 'x86_64')
url="http://hpoj.sourceforge.net"
license=('GPL' 'custom')
depends=('perl' 'libusb-compat' 'net-snmp' 'hplip>=1.7.2')
#makedepends=('qt3')
#optdepends=('qt3: for using xojpanel')
install=hpoj.install
source=(http://downloads.sourceforge.net/sourceforge/hpoj/$pkgname-$pkgver.tgz \
        hpoj-gcc4.patch hpoj-kernel26.patch hpoj-pack.patch \
        hpoj_gcc43.diff hpoj0.91-snmp5.5.patch)
md5sums=('0e083aeab9b00495aa433fa9465456e0' '347bb155c5dde443a93d92d8e64579a2'\
         '18481d3dcf6e9cadf0a3d196ee164e37' '1c3b99f1a2178675d56ece29daba0fd7'\
         '42bb57791cacf83e4d339e3653ad003e' 'af1cf13e95ff2654b84e470d0e18f537')
sha1sums=('36785cf1a925f569ed3983b8c068620e2c9b4456' 'cd2d37c2620e29b92b96fe779d10a6635c7f31b7'\
         'fe3328fd7a43ec83d76d0d7fb7be6c41027cddb3' '80258e3190ffb514c20386e8a7cf70ee18df95a5'\
         '22409b96d7bc67a10384a88c6b710981c0b90078' '4827cfa319bcd74ff8956e1bc69360f319a26c6a')

prepare() {
   cd "$srcdir"/$pkgname-$pkgver
   # adding various patches
   patch -Np1 -i ../hpoj-gcc4.patch
   patch -Np1 -i ../hpoj-kernel26.patch
   patch -Np1 -i ../hpoj-pack.patch
   patch -Np1 -i ../hpoj_gcc43.diff
   patch -Np1 -i ../hpoj0.91-snmp5.5.patch
}

build() {
   cd "$srcdir"/$pkgname-$pkgver
#   ./configure --prefix=/usr
   ./configure --prefix=/usr --without-qt
   make
}

package() {
   cd "$srcdir"/$pkgname-$pkgver
   make prefix="$pkgdir"/usr/ sbindir="$pkgdir"/usr/bin user_install
   mkdir -p "$pkgdir"/etc/rc.d
   mkdir -p "$pkgdir"/usr/lib/sane
   mkdir -p "$pkgdir"/usr/lib/cups/backend
   install -m 644 lib/sane/libsane-hpoj.so.1.0 "$pkgdir"/usr/lib/sane
   install -D -m644 LICENSE $pkgdir/usr/share/licenses/$pkgname/LICENSE
   install -D -m644 LICENSE.OpenSSL $pkgdir/usr/share/licenses/$pkgname/LICENSE.OpenSSL
   cd "$pkgdir"/usr/lib/sane  
   ln -s libsane-hpoj.so.1.0 libsane-hpoj.so
   ln -s libsane-hpoj.so.1.0 libsane-hpoj.so.1
   ln -s /usr/bin/ptal-init "$pkgdir"/etc/rc.d
   ln -s /usr/bin/ptal-cups "$pkgdir"/usr/lib/cups/backend/ptal
}
