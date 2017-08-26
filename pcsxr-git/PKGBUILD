# Maintainer : Özgür Sarıer <echo b3pndXJzYXJpZXIxMDExNjAxMTE1QGdtYWlsLmNvbQo= | base64 -d>
# Contributor: Maxime Gauduin <alucryd@archlinux.org>
# Contributor: Infy <eugene.yudin@gmail.com>

pkgname=pcsxr-git
pkgver=1.9.94.r1697.6484236c
pkgrel=1
pkgdesc='A Sony PlayStation emulator based on the PCSX-df Project'
arch=('i686' 'x86_64')
url='https://github.com/pcsxr/PCSX-Reloaded/tree/master/pcsxr'
license=('GPL')
depends=('ffmpeg' 'gdk-pixbuf2' 'glib2' 'glibc' 'gtk3' 'libarchive' 'libcdio'
         'libgl' 'libpulse' 'libx11' 'libxext' 'libxtst' 'libxv' 'libxxf86vm'
         'sdl2' 'zlib')
makedepends=('cmake' 'git' 'intltool' 'mesa')
[[ $CARCH == i686 ]] && makedepends+=('nasm')
provides=('pcsxr')
conflicts=('pcsxr' 'pcsx-df')
replaces=('pcsxr-svn')
source=('pcsxr::git+https://github.com/pcsxr/PCSX-Reloaded.git')
sha256sums=('SKIP')

pkgver() {
  cd pcsxr

  echo "1.9.94.r$(git rev-list --count HEAD).$(git rev-parse --short HEAD)"
}

prepare() {
  cd pcsxr/pcsxr

  if [[ -d build ]]; then
    rm -rf build
  fi
  mkdir build
}

build() {
  cd pcsxr/pcsxr/build

  cmake .. \
    -DCMAKE_BUILD_TYPE='Release' \
    -DCMAKE_INSTALL_PREFIX='/usr' \
    -DCMAKE_INSTALL_LIBDIR='/usr/lib' \
    -DSND_BACKEND='pulse' \
    -DENABLE_CCDDA='ON' \
    -DUSE_LIBARCHIVE='ON' \
    -DUSE_LIBCDIO='ON'
  make
}

package() {
  cd pcsxr/pcsxr/build

  make DESTDIR="${pkgdir}" install
}

# vim: ts=2 sw=2 et:
