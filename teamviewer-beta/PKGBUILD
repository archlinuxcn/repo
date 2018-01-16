# Maintainer: Louis Tim Larsen <louis(a)louis.dk>
# Contributor: Ignacio <nachohc89 at gmail dot com>
# Contributor: Gun Onen <brookline653 at yahoo dot com>
# Contributor: Christian Hesse <mai at eworm dot de>
# Contributor: Yakir Sitbon <kingyes1 at gmail dot com>
# Contributor: Alucryd <alucryd at gmail dot com>
# Contributor: Stas S <whats_up at tut dot by>
# Contributor: Hilinus <itahilinus at hotmail dot it>

pkgname=teamviewer-beta
pkgver=13.0.6634 
pkgrel=1
pkgdesc='All-In-One Software for Remote Support and Online Meetings - beta version'
arch=('i686' 'x86_64')
url='http://www.teamviewer.com'
license=('custom')
options=('!strip')
provides=('teamviewer')
conflicts=('teamviewer')
depends=('qt5-base' 'qt5-declarative' 'qt5-x11extras' 'qt5-webkit' 'hicolor-icon-theme' 'qt5-x11extras' 'qt5-quickcontrols')
install=teamviewer.install
source_x86_64=("https://dl.tvcdn.de/download/linux/version_${pkgver%%.*}x/teamviewer_${pkgver}_amd64.deb")
source_i686=("https://dl.tvcdn.de/download/linux/version_${pkgver%%.*}x/teamviewer_${pkgver}_i386.deb")
sha256sums_i686=('2a3701d03e1ca7d836139b5f76c70cd0de95ddad90a73d7af5c9855676130e6d')
sha256sums_x86_64=('92171c89c74764ab0d654093fcc59bb3ffead2d197bd9473bfb5e93f65dc1120')

prepare() {
        tar -xf data.tar.xz
}

package() {
        # Install
        cp -dr --no-preserve=ownership {etc,opt,usr,var} "${pkgdir}"/
        rm -rf ${pkgdir}/etc/apt
        # Additional files
        rm "${pkgdir}"/opt/teamviewer/tv_bin/xdg-utils/xdg-email
        install -D -m0644 "${pkgdir}"/opt/teamviewer/tv_bin/script/teamviewerd.service \
                "${pkgdir}"/usr/lib/systemd/system/teamviewerd.service
        install -d -m0755 "${pkgdir}"/usr/{share/applications,share/licenses/teamviewer}
        ln -s /opt/teamviewer/doc/License.txt \
                "${pkgdir}"/usr/share/licenses/teamviewer/LICENSE
}
