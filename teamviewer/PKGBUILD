# Maintainer: Alex Taber <aft dot pokemon at gmail dot com>

pkgname=teamviewer
pkgver=11.0.52520
pkgrel=1.5
pkgdesc='All-In-One Software for Remote Support and Online Meetings'
arch=('i686' 'x86_64')
url='http://www.teamviewer.com'
license=('custom')
options=('!strip')
provides=('teamviewer')
conflicts=('teamviewer-beta')
depends_x86_64=(
	'lib32-fontconfig'
	'lib32-libpng12'
	'lib32-libsm'
	'lib32-libxinerama'
	'lib32-libxrender')
depends_i686=(
	'fontconfig'
	'libpng12'
	'libsm'
	'libxinerama'
	'libxrender')
install=teamviewer.install
source_x86_64=("http://download.teamviewer.com/download/version_${pkgver%%.*}x/teamviewer_${pkgver}_amd64.deb")
source_i686=("http://download.teamviewer.com/download/version_${pkgver%%.*}x/teamviewer_${pkgver}_i386.deb")
sha256sums_x86_64=('d862fe3f26bf05e7b7f5fd5972873b5d859e40059c7f41783865594fc58d38fd')
sha256sums_i686=('66f2444b660b87f2fdc1d19949b94bbd840982d51c3405e4a53799cd6a6c6090')

prepare() {
	echo "If the install fails, you need to uninstall Teamviewer 10"
	tar -xf data.tar.bz2
}

package() {
	# Install
	echo "If the install fails here, you need to uninstall Teamviewer 10"
	cp -dr --no-preserve=ownership {etc,opt,usr,var} "${pkgdir}"/

	# Additional files
	rm "${pkgdir}"/opt/teamviewer/tv_bin/xdg-utils/xdg-email
	install -D -m0644 "${pkgdir}"/opt/teamviewer/tv_bin/script/teamviewerd.service \
		"${pkgdir}"/usr/lib/systemd/system/teamviewerd.service
	install -d -m0755 "${pkgdir}"/usr/{share/applications,share/licenses/teamviewer}
	ln -s /opt/teamviewer/tv_bin/desktop/teamviewer-teamviewer${pkgver%%.*}.desktop \
		"${pkgdir}"/usr/share/applications/teamviewer.desktop
	ln -s /opt/teamviewer/License.txt \
		"${pkgdir}"/usr/share/licenses/teamviewer/LICENSE
}
