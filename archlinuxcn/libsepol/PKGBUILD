# Maintainer: Nicolas Iooss (nicolas <dot> iooss <at> m4x <dot> org)
# Contributor: Timothée Ravier <tim@siosm.fr>
# Contributor: Nicky726 (Nicky726 <at> gmail <dot> com)
# Contributor: Sergej Pupykin (pupykin <dot> s+arch <at> gmail <dot> com)
#
# This PKGBUILD is maintained on https://github.com/archlinuxhardened/selinux.
# If you want to help keep it up to date, please open a Pull Request there.

pkgname=libsepol
pkgver=3.0
pkgrel=1
pkgdesc="SELinux binary policy manipulation library"
arch=('i686' 'x86_64' 'armv6h')
url='http://userspace.selinuxproject.org'
license=('LGPL2.1')
groups=('selinux')
makedepends=('flex')
depends=('glibc')
options=(staticlibs)
conflicts=("selinux-usr-${pkgname}")
provides=("selinux-usr-${pkgname}=${pkgver}-${pkgrel}")
source=("https://github.com/SELinuxProject/selinux/releases/download/20191204/${pkgname}-${pkgver}.tar.gz")
sha256sums=('5b7ae1881909f1048b06f7a0c364c5c8a86ec12e0ec76e740fe9595a6033eb79')

build() {
  cd "${pkgname}-${pkgver}"
  make
}

package() {
  cd "${pkgname}-${pkgver}"
  make DESTDIR="${pkgdir}" SHLIBDIR=/usr/lib install
}
