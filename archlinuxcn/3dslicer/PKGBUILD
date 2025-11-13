# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=3dslicer
pkgname=3dslicer
pkgver=5.10.0
pkgrel=4
pkgdesc='A free, open source and multi-platform software package widely used for medical, biomedical, and related imaging research'
arch=('x86_64')
url='https://www.slicer.org'
license=('BSD-3-Clause')
depends=(
  bzip2
  curl
  dcmtk
  fftw
  glibc
  hwloc
  icu76
  libarchive
  libffi
  libglvnd
  libice
  libpng
  libsm
  libx11
  libxcrypt
  libxcursor
  libxext
  libxfixes
  libxrender
  openssl
  qt5-base
  qt5-declarative
  qt5-location
  qt5-multimedia
  qt5-svg
  qt5-webchannel
  qt5-webengine
  qt5-x11extras
  qt5-xmlpatterns
  sqlite
  teem
  util-linux-libs
  xz
  zlib
)
makedepends=(
  cmake
  gcc14
  gendesk
  git
  ninja
  qt5-script
  qt5-tools
  rapidjson
  subversion
)
options=(!emptydirs !strip)
source=("${_pkgname}::git+https://github.com/Slicer/Slicer.git#tag=v${pkgver}"
        "${_pkgname}.svg::https://www.slicer.org/assets/img/3D-Slicer-Mark.svg"
        "https://github.com/Kitware/CMake/releases/download/v3.31.6/cmake-3.31.6-linux-x86_64.tar.gz"
        "0001-fix-build-with-system-rapidjson.patch"
        "0002-fix-build-with-system-sqlite3.patch"
)
sha512sums=('c3d91fdd02292c5231389baec26827a5e2503a2c5ba0bf226c7ef383e12fb11cf5b7925d9689a359428bc6a55431140b1b0aa43c1f0a8270256d12c1e47ad8ea'
            '3422d244f819a7ec4c475d3d8a90c79fcb73738920c0830b100c6342ca24d5be607ba60ee3d91892402036a0adf31d5ab7c8fc83f451121a7b537f7de5306014'
            '42395e20b10a8e9ef3e33014f9a4eed08d46ab952e02d2c1bbc8f6133eca0d7719fb75680f9bbff6552f20fcd1b73d86860f7f39388d631f98fb6f622b37cf04'
            'b1cc508098af1b5b5bbef187b85032fe921ed04e29653983282c00022db65d579fd68b5aebb089980faf598ef4af1a262971b354e7841219bd2b0d9cfde5c499'
            'b6cbe68b1639410322f669fb822e5a6c52daa7873bc1eb9b63610aa8f894b7c9c6892b1d01e47ac3492dc233c02e1f45fbcf148e91597a4d3c6c95b1bd619592')

prepare() {
  # fix building with system rapidjson
  patch -d ${_pkgname} -p1 -i ${srcdir}/0001-fix-build-with-system-rapidjson.patch
  # fix building with system sqlite3
  patch -d ${_pkgname} -p1 -i ${srcdir}/0002-fix-build-with-system-sqlite3.patch
  echo "Creating desktop file"
  gendesk -f -n --pkgname ${_pkgname} \
    --categories "Graphics;MedicalSoftware;Science;" \
    --exec "Slicer" \
    --icon "${_pkgname}" \
    --pkgdesc "${pkgdesc}" \
    --startupnotify \
    --custom="StartupWMClass=Slicer"
}

build() {
  export CC=gcc-14
  export CXX=g++-14
  cmake \
    -B "${srcdir}/build" \
    -DBUILD_TESTING=OFF \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DEXTERNAL_PROJECT_OPTIONAL_CMAKE_ARGS="-DSQLite3_INCLUDE_DIRS=/usr/include;-DSQLite3_LIBRARIES=/usr/lib/libsqlite3.so" \
    -DSlicer_BUILD_DOCUMENTATION=OFF \
    -DSlicer_BUILD_I18N_SUPPORT=ON \
    -DSlicer_STORE_SETTINGS_IN_APPLICATION_HOME_DIR=OFF \
    -DSlicer_USE_GIT_PROTOCOL=OFF \
    -DSlicer_USE_SYSTEM_CTK=OFF \
    -DSlicer_USE_SYSTEM_CTKAPPLAUNCHER=OFF \
    -DSlicer_USE_SYSTEM_CTKAppLauncherLib=OFF \
    -DSlicer_USE_SYSTEM_DCMTK=ON \
    -DSlicer_USE_SYSTEM_ITK=OFF \
    -DSlicer_USE_SYSTEM_JsonCpp=OFF \
    -DSlicer_USE_SYSTEM_LZMA=ON \
    -DSlicer_USE_SYSTEM_LibArchive=ON \
    -DSlicer_USE_SYSTEM_LibFFI=ON \
    -DSlicer_USE_SYSTEM_LZMA=ON \
    -DSlicer_USE_SYSTEM_OpenSSL=ON \
    -DSlicer_USE_SYSTEM_ParameterSerializer=OFF \
    -DSlicer_USE_SYSTEM_PCRE2=OFF \
    -DSlicer_USE_SYSTEM_QT=ON \
    -DSlicer_USE_SYSTEM_RapidJSON=ON \
    -DSlicer_USE_SYSTEM_SimpleITK=OFF \
    -DSlicer_USE_SYSTEM_SlicerExecutionModel=OFF \
    -DSlicer_USE_SYSTEM_Swig=OFF \
    -DSlicer_USE_SYSTEM_VTK=OFF \
    -DSlicer_USE_SYSTEM_bzip2=ON \
    -DSlicer_USE_SYSTEM_curl=ON \
    -DSlicer_USE_SYSTEM_qRestAPI=OFF \
    -DSlicer_USE_SYSTEM_sqlite=ON \
    -DSlicer_USE_SYSTEM_tbb=OFF \
    -DSlicer_USE_SYSTEM_teem=ON \
    -DSlicer_USE_SYSTEM_zlib=ON \
    -DSlicer_USE_SimpleITK=ON \
    -DSlicer_USE_SimpleITK_SHARED=ON \
    -GNinja \
    -S "${srcdir}/${_pkgname}" \
    -Wno-dev
  cmake --build "${srcdir}/build"
}

package() {
  cmake --build "${srcdir}/build/Slicer-build" --target package
  install -d "${pkgdir}/opt/${_pkgname}" "${pkgdir}/usr/bin"
  tar xvf "${srcdir}/build/Slicer-build/"*.tar.gz -C "${pkgdir}/opt/${_pkgname}" --strip-components 1
  ln -s /opt/${_pkgname}/Slicer "${pkgdir}/usr/bin/Slicer"
  install -Dm644 "${srcdir}/${_pkgname}.desktop" "${pkgdir}/usr/share/applications/${_pkgname}.desktop"
  install -Dm644 "${srcdir}/${_pkgname}.svg" "${pkgdir}/usr/share/pixmaps/${_pkgname}.svg"
}
# vim:set ts=2 sw=2 et:
