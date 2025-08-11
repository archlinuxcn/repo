# Maintainer:

## options
: ${_use_sodeps:=false}

: ${_use_cuda:=false} # nvenc
: ${_cuda_gcc_version:=$(LC_ALL=C pacman -Si cuda | grep -Pom1 '^Depends On\s*:.*\bgcc\K[0-9]+\b')}

: ${_commit=65f14e1003f831e776c170621bd06d8292f65155}

_pkgname="sunshine"
pkgname="$_pkgname"
pkgver=2025.628.4510
pkgrel=3
pkgdesc="A self-hosted GameStream host for Moonlight"
url="https://github.com/LizardByte/Sunshine"
license=('GPL-3.0-only')
arch=('x86_64' 'aarch64')

depends=(
  'gtk3'
  'icu'
  'libayatana-appindicator'
  'libcap'
  'libdrm'
  'libevdev'
  'libnotify'
  'libpulse'
  'libva'
  'miniupnpc'
  'numactl'
  'openssl'
  'opus'
  'wayland'
)
makedepends=(
  "gcc${_cuda_gcc_version:?}"
  'boost'
  'cmake'
  'git'
  'ninja'
  'npm'
)
optdepends=(
  'intel-media-driver: Intel GPU encoding support'
  'libva-mesa-driver: AMD GPU encoding support'
)

if pacman -Qi cuda &> /dev/null; then
  _use_cuda=true
fi

if [[ "${_use_cuda::1}" == "t" ]]; then
  makedepends+=('cuda')
  checkdepends+=('nvidia-utils')
  optdepends+=(
    'cuda: Nvidia GPU encoding support'
    'nvidia-utils: Nvidia GPU encoding support'
  )
fi

install="sunshine.install"

_pkgsrc="$_pkgname"
source=("$_pkgsrc"::"git+$url.git#commit=$_commit")
sha256sums=('SKIP')

prepare() {
  cd "$_pkgsrc"

  local i _unwanted=(
    third-party/nv-codec-headers
    packaging/linux/flatpak/deps/shared-modules
    packaging/linux/flatpak/deps/flatpak-builder-tools
    third-party/doxyconfig
  )

  for i in "${_unwanted[@]}"; do
    if [ -e "$i" ]; then
      git rm -r "$i"
    fi
  done

  git submodule update --init --recursive --depth 1

  ## disable unwanted macros
  sed 's&macro(find_package)&macro(_disable_find_package)&' -i cmake/macros/common.cmake

  ## fix for miniupnpc 2.3.3
  sed '1i #include <cstddef>' -i src/upnp.cpp

  ## fix for boost 1.88
  sed -E 's&(Boost CONFIG) \S+ EXACT\b&\1&' -i cmake/dependencies/Boost_Sunshine.cmake

  sed -E 's&<boost/process.hpp>&"'"${srcdir}"'/boost_process_v1.hpp"&' \
    -i src/platform/common.h

  sed -E 's&(namespace bp = boost::process);&\1::v1;&' \
    -i src/platform/linux/misc.cpp

  sed -E 's&<boost/process/v1.hpp>&"'"${srcdir}"'/boost_process_v1.hpp"&' \
    -i src/platform/linux/misc.cpp \
    src/process.h

  install -Dm644 /dev/stdin "$srcdir/boost_process_v1.hpp" << END
#ifndef BOOST_PROCESS_V1_HPP
#define BOOST_PROCESS_V1_HPP
#include <boost/process/v1/args.hpp>
#include <boost/process/v1/async.hpp>
#include <boost/process/v1/async_system.hpp>
#include <boost/process/v1/group.hpp>
#include <boost/process/v1/child.hpp>
#include <boost/process/v1/cmd.hpp>
#include <boost/process/v1/env.hpp>
#include <boost/process/v1/environment.hpp>
#include <boost/process/v1/error.hpp>
#include <boost/process/v1/exe.hpp>
#include <boost/process/v1/group.hpp>
#include <boost/process/v1/handles.hpp>
#include <boost/process/v1/io.hpp>
#include <boost/process/v1/pipe.hpp>
#include <boost/process/v1/shell.hpp>
#include <boost/process/v1/search_path.hpp>
#include <boost/process/v1/spawn.hpp>
#include <boost/process/v1/system.hpp>
#include <boost/process/v1/start_dir.hpp>
#endif //BOOST_PROCESS_V1_HPP
END
}

pkgver() {
  cd "$_pkgsrc"
  git describe --tags --abbrev=7 --exclude='*[a-zA-Z][a-zA-Z]*' \
    | sed -E 's/^[^0-9]*//;s/([^-]*-g)/r\1/;s/-/./g'
}

build() (
  export BRANCH="master"
  export BUILD_VERSION="${pkgver}"
  export COMMIT="$(git -C "$_pkgsrc" rev-parse HEAD)"

  export CFLAGS="${CFLAGS/-Werror=format-security/} -std=gnu17"
  export CXXFLAGS="${CXXFLAGS/-Werror=format-security/} -std=gnu++17"

  export CC="gcc-$_cuda_gcc_version"
  export CXX="g++-$_cuda_gcc_version"

  export CUDA_PATH=/opt/cuda
  export NVCC_CCBIN="/usr/bin/g++-$_cuda_gcc_version"

  local _cmake_options=(
    -B build
    -S "$_pkgsrc"
    -G Ninja
    -DCMAKE_BUILD_TYPE=None
    -DCMAKE_INSTALL_PREFIX='/usr'
    -DSUNSHINE_ASSETS_DIR="share/sunshine"
    -DSUNSHINE_EXECUTABLE_PATH='/usr/bin/sunshine'
    -DSUNSHINE_ENABLE_CUDA=ON
    -DSUNSHINE_ENABLE_DRM=ON
    -DSUNSHINE_ENABLE_TRAY=ON
    -DSUNSHINE_ENABLE_VAAPI=ON
    -DSUNSHINE_ENABLE_WAYLAND=ON
    -DSUNSHINE_ENABLE_X11=ON
    -DBUILD_DOCS=OFF
    -Wno-dev
  )

  if [[ "${_use_cuda::1}" == "t" ]]; then
    _cmake_options+=(-DCUDA_FAIL_ON_MISSING=ON)
  else
    _cmake_options+=(-DCUDA_FAIL_ON_MISSING=OFF)
  fi

  cmake "${_cmake_options[@]}"
  cmake --build build
)

check() {
  cd "build/tests"
  ./test_sunshine || :
}

package() {
  depends+=(
    'avahi'
    'libx11'
    'libxcb'
    'libxfixes'
    'libxrandr'
    'mesa' # libgbm
  )

  if [[ "$_use_sodeps::1}" == "t" ]]; then
    eval "depends+=(
      'libicuuc.so'     # icu
      'libminiupnpc.so' # miniupnpc
    )"
  fi

  DESTDIR="$pkgdir" cmake --install build
}
