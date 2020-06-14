# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=vlfeat
pkgname=(vlfeat octave-vlfeat)
pkgver=0.9.21
pkgrel=4
pkgdesc='An open library of computer vision algorithms'
arch=('x86_64')
url='https://www.vlfeat.org/'
license=('BSD')
depends=(
  openmp
)
makedepends=(
  clang
  octave
  patchelf
)
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/vlfeat/vlfeat/archive/v${pkgver}.tar.gz")
sha512sums=('ba7f83392d778a4a8c121aed10ae98693d8d61ae127e627322324c245cd1984ab8c0c3e3afe743075e7c022b3efb78e7dfc653bc488c8f19c93b3aa0f87e803e')

prepare() {
  # fix https://github.com/vlfeat/vlfeat/issues/168
  sed -i "s,if(! (max_value >= 65536)),if(max_value >= 65536)," "${srcdir}/${pkgname}-${pkgver}/vl/pgm.c"
  # fix octave building, see https://github.com/vlfeat/vlfeat/issues/188
  mkdir -p "${srcdir}/${pkgname}-${pkgver}/toolbox/mex/octave/mexa64"
  sed -i '32,35d' "${srcdir}/${pkgname}-${pkgver}/toolbox/mexutils.h"
}

build() {
  cd "${srcdir}/${_pkgname}-${pkgver}"
  make CC=clang CXX=clang++ DISABLE_OPENMP=no MKOCTFILE=mkoctfile
}

package_vlfeat() {
  # delete unneeded files and install binary & libs to correct location
  find "${srcdir}/${_pkgname}-${pkgver}/bin" -type f -perm 0755 -name "test_*" -delete
  install -Dm755 "${srcdir}/${_pkgname}-${pkgver}/bin/glnxa64/libvl.so" -t "${pkgdir}/usr/lib"
  install -Dm755 "${srcdir}/${_pkgname}-${pkgver}/bin/glnxa64/aib" -t "${pkgdir}/usr/bin"
  install -Dm755 "${srcdir}/${_pkgname}-${pkgver}/bin/glnxa64/mser" -t "${pkgdir}/usr/bin"
  install -Dm755 "${srcdir}/${_pkgname}-${pkgver}/bin/glnxa64/sift" -t "${pkgdir}/usr/bin"
  # patch rpath
  find "${pkgdir}/usr" -type f -perm 0755 -exec patchelf --remove-rpath {} \;
  # install headers
  find "${srcdir}/${_pkgname}-${pkgver}/vl" -type f -name "*.h" -exec install -Dm644 {} -t "${pkgdir}/usr/include/vl" \;
  # install manpages
  for manfile in mser.1 sift.1 vlfeat.7; do
    gzip "${srcdir}/${_pkgname}-${pkgver}/src/${manfile}"
  done
  install -Dm644 "${srcdir}/${_pkgname}-${pkgver}/src/mser.1.gz" -t "${pkgdir}/usr/share/man/man1"
  install -Dm644 "${srcdir}/${_pkgname}-${pkgver}/src/sift.1.gz" -t "${pkgdir}/usr/share/man/man1"
  install -Dm644 "${srcdir}/${_pkgname}-${pkgver}/src/vlfeat.7.gz" -t "${pkgdir}/usr/share/man/man7"

  install -Dm644 "${srcdir}/${_pkgname}-${pkgver}/COPYING" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}

package_octave-vlfeat() {
  pkgdesc+=' (octave package)'
  depends+=(vlfeat octave)

  install -d "${pkgdir}/usr/share/octave/packages/${_pkgname}-${pkgver}"
  find "${srcdir}/${_pkgname}-${pkgver}/toolbox" -type f -perm 0755 -name "*.mex" -exec install -Dm755 {} -t "${pkgdir}/usr/lib/octave/packages/${_pkgname}-${pkgver}" \;
  cp -a "${srcdir}/${_pkgname}-${pkgver}/toolbox" "${pkgdir}/usr/share/octave/packages/${_pkgname}-${pkgver}"
  cp -a "${srcdir}/${_pkgname}-${pkgver}/data" "${pkgdir}/usr/share/octave/packages/${_pkgname}-${pkgver}"
  for mexfile in $(ls "${pkgdir}/usr/share/octave/packages/${_pkgname}-${pkgver}/toolbox/mex/octave/mexa64/"); do
    ln -sf "/usr/lib/octave/packages/${_pkgname}-${pkgver}/${mexfile}" "${pkgdir}/usr/share/octave/packages/${_pkgname}-${pkgver}/toolbox/mex/octave/mexa64/${mexfile}"
  done
  # patch rpath
  find "${pkgdir}/usr/lib" -type f -perm 0755 -exec patchelf --remove-rpath {} \;

  install -Dm644 "${srcdir}/${_pkgname}-${pkgver}/COPYING" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
