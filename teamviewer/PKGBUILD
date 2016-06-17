# Maintainer: Alex Taber <aft dot pokemon at gmail dot com>

pkgname=teamviewer
pkgver=11.0.57095
pkgrel=4
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
	'lib32-libxrender'
	'lib32-libjpeg6-turbo')
depends_i686=(
	'fontconfig'
	'libpng12'
	'libsm'
	'libxinerama'
	'libxrender'
	'libjpeg6-turbo')
install=teamviewer.install
source_x86_64=("https://download.teamviewer.com/download/version_${pkgver%%.*}x/teamviewer_${pkgver}_amd64.deb")
source_i686=("https://download.teamviewer.com/download/version_${pkgver%%.*}x/teamviewer_${pkgver}_i386.deb")
md5sums_i686=('e46cef43ea873dc00a74bc44f9990964')
md5sums_x86_64=('b8e2023b0dbfe7bfbbc1d391e1687929')

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
