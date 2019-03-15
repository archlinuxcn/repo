# Maintainer: Bailey Fox <bfox200012@gmail.com>
# Contributor: ajs124 < aur AT ajs124 DOT de >
# Contributor: Benoit Favre <benoit.favre@gmail.com>
# Contributor: Thomas Hebb <tommyhebb@gmail.com>

pkgname=abootimg-git
pkgver=r38.7e127fe
pkgrel=1
pkgdesc="A tool to read/write/update android boot images"
arch=('i686' 'x86_64' 'arm' 'armv7h')
url="https://github.com/ggrandou/abootimg"
license=('GPL')
depends=('util-linux' 'cpio')
makedepends=('git')
provides=('abootimg')
source=('git+https://github.com/ggrandou/abootimg.git'
	'no-initrd.patch')
sha256sums=('SKIP'
            '5fe9400e71f1ade170c1e0e99f343881edca2022300c7e7a1d34d776c22cc126')

pkgver() {
  cd "abootimg"
  printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

prepare() {
  cd "${srcdir}/abootimg"
  patch -p0 --binary < ../no-initrd.patch
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
