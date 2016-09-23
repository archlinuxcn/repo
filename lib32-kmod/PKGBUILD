# Maintainer: Jesse Jaara <gmail.com: jesse.jaara>

pkgname=lib32-kmod
pkgver=23
pkgrel=1
pkgdesc="Linux kernel module handling"
arch=('x86_64')
url="http://git.kernel.org/?p=utils/kernel/kmod/kmod.git;a=summary"
license=('GPL2')
depends=('lib32-zlib' 'lib32-xz')
makedepends=('gcc-multilib')
options=('!libtool')
source=("ftp://ftp.kernel.org/pub/linux/utils/kernel/kmod/kmod-$pkgver.tar.xz")
md5sums=('3cf469f40ec2ed51f56ba45ea03793e7')

build() {
  export CC="gcc -m32"
  export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"

  cd "${srcdir}/kmod-${pkgver}"

  ./configure \
    --libdir=/usr/lib32 \
    --sysconfdir=/etc \
    --disable-tools \
    --with-zlib \
    --with-xz

  make
}

package() {
  cd "${srcdir}/kmod-${pkgver}"

  make DESTDIR="${pkgdir}" install

  # nuke manpages and headers
  rm -rf "${pkgdir}"/usr/{share,include,bin}
}


