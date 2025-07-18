# Maintainer: Oleksandr Natalenko aka post-factum <oleksandr@natalenko.name>

pkgbase="linux-pf"
_suffix=""
pkgname=(${pkgbase}${_suffix} ${pkgbase}-headers${_suffix})
_rev=26abbca142851f9a979604851e13ceac1e03fa32
pkgver=6.15.pf6
pkgrel=1
pkgdesc="pf-kernel"
arch=(x86_64)
url=https://pfkernel.natalenko.name
license=(GPL-2.0-only)
makedepends=(bc cpio gettext libelf pahole perl python rust rust-bindgen rust-src tar xz)
options=(!debug !strip)
source=(https://codeberg.org/pf-kernel/linux/archive/${_rev}.tar.gz
		config)
b2sums=(SKIP
		'412ff0c11697f377f6ef1551e67078c94aaf1cb6e8a4014e706e1c661541a3b579c83fb847280638b6a6a5f9fc508e61439b85ca6c80e5ac58069972da8cd158')

export KBUILD_BUILD_HOST=archlinux
export KBUILD_BUILD_USER=${pkgbase}
export KBUILD_BUILD_TIMESTAMP="$(date -Ru${SOURCE_DATE_EPOCH:+d @$SOURCE_DATE_EPOCH})"
# export KBUILD_X86_64_ISA_LEVEL=

prepare() {
	cd linux

	echo "Setting config..."
	cp ../config .config

	if [[ -n ${KBUILD_X86_64_ISA_LEVEL} && ${KBUILD_X86_64_ISA_LEVEL} != 1 ]]; then
		echo "x86_64 ISA level to be used: ${KBUILD_X86_64_ISA_LEVEL}"
		scripts/config --set-val X86_64_ISA_LEVEL ${KBUILD_X86_64_ISA_LEVEL}
	fi

	make olddefconfig
	diff -u ../config .config || :

	make -s kernelrelease >version
	echo "Prepared ${pkgdesc} version $(<version)"
}

build() {
	cd linux

	__nthreads=$(($(nproc) + 1))
	make -j${__nthreads} all
	make -C tools/bpf/bpftool vmlinux.h feature-clang-bpf-co-re=1
}

_package() {
	pkgdesc="The ${pkgdesc} and modules"
	depends=(coreutils initramfs kmod)
	optdepends=('ksmbd-tools: userspace tools for the ksmbd kernel SMB server'
				'linux-firmware: firmware images needed for some devices'
				'scx-scheds: to use sched-ext schedulers'
				'v4l2loopback-utils: v4l2-loopback device utilities'
				'wireless-regdb: to set the correct wireless channels of your country')
	provides=(linux-pf KSMBD-MODULE NTFS3-MODULE NTSYNC-MODULE OVPN-MODULE V4L2LOOPBACK-MODULE VIRTUALBOX-GUEST-MODULES WIREGUARD-MODULE)
	replaces=(virtualbox-guest-modules-arch wireguard-arch)

	cd linux
	local modulesdir="${pkgdir}"/usr/lib/modules/$(<version)

	echo "Installing boot image..."
	# systemd expects to find the kernel here to allow hibernation
	# https://github.com/systemd/systemd/commit/edda44605f06a41fb86b7ab8128dcf99161d2344
	install -Dm644 "$(make -s image_name)" "${modulesdir}"/vmlinuz

	# Used by mkinitcpio to name the kernel
	echo ${pkgbase} | install -Dm644 /dev/stdin "${modulesdir}"/pkgbase

	echo "Installing modules..."
	ZSTD_CLEVEL=19 make INSTALL_MOD_PATH="${pkgdir}"/usr INSTALL_MOD_STRIP=1 \
		DEPMOD=/doesnt/exist modules_install  # Suppress depmod

	# remove build link
	rm "${modulesdir}"/build
}

