# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=vlfeat
pkgname=(vlfeat octave-vlfeat)
pkgver=0.9.21
pkgrel=9
pkgdesc='An open library of computer vision algorithms'
arch=('x86_64')
url='https://www.vlfeat.org/'
license=('BSD')
depends=(
  gcc-libs
)
makedepends=(
  git
  octave
  patchelf
)
source=("${_pkgname}::git+https://github.com/vlfeat/vlfeat.git"
    "0001-fix-openmp-building-with-gcc.patch::https://github.com/vlfeat/vlfeat/pull/200.patch"
    "0002-fix-pgm-max-value.patch::https://github.com/vlfeat/vlfeat/pull/170.patch"
    "0003-fix-typo-in-makefile.patch::https://github.com/vlfeat/vlfeat/pull/191.patch")
sha512sums=('SKIP'
            '181814a521b28e3c6fcdcff354f66f32f597db24a738e6db3bbb6418f62d4ab80a13b7b99707851f4e33d887cf906ce823f707d9cee20e2a34e4db9896a9b880'
            'd6c11b979785b1ed26655fbfc20ecfc0cce249c03fe54168a6580503b54e325a85c3e841a0e230a57c9fb21f73884d38a22020bd999b1a68841e09a8cd8c506e'
            '420c032aab1b6f32f6aabf319ad27bd66749a587deb36f7e60d3efa1512f6c3c56b680ffa5b510cb40c9bf895b1fd408599eda5ed23cdaec7626640bd69085f3')

prepare() {
  # fix building with openmp using gcc > 9.0
  cd ${_pkgname}
  patch -p1 -i "${srcdir}/0001-fix-openmp-building-with-gcc.patch"
  # fix https://github.com/vlfeat/vlfeat/issues/168
  patch -p1 -i "${srcdir}/0002-fix-pgm-max-value.patch"
  # fix Makefile typo
  patch -p1 -i "${srcdir}/0003-fix-typo-in-makefile.patch"
  # fix octave building, see https://github.com/vlfeat/vlfeat/issues/188
  mkdir -p "${srcdir}/${_pkgname}/toolbox/mex/octave/mexa64"
  sed -i '32,35d' "${srcdir}/${_pkgname}/toolbox/mexutils.h"
}

build() {
  cd "${srcdir}/${_pkgname}"
  make MKOCTFILE=$(which mkoctfile)
}

package_vlfeat() {
  # delete unneeded files and install binary & libs to correct location
  find "${srcdir}/${_pkgname}/bin" -type f -perm 0755 -name "test_*" -delete
  install -Dm755 "${srcdir}/${_pkgname}/bin/glnxa64/libvl.so" -t "${pkgdir}/usr/lib"
  install -Dm755 "${srcdir}/${_pkgname}/bin/glnxa64/aib" -t "${pkgdir}/usr/bin"
  install -Dm755 "${srcdir}/${_pkgname}/bin/glnxa64/mser" -t "${pkgdir}/usr/bin"
  install -Dm755 "${srcdir}/${_pkgname}/bin/glnxa64/sift" -t "${pkgdir}/usr/bin"
  # patch rpath
  find "${pkgdir}/usr" -type f -perm 0755 -exec patchelf --remove-rpath {} \;
  # install headers
  find "${srcdir}/${_pkgname}/vl" -type f -name "*.h" -exec install -Dm644 {} -t "${pkgdir}/usr/include/vl" \;
  # install manpages
  for manfile in mser.1 sift.1 vlfeat.7; do
    gzip "${srcdir}/${_pkgname}/src/${manfile}"
  done
  install -Dm644 "${srcdir}/${_pkgname}/src/mser.1.gz" -t "${pkgdir}/usr/share/man/man1"
  install -Dm644 "${srcdir}/${_pkgname}/src/sift.1.gz" -t "${pkgdir}/usr/share/man/man1"
  install -Dm644 "${srcdir}/${_pkgname}/src/vlfeat.7.gz" -t "${pkgdir}/usr/share/man/man7"

  install -Dm644 "${srcdir}/${_pkgname}/COPYING" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}

package_octave-vlfeat() {
  pkgdesc+=' (octave package)'
  depends+=(vlfeat octave)

  install -d "${pkgdir}/usr/share/octave/packages/${_pkgname}-${pkgver}"
  find "${srcdir}/${_pkgname}/toolbox" -type f -perm 0755 -name "*.mex" -exec install -Dm755 {} -t "${pkgdir}/usr/lib/octave/packages/${_pkgname}-${pkgver}" \;
  cp -a "${srcdir}/${_pkgname}/toolbox" "${pkgdir}/usr/share/octave/packages/${_pkgname}-${pkgver}"
  cp -a "${srcdir}/${_pkgname}/data" "${pkgdir}/usr/share/octave/packages/${_pkgname}-${pkgver}"
  rm -vf "${pkgdir}/usr/share/octave/packages/${_pkgname}-${pkgver}/toolbox/mex/octave/mexa64/libvl.so"
  for mexfile in $(ls "${pkgdir}/usr/share/octave/packages/${_pkgname}-${pkgver}/toolbox/mex/octave/mexa64/"); do
    ln -sf "/usr/lib/octave/packages/${_pkgname}-${pkgver}/${mexfile}" "${pkgdir}/usr/share/octave/packages/${_pkgname}-${pkgver}/toolbox/mex/octave/mexa64/${mexfile}"
  done
  # patch rpath
  find "${pkgdir}/usr/lib" -type f -perm 0755 -exec patchelf --remove-rpath {} \;

  install -Dm644 "${srcdir}/${_pkgname}/COPYING" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
