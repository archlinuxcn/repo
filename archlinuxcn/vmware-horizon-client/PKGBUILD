# Maintainer: Christian Hesse <mail@eworm.de>

pkgbase=vmware-horizon-client
pkgname=(
  'vmware-horizon-client'
  'vmware-horizon-html5mmr'
  'vmware-horizon-integrated-printing'
  'vmware-horizon-mmr'
  'vmware-horizon-rtav'
  'vmware-horizon-smartcard'
  'vmware-horizon-tsdr'
  'vmware-horizon-usb')
_bundled_with_client=(
  'vmware-horizon-hosted-apps'
  'vmware-horizon-pcoip')
# Extract anyway so we can find messing components... :-p
_unused_components=(
  'vmware-horizon-media-provider'
  'vmware-horizon-scannerclient'
  'vmware-horizon-serialportclient'
  'vmware-horizon-url-redirection')
pkgver=2212
_build1=8.8.0
_build2=21079016
_cart="CART23FQ4_LIN64_${pkgver/./_}"
pkgrel=1
pkgdesc='VMware Horizon Client connect to VMware Horizon virtual desktop'
arch=('x86_64')
url='https://www.vmware.com/go/viewclients'
license=('custom')
makedepends=('libxslt' 'patchelf' 'librsvg')
source=("${pkgbase}-${pkgver}-${_build1}-${_build2}-x86_64.bundle::https://download3.vmware.com/software/${_cart}/VMware-Horizon-Client-${pkgver}-${_build1}-${_build2}.x64.bundle"
        "vmware-bundle.eclass-${pkgver}::https://gitweb.gentoo.org/proj/vmware.git/plain/eclass/vmware-bundle.eclass"
        'vmware-horizon-usb'
        'vmware-horizon-usb.service'
        'vmware-horizon.svg')
sha256sums=('d5d8e175479120cab97e1789a30e90e9cd1f0f963821be9de247198897abd688'
            'd6863e92b891fc506fc8e81714a47ca3f9f74b7fe68bdf48be058d5e0d433033'
            '008b60ebf45f7d1e033c8ad8ce1688d5e1c59fc0668493067fb89b563b1dc00f'
            'a897c1b9e8928fc222880ebbfc7bb6aff940bff4acf4e4e0cd4002fff81c7226'
            '0fe0b3d1c253361321e96d50997eaf151d311c55c62c73e8ea5007f9ae4448cb')

# We need these functions for the Gentoo eclass...
ebegin() {
	echo -n "Begin ${1}: "
}
eend() {
	echo 'done'
}

prepare() {
	# We need this variable for the Gentoo eclass...
	export T="${srcdir}"

	source "${srcdir}/vmware-bundle.eclass-${pkgver}"

	for bundle in "${pkgname[@]}" "${_bundled_with_client[@]}" "${_unused_components[@]}"; do
	        vmware-bundle_extract-bundle-component "${srcdir}/${pkgbase}-${pkgver}-${_build1}-${_build2}-${CARCH}.bundle" "${bundle}" "${srcdir}/extract/${bundle}"
	done

	# remove legacy stuff
	find "${srcdir}/extract/" -name 'legacy' -print0 | xargs -0 rm -rf
}

build() {
	cd "${srcdir}/extract/"

	for bundle in "${pkgname[@]}" "${_bundled_with_client[@]}"; do
		for FILE in $(find "${bundle}" -type f); do
			# executables and libraries only
			file --mime "${FILE}" | grep -Eq "(application/x-(pie-)?(executable|sharedlib)|text/x-shellscript)" || continue

			# make executable
			chmod +x "${FILE}"
		done
	done

	# remove rpath to fix dynamic linking...
	for LIB in ${srcdir}/extract/vmware-horizon-pcoip/lib/vmware/lib*.so*; do
		patchelf --remove-rpath "${LIB}"
	done

	# remove keymap files, depend on vmware-keymaps instead
	rm -rf "${srcdir}"/extract/vmware-horizon-pcoip/lib/vmware/xkeymap/

	# remove png icon, we install svg and rendered pngs
	sed -i -e '/Name=/a Comment=Connect to VMware Horizon View virtual machines' -e '/^Icon=/c Icon=vmware-horizon' \
		"${srcdir}"/extract/vmware-horizon-client/share/applications/vmware-view.desktop
	rm -r "${srcdir}"/extract/vmware-horizon-client/share/{icons,pixmaps}/
}

