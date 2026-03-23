# Maintainer: Fabio 'Lolix' Loli <fabio.loli@disroot.org> -> https://github.com/FabioLolix
# Maintainer:  Chris Severance aur.severach aATt spamgourmet dott com
# Contributor: Pellegrino Prevete <pellegrinoprevete at gmail dot com>
# Contributor: elliotwutingfeng
# Contributor: Frederik Schwan <freswa at archlinux dot org>
# Contributor: Jonathon Fernyhough <jonathon+m2x+dev>
# Contributor: Giancarlo Razzolini <grazzolini@archlinux.org>
# Contributor: Bartłomiej Piotrowski <bpiotrowski@archlinux.org>
# Contributor: Allan McRae <allan@archlinux.org>
# Contributor: Daniel Kozak <kozzi11@gmail.com>

set -u
pkgbase='gcc11'
pkgname=("${pkgbase}" "${pkgbase}-libs" "${pkgbase}-fortran")
pkgver='11.5.0'
_majorver="${pkgver%%.*}"
_islver='0.24'
pkgrel='1'
pkgdesc="The GNU Compiler Collection (${_majorver}.x.x)"
arch=('x86_64')
url='https://gcc.gnu.org'
license=('GPL' 'LGPL' 'FDL' 'custom')
makedepends=('binutils' 'doxygen' 'libmpc' 'python')
#makedepends+=('libisl.so' 'gcc13')
#export CC='/usr/bin/gcc-13' CXX='/usr/bin/g++-13'
checkdepends=('dejagnu' 'inetutils')
options=('!emptydirs' '!strip' '!buildflags')
options+=('!lto')
source=(
  "https://ftp.gnu.org/gnu/gcc/gcc-${pkgver}/gcc-${pkgver}.tar.xz"{,.sig}
  "https://gcc.gnu.org/pub/gcc/infrastructure/isl-${_islver}.tar.bz2"
  'c89'
  'c99'
  '78_all-libsanitizer-Fix-build-with-glibc-2.42.patch'
  '79_all-sanitizer_common-Remove-reference-to-obsolete-termio.patch'
)
validpgpkeys=(F3691687D867B81B51CE07D9BBE43771487328A9  # bpiotrowski@archlinux.org
              86CFFCA918CF3AF47147588051E8B148A9999C34  # evangelos@foutrelis.com
              13975A70E63C361C73AE69EF6EEB81F8981C74C7  # richard.guenther@gmail.com
              D3A93CAD751C2AF4F8C7AD516C35B99309B5FA62) # Jakub Jelinek <jakub@redhat.com>
md5sums=('03473f26c87e05e789a32208f1fe4491'
         'SKIP'
         'dd2f7b78e118c25bd96134a52aae7f4d'
         '3d333df77302ed89e06a4a8539943b7d'
         'da96f545b863e57c6ab2598c1ea9a740'
         '9be978cc7cb6388c6694f79703b73d29'
         '17a0188095828d0ebc49bb4c5d6afd8a')
b2sums=('f4a61faad32aac9e9cb553c1a1a011df0a057f6e2cac92a13cc7e285d08191dd4a117f41a8faac2359c0e2a16f954c7fef354dda9df8c63bff1c5cefda82602c'
        'SKIP'
        '88a178dad5fe9c33be5ec5fe4ac9abc0e075a86cff9184f75cedb7c47de67ce3be273bd0db72286ba0382f4016e9d74855ead798ad7bccb015b853931731828e'
        '2c64090b879d6faea7f20095eff1b9bd6a09fe3b15b3890783d3715171678ab62d32c91af683b878746fb14441dbe09768474417840f96a561443415f76afb63'
        '3cf318835b9833ac7c5d3a6026fff8b4f18b098e18c9649d00e32273688ff06ec3af41f0d0aee9d2261725e0ff08f47a224ccfe5ebb06646aaf318ff8ac9a0d1'
        'de7d446f88afe0a07e77717459c02a03fd66728788ba0473d687efb51904dfc63e525caeeff2cc79ce1e5187a3eda226936a2e50a2e1bf96bcb936534b2f9cc9'
        '9baecc980110ca4fb6fd8c087f6c3865dbfe334b0ae647bb002569653eb7f16ce90d3bfe45706165306c4e860518a21e2645d7e71be006a3931ab39e98efd91e')

if [ -n "${_snapshot:-}" ]; then
  _basedir="gcc-${_snapshot}"
