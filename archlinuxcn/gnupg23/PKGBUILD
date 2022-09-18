# Maintainer: Jerzy Kolosowski <jerzy@kolosowscy.pl>
# Merged with official ABS gnupg PKGBUILD by João, 2021/07/23 (all respective contributors apply herein)
# Maintainer: João Figueiredo & chaotic-aur <islandc0der@chaotic.cx>
# Contributor: Stephanie Wilde-Hobbs <git@stephanie.is>
# Contributor: Levente Polyak <anthraxx[at]archlinux[dot]org>
# Contributor: Lukas Fleischer <lfleischer@archlinux.org>
# Contributor: Lex Black <autumn-wind at web dot de>
# Contributor: alphazo@gmail.com
# Contributor: Gaetan Bisson <bisson@archlinux.org>
# Contributor: Tobias Powalowski <tpowa@archlinux.org>
# Contributor: Andreas Radke <andyrtr@archlinux.org>
# Contributor: Judd Vinet <jvinet@zeroflux.org>
# Contributor: @holos

pkgname=gnupg23
pkgver=2.3.7
pkgrel=1
pkgdesc='Complete and free implementation of the OpenPGP standard'
url='https://www.gnupg.org/'
license=(GPL)
arch=($CARCH)
# checkdepends=(openssh fig2dev)
makedepends=(git libldap libusb-compat pcsclite fig2dev)
conflicts=(${pkgname%23})
provides=(${pkgname%23}=${pkgver})
depends=(npth libgpg-error libgcrypt libksba libassuan pinentry libbz2.so readline libreadline.so gnutls sqlite zlib)
optdepends=('libldap: gpg2keys_ldap'
            'libusb-compat: scdaemon'
            'pcsclite: scdaemon')
validpgpkeys=(
  '5B80C5754298F0CB55D8ED6ABCEF7E294B092E28' # Andre Heinecke (Release Signing Key)
  '6DAA6E64A76D2840571B4902528897B826403ADA' # Werner Koch (dist signing 2020)
  'AC8E115BF73E2D8D47FA9908E98E9B2D19C6C8BD' # Niibe Yutaka (GnuPG Release Key)
  '02F38DFF731FF97CB039A1DA549E695E905BA208' # GnuPG.com (Release Signing Key 2021)
)
source=("https://gnupg.org/ftp/gcrypt/${pkgname%23}/${pkgname%23}-${pkgver}.tar.bz2"{,.sig}
	"drop-import-clean.patch"
	"avoid-beta-warning.patch"
        "yubikey.patch")
sha256sums=('ee163a5fb9ec99ffc1b18e65faef8d086800c5713d15a672ab57d3799da83669'
            'SKIP'
            '2d573d1a5a0d0272b0be0d70e6dabf2d8c7897e873ace4ce7fffd6e96599a30a'
            '22fdf9490fad477f225e731c417867d9e7571ac654944e8be63a1fbaccd5c62d'
            'c9450b81c9108ca41b227eae86c957158419027b21f716819956c2a3184fe864')
install=gnupg23.install

prepare() {
  cd "${srcdir}/${pkgname%23}-${pkgver}"
  patch -p1 -i ../drop-import-clean.patch
  patch -p1 -i ../avoid-beta-warning.patch
  patch -p1 -i ../yubikey.patch

  # improve reproducibility
  rm doc/gnupg.info*

  ./autogen.sh
}

build() {
  cd "${srcdir}/${pkgname%23}-${pkgver}"
  ./configure \
    --prefix=/usr \
    --sysconfdir=/etc \
    --sbindir=/usr/bin \
    --libexecdir=/usr/lib/gnupg \
    --enable-maintainer-mode \

  make
}

check() {
  cd "${srcdir}/${pkgname%23}-${pkgver}"
  make check
}

package() {
  cd "${srcdir}/${pkgname%23}-${pkgver}"
  make DESTDIR="${pkgdir}" install
  ln -s gpg "${pkgdir}"/usr/bin/gpg2
  ln -s gpgv "${pkgdir}"/usr/bin/gpgv2

  install -Dm 644 doc/examples/systemd-user/*.* -t "${pkgdir}/usr/lib/systemd/user"
  install -Dm 644 COPYING.{CC0,other} -t "${pkgdir}/usr/share/licenses/$pkgname/"
}
