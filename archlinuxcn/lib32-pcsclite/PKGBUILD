# Maintainer: Chih-Hsuan Yen <yan12125@gmail.com>
# Forked from community/pcsclite. Original contribution block:
# Maintainer: Alad Wenter <alad@archlinux.org>
# Maintainer: Christian Hesse <mail@eworm.de>
# Contributor: Giovanni Scafora <giovanni@archlinux.org>
# Contributor: Daniel Plaza <daniel.plaza.espi@gmail.com>

_pkgname=pcsclite
pkgname=lib32-$_pkgname
pkgver=1.9.0
pkgrel=1
pkgdesc="PC/SC Architecture smartcard middleware library (for proprietary 32-bit drivers)"
arch=('x86_64')
url='https://pcsclite.apdu.fr/'
license=('BSD')
depends=('lib32-systemd' $_pkgname)
makedepends=('pkg-config' 'lib32-gcc-libs')
options=('!docs')
validpgpkeys=('F5E11B9FFE911146F41D953D78A1B4DFE8F9C57E') # Ludovic Rousseau <rousseau@debian.org>
source=("https://pcsclite.apdu.fr/files/pcsc-lite-${pkgver}.tar.bz2"{,.asc})
sha256sums=('0148d403137124552c5d0f10f8cdab2cbb8dfc7c6ce75e018faf667be34f2ef9'
            'SKIP')

prepare() {
  cd "pcsc-lite-$pkgver"
  # Seems pcscd-32 needs exclusive access to devices
  sed -i -e 's#pcscd#pcscd-32#' -e '/^Requires=/a Conflicts=pcscd.service' etc/pcscd.service.in
}

build() {
  export CFLAGS+=" -m32"
  export CXXFLAGS+=" -m32"
  export LDFLAGS+=" -m32"
  export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"

  cd "pcsc-lite-$pkgver"

  ./configure \
    --prefix=/usr \
    --libdir=/usr/lib32 \
    --sbindir=/usr/bin \
    --program-suffix="-32" \
    --sysconfdir=/etc \
    --enable-filter \
    --enable-ipcdir=/run/pcscd \
    --enable-libudev \
    --enable-usbdropdir=/usr/lib32/pcsc/drivers \
    --with-systemdsystemunitdir=/usr/lib/systemd/system

  make
}

package() {
  cd "pcsc-lite-$pkgver"
  make DESTDIR="$pkgdir" install

  install -D -m644 "$srcdir/pcsc-lite-$pkgver/COPYING" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
  install -d "$pkgdir/usr/lib32/pcsc/drivers"

  rm -rv "$pkgdir"/usr/include
  mv "$pkgdir"/usr/lib/systemd/system/pcscd{,-32}.service
  mv "$pkgdir"/usr/lib/systemd/system/pcscd{,-32}.socket
}
