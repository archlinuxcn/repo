# Contributor: Tom < reztho at archlinux dot us >
pkgname=openmsx-catapult-git
pkgver=936.7f9c72a
pkgrel=1
pkgdesc="Front-end for openMSX: the MSX emulator that aims for perfection."
arch=('i686' 'x86_64')
url="http://openmsx.org"
license=('GPL')
depends=('libxml2' 'wxgtk' 'zlib' 'libjpeg' 'libpng' 'libtiff')
makedepends=('python2' 'git')
optdepends=('openmsx')
source=("git://github.com/openMSX/wxcatapult.git")
provides=("openmsx-catapult")
conflicts=("openmsx-catapult")

pkgver() {
  cd "${srcdir}/wxcatapult"
  printf "%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

build() {
  cd "${srcdir}/wxcatapult"

  # Catapult requires python2
  sed -i 's@=python@=python2@' build/main.mk

  # Changing some default configurations...
  sed -i 's@SYMLINK_FOR_BINARY:=true@SYMLINK_FOR_BINARY:=false@' build/custom.mk
  sed -i 's@/opt/openMSX-Catapult@/usr/share/openmsx-catapult@' build/custom.mk
  sed -i 's@/opt/openMSX/bin/openmsx@/usr/bin/openmsx@' build/custom.mk
  sed -i 's@/opt/openMSX/share@/usr/share/openmsx@' build/custom.mk
  echo 'INSTALL_DOC_DIR:=/usr/share/doc/openmsx-catapult' >> build/custom.mk
  echo 'INSTALL_SHARE_DIR:=/usr/share/openmsx-catapult' >> build/custom.mk
  echo 'INSTALL_BINARY_DIR:=/usr/bin' >> build/custom.mk

  # Compiling
  make
}

package() {
  cd "${srcdir}/wxcatapult"

  mkdir -p "${pkgdir}/usr/share/applications"
  make DESTDIR="${pkgdir}" install

  # Fixing the .desktop file
  sed -i 's@/usr/share/openmsx-catapult/bin/catapult@/usr/bin/catapult@' \
  "${pkgdir}/usr/share/applications/openMSX-Catapult.desktop"
  sed -i 's@/usr/share/openmsx-catapult/doc/@/usr/share/doc/openmsx-catapult/@' \
  "${pkgdir}/usr/share/applications/openMSX-Catapult.desktop"
}

md5sums=('SKIP')