else
  _basedir="gcc-${pkgver}"
fi

_fn_setlibdir() {
  _libdir="usr/lib/gcc/${CHOST}/${pkgver%%+*}"
}

prepare() {
  set -u
  cd "${_basedir}"

  # link isl for in-tree build
  ln -s "../isl-${_islver}" 'isl'

  # Do not run fixincludes
  sed -e 's@\./fixinc\.sh@-c true@' -i 'gcc/Makefile.in'

  # Arch Linux installs x86_64 libraries /lib
  case "${CARCH}" in
  'x86_64') sed -e '/m64=/ s/lib64/lib/' -i 'gcc/config/i386/t-linux64' ;;
  esac

  # hack! - some configure tests for header files using "$CPP $CPPFLAGS"
  sed -e '/ac_cpp=/s/$CPPFLAGS/$CPPFLAGS -O2/' -i 'gcc/configure'

  # Apply patches
  local _pt
  for _pt in "${source[@]%%::*}"; do
    _pt="${_pt##*/}"
    case "${_pt}" in
    *.patch)
      set +u; msg2 "*** Applying patch ${_pt}"; set -u
      patch --no-backup-if-mismatch -Np1 -i "${srcdir}/${_pt}"
      ;;
    esac
  done

  rm -rf 'gcc-build'
  mkdir 'gcc-build'

  set +u
}

build() {
  set -u
  cd "${_basedir}/gcc-build"

  if [ ! -s 'Makefile' ]; then
    # The following options are one per line, mostly sorted so they are easy to diff compare to other gcc packages.
    local _conf=(
      --build="${CHOST}"
      --host="${CHOST}"
      --target="${CHOST}"
      --disable-libssp
      --disable-libstdcxx-pch
      --disable-libunwind-exceptions
      --disable-multilib
      --disable-werror
      # --enable-bootstrap
      --enable-__cxa_atexit
      --enable-cet='auto'
      --enable-checking='release'
      --enable-clocale='gnu'
      --enable-default-pie
      --enable-default-ssp
      --enable-gnu-indirect-function
      --enable-gnu-unique-object
      --enable-install-libiberty
      --enable-languages='c,c++,fortran,lto'
      --enable-linker-build-id
      # --enable-link-serialization='1'
      --enable-lto
      --enable-plugin
      --enable-shared
      --enable-threads='posix'
      --enable-version-specific-runtime-libs
      --infodir='/usr/share/info'
      --libdir='/usr/lib'
      --libexecdir='/usr/lib'
      --mandir='/usr/share/man'
      --program-suffix="-${_majorver}"
      --with-bugurl="https://aur.archlinux.org/packages/${pkgname}/"
      # --with-build-config='bootstrap-lto'
      --with-isl
      --with-linker-hash-style='gnu'
      --with-pkgversion="Arch Linux ${pkgver}-${pkgrel}"
      --with-system-zlib
      --prefix='/usr'
    )

if ! :; then
    export CPPFLAGS=""
    export CFLAGS=""
    export CXXFLAGS=""
    export LDFLAGS=""

    # Credits @allanmcrae
    # https://github.com/allanmcrae/toolchain/blob/f18604d70c5933c31b51a320978711e4e6791cf1/gcc/PKGBUILD
    # TODO: properly deal with the build issues resulting from this
    #CFLAGS=${CFLAGS/-Werror=format-security/}
    #CXXFLAGS=${CXXFLAGS/-Werror=format-security/}

    local _cflags=(
      -I'/usr/include'
    )

    local _ldflags=(
      # /${_libdir}/libstdc++.so
    )

    # see https://bugs.archlinux.org/task/71777 for rationale re *FLAGS handling

    local _make_opts=(
      STAGE1_CFLAGS='-O2'
      BOOT_CFLAGS="${_cflags[*]}"
      BOOT_LDFLAGS="${_ldflags[*]}"
      LDFLAGS_FOR_TARGET="${_ldflags[*]}"
    )

    # CC="gcc-9" \
    # CXX="g++-9" \
    CPPFLAGS="${_cflags[*]}" \
    CFLAGS="${_cflags[*]}" \
    CXXFLAGS="${_cflags[*]}" \
    LDFLAGS="${_ldflags[*]}" \

fi
    ../configure "${_conf[@]}"

    #sed -e 's/^STAGE1_CXXFLAGS.*$/& -std=gnu++11/' -i 'Makefile'
  fi

if ! :; then
  # CC="gcc-9" \
  # CXX="g++-9" \
  CPPFLAGS="${_cflags[*]}" \
  CFLAGS="${_cflags[*]}" \
  CXXFLAGS="${_cflags[*]}" \
  LDFLAGS="${_ldflags[*]}" \

fi

  # Work-around `msgfmt: /build/gcc11/src/gcc-build/x86_64-pc-linux-gnu/libstdc++-v3/src/.libs/libstdc++.so.6: version `GLIBCXX_3.4.30' not found (required by /usr/lib/libicuuc.so.72)`
  # The trick is borrowed from https://aur.archlinux.org/packages/gcc49
  LD_PRELOAD='/usr/lib/libstdc++.so' \
  nice -n1 make -s

  set +u; msg 'Compile complete'; set -u

  # make documentation
  make -s -j1 -C "${CHOST}/libstdc++-v3/doc" 'doc-man-doxygen'
  set +u
}

