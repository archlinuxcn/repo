# Maintainer:  Chris Severance aur.severach aATt spamgourmet dott com
# Contributor: Alex Taber <aft dot pokemon at gmail dot com>
# Contributor: Louis Tim Larsen <louis(a)louis.dk>
# Contributor: Ignacio <nachohc89 at gmail dot com>
# Contributor: Gun Onen <brookline653 at yahoo dot com>
# Contributor: Christian Hesse <mai at eworm dot de>
# Contributor: Yakir Sitbon <kingyes1 at gmail dot com>
# Contributor: Alucryd <alucryd at gmail dot com>
# Contributor: Stas S <whats_up at tut dot by>
# Contributor: Hilinus <itahilinus at hotmail dot it>

_opt_RPM=0

set -u
pkgname=teamviewer
pkgname+='-beta'
pkgver=13.2.26559
pkgrel=1
pkgdesc='All-In-One Software for Remote Support and Online Meetings'
arch=('i686' 'x86_64' 'armv7h')
url='http://www.teamviewer.com'
license=('custom')
options=('!strip')
provides=("teamviewer=${pkgver%%.*}")
conflicts=('teamviewer')
depends=(
	'qt5-base'
	'qt5-declarative'
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
sha256sums_i686=('52adf3cebcb32b88a0290de6a0071fd7ced4619d810c483128a662f05c7e8e84')
sha256sums_x86_64=('ad9820118b18b66bd31552c30fd8965436ac3c4ffb733ec9d8a22db5b6d193b1')
sha256sums_armv7h=('c7083c0fed10350c1f0893daa562422473d74e6a57727969068b1c6fd4d54151')

if [ "${_opt_RPM}" -ne 0 ]; then
  source_x86_64=("${source_x86_64[@]//_amd64.deb/.x86_64.rpm}")
  source_i686=("${source_i686[@]//_i386.deb/.i686.rpm}")
  source_armv7h=("${source_armv7h[@]//_armhf.deb/.armv7hl.rpm}")
fi

prepare() {
	warning "If the install fails, you need to uninstall previous major version of Teamviewer"
	local datatar
	shopt -s nullglob
	for datatar in data.tar.*; do
		msg2 "Unpacking $datatar"
		tar -xf $datatar
	done
	shopt -u nullglob
	sed -i '/function CheckQtQuickControls()/{N;a ls /usr/lib/qt/qml/QtQuick/Controls/qmldir &>/dev/null && return # ArchLinux
}' ./opt/teamviewer/tv_bin/script/teamviewer_setup || msg2 "Patching CheckQtQuickControls failed! Contact maintainer"
}

check() {
	msg2 "Running teamviewer_setup checklibs"
	if ! ./opt/teamviewer/tv_bin/script/teamviewer_setup checklibs; then
		msg2 "teamviewer_setup checklibs failed, contact maintainer with /tmp/teamviewerTARLibCheck/DependencyCheck.log" # Currently it always exits 0
		false
	fi
}

package() {
	# Install
	warning "If the install fails, you need to uninstall previous major version of Teamviewer"
	cp -dr --no-preserve=ownership {etc,opt,usr,var} "${pkgdir}"/

	# Additional files
	rm "${pkgdir}"/opt/teamviewer/tv_bin/xdg-utils/xdg-email
	rm -rf "${pkgdir}"/etc/apt
	rm -rf "${pkgdir}"/etc/yum.repos.d
	install -D -m0644 "${pkgdir}"/opt/teamviewer/tv_bin/script/teamviewerd.service \
		"${pkgdir}"/usr/lib/systemd/system/teamviewerd.service
	install -d -m0755 "${pkgdir}"/usr/{share/applications,share/licenses/teamviewer}
	ln -s /opt/teamviewer/doc/License.txt \
		"${pkgdir}"/usr/share/licenses/teamviewer/LICENSE
	if [ "$CARCH" = "x86_64" ] && [ -f "${pkgdir}/opt/teamviewer/tv_bin/script/libdepend" ]; then
		msg2 "Removing libdepend to ditch lib32 dependencies"
		rm "${pkgdir}/opt/teamviewer/tv_bin/script/libdepend"
	fi
}
set +u
