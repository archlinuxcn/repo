# Maintainer: Marcel Korpel <marcel[dot]korpel[at]gmail>
# Contributor: Thayer Williams <thayer@archlinux.org>
# Contributor: Hugo Doria <hugo@archlinux.org>
# Contributor: TuxSpirit<tuxspirit@archlinux.fr>  2007/11/17 21:22:36 UTC
# Contributor: Daniel J Griffiths <ghost1227@archlinux.us>
# Contributor: Gaetan Bisson <bisson@archlinux.org>

_pkgname=p7zip
pkgname=${_pkgname}920
pkgver=9.20.1
pkgrel=9
pkgdesc='7zip compressed file archiver, version 9.20(.x)'
arch=('i686' 'x86_64')
url='http://p7zip.sourceforge.net/'
license=('GPL' 'custom')
depends=('gcc-libs' 'bash')
makedepends=('yasm' 'nasm' 'wxgtk2.8')
optdepends=('wxgtk2.8: GUI'
            'desktop-file-utils: desktop entries')
provides=("${_pkgname}=$pkgver")
conflicts=("${_pkgname}")
options=('!makeflags')
install=$pkgname.install
source=("http://downloads.sourceforge.net/project/${_pkgname}/${_pkgname}/${pkgver}/${_pkgname}_${pkgver}_src_all.tar.bz2"
        '7zFM.desktop')
sha1sums=('1cd567e043ee054bf08244ce15f32cb3258306b7'
          'f2c370d6f1b286b7ce9a2804e22541b755616a40')

prepare() {
  cd "${srcdir}/${_pkgname}_${pkgver}"
  rm GUI/kde4/p7zip_compress.desktop
  [[ $CARCH = x86_64 ]] \
  && cp makefile.linux_amd64_asm makefile.machine \
  || cp makefile.linux_x86_asm_gcc_4.X makefile.machine

  sed -i 's/wx-config/wx-config-2.8/g' CPP/7zip/TEST/TestUI/makefile \
    CPP/7zip/UI/{FileManager,GUI,P7ZIP}/makefile
}

build() {
  cd "${srcdir}/${_pkgname}_${pkgver}"
  make all4 OPTFLAGS="${CXXFLAGS}"
}

package() {
  cd "${srcdir}/${_pkgname}_${pkgver}"
  make install \
    DEST_DIR="${pkgdir}" \
    DEST_HOME="/usr" \
    DEST_MAN="/usr/share/man"

  # Licenses
  install -d "${pkgdir}"/usr/share/licenses/p7zip
  ln -s -t "${pkgdir}"/usr/share/licenses/p7zip \
    /usr/share/doc/p7zip/DOCS/License.txt \
    /usr/share/doc/p7zip/DOCS/unRarLicense.txt

  # Integration with stuff...
  install -Dm644 GUI/p7zip_32.png "${pkgdir}"/usr/share/icons/hicolor/32x32/apps/p7zip.png
  install -d "${pkgdir}"/usr/share/{applications,kde4/services/ServiceMenus}
  cp GUI/kde4/* "${pkgdir}"/usr/share/kde4/services/ServiceMenus/
  cp ../7zFM.desktop "${pkgdir}"/usr/share/applications/
  ln -s 7zCon.sfx "${pkgdir}"/usr/lib/p7zip/7z.sfx

  find GUI/help -type d -exec chmod 755 {} \;
  cp -r GUI/help "${pkgdir}"/usr/lib/p7zip/

  chmod -R u+w "${pkgdir}/usr"
}
