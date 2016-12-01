# Maintainer: Steven Honeyman <stevenhoneyman at gmail com>

pkgname=flite
pkgver=2.0.0
pkgrel=2
pkgdesc="A lighweight speech synthesis engine (text to speech)"
arch=('i686' 'x86_64')
url="http://cmuflite.org"
license=('custom')
depends=('alsa-lib')
options=('strip' '!buildflags')
source=(http://festvox.org/flite/packed/flite-2.0/flite-2.0.0-release.tar.bz2)
md5sums=('645db96ffc296cbb6d37f231cc1cc6b2')

prepare() {
  cd "${srcdir}/${pkgname}-${pkgver}-release"
  sed '/^#VOXES.*$/d; s/+//g; s/cmu_indic_lex/&\nVOXES = cmu_us_kal16 cmu_us_slt/' config/android.lv >config/archlinux.lv
  sed -i '/$(INSTALL) -m 755 $(BINDIR)\/flite_time $(DESTDIR)$(INSTALLBINDIR)/d' main/Makefile
}

build() {
  cd "${srcdir}/${pkgname}-${pkgver}-release"
  ./configure --prefix=/usr --enable-shared \
			    --with-audio=alsa \
			    --with-vox=cmu_us_kal16 \
			    --with-langvox=archlinux
  make
}

package() {
  cd "${srcdir}/${pkgname}-${pkgver}-release"
  make prefix="${pkgdir}/usr" install
  install -D -m644 COPYING "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE" 
}
