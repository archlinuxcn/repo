# Contributor: der_FeniX <derfenix@gmail.com>
# Maintainer: Albert Graef <aggraef@gmail.com>

# This is version 1 of flite. If you're looking for version 2 then you should
# install package flite instead (also available in the AUR).

pkgname=flite1
_pkgname=flite
pkgver=1.4
pkgrel=2
pkgdesc="A lighweight version of festival speech synthesis (version 1)"
arch=('i686' 'x86_64')
url="http://www.speech.cs.cmu.edu/flite/"
license=('custom')
depends=('glibc' 'alsa-lib')
conflicts=('flite' 'flite-fpic')
source=(http://www.festvox.org/flite/packed/${_pkgname}-${pkgver}/${_pkgname}-${pkgver}-release.tar.bz2
	${pkgname}.patch)
md5sums=('b7c3523b3bbc6f29ce61e6650cd9a428'
         '83ea65d511d5cf0e1471bc10af16ab7d')

prepare() {
  cd "${srcdir}/${_pkgname}-${pkgver}-release"
  patch -p1 -i ../${pkgname}.patch
  sed -i 's/BUILDDIR/_FLITE1_BUILDPATH/g' config/common_make_rules
}

build() {
  cd "${srcdir}/${_pkgname}-${pkgver}-release"
  # we want the 16k, not the 8k voice
  CFLAGS="-O3" ./configure --prefix=/usr --enable-shared --with-vox=cmu_us_kal16
  # no parallel builds
  make -j1
}

package() {
  cd "${srcdir}/${_pkgname}-${pkgver}-release"
  make prefix="${pkgdir}/usr" install
  install -D -m644 COPYING "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