check_disabled() {
  set -u
  cd "${_basedir}/gcc-build"

  # disable libphobos test to avoid segfaults and other unfunny ways to waste my time
  sed -e '/maybe-check-target-libphobos \\/d' -i 'Makefile'

  # do not abort on error as some are "expected"
  make -O -k check || :
  ../contrib/test_summary
  set +u
}

package_gcc11-libs() {
  set -u
  pkgdesc="Runtime libraries shipped by GCC (${_majorver}.x.x)"
  depends=('glibc>=2.27')
  options=('!emptydirs' '!strip')
  #provides=("libgfortran.so=${pkgver}" "libubsan.so=${pkgver}" "libasan.so=${pkgver}" "libtsan.so=${pkgver}" "liblsan.so=${pkgver}")

  cd "${_basedir}/gcc-build"
  make -j1 -s -C "${CHOST}/libgcc" DESTDIR="${pkgdir}" 'install-shared'
  local _libdir; _fn_setlibdir
  mv "${pkgdir}/${_libdir}/../lib"/* "${pkgdir}/${_libdir}"
  rmdir "${pkgdir}/${_libdir}/../lib"
  rm -f "${pkgdir}/${_libdir}/libgcc_eh.a"

  local _lib _libs=(
    libasan
    libatomic
    libgfortran
    libgomp
    libitm
    liblsan
    libquadmath
    libstdc++
    libtsan
    libubsan
  )
  for _lib in "${_libs[@]}"; do
    ln -s "/usr/lib/${_lib}.so" "${pkgdir}/${_libdir}/${_lib}.so"
  done

  make -j1 -s -C "${CHOST}/libstdc++-v3/po" DESTDIR="${pkgdir}" install

  # Install Runtime Library Exception
  install -Dpm644 '../COPYING.RUNTIME' \
    "${pkgdir}/usr/share/licenses/${pkgbase}-libs/RUNTIME.LIBRARY.EXCEPTION"

  # remove conflicting files
  rm -rf "${pkgdir}/usr/share/locale"
  set +u
}

package_gcc11() {
  set -u
  pkgdesc="The GNU Compiler Collection - C and C++ frontends (${_majorver}.x.x)"
  depends=("${pkgbase}-libs=${pkgver}-${pkgrel}" 'binutils>=2.28' 'libmpc' 'zstd')
  #depends+=('libisl.so')
  options=('!emptydirs' 'staticlibs')

  cd "${_basedir}/gcc-build"

  make -j1 -s -C 'gcc' DESTDIR="${pkgdir}" 'install-driver' 'install-cpp' 'install-gcc-ar' \
    'c++.install-common' 'install-headers' 'install-plugin' 'install-lto-wrapper'

  local _libdir; _fn_setlibdir
  install -m755 -t "${pkgdir}/${_libdir}/" gcc/{cc1,cc1plus,collect2,lto1,gcov{,-tool}}

  make -j1 -s -C "${CHOST}/libgcc" DESTDIR="${pkgdir}" install
  rm -rf "${pkgdir}/${_libdir}/../lib"

  make -j1 -s -C "${CHOST}/libstdc++-v3/src" DESTDIR="${pkgdir}" install
  make -j1 -s -C "${CHOST}/libstdc++-v3/include" DESTDIR="${pkgdir}" install
  make -j1 -s -C "${CHOST}/libstdc++-v3/libsupc++" DESTDIR="${pkgdir}" install
  make -j1 -s -C "${CHOST}/libstdc++-v3/python" DESTDIR="${pkgdir}" install
  rm -f "${pkgdir}/${_libdir}/"libstdc++.so*

  make -j1 -s DESTDIR="${pkgdir}" 'install-fixincludes'
  make -j1 -s -C 'gcc' DESTDIR="${pkgdir}" 'install-mkheaders'

  make -j1 -s -C 'lto-plugin' DESTDIR="${pkgdir}" install
  install -dm755 "${pkgdir}/${_libdir}/bfd-plugins/"
  ln -s "/${_libdir}/liblto_plugin.so" \
    "${pkgdir}/${_libdir}/bfd-plugins/"

  make -j1 -s -C "${CHOST}/libgomp" DESTDIR="${pkgdir}" install-nodist_{libsubinclude,toolexeclib}HEADERS
  make -j1 -s -C "${CHOST}/libitm" DESTDIR="${pkgdir}" 'install-nodist_toolexeclibHEADERS'
  make -j1 -s -C "${CHOST}/libquadmath" DESTDIR="${pkgdir}" 'install-nodist_libsubincludeHEADERS'
  make -j1 -s -C "${CHOST}/libsanitizer" DESTDIR="${pkgdir}" install-nodist_{saninclude,toolexeclib}HEADERS
  make -j1 -s -C "${CHOST}/libsanitizer/asan" DESTDIR="${pkgdir}" 'install-nodist_toolexeclibHEADERS'
  make -j1 -s -C "${CHOST}/libsanitizer/tsan" DESTDIR="${pkgdir}" 'install-nodist_toolexeclibHEADERS'
  make -j1 -s -C "${CHOST}/libsanitizer/lsan" DESTDIR="${pkgdir}" 'install-nodist_toolexeclibHEADERS'

  make -j1 -s -C 'libcpp' DESTDIR="${pkgdir}" install
  make -j1 -s -C 'gcc' DESTDIR="${pkgdir}" 'install-po'

  # many packages expect this symlink
  ln -s "gcc-${_majorver}" "${pkgdir}/usr/bin/cc-${_majorver}"

  # POSIX conformance launcher scripts for c89 and c99
  install -Dm755 "${srcdir}/c89" "${pkgdir}/usr/bin/c89-${_majorver}"
  install -Dm755 "${srcdir}/c99" "${pkgdir}/usr/bin/c99-${_majorver}"

  # byte-compile python libraries
  python -m 'compileall' "${pkgdir}/usr/share/gcc-${pkgver%%+*}/"
  python -O -m 'compileall' "${pkgdir}/usr/share/gcc-${pkgver%%+*}/"

  # Install Runtime Library Exception
  install -d "${pkgdir}/usr/share/licenses/${pkgname}/"
  ln -s "/usr/share/licenses/${pkgbase}-libs/RUNTIME.LIBRARY.EXCEPTION" \
    "${pkgdir}/usr/share/licenses/${pkgname}/"

  # Remove conflicting files
  rm -rf "${pkgdir}/usr/share/locale"
  set +u
}

package_gcc11-fortran() {
  set -u
  pkgdesc="Fortran front-end for GCC (${_majorver}.x.x)"
  depends=("${pkgbase}=${pkgver}-${pkgrel}")
  #depends+=('libisl.so')

  cd "${_basedir}/gcc-build"
  make -j1 -s -C "${CHOST}/libgfortran" DESTDIR="${pkgdir}" 'install-cafexeclibLTLIBRARIES' \
    install-{toolexeclibDATA,nodist_fincludeHEADERS,gfor_cHEADERS}
  make -j1 -s -C "${CHOST}/libgomp" DESTDIR="${pkgdir}" 'install-nodist_fincludeHEADERS'
  make -j1 -s -C 'gcc' DESTDIR="${pkgdir}" 'fortran.install-common'
  local _libdir; _fn_setlibdir
  install -Dm755 'gcc/f951' "${pkgdir}/${_libdir}/f951"

  ln -s "gfortran-${_majorver}" "${pkgdir}/usr/bin/f95-${_majorver}"

  # Install Runtime Library Exception
  install -d "${pkgdir}/usr/share/licenses/${pkgname}/"
  ln -s "/usr/share/licenses/${pkgbase}-libs/RUNTIME.LIBRARY.EXCEPTION" \
    "${pkgdir}/usr/share/licenses/${pkgname}/"
  set +u
}
set +u
