# Maintainer: Christian Hesse <mail@eworm.de>

pkgbase=vmware-horizon-client
pkgname=('vmware-horizon-client'
	'vmware-horizon-rtav'
	'vmware-horizon-smartcard'
	'vmware-horizon-usb'
	'vmware-horizon-virtual-printing'
	'vmware-horizon-tsdr'
	'vmware-horizon-mmr'
	'vmware-horizon-docs')
pkgver=4.5.0
_build=5650368
_cart='CART17Q2'
_docver=45
pkgrel=6
pkgdesc='VMware Horizon Client connect to VMware Horizon virtual desktop'
arch=('i686' 'x86_64')
url='https://my.vmware.com/web/vmware/info/slug/desktop_end_user_computing/vmware_horizon_clients/4_0'
license=('custom')
makedepends=('libxslt')
source=('http://sources.gentoo.org/cgi-bin/viewvc.cgi/gentoo-x86/eclass/vmware-bundle.eclass'
	"https://www.vmware.com/pdf/horizon-view/horizon-client-linux-${_docver}-document.pdf"
	'vmware-horizon-usb'
	'vmware-horizon-usb.service'
	'vmware-horizon-virtual-printing.service')
source_x86_64=("${pkgbase}-${pkgver}-${_build}-x86_64.bundle::https://download3.vmware.com/software/view/viewclients/${_cart}/VMware-Horizon-Client-${pkgver}-${_build}.x64.bundle"
	'http://archive.ubuntu.com/ubuntu/pool/main/g/glibmm2.4/libglibmm-2.4-1c2a_2.39.93-0ubuntu1_amd64.deb')
source_i686=("${pkgbase}-${pkgver}-${_build}-i686.bundle::https://download3.vmware.com/software/view/viewclients/${_cart}/VMware-Horizon-Client-${pkgver}-${_build}.x86.bundle"
	'http://archive.ubuntu.com/ubuntu/pool/main/g/glibmm2.4/libglibmm-2.4-1c2a_2.39.93-0ubuntu1_i386.deb')
sha256sums=('d8794c22229afdeb698dae5908b7b2b3880e075b19be38e0b296bb28f4555163'
            '9f34fd9b3d1ef5822f3927829d6f28db6197d72896bb4a1108233db3731f064c'
            '008b60ebf45f7d1e033c8ad8ce1688d5e1c59fc0668493067fb89b563b1dc00f'
            'f0944ca74a44292e7f853792335d3bbd1a89a1d4964d6d74a7e9485a8b068b0b'
            'e47e770a1e19ed321de7c2765b2d682f59ac466aef92b2e4ea5e65cacf56de36')
sha256sums_x86_64=('70281bcac267e72b816e62cb0742c8707a5f29dccae977613d6b837e3248d429'
                   'fe0c8d8a71ab4261f73469871c06665941a04c2e26c71cd6cbb3c2dd42faa2b9')
sha256sums_i686=('2fa5bac1445c3619a295b1f64ddc0432da3d6d9a4f1930885fcdc6fd111bd5df'
                 'fa5d97b7514574b87b2e0e3b2f8638a56d68a6f57fdc5128e33b7b018b4a12dd')

# VMware bundles old versions of openssl. Usually we can use system openssl.
# If things break because VMware relies on legacy or buggy code you can use
# bundled openssl.
_USE_BUNDLED_OPENSSL=1

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

	source "${srcdir}/vmware-bundle.eclass"

	for bundle in "${pkgname[@]}" vmware-horizon-pcoip; do
	        vmware-bundle_extract-bundle-component "${srcdir}/${pkgbase}-${pkgver}-${_build}-${CARCH}.bundle" "${bundle}" "${srcdir}/extract/${bundle}"
	done
}

