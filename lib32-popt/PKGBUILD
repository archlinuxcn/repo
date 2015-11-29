# Maintainer: Michael Lass <bevan@bi-co.net>
# Contributor: jospehgbr <rafael.f.f1@gmail.com>
# Contributor: coderoar <coderoar@gmail.com>
# Contributor: webjdm <web.jdm@gmail.com>

# This PKGBUILD is maintained on github:
# https://github.com/michaellass/AUR

_pkgbase=popt
pkgname=lib32-${_pkgbase}
pkgver=1.16
pkgrel=6
pkgdesc="Commandline option parser (32 bit)"
arch=('x86_64')
url="http://rpm5.org"
license=('custom')
depends=('lib32-glibc' "${_pkgbase}")
makedepends=('gcc-multilib')
options=('!libtool')
source=(${url}/files/${_pkgbase}/${_pkgbase}-${pkgver}.tar.gz)
# Alternative: http://launchpad.net/$_pkgbase/head/$pkgver/+download/$_pkgbase-$pkgver.tar.gz
sha256sums=('e728ed296fe9f069a0e005003c3d6b2dde3d9cad453422a10d6558616d304cc8')

build() {
  export CC="gcc -m32"

  cd ${_pkgbase}-${pkgver}
  ./configure --prefix=/usr --libdir=/usr/lib32 --disable-nls
  make
}

package() {
  cd ${_pkgbase}-${pkgver}
  make DESTDIR="${pkgdir}" pkgconfigdir='/usr/lib32/pkgconfig' install

  rm -rf "${pkgdir}"/usr/{include,share}
  install -dm755 "${pkgdir}"/usr/share/licenses
  ln -s ${_pkgbase} "${pkgdir}"/usr/share/licenses/${pkgname}
}
