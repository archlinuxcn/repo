# Maintainer: Steven De Bondt <egnappah at gmail dot com>

pkgbase=linux-amd
_srcname=linux
gitver=v6.7.9
patchver=20240221.2
patchname=more-uarches-for-kernel-6.1.79-6.8-rc3.patch
pkgver=6.7.v.9
pkgrel=1
arch=('x86_64')
url="https://www.kernel.org/"
license=('GPL2')
makedepends=('xmlto' 'docbook-xsl' 'kmod' 'inetutils' 'bc' 'git' 'libelf' 'lzop' 'gcc>=10.3')
options=('!strip')

source=("git+https://git.kernel.org/pub/scm/linux/kernel/git/stable/linux.git#tag=$gitver"
        # the main kernel config files
        'config.x86_64'
        # standard config files for mkinitcpio ramdisk
        "${pkgbase}.preset"
	# patch from our graysky archlinux colleague
	"https://raw.githubusercontent.com/graysky2/kernel_compiler_patch/$patchver/$patchname"
)
sha256sums=('SKIP'
            #config.x86_64
            'eb991f0e38175a84e655ef9a0aa5c80bac5a1f2a77eab22026f2bd54bd798f9f'
            #.preset file
            '60c6ba602443e94a9eba3aeee9d194027d69bffaa428c6d055348ebf03681b5c'
            #grayskypatch
            '1a3825b790413d09806c9a2115f679be28e434cfcc69c01dc069b634d1e8007a'
)

