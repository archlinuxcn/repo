# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=3dslicer
pkgname=3dslicer-git
pkgver=5.10.0.r86.f267a5edda
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
  qt6-base
  qt6-declarative
  qt6-location
  qt6-multimedia
  qt6-svg
  qt6-webchannel
  qt6-webengine
  qt6-scxml
  qt6-5compat
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
  qt6-tools
  subversion
)
options=(!emptydirs !strip)
provides=(3dslicer=${pkgver})
conflicts=(3dslicer)
source=("${_pkgname}::git+https://github.com/Slicer/Slicer.git"
        "${_pkgname}.svg::https://www.slicer.org/assets/img/3D-Slicer-Mark.svg"
        "0001-fix-building-with-ctk.patch"
        "0001-fix-building-ctk-with-pythonqt.patch"
        "0002-fix-undefined-reference-error-when-building-with-qt6.patch"
)
sha512sums=('SKIP'
            '3422d244f819a7ec4c475d3d8a90c79fcb73738920c0830b100c6342ca24d5be607ba60ee3d91892402036a0adf31d5ab7c8fc83f451121a7b537f7de5306014'
            'a1ee4b34ec9bb3de794b5ef6a5b99984957e464e575b6c264b0ab56333fec86525f5d14ea50b2e13faeac72c776d053f4955c62badf1270ab3defa021a3ebc90'
            '18b0625cff59cb057688fd06d9bad6e0b4be62c4d5848b94e92da11c425c9091105c2b7846f237d5ee0bdad2b48259527f893e6448c6960c4cce7f41761dcd77'
            'f947a910297b1434f2cd15859996039587ebcd2d1bb4bd8628421dd68233bfa6cc26f9c5e614b2b069a9744afdf0c3a5cfe6695d48b32cf20d38a48752e05cc3')

pkgver() {
  cd "${srcdir}/${_pkgname}"
  _max_tag=$(git tag --sort=-v:refname | head -n1)
  _commit_count=$(git rev-list --count "${_max_tag}"..HEAD)
  _commit_hash=$(git rev-parse --short HEAD)
  _max_tag=$(echo "$_max_tag" | sed 's/^v//')
  _full_version="${_max_tag}.r${_commit_count}.${_commit_hash}"
  printf "%s" "${_full_version}"
}

prepare() {
  patch -p1 -d ${srcdir}/${_pkgname} -i ${srcdir}/0001-fix-building-with-ctk.patch
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
    -DSlicer_BUILD_DOCUMENTATION=OFF \
    -DSlicer_BUILD_I18N_SUPPORT=ON \
    -DSlicer_BUILD_PARAMETERSERIALIZER_SUPPORT=OFF \
    -DSlicer_REQUIRED_QT_VERSION=6 \
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
  VERBOSE=1 cmake --build "${srcdir}/build"
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
