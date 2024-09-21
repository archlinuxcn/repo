# Maintainer: Jeremy Kescher <jeremy@kescher.at>
# Based on Arch `fmt` package
# Maintainer: Maxime Gauduin <alucryd@archlinux.org>
# Contributor: Mihai Bişog <mihai.bisog@gmail.com>

pkgname=fmt10
pkgver=10.2.1
pkgrel=1
pkgdesc='Open-source formatting library for C++'
arch=(x86_64)
url=https://fmt.dev
license=(MIT)
depends=(gcc-libs)
makedepends=(
  cmake
  doxygen
  git
  ninja
  npm
  python-breathe
  python-docutils
  python-jinja
  python-six
  python-sphinx
  python-wheel
)
provides=(libfmt.so)
_tag=e69e5f977d458f2650bb346dadf2ad30c5320281
source=(
  git+https://github.com/fmtlib/fmt.git#tag=${_tag}
  fmt-no-pip-no-virtualenv.patch
  fmt-10.0.0-sphinx.patch
)
b2sums=('e79699a46afe099007f9ad4b5ba063fbd8a90575535cd006452c7e648d4a6131460407ecfeb824c7e4d64d793f9e09ff2953afd7f997cd4a273b9422b832e46b'
        '0bc421afdc4c2527525ce2e21740c9f72e05431394fb4710c1a8fa6d3bb2ee20d0630e2a76ddbac3c0ba27c1ab08f0c8e27d060def1370721b1c94246cbbf0ff'
        '4eabdf38317e22e6b650b91821f1fab50bb3641e4f9a63847cb9b823becd3a4106fe47df37c8dc886f5fe1d1d3e529136c867459105df07c359582214d6fa01f')

prepare() {
  cd fmt
  patch -Np1 -i ../fmt-no-pip-no-virtualenv.patch
  patch -Np1 -i ../fmt-10.0.0-sphinx.patch
}

pkgver() {
  cd fmt
  git describe --tags
}

build() {
  cmake -S fmt -B build -G Ninja \
    -DCMAKE_BUILD_TYPE=None \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_INSTALL_LIBDIR=/usr/lib \
    -DFMT_CMAKE_DIR=lib/cmake/$pkgname \
    -DFMT_DOC=OFF \
    -DFMT_INC_DIR=include/$pkgname \
    -DFMT_PKGCONFIG_DIR=lib/$pkgname/pkgconfig \
    -DFMT_TEST="$CHECKFUNC" \
    -DBUILD_SHARED_LIBS=ON \
    -Wno-dev
  cmake --build build
}

check() {
  cmake --build build --target test
}

package() {
  DESTDIR="${pkgdir}" cmake --install build
  install -Dm 644 fmt/LICENSE -t "${pkgdir}"/usr/share/licenses/fmt10/
  
  cd "$pkgdir"
  ln -sf ../libfmt.so.10 usr/lib/$pkgname/libfmt.so
  rm usr/lib/libfmt.so
  sed -i "/libdir/s/\/lib/&\/$pkgname/" usr/lib/$pkgname/pkgconfig/*.pc
}

# vim: ts=2 sw=2 et:
