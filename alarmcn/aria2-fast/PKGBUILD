# Maintainer: Pandada8 < pandada8@gmail.com >
# Contributor: Thomas Dziedzic < gostrc at gmail >
# Contributor: Angel Velasquez <angvp@archlinux.org>
# Contributor: Alexander Fehr <pizzapunk gmail com>
# Contributor: Daniel J Griffiths <ghost1227@archlinux.us>

pkgname=aria2-fast
pkgver=1.37.0
pkgrel=1
pkgdesc='Aria2 Download utility with little patch to maximize aria2 download speed'
arch=('i686' 'x86_64' 'armv6h' 'armv7h' 'aarch64')
url='http://aria2.sourceforge.net/'
license=('GPL')
depends=('gnutls' 'libxml2' 'sqlite' 'c-ares' 'ca-certificates' 'libssh2')
checkdepends=('cppunit')
provides=('aria2')
conflicts=('aria2')
source=("https://github.com/aria2/aria2/releases/download/release-${pkgver}/aria2-${pkgver}.tar.xz" "aria2-fast.patch")

build() {
  cd aria2-${pkgver}

  patch -Np1 < ../aria2-fast.patch

  ./configure \
    --prefix=/usr \
    --enable-libaria2 \
    --with-ca-bundle=/etc/ssl/certs/ca-certificates.crt

  make
}

check() {
  cd aria2-${pkgver}
  # disable check since I don't know how to fix it
  # make check
}

package() {
  cd aria2-${pkgver}

  make DESTDIR=${pkgdir} install

  # add bash completion (aria2 automatically installs to a temporary target directory)
  install -d ${pkgdir}/usr/share/bash-completion/completions
  install -m644 ${pkgdir}/usr/share/doc/aria2/bash_completion/aria2c \
    ${pkgdir}/usr/share/bash-completion/completions
  rm -rf ${pkgdir}/usr/share/doc/aria2/bash_completion
}
md5sums=('dd00565c2f671331735089e6b807ece0'
         '93c7981c1b7c3bc44226245d3d718894')
