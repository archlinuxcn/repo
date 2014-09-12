# Maintainer: Hilinus <itahilinus at hotmail dot it>
# Contributor: Alucryd <alucryd at gmail dot com>
# Contributor: Stas S <whats_up at tut dot by>

pkgname=teamviewer
pkgver=9.0.32150
pkgrel=1
pkgdesc="All-In-One Software for Remote Support and Online Meetings"
arch=('i686' 'x86_64')
url="http://www.teamviewer.com"
license=('custom')
depends=('bash')
options=('!strip')
install=${pkgname}.install

if [[ $CARCH == 'i686' ]]; then
  source=("teamviewer_linux-${pkgver}.deb::http://www.teamviewer.com/download/teamviewer_linux.deb")
  md5sums=('2340e7f8d3f825012907104e0b166bcb')
  depends+=('alsa-lib' 'gcc-libs' 'libxdamage' 'libxtst' 'zlib' 'freetype2')
elif [[ $CARCH == 'x86_64' ]]; then
  source=("teamviewer_linux_x64-${pkgver}.deb::http://www.teamviewer.com/download/teamviewer_linux_x64.deb")
  md5sums=('4e930ec1ff2601e7fb65eb8edfec0bc0')
  depends+=('lib32-gcc-libs' 'lib32-alsa-lib' 'lib32-libxtst' 'lib32-libxdamage' 'lib32-zlib' 'lib32-freetype2')
fi

build() {
  cd "${srcdir}"
  tar -xf data.tar.gz
}

package() {
  cd "${srcdir}"

# Install
  cp -dr --no-preserve=ownership {etc,opt,usr,var} "${pkgdir}"/

# Additional files
  rm "${pkgdir}"/opt/teamviewer9/tv_bin/xdg-utils/xdg-email
  install -dm 755 "${pkgdir}"/usr/{lib/systemd/system,share/applications,share/licenses/teamviewer}
  install -m 644 "${pkgdir}"/opt/teamviewer9/tv_bin/script/teamviewerd.service "${pkgdir}"/usr/lib/systemd/system/teamviewerd.service
  ln -s /opt/teamviewer9/tv_bin/desktop/teamviewer-teamviewer9.desktop "${pkgdir}"/usr/share/applications/teamviewer.desktop
  ln -s /opt/teamviewer9/License.txt "${pkgdir}"/usr/share/licenses/teamviewer/LICENSE
}

