# Maintainer: Chris Severance aur.severach aATt spamgourmet dott com
# Contributor: James Bunton <jamesbunton@delx.net.au>
# Contributor: Andreas Radke <andyrtr@archlinux.org>

set -u
pkgbase="linux-lts44"
pkgver="4.4.216"
_srcname="linux-${pkgver%.*}"
pkgrel='1'
arch=('x86_64')
url="https://www.kernel.org/"
license=('GPL2')
makedepends=('xmlto' 'kmod' 'inetutils' 'bc' 'libelf')
options=('!strip')
source=(
  "https://www.kernel.org/pub/linux/kernel/v4.x/${_srcname}.tar.xz"
  "https://www.kernel.org/pub/linux/kernel/v4.x/patch-${pkgver}.xz"
  'config'         # the main kernel config file
  '60-linux.hook'  # pacman hook for depmod
  '90-linux.hook'  # pacman hook for initramfs regeneration
  'linux-lts.preset'   # standard config files for mkinitcpio ramdisk
  'change-default-console-loglevel.patch'
  '0001-sdhci-revert.patch'
  '0002-binutils.2.34.sysexit.patch' # https://gist.github.com/bbidulock/263c5c3aee34e3a1b09dca0b937c210b
)
validpgpkeys=(
  'ABAF11C65A2970B130ABE3C479BE3E4300411886' # Linus Torvalds <torvalds@linux-foundation.org>
  '647F28654894E3BD457199BE38DBBDC86092693E' # Greg Kroah-Hartman (Linux kernel stable release signing key) <greg@kroah.com>
)
md5sums=('9a78fa2eb6c68ca5a40ed5af08142599'
         'e0161027bbd1fc7fb30192cab9e87f75'
         'a222765e40974acb8318be704f472141'
         'ce6c81ad1ad1f8b333fd6077d47abdaf'
         'a85bfae59eb537b973c388ffadb281ff'
         'a329f9581060d555dc7358483de9760a'
         'df7fceae6ee5d7e7be7b60ecd7f6bb35'
         'e1093d9bc718f362344ab56b85d4fb76'
         '43d62abf4cd27fa1863759ac87b62ac5')