build() {
	cd "${srcdir}/extract/"

	# This is a dirty hack, but it works.
	# Change dynamic section in ELF files to fix dynamic linking.
	# Make sure the length is not changed!
	#
	# for system openssl:
	#	libssl.so.1.0.[12] -> libssl.so.1.0.0
	#	libcrypto.so.1.0.[12] -> libcrypto.so.1.0.0
	#
	# for bundled openssl - we use uncommon name to make sure no other application will care:
	#	libssl.so.1.0.[12] -> libssl-vmw.so.0
	#	libcrypto.so.1.0.[12] -> libcrypto-vmw.so.0

	for bundle in "${pkgname[@]}" vmware-horizon-pcoip; do
		# not in bundle
		[ "${bundle}" == 'vmware-horizon-docs' ] && continue
		
		for FILE in $(find "${bundle}" -type f); do
			# executables and libraries only
			file --mime "${FILE}" | egrep -q "(application/x-(executable|sharedlib)|text/x-shellscript)" || continue

			# make executable
			chmod +x "${FILE}"

			# ELF executables and libraries only
			file --mime "${FILE}" | egrep -q "application/x-(executable|sharedlib)" || continue

			# even openssl 1.0.[12].x has library file names ending in .so.1.0.0
			if [ ${_USE_BUNDLED_OPENSSL:=0} -eq 0 ]; then
				sed -i -e 's/libssl.so.1.0.[12]/libssl.so.1.0.0/' \
					-e 's/libcrypto.so.1.0.[12]/libcrypto.so.1.0.0/' \
					"${FILE}"
			else
				# Some files link against openssl...
				# Use the bundled version there.
				sed -i -e 's/libssl.so.1.0.[012]/libssl-vmw.so.0/' \
					-e 's/libcrypto.so.1.0.[012]/libcrypto-vmw.so.0/' \
					"${FILE}"
			fi
		done
	done

	# now that we fixed dynamic linking...
	# ... let's finish the hack
	if [ ${_USE_BUNDLED_OPENSSL:=0} -eq 0 ]; then
		rm -f "${srcdir}"/extract/vmware-horizon-pcoip/pcoip/lib/vmware/lib{crypto,ssl}.so.1.0.2

		ln -sf ../libcrypto.so.1.0.0 "${srcdir}"/extract/vmware-horizon-pcoip/pcoip/lib/vmware/libcrypto.so.1.0.0
		ln -sf ../libssl.so.1.0.0 "${srcdir}"/extract/vmware-horizon-pcoip/pcoip/lib/vmware/libssl.so.1.0.0
	else
		rename -- '.so.1.0.2' '-vmw.so.0' \
			"${srcdir}"/extract/vmware-horizon-pcoip/pcoip/lib/vmware/lib{crypto,ssl}.so.1.0.2
	fi

	sed -i '/Name=/a Comment=Connect to VMware Horizon View virtual machines' \
		"${srcdir}"/extract/vmware-horizon-client/share/applications/vmware-view.desktop
}

package_vmware-horizon-client() {
	conflicts=('vmware-view-open-client' 'vmware-view-open-client-beta' 'vmware-view-client'
		'vmware-horizon-pcoip')
	replaces=('vmware-horizon-pcoip')
	depends=('gnome-icon-theme' 'gtk2' 'libpng12' 'libudev0-shim' 'libxml2' 'libxss'
		'libxtst' 'openssl')
	optdepends=('alsa-lib: audio support via alsa'
		'freerdp: RDP remote desktop connections'
		'libpulse: audio support via pulse sound server'
		'rdesktop: RDP remote desktop connections'
		'vmware-horizon-rtav: Real-Time Audio-Video (webcam and audio-in)'
		'vmware-horizon-smartcard: smartcard authentication'
		'vmware-horizon-usb: USB device redirection'
		'vmware-horizon-virtual-printing: virtual printing'
		'vmware-horizon-tsdr: folder sharing'
		'vmware-horizon-mmr: multimedia redirection')
	install=vmware-horizon-client.install

	cd "${srcdir}/extract/vmware-horizon-client/"

	mkdir -p "${pkgdir}/usr/"
	cp -a bin/ "${pkgdir}/usr/"
	cp -a lib/ "${pkgdir}/usr/"
	cp -a share/ "${pkgdir}/usr/"

	mkdir -p "${pkgdir}/usr/share/doc/"
	cp -a doc/ "${pkgdir}/usr/share/doc/vmware-horizon-client"
	cp -a debug/ "${pkgdir}/usr/share/doc/vmware-horizon-client/"

	cd "${srcdir}/extract/vmware-horizon-pcoip/"

	mkdir -p "${pkgdir}/usr/"
	cp -a pcoip/lib/ "${pkgdir}/usr/"
	cp -a pcoip/bin/ "${pkgdir}/usr/"
}

package_vmware-horizon-rtav() {
	pkgdesc='VMware Horizon Client connect to VMware Horizon virtual desktop - Real-Time Audio-Video (webcam and audio-in)'
	depends=('vmware-horizon-client')
	cd "${srcdir}/extract/vmware-horizon-rtav/"

	mkdir -p "${pkgdir}/usr/"
	cp -a lib/ "${pkgdir}/usr/"
}

