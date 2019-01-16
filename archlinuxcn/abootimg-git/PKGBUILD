# Maintainer: ajs124 < aur AT ajs124 DOT de >
# Contributor: Benoit Favre <benoit.favre@gmail.com>
# Contributor: Thomas Hebb <tommyhebb@gmail.com>

pkgname=abootimg-git
pkgver=0.6.r6.g1ebeb39
pkgrel=1
pkgdesc="A tool to read/write/update android boot images"
arch=('i686' 'x86_64' 'arm' 'armv7h')
url="http://gitorious.org/ac100/abootimg"
license=('GPL')
depends=('util-linux' 'cpio')
makedepends=('git')
provides=('abootimg')
# upstream seems dead and gitorious is about to shut down -> use my mirror
#source=('git+https://gitorious.org/ac100/abootimg.git')
source=('git+https://gitlab.com/ajs124/abootimg.git')
sha256sums=('SKIP')

pkgver() {
  cd "abootimg"
  git describe --long --tags | sed -r 's/^v//;s/([^-]*-g)/r\1/;s/-/./g'
}

build() {
  cd "${srcdir}/abootimg"

  make
  gzip -f debian/abootimg.1
}

package() {
  cd "${srcdir}/abootimg"

  install -d "${pkgdir}/usr/bin" "${pkgdir}/usr/share/man/man1/"
  install -t "${pkgdir}/usr/bin" abootimg abootimg-pack-initrd abootimg-unpack-initrd
  install -t "${pkgdir}/usr/share/man/man1/" debian/abootimg.1.gz
}
