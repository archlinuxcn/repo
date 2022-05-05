# Maintainer:  Marcell Meszaros < marcell.meszaros AT runbox.eu >
# Contributor: aksr <aksr at t-com dot me>

pkgname=libeb
_pkgname=eb
pkgver=4.4.3
pkgrel=5
epoch=
pkgdesc='C library for accessing CD-ROM books. Supports EB, EBG, EBXA, EBXA-C, S-EBXA and EPWING formats.'
arch=('i686' 'x86_64')
url='http://www.mistys-internet.website/eb/index-en.html'
license=('BSD')
depends=('libnsl'
         'perl'
         'zlib')
provides=('libeb.so' 'eb-library')
conflicts=('eb-library')
replaces=('eb-library')  # Has been deleted from AUR and merged into this package
_patch1_name="${_pkgname}-fix_bmp_size_header.patch"
_patch1_source="https://github.com/eb4j/${_pkgname}/commit/8292c7814e2c65d0809bb8a401c00b593aefec43.patch"
source=("https://github.com/mistydemeo/eb/releases/download/v${pkgver}/${_pkgname}-${pkgver}.tar.bz2"
        "${_patch1_name}::${_patch1_source}")
sha256sums=('abe710a77c6fc3588232977bb2f30a2e69ddfbe9fa8d0b05b0d67d95e36f4b5f'
            '042c94bff12a653881bc182e88f5c27eef995ac401377d818a42216c8ea45c14')

prepare() {
  cd "${_pkgname}-${pkgver}"

  msg2 "[patch] Applying ${_patch1_name}..."
  patch --forward --strip=1 --input="../${_pkgname}-fix_bmp_size_header.patch"

  msg2 "[autoupdate] Refreshing configure.ac..."
  autoupdate --force

  msg2 '[autoreconf] Refreshing make configuration scripts...'
  autoreconf --verbose --force --install --symlink
}

build() {
  cd "${_pkgname}-${pkgver}"
  ./configure \
    --prefix='/usr' \
    --libexecdir="/usr/lib/${_pkgname}" \
    --sysconfdir='/etc' \
    --with-pkgdocdir="/usr/share/doc/${_pkgname}" \
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