package_vmware-horizon-smartcard() {
	pkgdesc='VMware Horizon Client connect to VMware Horizon virtual desktop - smartcard authentication'
	depends=('vmware-horizon-client' 'pcsclite')

	cd "${srcdir}/extract/vmware-horizon-smartcard/"

	mkdir -p "${pkgdir}/usr/"
	cp -a lib/ "${pkgdir}/usr/"
}

package_vmware-horizon-usb() {
	pkgdesc='VMware Horizon Client connect to VMware Horizon virtual desktop - USB device redirection'
	depends=('vmware-horizon-client')
	install=vmware-horizon-usb.install

	cd "${srcdir}/extract/vmware-horizon-usb/"

	mkdir -p "${pkgdir}/usr/lib/vmware/view/"
	cp -a bin/ "${pkgdir}/usr/lib/vmware/view/usb"
	cp -a lib/ "${pkgdir}/usr/"

	install -D -m0755 "${srcdir}/vmware-horizon-usb" "${pkgdir}/usr/lib/systemd/scripts/vmware-horizon-usb"
	install -D -m0644 "${srcdir}/vmware-horizon-usb.service" "${pkgdir}/usr/lib/systemd/system/vmware-horizon-usb.service"
}

package_vmware-horizon-virtual-printing() {
	pkgdesc='VMware Horizon Client connect to VMware Horizon virtual desktop - virtual printing'
	depends=('vmware-horizon-client' 'openssl098' 'libcups')
	install=vmware-horizon-virtual-printing.install

	cd "${srcdir}/extract/vmware-horizon-virtual-printing/"

	mkdir -p "${pkgdir}/usr/bin/"

	case ${CARCH} in
		x86_64)
			cp -a bin/x86_64-linux-NOSSL/thnu* "${pkgdir}/usr/bin/"
			install -D -m0755 bin/x86_64-linux-NOSSL/.thnumod "${pkgdir}/etc/thnuclnt/.thnumod"
			;;
		i686)
			cp -a bin/i586-linux-NOSSL/thnu* "${pkgdir}/usr/bin/"
			install -D -m0755 bin/i586-linux-NOSSL/.thnumod "${pkgdir}/etc/thnuclnt/.thnumod"
			;;
	esac

	install -D -m0755 lib/tprdp.so "${pkgdir}/usr/lib/vmware/rdpvcbridge/tprdp.so"

	install -D -m0644 bin/conf/thnuclnt.convs "${pkgdir}/usr/share/cups/mime/thnuclnt.convs"
	install -D -m0644 bin/conf/thnuclnt.types "${pkgdir}/usr/share/cups/mime/thnuclnt.types"

	install -D -m0644 "${srcdir}/vmware-horizon-virtual-printing.service" \
		"${pkgdir}/usr/lib/systemd/system/vmware-horizon-virtual-printing.service"
}

package_vmware-horizon-tsdr() {
	pkgdesc='VMware Horizon Client connect to VMware Horizon virtual desktop - folder sharing'
	depends=('vmware-horizon-client' 'glibmm')

	# this is from libglibmm package from Ubuntu
	bsdtar xf data.tar.xz
	mkdir -p "${pkgdir}/usr/lib/vmware/"
	cp -a $(find usr/lib/ -name "libglibmm-2.4.so.1*") "${pkgdir}/usr/lib/vmware/"

	cd "${srcdir}/extract/vmware-horizon-tsdr/"

	mkdir -p "${pkgdir}/usr/"
	cp -a lib/ "${pkgdir}/usr/"
}

package_vmware-horizon-mmr() {
	pkgdesc='VMware Horizon Client connect to VMware Horizon virtual desktop - multimedia redirection'
	depends=('vmware-horizon-client' 'gstreamer0.10-base' 'libpulse')

	cd "${srcdir}/extract/vmware-horizon-mmr/"

	mkdir -p "${pkgdir}/usr/"
	cp -a lib/ "${pkgdir}/usr/"
}

package_vmware-horizon-docs() {
	pkgdesc='VMware Horizon Client connect to VMware Horizon virtual desktop - documentation'
	depends=('vmware-horizon-client')

	install -D -m0644 horizon-client-linux-${_docver}-document.pdf \
		"${pkgdir}/usr/share/doc/vmware-horizon/horizon-client-linux-${_docver}-document.pdf"
}

