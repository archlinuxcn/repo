# Maintainer: Fabio 'Lolix' Loli <fabio.loli@disroot.org> -> https://github.com/FabioLolix
# Contributor: Marcel Korpel <marcel[dot]korpel[at]gmail>
# Contributor: Olaf Bauer <hydro@freenet.de>

pkgname=makemkv
pkgver=1.17.1
pkgrel=1
pkgdesc="DVD and Blu-ray to MKV converter"
arch=(x86_64 i686)
url="https://www.makemkv.com"
license=(LGPL MPL custom)
depends=(qt5-base ffmpeg)
optdepends=(java-runtime)
optdepends_x86_64=('lib32-glibc: dts support')
install=makemkv.install
source=(${url}/download/${pkgname}-bin-${pkgver}.tar.gz
        ${url}/download/${pkgname}-oss-${pkgver}.tar.gz
        makemkv.1
        makemkvcon.1
        mmdtsdec.1)
sha256sums=('0784908b07f9fc87307a0f958105b7e2d37f5f10c0ef1a1280854e7d7c06b1f3'
            '0d572b1b937d97275cb75d71a142b3d555428aebd53a64161a500fda7ae766fe'
            '5573b2e4bade10d8cd258a7c235eb46f66ef8c8c97e5d5eb090c38fa0f94389b'
            'f12c0facf2f0071a9f728b138986f0a4c2b4ff6ace2dfb2e96364e215e9fda6f'
            '2a6237d3d5ce073734c658c7ec5d2141ecd0047e6d3c45d1bd594135c928878f')

build() {
  cd "${srcdir}/${pkgname}-oss-${pkgver}"
  CFLAGS="$CFLAGS -std=c++11" CC=gcc CXX=g++ ./configure --prefix=/usr
  make
}

package() {
  cd "${srcdir}/${pkgname}-oss-${pkgver}"
  make DESTDIR="${pkgdir}" install

  cd "${srcdir}/${pkgname}-bin-${pkgver}"
  install -d tmp
  echo accepted > tmp/eula_accepted
  make DESTDIR="${pkgdir}" install

  install -Dm 644 src/eula_en_linux.txt "${pkgdir}/usr/share/licenses/${pkgname}/eula_en_linux.txt"

  cd "${srcdir}/"
  install -d "${pkgdir}/usr/share/man/man1/"
  install -m 644 -t "${pkgdir}/usr/share/man/man1/" makemkv.1 makemkvcon.1 mmdtsdec.1
}
