pkgname=teamviewer
pkgver=15.37.8
pkgrel=1
pkgdesc='All-In-One Software for Remote Support and Online Meetings'
arch=('i686' 'x86_64' 'armv7h' 'aarch64')
url='http://www.teamviewer.com'
license=('custom')
options=('!strip')
provides=('teamviewer')
conflicts=('teamviewer-beta')
# /opt/teamviewer/tv_bin/script/teamviewer_setup checklibs can check deps for each TV component:
# TV_DMN, TV_DESK, TV_GUI
depends=(
	'hicolor-icon-theme'
	'qt5-x11extras'
	'qt5-quickcontrols' # Doesn't appear in namcap, won't display UI without it.
	'qt5-webengine'
	'qt5-svg'
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
source_x86_64=("https://dl.teamviewer.com/download/linux/version_${pkgver%%.*}x/teamviewer_${pkgver}_amd64.deb")
source_i686=("https://dl.teamviewer.com/download/linux/version_${pkgver%%.*}x/teamviewer_${pkgver}_i386.deb")
source_armv7h=("https://dl.teamviewer.com/download/linux/version_${pkgver%%.*}x/teamviewer_${pkgver}_armhf.deb")
source_aarch64=("https://dl.teamviewer.com/download/linux/version_${pkgver%%.*}x/teamviewer_${pkgver}_arm64.deb")
sha256sums_i686=('fff77cec6421fd1d13777d39e8f89ef607cb2699bb593ce87b37b969499217c7')
sha256sums_x86_64=('2001c7f3f6d8a7ad7263e512750f33c84523bd996ec9d506d60adb2931933c8a')
sha256sums_armv7h=('0a846135b01bd908a29616c2e9b537749c4c41da91c27e85133aaa682f398c45')
sha256sums_aarch64=('f98b6391b20c6f04debec22b18e5ff97d3a2d6de6a79cd965f7271c352bae11f')

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
	# Uncomment to use system's native libraries. This can save around 150MiB of disk space
	#rm -rf "${pkgdir}"/opt/teamviewer/tv_bin/RTlib
}
