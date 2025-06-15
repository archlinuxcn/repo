# Maintainer:

## options
: ${_build_cuda:=false} # nvenc

: ${_cuda_gcc_version:=14}

: ${_commit=64544e7960f5141f71438d72e5dedad81c03729c}

_pkgname="sunshine"
pkgname="$_pkgname"
pkgver=2025.122.141614
pkgrel=8
pkgdesc="A self-hosted GameStream host for Moonlight"
url="https://github.com/LizardByte/Sunshine"
license=('GPL-3.0-only')
arch=('x86_64' 'aarch64')

depends=(
  'libayatana-appindicator'
  'libcap'
  'libdrm'
  'libevdev'
  'libicuuc.so'     # icu
  'libminiupnpc.so' # miniupnpc
  'libnotify'
  'libpulse'
  'libva'
  'numactl'
  'openssl'
  'opus'
  'wayland'
)
makedepends=(
  "gcc${_cuda_gcc_version:?}"
  'boost'
  'cmake'
  'ffnvcodec-headers'
  'git'
  'ninja'
  'npm'
)
optdepends=(
  'cuda: Nvidia GPU encoding support'
  'intel-media-driver: Intel GPU encoding support'
  'libva-mesa-driver: AMD GPU encoding support'
)

if [[ "${_build_cuda::1}" == "t" ]]; then
  makedepends+=('cuda')
  checkdepends+=('nvidia-utils')
fi

install="sunshine.install"

_source_main() {
  _pkgsrc="$_pkgname"
  source=("$_pkgsrc"::"git+$url.git#commit=$_commit")
  sha256sums=('SKIP')
}

_source_sunshine() {
  local _sources_add=(
    'eidheim.simple-web-server'::'git+https://gitlab.com/eidheim/Simple-Web-Server.git'
    #'ffmpeg.nv-codec-headers'::'git+https://github.com/FFmpeg/nv-codec-headers.git'
    #'flathub.shared-modules'::'git+https://github.com/flathub/shared-modules.git'
    #'flatpak.flatpak-builder-tools'::'git+https://github.com/flatpak/flatpak-builder-tools.git'
    'games-on-whales.inputtino'::'git+https://github.com/games-on-whales/inputtino.git'
    'google.googletest'::'git+https://github.com/google/googletest.git'
    'lizardbyte.build-deps'::'git+https://github.com/LizardByte/build-deps.git'
    #'lizardbyte.doxyconfig'::'git+https://github.com/LizardByte/doxyconfig.git'
    'lizardbyte.libdisplaydevice'::'git+https://github.com/LizardByte/libdisplaydevice.git'
    'lizardbyte.nvapi-open-source-sdk'::'git+https://github.com/LizardByte/nvapi-open-source-sdk.git'
    'lizardbyte.tray'::'git+https://github.com/LizardByte/tray.git'
    'lizardbyte.virtual-gamepad-emulation-client'::'git+https://github.com/LizardByte/Virtual-Gamepad-Emulation-Client.git'
    'michaeltyson.tpcircularbuffer'::'git+https://github.com/michaeltyson/TPCircularBuffer.git'
    'moonlight-stream.moonlight-common-c'::'git+https://github.com/moonlight-stream/moonlight-common-c.git'
    'sleepybishop.nanors'::'git+https://github.com/sleepybishop/nanors.git'
    'wayland.wayland-protocols'::'git+https://gitlab.freedesktop.org/wayland/wayland-protocols.git'
    'wlroots.wlr-protocols'::'git+https://gitlab.freedesktop.org/wlroots/wlr-protocols.git'
  )

  local _p
  for _p in ${_sources_add[@]}; do
    source+=("$_p")
    sha256sums+=('SKIP')
  done

  _prepare_sunshine() (
    cd "$srcdir/$_pkgsrc"
    local _submodules=(
      'eidheim.simple-web-server'::'third-party/Simple-Web-Server'
      #'ffmpeg.nv-codec-headers'::'third-party/nv-codec-headers'
      #'flathub.shared-modules'::'packaging/linux/flatpak/deps/shared-modules'
      #'flatpak.flatpak-builder-tools'::'packaging/linux/flatpak/deps/flatpak-builder-tools'
      'games-on-whales.inputtino'::'third-party/inputtino'
      'google.googletest'::'third-party/googletest'
      'lizardbyte.build-deps'::'third-party/build-deps'
      #'lizardbyte.doxyconfig'::'third-party/doxyconfig'
      'lizardbyte.libdisplaydevice'::'third-party/libdisplaydevice'
      'lizardbyte.nvapi-open-source-sdk'::'third-party/nvapi-open-source-sdk'
      'lizardbyte.tray'::'third-party/tray'
      'lizardbyte.virtual-gamepad-emulation-client'::'third-party/ViGEmClient'
      'michaeltyson.tpcircularbuffer'::'third-party/TPCircularBuffer'
      'moonlight-stream.moonlight-common-c'::'third-party/moonlight-common-c'
      'sleepybishop.nanors'::'third-party/nanors'
      'wayland.wayland-protocols'::'third-party/wayland-protocols'
      'wlroots.wlr-protocols'::'third-party/wlr-protocols'
    )
    _submodule_update
  )
}

_source_moonlight_common_c() {
  local _sources_add=(
    'cgutman.enet'::'git+https://github.com/cgutman/enet.git'
  )

  local _p
  for _p in ${_sources_add[@]}; do
    source+=("$_p")
    sha256sums+=('SKIP')
  done

  _prepare_moonlight_common_c() (
    cd "$srcdir/$_pkgsrc"
    cd 'third-party/moonlight-common-c'
    local _submodules=(
      'cgutman.enet'::'enet'
    )
    _submodule_update
  )
}

_source_main
_source_sunshine
_source_moonlight_common_c

prepare() {
  _submodule_update() {
    local _module
    for _module in "${_submodules[@]}"; do
      git submodule init "${_module##*::}"
      git submodule set-url "${_module##*::}" "$srcdir/${_module%::*}"
      git -c protocol.file.allow=always submodule update "${_module##*::}"
      echo
    done
  }

  _run_if_exists _prepare_sunshine
  _run_if_exists _prepare_moonlight_common_c

  ## fix for miniupnpc 2.3.3
  sed '1i #include <stddef.h>' -i "$_pkgsrc"/src/upnp.cpp

  ## fix for boost 1.88
  sed -E 's&<boost/process.hpp>&"'"${srcdir}"'/boost_process_v1.hpp"&' \
    -i "$_pkgsrc"/src/platform/common.h

  sed -E 's&(namespace bp = boost::process);&\1::v1;&' \
    -i "$_pkgsrc"/src/platform/linux/misc.cpp

  sed -E 's&<boost/process/v1.hpp>&"'"${srcdir}"'/boost_process_v1.hpp"&' \
    -i "$_pkgsrc"/src/platform/linux/misc.cpp \
    "$_pkgsrc"/src/process.h

  install -Dm644 /dev/stdin "boost_process_v1.hpp" << END
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

build() (
  export BRANCH="master"
  export BUILD_VERSION="${pkgver}"
  export COMMIT="$(git -C "$_pkgsrc" rev-parse HEAD)"

  export CFLAGS="${CFLAGS/-Werror=format-security/}"
  export CXXFLAGS="${CXXFLAGS/-Werror=format-security/}"

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

  if [[ "${_build_cuda::1}" == "t" ]]; then
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

  DESTDIR="$pkgdir" cmake --install build
}

_run_if_exists() {
  if declare -F "$1" > /dev/null; then
    eval "$1"
  fi
}
