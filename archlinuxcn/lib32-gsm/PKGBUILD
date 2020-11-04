# Maintainer: Ondřej Hošek <ondra.hosek@gmail.com>
# Contributor: Jan de Groot <jgc@archlinux.org>
# Contributor: Maxime de Roucy <maxime.deroucy@gmail.com>
# Contributor: Darwin Bautista <djclue917@gmail.com>

pkgname=lib32-gsm
_pkgbase=gsm
pkgver=1.0.19
pkgrel=1
pkgdesc="Shared libraries for GSM 06.10 lossy speech compression"
arch=('x86_64')
url="http://www.quut.com/gsm/"
license=('custom')
depends=('glibc' 'gsm' 'lib32-glibc' 'lib32-gcc-libs')
source=("http://www.quut.com/${_pkgbase}/${_pkgbase}-${pkgver}.tar.gz"
        'gsm-shared.patch')
sha256sums=('4903652f68a8c04d0041f0d19b1eb713ddcd2aa011c5e595b3b8bca2755270f6'
            '1b9fabd7da83a688fc0e5ec712d53c428ff5575b1d5feac8437283ade1448c2b')

prepare() {
  cd "${srcdir}/${_pkgbase}-${pkgver%.*}-pl${pkgver##*.}/"

  patch -p0 -i "${srcdir}/gsm-shared.patch"
}

build() {
  cd "${srcdir}/${_pkgbase}-${pkgver%.*}-pl${pkgver##*.}/"

  # flags for shared lib
  CFLAGS="${CFLAGS} -fPIC"
  make \
    CC="gcc -m32" \
    CCFLAGS="-c ${CFLAGS} -fPIC"
}

package() {
  cd "${srcdir}/${_pkgbase}-${pkgver%.*}-pl${pkgver##*.}/"

  # Prepare directories
  install -m755 -d "${pkgdir}"/usr/{bin,lib,lib32,include/gsm,share/{licenses/${_pkgbase},man/man{1,3}}}

  make -j1 \
    CC="gcc -m32" \
    INSTALL_ROOT="${pkgdir}/usr" \
    GSM_INSTALL_LIB="${pkgdir}/usr/lib32" \
    GSM_INSTALL_INC="${pkgdir}/usr/include/gsm" \
    GSM_INSTALL_MAN="${pkgdir}/usr/share/man/man3" \
    TOAST_INSTALL_MAN="${pkgdir}/usr/share/man/man1" \
    install

  # clean directories provided by 64-bit package
  rm -Rf "${pkgdir}"/usr/{bin,include,lib,share}
}
