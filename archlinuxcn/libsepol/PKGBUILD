# Maintainer: Nicolas Iooss (nicolas <dot> iooss <at> m4x <dot> org)
# Contributor: Timothée Ravier <tim@siosm.fr>
# Contributor: Nicky726 (Nicky726 <at> gmail <dot> com)
# Contributor: Sergej Pupykin (pupykin <dot> s+arch <at> gmail <dot> com)
#
# This PKGBUILD is maintained on https://github.com/archlinuxhardened/selinux.
# If you want to help keep it up to date, please open a Pull Request there.

pkgname=libsepol
pkgver=3.1
pkgrel=1
pkgdesc="SELinux binary policy manipulation library"
arch=('i686' 'x86_64' 'armv6h')
url='https://github.com/SELinuxProject/selinux'
license=('LGPL2.1')
groups=('selinux')
makedepends=('flex')
depends=('glibc')
options=(staticlibs)
conflicts=("selinux-usr-${pkgname}")
provides=("selinux-usr-${pkgname}=${pkgver}-${pkgrel}")
source=("https://github.com/SELinuxProject/selinux/releases/download/20200710/${pkgname}-${pkgver}.tar.gz")
sha256sums=('ae6778d01443fdd38cd30eeee846494e19f4d407b09872580372f4aa4bf8a3cc')

build() {
  cd "${pkgname}-${pkgver}"

  export CFLAGS="${CFLAGS} -fno-semantic-interposition"
  make
}

package() {
  cd "${pkgname}-${pkgver}"
  make DESTDIR="${pkgdir}" SHLIBDIR=/usr/lib install
}
