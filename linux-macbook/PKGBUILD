# Maintainer: Tony Lambiris <tony@critialstack.com>

# $Id$
# Maintainer: Tobias Powalowski <tpowa@archlinux.org>
# Maintainer: Thomas Baechler <thomas@archlinux.org>

#pkgbase=linux               # Build stock -ARCH kernel
pkgbase=linux-macbook       # Build kernel with a different name
_srcname=linux-4.14
pkgver=4.14.9
pkgrel=1
arch=('x86_64')
url="https://www.kernel.org/"
license=('GPL2')
makedepends=('xmlto' 'kmod' 'inetutils' 'bc' 'libelf')
options=('!strip')
source=(
  "https://www.kernel.org/pub/linux/kernel/v4.x/${_srcname}.tar.xz"
  "https://www.kernel.org/pub/linux/kernel/v4.x/${_srcname}.tar.sign"
  "https://www.kernel.org/pub/linux/kernel/v4.x/patch-${pkgver}.xz"
  "https://www.kernel.org/pub/linux/kernel/v4.x/patch-${pkgver}.sign"
  'config'         # the main kernel config file
  '60-linux.hook'  # pacman hook for depmod
  '90-linux.hook'  # pacman hook for initramfs regeneration
  'linux.preset'   # standard config files for mkinitcpio ramdisk
  macbook-wakeup.service # service file for suspend/resume events
  apple-gmux.patch # linux-macbook specific patches
  PCI-Work-around-poweroff-suspend-to-RAM-issue-on-Mac.patch
  RFC-PCI-Workaround-to-enable-poweroff-on-Mac-Pro-11.patch
  RFC-v2-PCI-Workaround-to-enable-poweroff-on-Mac-Pro-11.patch
  intel-pstate-backport.patch
  0001-add-sysctl-to-disallow-unprivileged-CLONE_NEWUSER-by.patch
  0001-e1000e-Fix-e1000_check_for_copper_link_ich8lan-retur.patch
  0002-dccp-CVE-2017-8824-use-after-free-in-DCCP-code.patch
  0001-Revert-xfrm-Fix-stack-out-of-bounds-read-in-xfrm_sta.patch
  0002-xfrm-Fix-stack-out-of-bounds-read-on-socket-policy-l.patch
  0003-cgroup-fix-css_task_iter-crash-on-CSS_TASK_ITER_PROC.patch
  0001-ALSA-usb-audio-Fix-the-missing-ctl-name-suffix-at-pa.patch
)
validpgpkeys=(
  'ABAF11C65A2970B130ABE3C479BE3E4300411886'  # Linus Torvalds
  '647F28654894E3BD457199BE38DBBDC86092693E'  # Greg Kroah-Hartman
)
sha256sums=('f81d59477e90a130857ce18dc02f4fbe5725854911db1e7ba770c7cd350f96a7'
            'SKIP'
            '5edc955bb67b04c7ed426b1df17a3e322e32ad9fdda9c6abb53ab6eca7faf704'
            'SKIP'
            '4d12ed868b05720c3d263c8454622c67bdee6969400049d7adac7b00907ad195'
            'ae2e95db94ef7176207c690224169594d49445e04249d2499e9d2fbc117a0b21'
            '75f99f5239e03238f88d1a834c50043ec32b1dc568f2cc291b07d04718483919'
            'ad6344badc91ad0630caacde83f7f9b97276f80d26a20619a87952be65492c65'
            'c5a714823c3418692bc5c212dd5d094a0e2ae6147d6726822911f1c26e3a1d1b'
            'e74dbeaa3fd04dbf93ef4498015234bdb65351857e07c03c00cee69fcfc844b4'
            '43bcb45f99da0242ec5b340631d0777f302a5f356ef3ccec8d1d30de5a3a025a'
            '7c99aaeaea7837f83a3ad215cf07277934ccf39720acee7f1c371dc86bdf89fc'
            '09189eb269a9fd16898cf90a477df23306236fb897791e8d04e5a75d5007bbff'
            '3d9fdbb4bee270efa6eef1d8e40a5ae562a87d5a2edae629e0829cc51714de13'
            '37b86ca3de148a34258e3176dbf41488d9dbd19e93adbd22a062b3c41332ce85'
            'c6e7db7dfd6a07e1fd0e20c3a5f0f315f9c2a366fe42214918b756f9a1c9bfa3'
            '1d69940c6bf1731fa1d1da29b32ec4f594fa360118fe7b128c9810285ebf13e2'
            'ed3266ab03f836f57de0faf8a10ffd7566c909515c2649de99adaab2fac4aa32'
            '64a014f7e1b4588728b3ea9538beee67ec63fb792d890c7be9cc13ddc2121b00'
            '3d4c41086c077fbd515d04f5e59c0c258f700433c5da3365d960b696c2e56efb'
            '95f0d0a94983b0dafd295f660a663f9be5ef2fcb9646098426a5d12b59f50638')

