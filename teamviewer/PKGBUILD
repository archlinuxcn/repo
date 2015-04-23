# Maintainer: Yakir Sitbon <kingyes1 at gmail dot com>
# Contributor: Alucryd <alucryd at gmail dot com>
# Contributor: Stas S <whats_up at tut dot by>
# Contributor: Hilinus <itahilinus at hotmail dot it>

pkgname=teamviewer
pkgver=10.0.41499
pkgrel=1
pkgdesc="All-In-One Software for Remote Support and Online Meetings"
arch=('i686' 'x86_64')
url="http://www.teamviewer.com"
license=('custom')
depends=('bash')
options=('!strip')
install=${pkgname}.install

if [[ $CARCH == 'i686' ]]; then
  source=("teamviewer_linux-${pkgver}.deb::http://download.teamviewer.com/download/teamviewer_i386.deb")
  md5sums=('5aa2ce43cd9aea23ff3b64bfd498fcf3')
  depends+=('alsa-lib' 'gcc-libs' 'libxdamage' 'libxtst' 'zlib' 'freetype2' 'libxrandr' 'libice' 'libsm')
elif [[ $CARCH == 'x86_64' ]]; then
  source=("teamviewer_linux_x64-${pkgver}.deb::http://download.teamviewer.com/download/teamviewer_amd64.deb")
  md5sums=('fdbc27543e0955e217097810a7983507')
  depends+=('lib32-gcc-libs' 'lib32-alsa-lib' 'lib32-libxtst' 'lib32-libxdamage' 'lib32-zlib' 'lib32-freetype2' 'lib32-libxrandr' 'lib32-libice' 'lib32-libsm' 'lib32-libxinerama')
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
  rm "${pkgdir}"/opt/teamviewer/tv_bin/xdg-utils/xdg-email
  install -dm 755 "${pkgdir}"/usr/{lib/systemd/system,share/applications,share/licenses/teamviewer}
  install -m 644 "${pkgdir}"/opt/teamviewer/tv_bin/script/teamviewerd.service "${pkgdir}"/usr/lib/systemd/system/teamviewerd.service
  ln -s /opt/teamviewer/tv_bin/desktop/teamviewer-teamviewer10.desktop "${pkgdir}"/usr/share/applications/teamviewer.desktop
  ln -s /opt/teamviewer/License.txt "${pkgdir}"/usr/share/licenses/teamviewer/LICENSE
}