_package-headers() {
	pkgdesc="Headers and scripts for building modules for the ${pkgdesc}"
	depends=(pahole)
	provides=(linux-pf-headers)

	cd linux
	local builddir="${pkgdir}"/usr/lib/modules/$(<version)/build

	echo "Installing build files..."
	install -Dt "${builddir}" -m644 .config Makefile Module.symvers System.map \
		version vmlinux tools/bpf/bpftool/vmlinux.h
	install -Dt "${builddir}"/kernel -m644 kernel/Makefile
	install -Dt "${builddir}"/arch/x86 -m644 arch/x86/Makefile
	cp -t "${builddir}" -a scripts
	ln -srt "${builddir}" "${builddir}"/scripts/gdb/vmlinux-gdb.py

	# required when STACK_VALIDATION is enabled
	install -Dt "${builddir}"/tools/objtool tools/objtool/objtool

	# required when DEBUG_INFO_BTF_MODULES is enabled
	install -Dt "${builddir}"/tools/bpf/resolve_btfids tools/bpf/resolve_btfids/resolve_btfids

	echo "Installing headers..."
	cp -t "${builddir}" -a include
	cp -t "${builddir}"/arch/x86 -a arch/x86/include
	install -Dt "${builddir}"/arch/x86/kernel -m644 arch/x86/kernel/asm-offsets.s

	install -Dt "${builddir}"/drivers/md -m644 drivers/md/*.h
	install -Dt "${builddir}"/net/mac80211 -m644 net/mac80211/*.h

	# https://bugs.archlinux.org/task/13146
	install -Dt "${builddir}"/drivers/media/i2c -m644 drivers/media/i2c/msp3400-driver.h

	# https://bugs.archlinux.org/task/20402
	install -Dt "${builddir}"/drivers/media/usb/dvb-usb -m644 drivers/media/usb/dvb-usb/*.h
	install -Dt "${builddir}"/drivers/media/dvb-frontends -m644 drivers/media/dvb-frontends/*.h
	install -Dt "${builddir}"/drivers/media/tuners -m644 drivers/media/tuners/*.h

	# https://bugs.archlinux.org/task/71392
	install -Dt "${builddir}"/drivers/iio/common/hid-sensors -m644 drivers/iio/common/hid-sensors/*.h

	echo "Installing Kconfig files..."
	find . -name 'Kconfig*' -exec install -Dm644 {} "${builddir}/{}" \;

	echo "Installing Rust files..."
	install -Dt "${builddir}"/rust -m644 rust/*.rmeta
	install -Dt "${builddir}"/rust rust/*.so

	echo "Installing unstripped VDSO..."
	make INSTALL_MOD_PATH="${pkgdir}"/usr vdso_install \
		link=  # Suppress build-id symlinks

	# remove unneeded architectures
	local arch
	for arch in "${builddir}"/arch/*/; do
		[[ ${arch} = */x86/ ]] && continue
		echo "Removing $(basename "${arch}")"
		rm -r "${arch}"
	done

	echo "Removing documentation..."
	rm -r "${builddir}"/Documentation

	echo "Removing broken symlinks..."
	find -L "${builddir}" -type l -printf 'Removing %P\n' -delete

	echo "Removing loose objects..."
	find "${builddir}" -type f -name '*.o' -printf 'Removing %P\n' -delete

	echo "Stripping build tools..."
	local file
	while read -rd '' file; do
		case "$(file -Sib "${file}")" in
			application/x-sharedlib\;*)      # Libraries (.so)
				strip -v ${STRIP_SHARED} "${file}" ;;
			application/x-archive\;*)        # Libraries (.a)
				strip -v ${STRIP_STATIC} "${file}" ;;
			application/x-executable\;*)     # Binaries
				strip -v ${STRIP_BINARIES} "${file}" ;;
			application/x-pie-executable\;*) # Relocatable binaries
				strip -v ${STRIP_SHARED} "${file}" ;;
		esac
	done < <(find "${builddir}" -type f -perm -u+x ! -name vmlinux -print0)

	echo "Stripping vmlinux..."
	strip -v ${STRIP_STATIC} "${builddir}"/vmlinux

	echo "Adding symlink..."
	mkdir -p "${pkgdir}"/usr/src
	ln -sr "${builddir}" "${pkgdir}"/usr/src/${pkgbase}
}

for _p in ${pkgname[@]}; do
	if [[ -n ${_suffix} ]]; then
		_i=$(echo ${_p} | sed "s/${_suffix}//g")
	else
		_i=${_p}
	fi
	eval "package_${_i}${_suffix}() {
		$(declare -f "_package${_i#${pkgbase}}")
		_package${_i#${pkgbase}}
	}"
done
