# Maintainer: Jiachen YANG <farseerfc at archlinux dot org>

_pkgname=libtg_owt
pkgname=${_pkgname}-git
pkgver=0.git.r73.d91d618
pkgrel=1
pkgdesc='WebRTC library - static linked, git version'
arch=('x86_64')
url='https://github.com/desktop-app/tg_owt'
license=('custom:BSD')
depends=('protobuf')
makedepends=('git' 'ninja' 'unzip' 'cmake' 'libxrandr' 'libxcomposite' 'openssl' 'glibc' 'ffmpeg' 'libva' 'opus' 'yasm' 'libjpeg-turbo')
options=('staticlibs')
source=("tg_owt::git+${url}.git"
        "libvpx::git+https://chromium.googlesource.com/webm/libvpx.git"
        "libyuv::git+https://chromium.googlesource.com/libyuv/libyuv.git")
b2sums=('SKIP'
        'SKIP'
        'SKIP')
provides=('libtg_owt')
conflicts=('libtg_owt')

pkgver(){
  cd $srcdir/tg_owt
  printf "0.git.r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

prepare() {
  cd tg_owt
  git submodule init
  git config submodule.src/third_party/libvpx/source/libvpx.url "$srcdir"/libvpx
  git config submodule.src/third_party/libyuv.url "$srcdir"/libyuv
  git submodule update
}

build() {
  cd tg_owt
  mkdir build
  cd build
  # path to openssl include is intentionally wrong, so that it will not mess up srtp include headers
  cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DTG_OWT_SPECIAL_TARGET=linux \
    -DTG_OWT_LIBJPEG_INCLUDE_PATH=/usr/include \
    -DTG_OWT_OPENSSL_INCLUDE_PATH=/usr/include \
    -DTG_OWT_OPUS_INCLUDE_PATH=/usr/include/opus \
    -DTG_OWT_FFMPEG_INCLUDE_PATH=/usr/include \
    ..
  ninja
}

package() {
  cd tg_owt/build
  DESTDIR="${pkgdir}/" ninja install
}
