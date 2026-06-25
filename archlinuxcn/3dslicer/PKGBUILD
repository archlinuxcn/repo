# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=3dslicer
pkgname=3dslicer
pkgver=5.12.0
pkgrel=1
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
  teem
  util-linux-libs
  xz
  zlib
)
makedepends=(
  clang
  cmake
  gendesk
  git
  ninja
  qt5-script
  qt5-tools
  subversion
)
options=(!emptydirs !strip)
source=("${_pkgname}::git+https://github.com/Slicer/Slicer.git#tag=v${pkgver}"
        "${_pkgname}.svg::https://www.slicer.org/assets/img/3D-Slicer-Mark.svg"
        "slicer-vtk-regex-version-script-name.patch"
)
sha512sums=('e23d2b699fab1c4b919fcd3b1f8c8c2bc082834ee07542dddc2491f7433752e4687f0713553bfb6a052e1ed0d4ea8dee3dbf55ca56df22bf2eccea299b02d248'
            '3422d244f819a7ec4c475d3d8a90c79fcb73738920c0830b100c6342ca24d5be607ba60ee3d91892402036a0adf31d5ab7c8fc83f451121a7b537f7de5306014'
            '3ac8a9e98953ddbffa28dcac5f67156670e24a190433e580e00691856f805602a995104c0e6bdf388289b9a2d0ba6e6a19b4bbea89da71a19d080e8dd7981307')

prepare() {
  echo "Creating desktop file"
  gendesk -f -n --pkgname ${_pkgname} \
    --categories "Science;MedicalSoftware;Education;MedicalSoftware" \
    --exec "Slicer" \
    --icon "${_pkgname}" \
    --pkgdesc "${pkgdesc}" \
    --startupnotify \
    --custom="StartupWMClass=Slicer"
  git -C "${srcdir}/${_pkgname}" apply "${srcdir}/slicer-vtk-regex-version-script-name.patch"
}

build() {
  export CC=clang
  export CXX=clang++
  cmake \
    -B "${srcdir}/build" \
    -DBUILD_TESTING=OFF \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DSlicer_BUILD_DOCUMENTATION=OFF \
    -DSlicer_BUILD_I18N_SUPPORT=ON \
    -DSlicer_BUILD_PARAMETERSERIALIZER_SUPPORT=OFF \
    -DSlicer_REQUIRED_QT_VERSION=5 \
    -DSlicer_STORE_SETTINGS_IN_APPLICATION_HOME_DIR=OFF \
    -DSlicer_USE_GIT_PROTOCOL=OFF \
    -DSlicer_USE_PYTHONQT=ON \
    -DSlicer_USE_SimpleITK_SHARED=ON \
    -DSlicer_USE_SimpleITK=ON \
    -DSlicer_USE_SYSTEM_bzip2=ON \
    -DSlicer_USE_SYSTEM_CTK=OFF \
    -DSlicer_USE_SYSTEM_CTKAPPLAUNCHER=OFF \
    -DSlicer_USE_SYSTEM_CTKAppLauncherLib=OFF \
    -DSlicer_USE_SYSTEM_curl=ON \
    -DSlicer_USE_SYSTEM_DCMTK=ON \
    -DSlicer_USE_SYSTEM_ITK=OFF \
    -DSlicer_USE_SYSTEM_JsonCpp=OFF \
    -DSlicer_USE_SYSTEM_LibArchive=ON \
    -DSlicer_USE_SYSTEM_LibFFI=ON \
    -DSlicer_USE_SYSTEM_LZMA=ON \
    -DSlicer_USE_SYSTEM_OpenSSL=ON \
    -DSlicer_USE_SYSTEM_ParameterSerializer=OFF \
    -DSlicer_USE_SYSTEM_PCRE2=OFF \
    -DSlicer_USE_SYSTEM_python=OFF \
    -DSlicer_USE_SYSTEM_qRestAPI=OFF \
    -DSlicer_USE_SYSTEM_QT=ON \
    -DSlicer_USE_SYSTEM_RapidJSON=OFF \
    -DSlicer_USE_SYSTEM_SimpleITK=OFF \
    -DSlicer_USE_SYSTEM_SlicerExecutionModel=OFF \
    -DSlicer_USE_SYSTEM_sqlite=OFF \
    -DSlicer_USE_SYSTEM_Swig=OFF \
    -DSlicer_USE_SYSTEM_tbb=OFF \
    -DSlicer_USE_SYSTEM_teem=ON \
    -DSlicer_USE_SYSTEM_VTK=OFF \
    -DSlicer_USE_SYSTEM_zlib=ON \
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
