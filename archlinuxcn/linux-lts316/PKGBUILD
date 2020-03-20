# Maintainer: Chris Severance aur.severach aATt spamgourmet dott com
# Contributor: James Bunton <jamesbunton@delx.net.au>
# Contributor: Tobias Powalowski <tpowa@archlinux.org>
# Contributor: Thomas Baechler <thomas@archlinux.org>

set -u
pkgbase="linux-lts316"
_srcname="linux-3.16"
pkgver="3.16.82"
pkgrel='1'
arch=('i686' 'x86_64')
url="https://www.kernel.org/"
license=('GPL2')
makedepends=('xmlto' 'docbook-xsl' 'kmod' 'inetutils' 'bc')
options=('!strip')
_verwatch=('https://mirrors.edge.kernel.org/pub/linux/kernel/v3.x/' '.*patch-\(3\.16\.[0-9]\+\)\.xz.*' 'f')
source=(
  "https://www.kernel.org/pub/linux/kernel/v3.x/${_srcname}.tar.xz"
  "https://www.kernel.org/pub/linux/kernel/v3.x/patch-${pkgver}.xz"
  # the main kernel config files
  'config' 'config.x86_64'
  # pacman hook for initramfs regeneration
  '99-linux.hook'
  # standard config files for mkinitcpio ramdisk
  'linux.preset'
  'change-default-console-loglevel.patch'
  #'0000-unknown-rela-relocation-4-binutils.2.31.kernel.3.16.patch' # https://www.reddit.com/r/linuxquestions/comments/903xwq/unable_to_compile_working_kernel_modules_anymore/
  '0001-binutils.2.31.max-page-size.patch' # http://lists.gnu.org/archive/html/bug-binutils/2018-03/msg00193.html
  '0002-binutils.2.34.sysexit.patch' # https://gist.github.com/bbidulock/263c5c3aee34e3a1b09dca0b937c210b
  '0003-systemd.245.kernel.316.ambient.capabilities.patch' # https://github.com/hardkernel/linux/commit/2ddfe869e9964afe1175919557e6b4f18b78941a
  'update.sh'
)
md5sums=('5c569ed649a0c9711879f333e90c5386'
         '8da6a4c655cecd0f2657436334a60d9c'
         '5c85a1cef25029a8eb87d0edeec0cb04'
         'f45197ec50bb5f7a85991f6e99ad49c6'
         '90cd68710e3064d9b65f5549570f7821'
         'eb14dcfd80c00852ef81ded6e826826a'
         'df7fceae6ee5d7e7be7b60ecd7f6bb35'
         '07dc499a909a3bb63fc3fdc0d0652e64'
         '43d62abf4cd27fa1863759ac87b62ac5'
         '4f2248545c0a3997a1d301195b7dcfe7'
         'e6a1be64b190d846648d671c012d6dd3')
sha256sums=('4813ad7927a7d92e5339a873ab16201b242b2748934f12cb5df9ba2cfe1d77a0'
            '82bd3706afe2beff9ff9a00fae0dd7f92e6f8f300ba0bbe8cc778c2bced20a11'
            '3bce3e9adce8ae3f826eebab75e9784ca92a914e526ae352de61c1da93aab8d3'
            '328539797005cb43362b75ca9965791a1ed34525101c286e4fb49694faa40e4c'
            '834bd254b56ab71d73f59b3221f056c72f559553c04718e350ab2a3e2991afe0'
            'f0d90e756f14533ee67afda280500511a62465b4f76adcc5effa95a40045179c'
            '1256b241cd477b265a3c2d64bdc19ffe3c9bbcee82ea3994c590c2c76e767d99'
            'f71e0de924013fe60c3cbed45f322e6a09942db978daeddd18adb8582373b5ed'
            '2c80046fa78bfa6e26ae6d8ac312142d9d67b394914fee423578583fe7ab15db'
            'abbb27b46cf00bf6d4859c4d8dfcf1d6f32e385d3dbf04790abda8b4dae6540a'
            '4dad3093e0c2bd7dafd30a0344b4df6432c3a7d1422edc4e0d1e6201aa513648')