_kernelname=${pkgbase#linux}

pkgver() {
  echo $pkgver
}

prepare() {
  cd "${_srcname}"
  if [ "${CARCH}" = "x86_64" ]; then
    cat "${srcdir}/config.x86_64" > ./.config
  else
    echo "Sorry, non x86_64 arch not supported."
      exit 2
  fi

  # Implement all packaged patches and reverts.
  msg2 "Implementing custom kernel patches/reverts"
  while read patch; do
   echo "Applying $patch"
   git apply $patch || exit 2
  done <<< $(ls ../*.patch)

  # get kernel version
  msg2 "Preparing kernel"
  yes "" | make prepare

  # load configuration
  msg2 "Preparing config"
  # Configure the kernel. Replace the line below with one of your choice.
  #make menuconfig # CLI menu for configuration
  #make nconfig # new CLI menu for configuration
  #make xconfig # X-based configuration
  #make oldconfig # using old config from previous kernel version
  make olddefconfig # old config from previous kernel, defaults for new options
  # ... or manually edit .config
}

build() {
  cd "${_srcname}"

  #Force zenv4 architecture optimisation and other optimisations.
  make ${MAKEFLAGS} LOCALVERSION= bzImage modules KCFLAGS='-march=znver4 -mtune=znver4 -O2 -pipe -fstack-protector-strong'
}

_package() {
  pkgdesc="Linux kernel aimed at the ZNVER4/MZEN4 AMD Ryzen CPU based hardware"
  depends=('coreutils' 'linux-firmware' 'kmod' 'lzop')
  optdepends=('crda: to set the correct wireless channels of your country')
  backup=("etc/mkinitcpio.d/${pkgbase}.preset")

  cd "${_srcname}"

  KARCH=x86

  # get kernel version
  _kernver="$(make LOCALVERSION= kernelrelease)"
  _basekernel=${_kernver%%-*}
  _basekernel=${_basekernel%.*}

  mkdir -p "${pkgdir}"/{lib/modules,lib/firmware,boot}
  make LOCALVERSION= INSTALL_MOD_PATH="${pkgdir}" modules_install

  # install mkinitcpio preset file for kernel
  install -D -m644 "${srcdir}/${pkgbase}.preset" "${pkgdir}/etc/mkinitcpio.d/${pkgbase}.preset"
  sed \
    -e "1s|'linux.*'|'${pkgbase}'|" \
    -e "s|ALL_kver=.*|ALL_kver=\"/boot/vmlinuz-${pkgbase}\"|" \
    -e "s|default_image=.*|default_image=\"/boot/initramfs-${pkgbase}.img\"|" \
    -e "s|fallback_image=.*|fallback_image=\"/boot/initramfs-${pkgbase}-fallback.img\"|" \
    -i "${pkgdir}/etc/mkinitcpio.d/${pkgbase}.preset"

  # remove build link
  rm -f "${pkgdir}"/lib/modules/${_kernver}/build
  # remove the firmware
  rm -rf "${pkgdir}/lib/firmware"

  # move module tree /lib -> /usr/lib
  mkdir -p "${pkgdir}/usr"
  mv "${pkgdir}/lib" "${pkgdir}/usr/"

  # add vmlinux
  install -D -m644 vmlinux "${pkgdir}/usr/lib/modules/${_kernver}/build/vmlinux" 

  # add vmlinuz in /usr/lib/modules/ and info for correct hook triggers
  cp arch/$KARCH/boot/bzImage "${pkgdir}/usr/lib/modules/${_kernver}/vmlinuz"
  echo ${pkgbase} > "${pkgdir}/usr/lib/modules/${_kernver}/pkgbase"

  # add System.map
  install -D -m644 System.map "${pkgdir}/boot/System.map-${_kernver}"
}

_package-headers() {
  pkgdesc="Header files and scripts for building modules for Linux kernel aimed at the ZNVER4/MZEN4 AMD CPU based hardware"

  install -dm755 "${pkgdir}/usr/lib/modules/${_kernver}"

  cd "${_srcname}"
  install -D -m644 Makefile \
    "${pkgdir}/usr/lib/modules/${_kernver}/build/Makefile"
  install -D -m644 kernel/Makefile \
    "${pkgdir}/usr/lib/modules/${_kernver}/build/kernel/Makefile"
  install -D -m644 .config \
    "${pkgdir}/usr/lib/modules/${_kernver}/build/.config"

  mkdir -p "${pkgdir}/usr/lib/modules/${_kernver}/build/include"

  for i in $(ls include/); do
    cp -a include/${i} "${pkgdir}/usr/lib/modules/${_kernver}/build/include/"
  done

  # copy arch includes for external modules
  mkdir -p "${pkgdir}/usr/lib/modules/${_kernver}/build/arch/x86"
  cp -a arch/x86/include "${pkgdir}/usr/lib/modules/${_kernver}/build/arch/x86/"

  # copy files necessary for later builds, like nvidia and vmware
  cp Module.symvers "${pkgdir}/usr/lib/modules/${_kernver}/build"
  cp -a scripts "${pkgdir}/usr/lib/modules/${_kernver}/build"

  # Make tmpdir for versions
  mkdir -p "${pkgdir}/usr/lib/modules/${_kernver}/build/.tmp_versions"

  # add kernel files to headers
  mkdir -p "${pkgdir}/usr/lib/modules/${_kernver}/build/arch/${KARCH}/kernel"
  cp arch/${KARCH}/Makefile "${pkgdir}/usr/lib/modules/${_kernver}/build/arch/${KARCH}/"
  cp arch/${KARCH}/kernel/asm-offsets.s "${pkgdir}/usr/lib/modules/${_kernver}/build/arch/${KARCH}/kernel/"

  # add dm headers
  mkdir -p "${pkgdir}/usr/lib/modules/${_kernver}/build/drivers/md"
  cp drivers/md/*.h "${pkgdir}/usr/lib/modules/${_kernver}/build/drivers/md"

  # add inotify.h
  mkdir -p "${pkgdir}/usr/lib/modules/${_kernver}/build/include/linux"
  cp include/linux/inotify.h "${pkgdir}/usr/lib/modules/${_kernver}/build/include/linux/"

  # add wireless headers
  mkdir -p "${pkgdir}/usr/lib/modules/${_kernver}/build/net/mac80211/"
  cp net/mac80211/*.h "${pkgdir}/usr/lib/modules/${_kernver}/build/net/mac80211/"

  # copy in Kconfig files
  for i in $(find . -name "Kconfig*"); do
    mkdir -p "${pkgdir}"/usr/lib/modules/${_kernver}/build/`echo ${i} | sed 's|/Kconfig.*||'`
    cp ${i} "${pkgdir}/usr/lib/modules/${_kernver}/build/${i}"
  done

  # Add objtool for CONFIG_STACK_VALIDATION
  mkdir -p "${pkgdir}/usr/lib/modules/${_kernver}/build/tools"
  cp -a tools/objtool "${pkgdir}/usr/lib/modules/${_kernver}/build/tools"

  chown -R root:root "${pkgdir}/usr/lib/modules/${_kernver}/build"
  find "${pkgdir}/usr/lib/modules/${_kernver}/build" -type d -exec chmod 755 {} \;

  # strip scripts directory
  find "${pkgdir}/usr/lib/modules/${_kernver}/build/scripts" -type f -perm -u+w 2>/dev/null | while read binary ; do
    case "$(file -bi "${binary}")" in
      *application/x-sharedlib*) # Libraries (.so)
        /usr/bin/strip ${STRIP_SHARED} "${binary}";;
      *application/x-archive*) # Libraries (.a)
        /usr/bin/strip ${STRIP_STATIC} "${binary}";;
      *application/x-executable*) # Binaries
        /usr/bin/strip ${STRIP_BINARIES} "${binary}";;
    esac
  done

  # remove unneeded architectures
  while read modarch; do
   rm -rf $modarch
  done <<< $(find "${pkgdir}"/usr/lib/modules/${_kernver}/build/arch/ -maxdepth 1 -mindepth 1 -type d | grep -v /x86$)

}

pkgname=("${pkgbase}" "${pkgbase}-headers")
for _p in ${pkgname[@]}; do
  eval "package_${_p}() {
    $(declare -f "_package${_p#${pkgbase}}")
    _package${_p#${pkgbase}}
  }"
done
