# Maintainer: tytan652 <tytan652 at tytanium dot xyz>

pkgname=cef-minimal-obs-bin
_cefver="103.0.0-5060-shared-textures_143.2591"
_version=${_cefver//-/_}
_commit="4204d54"
_cefbranch="5060"
_chromiumver="103.0.${_cefbranch}.134"
_rebuild="1" # The tarball sometime can get rebuild by OBS Project
pkgver="${_version}+g${_commit}+chromium_${_chromiumver}_${_rebuild}"
pkgrel=3
pkgdesc="Chromium Embedded Framework minimal release needed by OBS Studio release in /opt/cef-obs"
arch=("x86_64")
url="https://github.com/obsproject/cef/tree/5060-shared-textures"
license=("BSD")
depends=("nss" "alsa-lib" "pango" "libxrandr" "libxcomposite"
         "at-spi2-core" "libxkbcommon" "libcups" "mesa")
makedepends=("cmake")
provides=("cef-minimal-obs=$pkgver")
conflicts=("cef-minimal-obs")
# Prevent people from using link time optimisation for this package because it make OBS unable to be built against it
options=('!lto' '!strip' 'debug')
source_x86_64=("https://cdn-fastly.obsproject.com/downloads/cef_binary_${_cefbranch}_linux64.tar.bz2")
sha256sums_x86_64=("ac4e2a8ebf20700e4e36353e314f876623633dd5b474778a2548bb66bdbea11d")

# Kept for future-proofing, OBS now provide a custom CEF with some additions only for x86_64
if [[ $CARCH == 'x86_64' ]]; then
  _arch=64
  _parch=x86_64
elif [[ $CARCH == 'i686' ]]; then
  _arch=32
  _parch=x86
elif [[ $CARCH == 'aarch64' ]]; then
  _arch=arm64
  _parch=arm64
fi

prepare() {
  cd "$srcdir"/cef_binary_${_cefbranch}_linux${_arch}

  # Fix permissions
  chmod 755 Release
  chmod 755 Resources
  chmod 755 Resources/locales
  chmod 755 include
  chmod 755 include/base
  chmod 755 include/base/internal
  chmod 755 include/capi
  chmod 755 include/capi/test
  chmod 755 include/capi/views
  chmod 755 include/internal
  chmod 755 include/test
  chmod 755 include/views
  chmod 755 include/wrapper

  # Remove pre-built wrapper
  rm -rf build
}

build() {
  cd "$srcdir"/cef_binary_${_cefbranch}_linux${_arch}

  #The arm64 CEF set the wrong arch for the project
  cmake \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DPROJECT_ARCH=$_parch .

  make libcef_dll_wrapper

  # Remove unneeded generated files
  rm -f CMakeCache.txt Makefile cmake_install.cmake
  rm -rf CMakeFiles
    
  cd libcef_dll_wrapper
  rm -f Makefile cmake_install.cmake
  rm -rf CMakeFiles
}

package() {
    mkdir -p "$pkgdir"/opt/cef-obs/
    cp -a "$srcdir"/cef_binary_${_cefbranch}_linux${_arch}/* "$pkgdir"/opt/cef-obs
    rm -f "$pkgdir"/opt/cef-obs/CMakeLists.txt "$pkgdir"/opt/cef-obs/LICENSE.txt "$pkgdir"/opt/cef-obs/README.txt
    rm -rf "$pkgdir"/opt/cef-obs/cmake
    install -Dm644 "$srcdir"/cef_binary_${_cefbranch}_linux${_arch}/LICENSE.txt "$pkgdir"/usr/share/licenses/${pkgname}/LICENSE
}
