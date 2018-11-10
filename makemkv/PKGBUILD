# Maintainer: Olaf Bauer <hydro@freenet.de>

pkgname=makemkv
pkgver=1.14.1
pkgrel=1
pkgdesc="DVD and Blu-ray to MKV converter and network streamer"
arch=('i686' 'x86_64')
url="http://www.makemkv.com"
license=('LGPL' 'MPL' 'custom')
depends=('qt5-base' 'libxkbcommon-x11' 'hicolor-icon-theme' 'icu' 'ffmpeg')
if [ "$CARCH" = "x86_64" ]; then
  optdepends=('lib32-glibc: dts support')
fi
install=makemkv.install
source=(${url}/download/${pkgname}-bin-${pkgver}.tar.gz
        ${url}/download/${pkgname}-oss-${pkgver}.tar.gz
        makemkv.1
        makemkvcon.1
        mmdtsdec.1)
md5sums=('36429b35240c4a3a885f6bfc674c7a62'
         '3ba1e11da444a4fa831d5b13f441f336'
         '1f9b3a91427a2015434e501542443f4c'
         '7f4b112c5178860cc2eb25059ae1af2a'
         '9476154228bf1b1f983178ba8565ac44')

build() {
  cd "${srcdir}/${pkgname}-oss-${pkgver}"
  CC=gcc CXX=g++ ./configure --prefix=/usr
  make
}

package() {
  cd "${srcdir}/${pkgname}-oss-${pkgver}"
  make DESTDIR=\""${pkgdir}"\" install

  cd "${srcdir}/${pkgname}-bin-${pkgver}"
  install -d tmp
  echo accepted > tmp/eula_accepted
  make DESTDIR=\""${pkgdir}"\" install

  install -Dm 644 src/eula_en_linux.txt "${pkgdir}/usr/share/licenses/${pkgname}/eula_en_linux.txt"

  cd "${srcdir}/"
  install -d "${pkgdir}/usr/share/man/man1/"
  install -m 644 -t "${pkgdir}/usr/share/man/man1/" makemkv.1 makemkvcon.1 mmdtsdec.1
}
