# Maintainer: Xiao-Long Chen <chenxiaolong@cxl.epac.to>
# Original Maintainer: Hakim <acrox999 at gmail dot com>
# Contributor: Patrick Bartels <p4ddy.b@gmail.com>

pkgname=supertux-git
pkgver=7292.f24d3bc
pkgrel=1
pkgdesc="A classic 2D jump'n run sidescroller game in a style similar to the original SuperMario game"
url='http://supertux.lethargik.org/'
license=(GPL)
arch=(i686 x86_64)
depends=(sdl2_image physfs openal libvorbis curl boost glew)
makedepends=(git cmake)
conflicts=(supertux)
provides=(supertux)
source=('git+https://github.com/SuperTux/supertux'
        # submodules
        'git+https://github.com/SuperTux/data.git'
        'git+https://github.com/google/googletest.git'
        'git+https://github.com/SuperTux/physfs'
        'git+https://github.com/SuperTux/sexp-cpp.git'
        'git+https://github.com/albertodemichelis/squirrel.git'
        'git+https://github.com/SuperTux/tinygettext.git'
        'git+https://github.com/SuperTux/translations')
sha512sums=('SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP')

pkgver() {
  cd supertux
  echo $(git rev-list --count master).$(git rev-parse --short master)
}

prepare() {
  cd supertux

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
  cd supertux

  export CFLAGS+=" -fPIC"
  export CXXFLAGS+=" -fPIC"

  cmake . \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DINSTALL_SUBDIR_BIN=bin

  make
}

package() {
  cd supertux

  make DESTDIR="${pkgdir}/" install
}
