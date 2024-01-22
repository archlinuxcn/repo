# Maintainer: Tércio Martins <echo dGVyY2lvd2VuZGVsQGdtYWlsLmNvbQo= | base64 -d>

_pkgname=olive
pkgname=$_pkgname-git
pkgver=continuous.r2626.gbfc0d3191
pkgrel=1
arch=('x86_64')
pkgdesc="Free non-linear video editor"
url="https://www.olivevideoeditor.org/"
license=('GPL-3.0-or-later')
depends=('ffmpeg' 'openimageio' 'opentimelineio' 'portaudio' 'qt5-x11extras')
makedepends=('cmake' 'git' 'ninja' 'qt5-svg' 'qt5-tools')

# Temporarily, the "olive-git" package is incompatible
# with the dependency "olive-community-effects-git".
# More information on the link:
# https://github.com/cgvirus/Olive-Editor-Community-Effects/blob/65b96e093c128f2bb9336e6b7ed93f801e73435d/README.md
# optdepends=('olive-community-effects-git')

provides=('olive')
conflicts=('olive')
source=('git+https://github.com/olive-editor/olive.git'
        'git+https://github.com/olive-editor/KDDockWidgets.git'
        'git+https://github.com/olive-editor/core.git'
        'support_ocio_2_3.patch')
b2sums=('SKIP'
        'SKIP'
        'SKIP'
        '05d81f99409d78ae51a1200a14d07d29a830b53343d92d988e7ad8a2994b86d46f42ed0ec2c430829f8282e1284f067cc24ce78e8bd4233a40e09b5c179941df')

pkgver() {
  cd $_pkgname
  git describe --long --tags | sed 's/\([^-]*-g\)/r\1/;s/-/./g'
}

prepare(){
  cd $_pkgname
  git submodule init
  git config submodule.ext/core.url "$srcdir"/core
  git config submodule.ext/KDDockWidgets.url "$srcdir"/KDDockWidgets
  git -c protocol.file.allow=always submodule update

  # Add support for OpenColorIO version 2.3
  patch --forward --strip=1 --input="$srcdir"/support_ocio_2_3.patch
}

build() {
  cd $_pkgname
  cmake -GNinja \
        -Bbuild \
        -DCMAKE_BUILD_TYPE=RelWithDebInfo \
        -DCMAKE_INSTALL_PREFIX=/usr \
        -DOTIO_DEPS_INCLUDE_DIR=/usr/include/opentimelineio
  ninja -C build/
}

package() {
  cd $_pkgname
  DESTDIR="$pkgdir" ninja -C build/ install
}
