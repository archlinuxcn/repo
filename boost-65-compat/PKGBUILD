# Maintainer: Dmitry Kharitonov <darksab0r at gmail com>
# Contributor: Marcin Kornat <rarvolt+aur@gmail.com>
# Contributor:  Bartłomiej Piotrowski <bpiotrowski@archlinux.org>

pkgname=boost-65-compat
_pkgname=boost
pkgver=1.65.1
_boostver=${pkgver//./_}
pkgrel=2
pkgdesc="Free peer-reviewed portable C++ source libraries - compat version"
arch=('x86_64')
url='http://www.boost.org/'
license=('custom')
depends=('bzip2' 'zlib' 'icu>=55.1' 'openmpi')
makedepends=('python' 'python2' 'python-numpy' 'python2-numpy' )
source=(https://dl.bintray.com/boostorg/release/${pkgver}/source/${_pkgname}_${_boostver}.tar.bz2)
#source=(https://downloads.sourceforge.net/project/${_pkgname}/${_pkgname}/${pkgver}/${_pkgname}_${_boostver}.tar.bz2)
sha256sums=('9807a5d16566c57fd74fb522764e0b134a8bbe6b6e8967b83afefd30dcd3be81')

build() {
   export _stagedir="${srcdir}/stagedir"
   local JOBS="$(sed -e 's/.*\(-j *[0-9]\+\).*/\1/' <<< ${MAKEFLAGS})"

   cd ${_pkgname}_${_boostver}
   ./bootstrap.sh --with-toolset=gcc --with-icu --with-python=/usr/bin/python2

   _bindir="bin.linuxx86"
   [[ "${CARCH}" = "x86_64" ]] && _bindir="bin.linuxx86_64"
   install -Dm755 tools/build/src/engine/$_bindir/b2 "${_stagedir}"/bin/b2

   # Support for OpenMPI
   echo "using mpi ;" >> project-config.jam

   # boostbook is needed by quickbook
   install -dm755 "${_stagedir}"/share/boostbook
   cp -a tools/boostbook/{xsl,dtd} "${_stagedir}"/share/boostbook/

   # default "minimal" install: "release link=shared,static
   # runtime-link=shared threading=single,multi"
   # --layout=tagged will add the "-mt" suffix for multithreaded libraries
   # and installs includes in /usr/include/boost.
   # --layout=system no longer adds the -mt suffix for multi-threaded libs.
   # install to ${_stagedir} in preparation for split packaging
   "${_stagedir}"/bin/b2 \
      variant=release \
      debug-symbols=off \
      threading=multi \
      runtime-link=shared \
      link=shared,static \
      toolset=gcc \
      python=2.7 \
      cflags="${CPPFLAGS} ${CFLAGS} -fPIC -O3" \
      cxxflags="${CPPFLAGS} ${CXXFLAGS} -std=c++14 -fPIC -O3" \
      linkflags="${LDFLAGS}" \
      --layout=system \
      ${JOBS} \
      \
      --prefix="${_stagedir}" \
      install

   # because b2 in boost 1.62.0 doesn't seem to respect python parameter, we
   # need another run for liboost_python3.so
   sed -e '/using python/ s@;@: /usr/include/python${PYTHON_VERSION/3*/${PYTHON_VERSION}m} ;@' \
      -i bootstrap.sh

   ./bootstrap.sh --with-toolset=gcc --with-icu --with-python=/usr/bin/python3 \
      --with-libraries=python

   "${_stagedir}"/bin/b2 clean
   "${_stagedir}"/bin/b2 \
      variant=release \
      debug-symbols=off \
      threading=multi \
      runtime-link=shared \
      link=shared,static \
      toolset=gcc \
      python=3.6 \
      cflags="${CPPFLAGS} ${CFLAGS} -fPIC -O3" \
      cxxflags="${CPPFLAGS} ${CXXFLAGS} -std=c++14 -fPIC -O3" \
      linkflags="${LDFLAGS}" \
      --layout=system \
      ${JOBS} \
      \
      --prefix="${_stagedir}/python3" \
      --with-python \
      install
}

package() {
   # powerdns-recursor keeps being rebuild against outdated boost-libs
   provides=('libboost_context.so')

   install -dm755 "${pkgdir}"/usr
   cp -a "${_stagedir}"/lib "${pkgdir}"/usr
   cp -a "${_stagedir}"/python3/lib/libboost_* "${pkgdir}"/usr/lib
   rm "${pkgdir}"/usr/lib/*.a
   rm "${pkgdir}"/usr/lib/*.so

}

# build() {
#     export CPLUS_INCLUDE_PATH="$CPLUS_INCLUDE_PATH:/usr/include/python3.6m/"
#     cd "${srcdir}/boost_1_63_0"
#     ./bootstrap.sh
#     ./b2 variant=release link=shared runtime-link=shared stage
# }

# package() {
#     cd "${srcdir}/boost_1_63_0"
#     mkdir -p ${pkgdir}/usr/lib
#     ./b2 install --prefix=${pkgdir}/usr
#     for FILE in $(ls "${pkgdir}/usr/lib" | grep .so$); do
#         rm "${pkgdir}/usr/lib/${FILE}"
#     done
#     for FILE in $(ls "${pkgdir}/usr/lib" | grep .a$); do
#         rm "${pkgdir}/usr/lib/${FILE}"
#     done
#     rm -r "${pkgdir}/usr/include"
# }