_kernelname=${pkgbase#linux}

prepare() {
  cd ${_srcname}

  # add upstream patch
  patch -p1 -i ../patch-${pkgver}

  # security patches

  # add latest fixes from stable queue, if needed
  # http://git.kernel.org/?p=linux/kernel/git/stable/stable-queue.git

  # start of macbook specific patches
  msg "patch -p1 -F1 -i ${srcdir}/apple-gmux.patch"
  patch -p1 -F1 -i "${srcdir}/apple-gmux.patch"

  # https://patchwork.kernel.org/patch/9821773/
  #msg "patch -p1 -F1 -i ${srcdir}/PCI-Work-around-poweroff-suspend-to-RAM-issue-on-Mac.patch"
  #patch -p1 -F1 -i \
  #  "${srcdir}/PCI-Work-around-poweroff-suspend-to-RAM-issue-on-Mac.patch"

  # https://patchwork.kernel.org/patch/9140867/
  msg "patch -p1 -F1 -i ${srcdir}/RFC-PCI-Workaround-to-enable-poweroff-on-Mac-Pro-11.patch"
  patch -p1 -F1 -i \
    "${srcdir}/RFC-PCI-Workaround-to-enable-poweroff-on-Mac-Pro-11.patch"

  # https://patchwork.kernel.org/patch/9288825/
  msg "patch -p1 -F1 -i ${srcdir}/RFC-v2-PCI-Workaround-to-enable-poweroff-on-Mac-Pro-11.patch"
  patch -p1 -F1 -i \
    "${srcdir}/RFC-v2-PCI-Workaround-to-enable-poweroff-on-Mac-Pro-11.patch"

  # disable USER_NS for non-root users by default
  patch -Np1 -i ../0001-add-sysctl-to-disallow-unprivileged-CLONE_NEWUSER-by.patch

  # https://bugs.archlinux.org/task/56575
  patch -Np1 -i ../0001-e1000e-Fix-e1000_check_for_copper_link_ich8lan-retur.patch

  # https://nvd.nist.gov/vuln/detail/CVE-2017-8824
  patch -Np1 -i ../0002-dccp-CVE-2017-8824-use-after-free-in-DCCP-code.patch

  # https://bugs.archlinux.org/task/56605
  patch -Np1 -i ../0001-Revert-xfrm-Fix-stack-out-of-bounds-read-in-xfrm_sta.patch
  patch -Np1 -i ../0002-xfrm-Fix-stack-out-of-bounds-read-on-socket-policy-l.patch

  # https://bugs.archlinux.org/task/56846
  patch -Np1 -i ../0003-cgroup-fix-css_task_iter-crash-on-CSS_TASK_ITER_PROC.patch

  # https://bugs.archlinux.org/task/56830
  patch -Np1 -i ../0001-ALSA-usb-audio-Fix-the-missing-ctl-name-suffix-at-pa.patch

  cp -Tf ../config .config

  if [ "${_kernelname}" != "" ]; then
    sed -i "s|CONFIG_LOCALVERSION=.*|CONFIG_LOCALVERSION=\"${_kernelname}\"|g" ./.config
    sed -i "s|CONFIG_LOCALVERSION_AUTO=.*|CONFIG_LOCALVERSION_AUTO=n|" ./.config
  fi

  # set extraversion to pkgrel
  sed -ri "s|^(EXTRAVERSION =).*|\1 -${pkgrel}|" Makefile

  # don't run depmod on 'make install'. We'll do this ourselves in packaging
  sed -i '2iexit 0' scripts/depmod.sh

  # get kernel version
  make prepare

  # load configuration
  # Configure the kernel. Replace the line below with one of your choice.
  #make menuconfig # CLI menu for configuration
  #make nconfig # new CLI menu for configuration
  #make xconfig # X-based configuration
  #make oldconfig # using old config from previous kernel version
  # ... or manually edit .config

  # rewrite configuration
  yes "" | make config >/dev/null
}

build() {
  cd ${_srcname}

  make ${MAKEFLAGS} LOCALVERSION= bzImage modules
}

_package() {
  pkgdesc="The ${pkgbase/linux/Linux} kernel and modules"
  [ "${pkgbase}" = "linux" ] && groups=('base')
  depends=('coreutils' 'linux-firmware' 'kmod' 'mkinitcpio>=0.7')
  optdepends=('crda: to set the correct wireless channels of your country')
  backup=("etc/mkinitcpio.d/${pkgbase}.preset")
  install=linux.install

  cd ${_srcname}

  # get kernel version
  _kernver="$(make LOCALVERSION= kernelrelease)"
  _basekernel=${_kernver%%-*}
  _basekernel=${_basekernel%.*}

  mkdir -p "${pkgdir}"/{boot,usr/lib/modules}
  make LOCALVERSION= INSTALL_MOD_PATH="${pkgdir}/usr" modules_install
  cp arch/x86/boot/bzImage "${pkgdir}/boot/vmlinuz-${pkgbase}"

  # make room for external modules
  local _extramodules="extramodules-${_basekernel}${_kernelname:--ARCH}"
  ln -s "../${_extramodules}" "${pkgdir}/usr/lib/modules/${_kernver}/extramodules"

  # add real version for building modules and running depmod from hook
  echo "${_kernver}" |
    install -Dm644 /dev/stdin "${pkgdir}/usr/lib/modules/${_extramodules}/version"

  # remove build and source links
  rm "${pkgdir}"/usr/lib/modules/${_kernver}/{source,build}

  # now we call depmod...
  depmod -b "${pkgdir}/usr" -F System.map "${_kernver}"

  # add vmlinux
  install -Dt "${pkgdir}/usr/lib/modules/${_kernver}/build" -m644 vmlinux

  # sed expression for following substitutions
  local _subst="
    s|%PKGBASE%|${pkgbase}|g
    s|%KERNVER%|${_kernver}|g
    s|%EXTRAMODULES%|${_extramodules}|g
  "

  # hack to allow specifying an initially nonexisting install file
  sed "${_subst}" "${startdir}/${install}" > "${startdir}/${install}.pkg"
  true && install=${install}.pkg

  # copy macbook-wakeup.service to systemd
  mkdir -p "${pkgdir}/usr/lib/systemd/system"
  cp "${srcdir}/macbook-wakeup.service" "${pkgdir}/usr/lib/systemd/system"

  # install mkinitcpio preset file
  sed "${_subst}" ../linux.preset |
    install -Dm644 /dev/stdin "${pkgdir}/etc/mkinitcpio.d/${pkgbase}.preset"

  # install pacman hooks
  sed "${_subst}" ../60-linux.hook |
    install -Dm644 /dev/stdin "${pkgdir}/usr/share/libalpm/hooks/60-${pkgbase}.hook"
  sed "${_subst}" ../90-linux.hook |
    install -Dm644 /dev/stdin "${pkgdir}/usr/share/libalpm/hooks/90-${pkgbase}.hook"
}

_package-headers() {
  pkgdesc="Header files and scripts for building modules for ${pkgbase/linux/Linux} kernel"

  cd ${_srcname}
  local _builddir="${pkgdir}/usr/lib/modules/${_kernver}/build"

  install -Dt "${_builddir}" -m644 Makefile .config Module.symvers
  install -Dt "${_builddir}/kernel" -m644 kernel/Makefile

  mkdir "${_builddir}/.tmp_versions"

  cp -t "${_builddir}" -a include scripts

  install -Dt "${_builddir}/arch/x86" -m644 arch/x86/Makefile
  install -Dt "${_builddir}/arch/x86/kernel" -m644 arch/x86/kernel/asm-offsets.s

  cp -t "${_builddir}/arch/x86" -a arch/x86/include

  install -Dt "${_builddir}/drivers/md" -m644 drivers/md/*.h
  install -Dt "${_builddir}/net/mac80211" -m644 net/mac80211/*.h

  # http://bugs.archlinux.org/task/9912
  install -Dt "${_builddir}/drivers/media/dvb-core" -m644 drivers/media/dvb-core/*.h

  # http://bugs.archlinux.org/task/13146
  install -Dt "${_builddir}/drivers/media/i2c" -m644 drivers/media/i2c/msp3400-driver.h

  # http://bugs.archlinux.org/task/20402
  install -Dt "${_builddir}/drivers/media/usb/dvb-usb" -m644 drivers/media/usb/dvb-usb/*.h
  install -Dt "${_builddir}/drivers/media/dvb-frontends" -m644 drivers/media/dvb-frontends/*.h
  install -Dt "${_builddir}/drivers/media/tuners" -m644 drivers/media/tuners/*.h

  # add xfs and shmem for aufs building
  mkdir -p "${_builddir}"/{fs/xfs,mm}

  # copy in Kconfig files
  find . -name Kconfig\* -exec install -Dm644 {} "${_builddir}/{}" \;

  # add objtool for external module building and enabled VALIDATION_STACK option
  install -Dt "${_builddir}/tools/objtool" tools/objtool/objtool

  # remove unneeded architectures
  local _arch
  for _arch in "${_builddir}"/arch/*/; do
    [[ ${_arch} == */x86/ ]] && continue
    rm -r "${_arch}"
  done

  # remove files already in linux-docs package
  rm -r "${_builddir}/Documentation"

  # Fix permissions
  chmod -R u=rwX,go=rX "${_builddir}"

  # strip scripts directory
  local _binary _strip
  while read -rd '' _binary; do
    case "$(file -bi "${_binary}")" in
      *application/x-sharedlib*)  _strip="${STRIP_SHARED}"   ;; # Libraries (.so)
      *application/x-archive*)    _strip="${STRIP_STATIC}"   ;; # Libraries (.a)
      *application/x-executable*) _strip="${STRIP_BINARIES}" ;; # Binaries
      *) continue ;;
    esac
    /usr/bin/strip ${_strip} "${_binary}"
  done < <(find "${_builddir}/scripts" -type f -perm -u+w -print0 2>/dev/null)
}

_package-docs() {
  pkgdesc="Kernel hackers manual - HTML documentation that comes with the ${pkgbase/linux/Linux} kernel"

  cd ${_srcname}
  local _builddir="${pkgdir}/usr/lib/modules/${_kernver}/build"

  mkdir -p "${_builddir}"
  cp -t "${_builddir}" -a Documentation

  # Fix permissions
  chmod -R u=rwX,go=rX "${_builddir}"
}

pkgname=("${pkgbase}" "${pkgbase}-headers" "${pkgbase}-docs")
for _p in ${pkgname[@]}; do
  eval "package_${_p}() {
    $(declare -f "_package${_p#${pkgbase}}")
    _package${_p#${pkgbase}}
  }"
done

# vim:set ts=8 sts=2 sw=2 et:
