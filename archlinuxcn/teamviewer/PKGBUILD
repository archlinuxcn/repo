# Maintainer: Alex Taber <aft dot pokemon at gmail dot com>

pkgname=teamviewer
pkgver=14.3.4730
pkgrel=1
pkgdesc='All-In-One Software for Remote Support and Online Meetings'
arch=('i686' 'x86_64' 'armv7h')
url='http://www.teamviewer.com'
license=('custom')
options=('!strip')
provides=('teamviewer')
conflicts=('teamviewer-beta')
# /opt/teamviewer/tv_bin/script/teamviewer_setup checklibs can check deps for each TV component:
# TV_DMN, TV_DESK, TV_GUI
depends=(
	'hicolor-icon-theme'
	'qt5-webkit'
	'qt5-x11extras'
	'qt5-quickcontrols' # Doesn't appear in namcap, won't display UI without it.
)
#depends_x86_64=(
# libdepends:
#	'lib32-libxtst'
#	'lib32-libxinerama'
#	'lib32-libxrandr'
#	'lib32-libxdamage'
#	'lib32-fontconfig'
#	'lib32-libsm')
#depends_i686=()
#depends_armv7h=()
install=teamviewer.install
source_x86_64=("https://dl.tvcdn.de/download/linux/version_${pkgver%%.*}x/teamviewer_${pkgver}_amd64.deb")
source_i686=("https://dl.tvcdn.de/download/linux/version_${pkgver%%.*}x/teamviewer_${pkgver}_i386.deb")
source_armv7h=("https://dl.tvcdn.de/download/linux/version_${pkgver%%.*}x/teamviewer-host_${pkgver}_armhf.deb")
#source_armv7h=("https://dl.tvcdn.de/download/linux/version_${pkgver%%.*}x/teamviewer-host_13.2.13582_armhf.deb")
sha256sums_i686=('ba973e77876dfff2ab4aafc0986513592a13f5d072aa52681c60360e9bf1ca18')
sha256sums_x86_64=('ce0e5aeebb991a8c8fd7e5b86a1f312f568bf5964faa7e34dfbcc036dfcc7bcc')
sha256sums_armv7h=('0268f2f49a24ae956b2b94f220e4292311f34db3001a198137b7ee1b605e612a')

prepare() {
	warning "If the install fails, you need to uninstall previous major version of Teamviewer"
	[ -d data ] && rm -rf data
	mkdir data
	cd data
	for datatar in ../data.tar.*; do
		msg2 "Unpacking $datatar"
		tar -xf $datatar
	done
	sed -i '/function CheckQtQuickControls()/{N;a ls /usr/lib/qt/qml/QtQuick/Controls/qmldir &>/dev/null && return # ArchLinux
}' ./opt/teamviewer/tv_bin/script/teamviewer_setup || msg2 "Patching CheckQtQuickControls failed! Contact maintainer"
	msg2 "Running teamviewer_setup checklibs"
	./opt/teamviewer/tv_bin/script/teamviewer_setup checklibs \
    || msg2 "teamviewer_setup checklibs failed, contact maintainer with /tmp/teamviewerTARLibCheck/DependencyCheck.log" # Currently it always exits 0
}

package() {
	# Install
	warning "If the install fails, you need to uninstall previous major version of Teamviewer"
	cp -dr --no-preserve=ownership ./data/{etc,opt,usr,var} "${pkgdir}"/

	# Additional files
	rm "${pkgdir}"/opt/teamviewer/tv_bin/xdg-utils/xdg-email
	rm -rf "${pkgdir}"/etc/apt
	install -D -m0644 "${pkgdir}"/opt/teamviewer/tv_bin/script/teamviewerd.service \
		"${pkgdir}"/usr/lib/systemd/system/teamviewerd.service
	install -d -m0755 "${pkgdir}"/usr/{share/applications,share/licenses/teamviewer}
	ln -s /opt/teamviewer/License.txt \
		"${pkgdir}"/usr/share/licenses/teamviewer/LICENSE
	if [ "$CARCH" = "x86_64" ] && [ -f "${pkgdir}/opt/teamviewer/tv_bin/script/libdepend" ]; then
		msg2 "Removing libdepend to ditch lib32 dependencies"
		rm "${pkgdir}/opt/teamviewer/tv_bin/script/libdepend"
	fi
}
