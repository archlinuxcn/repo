# Maintainer: Morten Linderud <foxboron@archlinux.org>
# Contributor: Giovanni Scafora <giovanni@archlinux.org>
# Contributor: dorphell <dorphell@archlinux.org>
# Contributor: Tom Newsom <Jeepster@gmx.co.uk>
# Contributor: Denis Tikhomirov <dvtikhomirov@gmail.com>

pkgname=minicom-line_timestamp
_pkgname=minicom
pkgver=2.7.1
pkgrel=1
pkgdesc='A serial communication program (with line_timestamp patch)'
arch=('x86_64')
url='https://salsa.debian.org/minicom-team/minicom'
license=('GPL')
depends=('bash')
optdepends=('lrzsz: for xmodem, ymodem and zmodem file transfer protocols')
provides=("minicom=$pkgver")
conflicts=('minicom')
backup=('etc/minirc.dfl')
source=("${_pkgname}-${pkgver}.tar.gz::http://ftp.debian.org/debian/pool/main/m/minicom/minicom_${pkgver}.orig.tar.gz"
        "minicom-2.7.1-gcc-10.patch"
        "minicom-line_timestamp-2.7.patch::https://salsa.debian.org/yan12125-guest/minicom/-/commit/7907402f7a9aa71c79a51063f1704927d427432b.patch")
sha256sums=('532f836b7a677eb0cb1dca8d70302b73729c3d30df26d58368d712e5cca041f1'
            'b7d8eab87a919feb6d519c06c70145624a6560208e8c79da3a2ed2c2e086def3'
            'e18bccbeb9e9c0bf717793cbb1e474cf3b9531ed89343d32efe077ff8ea38d05')

prepare(){
  cd "${_pkgname}-${pkgver}"
  patch -Np1 < "$srcdir/minicom-2.7.1-gcc-10.patch"
  patch -Np1 < "$srcdir/minicom-line_timestamp-2.7.patch"
}

build() {
  cd "${_pkgname}-${pkgver}"

  ./configure --prefix=/usr \
              --sysconfdir=/etc
  make
}

package() {
  cd "${_pkgname}-${pkgver}"

  make DESTDIR="${pkgdir}/" install
  install -Dm644 doc/minirc.dfl ${pkgdir}/etc/minirc.dfl
}
