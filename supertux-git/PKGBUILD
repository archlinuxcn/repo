# Maintainer: Frederic Bezies <fredbezies at gmail dot com>
# Contributor: Xiao-Long Chen <chenxiaolong@cxl.epac.to>
# Original Maintainer: Hakim <acrox999 at gmail dot com>
# Contributor: Patrick Bartels <p4ddy.b@gmail.com>

pkgname=supertux-git
_pkgname=supertux
pkgver=v0.5.1.r395.g620104563
pkgrel=1
epoch=1
pkgdesc="A classic 2D jump'n run sidescroller game in a style similar to the original SuperMario game"
url='http://supertux.lethargik.org/'
license=(GPL)
arch=(i686 x86_64)
depends=('sdl2_image' 'openal' 'libvorbis' 'glew' 'boost-libs' 'curl')
makedepends=('git' 'cmake' 'physfs' 'boost')
conflicts=(supertux)
provides=(supertux)
source=('git+https://github.com/SuperTux/supertux.git'
        # submodules
        'git+https://github.com/SuperTux/data.git'
        'git+https://github.com/google/googletest.git'
        'git+https://github.com/SuperTux/physfs.git'
        'git+https://github.com/SuperTux/sexp-cpp.git'
        'git+https://github.com/albertodemichelis/squirrel.git'
        'git+https://github.com/SuperTux/tinygettext.git'
        'git+https://github.com/SuperTux/translations.git')
sha512sums=('SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP')

pkgver() {
  cd "$_pkgname"
  git describe --long --tags | sed 's/\([^-]*-g\)/r\1/;s/-/./g'
}

prepare() {
  cd "$_pkgname"

  git submodule init
  git config submodule.data.url "${srcdir}"/data
  git config submodule.external/googletest.url "${srcdir}"/googletest
  git config submodule.external/physfs.url "${srcdir}"/physfs
  git config submodule.external/sexp-cpp.url "${srcdir}"/sexp-cpp
  git config submodule.external/squirrel.url "${srcdir}"/squirrel
  git config submodule.external/tinygettext.url "${srcdir}"/tinygettext
  git config submodule.translations.url "${srcdir}"/translations
  git submodule update

  sed -i '/curl\/types.h/d' src/addon/addon_manager.cpp
  sed -i '1i#include <cstddef>' src/supertux/screen_manager.hpp  
}

build() {
  cd "$_pkgname"

  export CFLAGS+=" -fPIC"
  export CXXFLAGS+=" -fPIC"

  cmake . \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DINSTALL_SUBDIR_BIN=bin

  make
}

package() {
  cd "$_pkgname"

  make DESTDIR="${pkgdir}/" install
}