package_vmware-horizon-client() {
	conflicts=('vmware-view-open-client' 'vmware-view-open-client-beta' 'vmware-view-client'
		'vmware-horizon-pcoip' 'vmware-horizon-teams-optimization')
	replaces=('vmware-horizon-pcoip' 'vmware-horizon-teams-optimization')
	depends=('binutils' 'expat' 'ffmpeg4.4' 'glib2' 'gtk3' 'libudev0-shim' 'libxml2' 'libxss'
		'libxtst' 'openssl' 'vmware-keymaps')
	optdepends=('alsa-lib: audio support via alsa'
		'freerdp: RDP remote desktop connections'
		'libpulse: audio support via pulse sound server'
		'rdesktop: RDP remote desktop connections'
		'vmware-horizon-html5mmr: HTML5 MultiMedia Redirection'
		'vmware-horizon-integrated-printing: integrated printing'
		'vmware-horizon-mmr: MultiMedia Redirection'
		'vmware-horizon-rtav: Real-Time Audio-Video (webcam and audio-in)'
		'vmware-horizon-smartcard: smartcard authentication'
		'vmware-horizon-tsdr: folder sharing'
		'vmware-horizon-usb: USB device redirection')
	install=vmware-horizon-client.install

	cd "${srcdir}/extract/vmware-horizon-client/"

	mkdir -p "${pkgdir}/usr/"
	cp -a 'bin/' "${pkgdir}/usr/"
	cp -a 'lib/' "${pkgdir}/usr/"
	cp -a 'share/' "${pkgdir}/usr/"

	mkdir -p "${pkgdir}/usr/share/doc/"
	cp -a 'doc/' "${pkgdir}/usr/share/doc/vmware-horizon-client"

	cd "${srcdir}/extract/vmware-horizon-pcoip/"

	mkdir -p "${pkgdir}/usr/"
	cp -a 'lib/' "${pkgdir}/usr/"

	cd "${srcdir}/extract/vmware-horizon-hosted-apps/"

	mkdir -p "${pkgdir}/usr/"
	cp -a 'lib/' "${pkgdir}/usr/"

	for LIB in 'libavcodec.so.58' 'libavutil.so.56'; do
		for I in $(find "${pkgdir}/usr/lib/vmware/view/" -name "${LIB}") "${pkgdir}/usr/lib/vmware/view/${LIB}"; do
			ln --symbolic --force --relative "/usr/lib/${LIB}" "${I}"
		done
	done

	install -D -m0644 "${srcdir}/vmware-horizon.svg" "${pkgdir}/usr/share/icons/hicolor/scalable/vmware-horizon.svg"
	for SIZE in 16 24 32 48 64 96 128; do
		install -d "${pkgdir}/usr/share/icons/hicolor/${SIZE}x${SIZE}/apps/"
		rsvg-convert -w "${SIZE}" -h "${SIZE}" "${srcdir}/vmware-horizon.svg" \
			-o "${pkgdir}/usr/share/icons/hicolor/${SIZE}x${SIZE}/apps/vmware-horizon.png"
	done
}

package_vmware-horizon-html5mmr() {
	pkgdesc='VMware Horizon Client connect to VMware Horizon virtual desktop - HTML5 MultiMedia Redirection'
	depends=('vmware-horizon-client')

	cd "${srcdir}/extract/vmware-horizon-html5mmr/"

	mkdir -p "${pkgdir}/usr/"
	cp -a 'lib/' "${pkgdir}/usr/"
}

package_vmware-horizon-integrated-printing() {
	pkgdesc='VMware Horizon Client connect to VMware Horizon virtual desktop - integrated printing'
	depends=('vmware-horizon-client' 'libcups' 'zlib')
	conflicts=('vmware-horizon-virtual-printing')
	replaces=('vmware-horizon-virtual-printing')

	cd "${srcdir}/extract/vmware-horizon-integrated-printing/"

	mkdir -p "${pkgdir}/usr/"
	cp -a 'lib/' "${pkgdir}/usr/"
}

package_vmware-horizon-mmr() {
	pkgdesc='VMware Horizon Client connect to VMware Horizon virtual desktop - multimedia redirection'
	depends=('vmware-horizon-client' 'gst-plugins-base' 'libpulse' 'libxml2' 'glib2')
	optdepends=('gstreamer-vaapi: MMR with Intel VAAPI'
	            'gst-plugins-bad: MMR with NVIDIA VDPAU')

	cd "${srcdir}/extract/vmware-horizon-mmr/"

	mkdir -p "${pkgdir}/usr/"
	cp -a 'lib/' "${pkgdir}/usr/"
}

package_vmware-horizon-rtav() {
	pkgdesc='VMware Horizon Client connect to VMware Horizon virtual desktop - Real-Time Audio-Video (webcam and audio-in)'
	depends=('vmware-horizon-client' 'gcc-libs' 'libutil-linux' 'zlib' 'glib2')

	cd "${srcdir}/extract/vmware-horizon-rtav/"

	mkdir -p "${pkgdir}/usr/"
	cp -a 'lib/' "${pkgdir}/usr/"
}

package_vmware-horizon-smartcard() {
	pkgdesc='VMware Horizon Client connect to VMware Horizon virtual desktop - smartcard authentication'
	depends=('vmware-horizon-client' 'pcsclite' 'glib2')

	cd "${srcdir}/extract/vmware-horizon-smartcard/"

	mkdir -p "${pkgdir}/usr/"
	cp -a 'lib/' "${pkgdir}/usr/"
}

package_vmware-horizon-tsdr() {
	pkgdesc='VMware Horizon Client connect to VMware Horizon virtual desktop - folder sharing'
	depends=('vmware-horizon-client' 'glibmm' 'glib2')

	cd "${srcdir}/extract/vmware-horizon-tsdr/"

	mkdir -p "${pkgdir}/usr/"
	cp -a 'lib/' "${pkgdir}/usr/"
}

package_vmware-horizon-usb() {
	pkgdesc='VMware Horizon Client connect to VMware Horizon virtual desktop - USB device redirection'
	depends=('vmware-horizon-client' 'glib2')
	install=vmware-horizon-usb.install

	cd "${srcdir}/extract/vmware-horizon-usb/"

	mkdir -p "${pkgdir}/usr/lib/vmware/view/"
	cp -a 'bin/' "${pkgdir}/usr/lib/vmware/view/usb"
	cp -a 'lib/' "${pkgdir}/usr/"

	install -D -m0755 "${srcdir}/vmware-horizon-usb" "${pkgdir}/usr/lib/systemd/scripts/vmware-horizon-usb"
	install -D -m0644 "${srcdir}/vmware-horizon-usb.service" "${pkgdir}/usr/lib/systemd/system/vmware-horizon-usb.service"
}
