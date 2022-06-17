# Maintainer:  Marcell Meszaros < marcell.meszaros AT runbox.eu >
# Contributor: aksr <aksr at t-com dot me>

pkgname='libeb'
_pkgname='eb'
pkgver=4.4.3
pkgrel=10
_pkgrel_debian=14  # Version of Debian package patch
pkgdesc='C library for accessing CD-ROM books. Supports EB, EBG, EBXA, EBXA-C, S-EBXA and EPWING formats.'
arch=('i686' 'x86_64')
url='http://www.mistys-internet.website/eb/index-en.html'
license=('BSD')
depends=('perl' 'zlib')
provides=('libeb.so' 'eb-library')
conflicts=('eb-library')
replaces=('eb-library')  # Has been deleted from AUR and merged into this package
_patch1_name="${pkgname}-${pkgver}-${_pkgrel_debian}-010_debian.patch"
source=("${pkgname}-${pkgver}.tar.bz2::https://github.com/mistydemeo/${_pkgname}/releases/download/v${pkgver}/${_pkgname}-${pkgver}.tar.bz2"
        "${_patch1_name}::https://sources.debian.org/data/main/${_pkgname:0:1}/${_pkgname}/${pkgver}-${_pkgrel_debian}/debian/patches/010_debian.patch")
sha256sums=('abe710a77c6fc3588232977bb2f30a2e69ddfbe9fa8d0b05b0d67d95e36f4b5f'
            'dc98114f7bc7e7fc0da2fac5c741f91fb2a3079b0e096fbdf955755fc61c0f19')

prepare() {
  cd "${_pkgname}-${pkgver}"

  msg2 "[patch] Applying ${_patch1_name}..."
  patch --forward --strip=1 --input="../${_patch1_name}"

  msg2 "Removing link configuration for unused libraries"
  sed -e 's/-liconv//g' \
      -i 'm4/gettext.m4' \
      -i 'configure'
  sed -e 's/-lnsl//g' \
      -e 's/-lresolv//g' \
      -i 'configure'
  sed -e '/AC_CHECK_LIB(nsl/c/' \
      -e '/AC_CHECK_LIB(resolv/c/' \
      -i 'configure.ac'

  msg2 "[autoupdate] Refreshing configure.ac..."
  autoupdate --force

  msg2 '[autoreconf] Refreshing make configuration scripts...'
  autoreconf --verbose --force --install --symlink
}

build() {
  cd "${_pkgname}-${pkgver}"
  ./configure \
    --prefix='/usr' \
    --libexecdir="/usr/lib/${pkgname}" \
    --localstatedir="/var/lib/${pkgname}" \
    --sysconfdir='/etc' \
    --with-pkgdocdir="/usr/share/doc/html/${pkgname}" \
    --disable-silent-rules \
    --disable-static
  make
}

check() {
  cd "${_pkgname}-${pkgver}"
  make -k check
}

package() {
  cd "${_pkgname}-${pkgver}"
  make DESTDIR="$pkgdir" install
  install -D -m644 'COPYING' "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