sha256sums=('401d7c8fef594999a460d10c72c5a94e9c2e1022f16795ec51746b0d165418b2'
            'd9d7d2701e094eac2004dba2fac5870dc405c1f8d504d1d8627e64bcafd75fc0'
            'c5115da0395fe7da1d30e1fd53faabf55bc6a9f616b8d1e22918f5c4933dac56'
            'ae2e95db94ef7176207c690224169594d49445e04249d2499e9d2fbc117a0b21'
            '75f99f5239e03238f88d1a834c50043ec32b1dc568f2cc291b07d04718483919'
            'ad6344badc91ad0630caacde83f7f9b97276f80d26a20619a87952be65492c65'
            '1256b241cd477b265a3c2d64bdc19ffe3c9bbcee82ea3994c590c2c76e767d99'
            '5313df7cb5b4d005422bd4cd0dae956b2dadba8f3db904275aaf99ac53894375'
            '2c80046fa78bfa6e26ae6d8ac312142d9d67b394914fee423578583fe7ab15db')

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

  # revert http://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git/commit/?id=9faac7b95ea4f9e83b7a914084cc81ef1632fd91
  # fixes #47778 sdhci broken on some boards
  # https://bugzilla.kernel.org/show_bug.cgi?id=106541
  patch -Nup1 -R -i "${srcdir}/0001-sdhci-revert.patch"

  # set DEFAULT_CONSOLE_LOGLEVEL to 4 (same value as the 'quiet' kernel param)
  # remove this when a Kconfig knob is made available by upstream
  # (relevant patch sent upstream: https://lkml.org/lkml/2011/7/26/227)
  patch -Nup1 -i "${srcdir}/change-default-console-loglevel.patch"

  # Fix for binutils 2.34
  patch -Nup1 -i "${srcdir}/0002-binutils.2.34.sysexit.patch"

  # Local or private patches
  shopt -s nullglob
  local _lpatch
  for _lpatch in "${startdir}"/*.localpatch; do
    set +u; msg2 "Local patch: ${_lpatch##*/}"; set -u
    patch -Nup1 -i "${_lpatch}"
  done
  unset _lpatch
  shopt -u nullglob

  declare -A _config=([x86_64]='config')
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
  install=linux-lts.install
  provides=("linux=${pkgver}")

  cd "${_srcname}"

  # get kernel version
  _kernver="$(make -j1 "${_makeopts[@]}" LOCALVERSION= kernelrelease)"
  _basekernel=${_kernver%%-*}
  _basekernel=${_basekernel%.*}

  mkdir -p "${pkgdir}"/{boot,usr/lib/modules}
  make -j1 "${_makeopts[@]}" LOCALVERSION= INSTALL_MOD_PATH="${pkgdir}/usr" modules_install
  cp arch/x86/boot/bzImage "${pkgdir}/boot/vmlinuz-${pkgbase}"

  # systemd expects to find the kernel here to allow hibernation
  # https://github.com/systemd/systemd/commit/edda44605f06a41fb86b7ab8128dcf99161d2344
  ln -sr "${pkgdir}/boot/vmlinuz-${pkgbase}" "${pkgdir}/usr/lib/modules/${_kernver}/vmlinuz"

  # remove the firmware
  rm -r "${pkgdir}/usr/lib/firmware"

  # make room for external modules
  local _extramodules="extramodules-${_basekernel}${_kernelname:--lts}"
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

  # install mkinitcpio preset file
  sed "${_subst}" ../linux-lts.preset |
    install -Dm644 /dev/stdin "${pkgdir}/etc/mkinitcpio.d/${pkgbase}.preset"

  # install pacman hooks
  sed "${_subst}" ../60-linux.hook |
    install -Dm644 /dev/stdin "${pkgdir}/usr/share/libalpm/hooks/60-${pkgbase}.hook"
  sed "${_subst}" ../90-linux.hook |
    install -Dm644 /dev/stdin "${pkgdir}/usr/share/libalpm/hooks/90-${pkgbase}.hook"
  set +u
}

_package-headers() {
  set -u
  pkgdesc="Header files and scripts for building modules for ${pkgbase/linux/Linux} kernel"
  provides=("linux-headers=${pkgver}")

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

  # http://bugs.archlinux.org/task/13146
  install -Dt "${_builddir}/drivers/media/i2c" -m644 drivers/media/i2c/msp3400-driver.h

  # http://bugs.archlinux.org/task/20402
  install -Dt "${_builddir}/drivers/media/dvb-core" -m644 drivers/media/dvb-core/*.h
  install -Dt "${_builddir}/drivers/media/usb/dvb-usb" -m644 drivers/media/usb/dvb-usb/*.h
  install -Dt "${_builddir}/drivers/media/dvb-frontends" -m644 drivers/media/dvb-frontends/*.h
  install -Dt "${_builddir}/drivers/media/tuners" -m644 drivers/media/tuners/*.h

  # add xfs and shmem for aufs building
  mkdir -p "${_builddir}"/{fs/xfs,mm}

  # copy in Kconfig files
  find . -name Kconfig\* -exec install -Dm644 {} "${_builddir}/{}" \;

  # remove unneeded architectures
  local _arch
  for _arch in "${_builddir}"/arch/*/; do
    [[ ${_arch} == */x86/ ]] && continue
    rm -r "${_arch}"
  done

  # remove files already in linux-docs package
  rm -r "${_builddir}/Documentation"

  # remove now broken symlinks
  find -L "${_builddir}" -type l -printf 'Removing %P\n' -delete

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
  set +u
}

_package-docs() {
  set -u
  pkgdesc="Kernel hackers manual - HTML documentation that comes with the ${pkgbase/linux/Linux} kernel"

  cd "${_srcname}"
  local _builddir="${pkgdir}/usr/lib/modules/${_kernver}/build"

  mkdir -p "${_builddir}"
  cp -t "${_builddir}" -a Documentation

  # Fix permissions
  chmod -R u=rwX,go=rX "${_builddir}"
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