_kernelname=${pkgbase#linux}

# CFLAGS CXXFLAGS are not used at all.
# LDFLAGS only works on the make command line. It is not used from the environment.
_makeopts=(
  #CC='gcc-5' CXX='g++-5' HOSTCC='gcc-5' HOSTCXX='g++-5' # LD='ld.gold'
  #CC='gcc-6' CXX='g++-6' HOSTCC='gcc-6' HOSTCXX='g++-6'
  #LDFLAGS='-z max-page-size=0x200000' # http://lists.gnu.org/archive/html/bug-binutils/2018-03/msg00193.html
)
#makedepends+=('gcc5')

prepare() {
  set -u
  cd "${_srcname}"

  # add upstream patch
  patch -Nup1 -i "${srcdir}/patch-${pkgver}"
  set +u; msg2 "Complete: patch-${pkgver}"; set -u

  # add latest fixes from stable queue, if needed
  # http://git.kernel.org/?p=linux/kernel/git/stable/stable-queue.git

  # set DEFAULT_CONSOLE_LOGLEVEL to 4 (same value as the 'quiet' kernel param)
  # remove this when a Kconfig knob is made available by upstream
  # (relevant patch sent upstream: https://lkml.org/lkml/2011/7/26/227)
  patch -Nup1 -i "${srcdir}/change-default-console-loglevel.patch"

  # diff -pNaru5 'linux-3.16'{.61.orig,} > 'new_0000-unknown-rela-relocation-4-binutils.2.31.kernel.3.16.patch'
  #(cd ..; cp -pr "${_srcname}"{,.61.orig})
  #patch -Nup1 -i "${srcdir}/0000-unknown-rela-relocation-4-binutils.2.31.kernel.3.16.patch"

  patch -Nup1 -i "${srcdir}/0001-binutils.2.31.max-page-size.patch"

  # Fix for binutils 2.34
  patch -Nup1 -i "${srcdir}/0002-binutils.2.34.sysexit.patch"

  # Fix for systemd 245
  # https://forum.odroid.com/viewtopic.php?f=141&t=38171
  # by stas-t Re: C2 won't boot up after upgrading systemd to 245-1 on Arch
  patch -Nup1 -i "${srcdir}/0003-systemd.245.kernel.316.ambient.capabilities.patch"

  declare -A _config=([i686]='config' [x86_64]='config.x86_64')
  cat "${srcdir}/${_config[${CARCH}]}" > './.config'
  if [ "${_kernelname}" != "" ]; then
    sed -i "s|CONFIG_LOCALVERSION=.*|CONFIG_LOCALVERSION=\"${_kernelname}\"|g" ./.config
    sed -i "s|CONFIG_LOCALVERSION_AUTO=.*|CONFIG_LOCALVERSION_AUTO=n|" ./.config
  fi
  cp './.config' "${srcdir}/config.cmp"
  rm -f "${startdir}/${_config[${CARCH}]}.new"

  # set extraversion to pkgrel
  sed -ri "s|^(EXTRAVERSION =).*|\1 -${pkgrel}|" Makefile

  # don't run depmod on 'make install'. We'll do this ourselves in packaging
  sed -i '2iexit 0' scripts/depmod.sh

  set +u; msg2 'get kernel version'; set +u
  set -x
  make -s -j1 prepare "${_makeopts[@]}"
  set +x

  if ! diff -pNau5 "${srcdir}/config.cmp" './.config'; then
    ln -s "${PWD}/.config" "${startdir}/${_config[${CARCH}]}.new"
    rm "${srcdir}/config.cmp"
    set +u
    echo 'Some changes were made. Please merge for automation.'
    false
  else
    rm "${srcdir}/config.cmp"
  fi

  # load configuration
  # Configure the kernel. Replace the line below with one of your choice.
  #make menuconfig # CLI menu for configuration
  #make nconfig # new CLI menu for configuration
  #make xconfig # X-based configuration
  #make oldconfig # using old config from previous kernel version
  # ... or manually edit .config

  set +u; msg2 'rewrite configuration'; set +u
  set -x
  yes "" | make -j1 config "${_makeopts[@]}" >/dev/null
  set +x
  set +u
}

build() {
  set -u
  cd "${srcdir}/${_srcname}"

  local _mflags=()
  local _nproc="$(nproc)"; _nproc=$((_nproc>8?8:_nproc))
  if [ -z "${MAKEFLAGS:=}" ] || [ "${MAKEFLAGS//-j/}" = "${MAKEFLAGS}" ]; then
    _mflags+=('-j' "${_nproc}")
  fi

  rm -f vmlinux vmlinux.o # force relink, for debugging binutils 2.31.1

  set -x
  nice make -s "${_makeopts[@]}" "${_mflags[@]}" ${MAKEFLAGS} LOCALVERSION= bzImage modules
  set +x
  set +u
}

_package() {
  set -u
  pkgdesc="The ${pkgbase/linux/Linux} kernel and modules"
  #[ "${pkgbase}" = "linux" ] && groups=('base')
  depends=('coreutils' 'linux-firmware' 'kmod' 'mkinitcpio>=0.7')
  optdepends=('crda: to set the correct wireless channels of your country')
  backup=("etc/mkinitcpio.d/${pkgbase}.preset")
  install=linux.install
  provides=("linux=${pkgver}")

  cd "${_srcname}"

  KARCH=x86

  # get kernel version
  _kernver="$(make -j1 "${_makeopts[@]}" LOCALVERSION= kernelrelease)"
  _basekernel=${_kernver%%-*}
  _basekernel=${_basekernel%.*}

  mkdir -p "${pkgdir}"/{lib/modules,lib/firmware,boot}
  make -j1 "${_makeopts[@]}" LOCALVERSION= INSTALL_MOD_PATH="${pkgdir}" modules_install
  cp arch/$KARCH/boot/bzImage "${pkgdir}/boot/vmlinuz-${pkgbase}"

  # set correct depmod command for install
  cp -f "${startdir}/${install}" "${startdir}/${install}.pkg"
  true && install=${install}.pkg
  sed \
    -e  "s/KERNEL_NAME=.*/KERNEL_NAME=${_kernelname}/" \
    -e  "s/KERNEL_VERSION=.*/KERNEL_VERSION=${_kernver}/" \
    -i "${startdir}/${install}"

  # install mkinitcpio preset file for kernel
  install -D -m644 "${srcdir}/linux.preset" "${pkgdir}/etc/mkinitcpio.d/${pkgbase}.preset"
  sed \
    -e "1s|'linux.*'|'${pkgbase}'|" \
    -e "s|ALL_kver=.*|ALL_kver=\"/boot/vmlinuz-${pkgbase}\"|" \
    -e "s|default_image=.*|default_image=\"/boot/initramfs-${pkgbase}.img\"|" \
    -e "s|fallback_image=.*|fallback_image=\"/boot/initramfs-${pkgbase}-fallback.img\"|" \
    -i "${pkgdir}/etc/mkinitcpio.d/${pkgbase}.preset"

  # install pacman hook for initramfs regeneration
  sed "s|%PKGBASE%|${pkgbase}|g" "${srcdir}/99-linux.hook" |
    install -D -m644 /dev/stdin "${pkgdir}/usr/share/libalpm/hooks/99-${pkgbase}.hook"

  # remove build and source links
  rm -f "${pkgdir}"/lib/modules/${_kernver}/{source,build}
  # remove the firmware
  rm -rf "${pkgdir}/lib/firmware"
  # gzip -9 all modules to save 100MB of space
  find "${pkgdir}" -name '*.ko' -exec gzip -9 {} \;
  # make room for external modules
  ln -s "../extramodules-${_basekernel}${_kernelname:--ARCH}" "${pkgdir}/lib/modules/${_kernver}/extramodules"
  # add real version for building modules and running depmod from post_install/upgrade
  mkdir -p "${pkgdir}/lib/modules/extramodules-${_basekernel}${_kernelname:--ARCH}"
  echo "${_kernver}" > "${pkgdir}/lib/modules/extramodules-${_basekernel}${_kernelname:--ARCH}/version"

  # Now we call depmod...
  depmod -b "${pkgdir}" -F System.map "${_kernver}"

  # move module tree /lib -> /usr/lib
  mkdir -p "${pkgdir}/usr"
  mv "${pkgdir}/lib" "${pkgdir}/usr/"

  # add vmlinux
  install -D -m644 vmlinux "${pkgdir}/usr/lib/modules/${_kernver}/build/vmlinux"
  set +u
}

_package-headers() {
  set -u
  pkgdesc="Header files and scripts for building modules for ${pkgbase/linux/Linux} kernel"
  provides=("linux-headers=${pkgver}")

  install -dm755 "${pkgdir}/usr/lib/modules/${_kernver}"

  cd "${srcdir}/${_srcname}"
  install -D -m644 Makefile \
    "${pkgdir}/usr/lib/modules/${_kernver}/build/Makefile"
  install -D -m644 kernel/Makefile \
    "${pkgdir}/usr/lib/modules/${_kernver}/build/kernel/Makefile"
  install -D -m644 .config \
    "${pkgdir}/usr/lib/modules/${_kernver}/build/.config"

  mkdir -p "${pkgdir}/usr/lib/modules/${_kernver}/build/include"

  for i in acpi asm-generic config crypto drm generated keys linux math-emu \
    media net pcmcia scsi sound trace uapi video xen; do
    cp -a include/${i} "${pkgdir}/usr/lib/modules/${_kernver}/build/include/"
  done

  # copy arch includes for external modules
  mkdir -p "${pkgdir}/usr/lib/modules/${_kernver}/build/arch/x86"
  cp -a arch/x86/include "${pkgdir}/usr/lib/modules/${_kernver}/build/arch/x86/"

  # copy files necessary for later builds, like nvidia and vmware
  cp Module.symvers "${pkgdir}/usr/lib/modules/${_kernver}/build"
  cp -a scripts "${pkgdir}/usr/lib/modules/${_kernver}/build"

  # fix permissions on scripts dir
  chmod og-w -R "${pkgdir}/usr/lib/modules/${_kernver}/build/scripts"
  mkdir -p "${pkgdir}/usr/lib/modules/${_kernver}/build/.tmp_versions"

  mkdir -p "${pkgdir}/usr/lib/modules/${_kernver}/build/arch/${KARCH}/kernel"

  cp arch/${KARCH}/Makefile "${pkgdir}/usr/lib/modules/${_kernver}/build/arch/${KARCH}/"

  if [ "${CARCH}" = "i686" ]; then
    cp arch/${KARCH}/Makefile_32.cpu "${pkgdir}/usr/lib/modules/${_kernver}/build/arch/${KARCH}/"
  fi

  cp arch/${KARCH}/kernel/asm-offsets.s "${pkgdir}/usr/lib/modules/${_kernver}/build/arch/${KARCH}/kernel/"

  # add docbook makefile
  install -D -m644 Documentation/DocBook/Makefile \
    "${pkgdir}/usr/lib/modules/${_kernver}/build/Documentation/DocBook/Makefile"

  # add dm headers
  mkdir -p "${pkgdir}/usr/lib/modules/${_kernver}/build/drivers/md"
  cp drivers/md/*.h "${pkgdir}/usr/lib/modules/${_kernver}/build/drivers/md"

  # add inotify.h
  mkdir -p "${pkgdir}/usr/lib/modules/${_kernver}/build/include/linux"
  cp include/linux/inotify.h "${pkgdir}/usr/lib/modules/${_kernver}/build/include/linux/"

  # add wireless headers
  mkdir -p "${pkgdir}/usr/lib/modules/${_kernver}/build/net/mac80211/"
  cp net/mac80211/*.h "${pkgdir}/usr/lib/modules/${_kernver}/build/net/mac80211/"

  # add dvb headers for external modules
  # in reference to:
  # http://bugs.archlinux.org/task/9912
  mkdir -p "${pkgdir}/usr/lib/modules/${_kernver}/build/drivers/media/dvb-core"
  cp drivers/media/dvb-core/*.h "${pkgdir}/usr/lib/modules/${_kernver}/build/drivers/media/dvb-core/"
  # and...
  # http://bugs.archlinux.org/task/11194
  mkdir -p "${pkgdir}/usr/lib/modules/${_kernver}/build/include/config/dvb/"
  cp include/config/dvb/*.h "${pkgdir}/usr/lib/modules/${_kernver}/build/include/config/dvb/"

  # add dvb headers for http://mcentral.de/hg/~mrec/em28xx-new
  # in reference to:
  # http://bugs.archlinux.org/task/13146
  mkdir -p "${pkgdir}/usr/lib/modules/${_kernver}/build/drivers/media/dvb-frontends/"
  cp drivers/media/dvb-frontends/lgdt330x.h "${pkgdir}/usr/lib/modules/${_kernver}/build/drivers/media/dvb-frontends/"
  mkdir -p "${pkgdir}/usr/lib/modules/${_kernver}/build/drivers/media/i2c/"
  cp drivers/media/i2c/msp3400-driver.h "${pkgdir}/usr/lib/modules/${_kernver}/build/drivers/media/i2c/"

  # add dvb headers
  # in reference to:
  # http://bugs.archlinux.org/task/20402
  mkdir -p "${pkgdir}/usr/lib/modules/${_kernver}/build/drivers/media/usb/dvb-usb"
  cp drivers/media/usb/dvb-usb/*.h "${pkgdir}/usr/lib/modules/${_kernver}/build/drivers/media/usb/dvb-usb/"
  mkdir -p "${pkgdir}/usr/lib/modules/${_kernver}/build/drivers/media/dvb-frontends"
  cp drivers/media/dvb-frontends/*.h "${pkgdir}/usr/lib/modules/${_kernver}/build/drivers/media/dvb-frontends/"
  mkdir -p "${pkgdir}/usr/lib/modules/${_kernver}/build/drivers/media/tuners"
  cp drivers/media/tuners/*.h "${pkgdir}/usr/lib/modules/${_kernver}/build/drivers/media/tuners/"

  # add xfs and shmem for aufs building
  mkdir -p "${pkgdir}/usr/lib/modules/${_kernver}/build/fs/xfs"
  mkdir -p "${pkgdir}/usr/lib/modules/${_kernver}/build/mm"
  cp fs/xfs/xfs_sb.h "${pkgdir}/usr/lib/modules/${_kernver}/build/fs/xfs/xfs_sb.h"

  # copy in Kconfig files
  for i in $(find . -name "Kconfig*"); do
    mkdir -p "${pkgdir}"/usr/lib/modules/${_kernver}/build/`echo ${i} | sed 's|/Kconfig.*||'`
    cp ${i} "${pkgdir}/usr/lib/modules/${_kernver}/build/${i}"
  done

  chown -R root.root "${pkgdir}/usr/lib/modules/${_kernver}/build"
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
  rm -rf "${pkgdir}"/usr/lib/modules/${_kernver}/build/arch/{alpha,arc,arm,arm26,arm64,avr32,blackfin,c6x,cris,frv,h8300,hexagon,ia64,m32r,m68k,m68knommu,metag,mips,microblaze,mn10300,openrisc,parisc,powerpc,ppc,s390,score,sh,sh64,sparc,sparc64,tile,unicore32,um,v850,xtensa}
  set +u
}

_package-docs() {
  set -u
  pkgdesc="Kernel hackers manual - HTML documentation that comes with the ${pkgbase/linux/Linux} kernel"

  cd "${srcdir}/${_srcname}"

  mkdir -p "${pkgdir}/usr/lib/modules/${_kernver}/build"
  cp -al Documentation "${pkgdir}/usr/lib/modules/${_kernver}/build"
  find "${pkgdir}" -type f -exec chmod 444 {} \;
  find "${pkgdir}" -type d -exec chmod 755 {} \;

  # remove a file already in linux package
  rm -f "${pkgdir}/usr/lib/modules/${_kernver}/build/Documentation/DocBook/Makefile"
  set +u
}

pkgname=("${pkgbase}" "${pkgbase}-headers" "${pkgbase}-docs")
for _p in ${pkgname[@]}; do
  eval "package_${_p}() {
    $(declare -f "_package${_p#${pkgbase}}")
    _package${_p#${pkgbase}}
  }"
done

set +u
