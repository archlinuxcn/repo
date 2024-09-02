#Maintainer: archdevlab <https://github.com/archdevlab>
#Credits: Jan Alexander Steffens (heftig) <heftig@archlinux.org>
#Credits: Andreas Radke <andyrtr@archlinux.org>
#Credits: Steven De Bondt <egnappah at gmail dot com>

################################# Arch ################################

ARCH=x86

################################# Grep GCC version ################################

_gccversion=$(gcc -dumpversion)

################################# CC/CXX/HOSTCC/HOSTCXX ################################

#Set compiler to build the kernel
#Set '1' to build with GCC
#Set '2' to build with CLANG and LLVM
#Default is empty. It will build with GCC. To build with different compiler just use : env _compiler=(1 or 2) makepkg -s
if [ -z ${_compiler+x} ]; then
  _compiler=
fi

if [[ "$_compiler" = "1" ]]; then
  _compiler=1
  BUILD_FLAGS=(CC=gcc CXX=g++ HOSTCC=gcc HOSTCXX=g++)
elif [[ "$_compiler" = "2" ]]; then
  _compiler=2
  BUILD_FLAGS=(CC=clang CXX=clang++ HOSTCC=clang HOSTCXX=clang++ LD=ld.lld LLVM=1 LLVM_IAS=1)
else
  _compiler=1
  BUILD_FLAGS=(CC=gcc CXX=g++ HOSTCC=gcc HOSTCXX=g++)
fi

###################################################################################

pkgbase=linux-amd
pkgver=6.10.5
_pkgver=6.10.5
pkgrel=1
major=6.10
commit=335b711f590650ef037442bf876f3551e5af0669
arch=(x86_64)
url='https://www.kernel.org/'
license=(GPL-2.0-only)
makedepends=(
  bc
  cpio
  gettext
  libelf
  pahole
  perl
  python
  tar
  xz
  kmod
  xmlto
  # htmldocs
  graphviz
  imagemagick
  python-sphinx
  python-yaml
  texlive-latexextra
)
makedepends+=(
  bison
  flex
  zstd
  make
  patch
  gcc
  gcc-libs
  glibc
  binutils
  git
)
if [[ "$_compiler" = "2" ]]; then
  makedepends+=(
    clang
    llvm
    llvm-libs
    lld
    clang
    python
  )
fi
options=(
  !debug
  !strip
)
archlinuxpath=https://gitlab.archlinux.org/archlinux/packaging/packages/linux/-/raw/$commit
source=(https://cdn.kernel.org/pub/linux/kernel/v6.x/linux-$_pkgver.tar.xz
        ${archlinuxpath}/config
        # Arch patches
        0001-ZEN-Add-sysctl-and-CONFIG-to-disallow-unprivileged-C.patch
        0002-drivers-firmware-skip-simpledrm-if-nvidia-drm.modese.patch
        0003-arch-Kconfig-Default-to-maximum-amount-of-ASLR-bits.patch
        0004-x86-apic-Remove-logical-destination-mode-for-64-bit.patch
        0005-btrfs-only-run-the-extent-map-shrinker-from-kswapd-t.patch
        # AMD Patches
        # sirlucjan
        0001-amd-pstate-patches.patch
        # Zen kernel
        0001-ZEN-cpufreq-Remove-schedutil-dependency-on-Intel-AMD.patch
        0001-ZEN-drm-amdgpu-pm-Allow-override-of-min_power_limit-.patch
        # Pf Kernel
        0001-x86-topology-Introduce-topology_logical_core_id.patch
        0002-perf-x86-rapl-Fix-the-energy-pkg-event-for-AMD-CPUs.patch
        0003-perf-x86-rapl-Rename-rapl_pmu-variables.patch
        0004-perf-x86-rapl-Make-rapl_model-struct-global.patch
        0005-perf-x86-rapl-Move-cpumask-variable-to-rapl_pmus-str.patch
        0006-perf-x86-rapl-Add-wrapper-for-online-offline-functio.patch
        0007-perf-x86-rapl-Add-an-argument-to-the-cleanup-and-ini.patch
        0008-perf-x86-rapl-Modify-the-generic-variable-names-to-_.patch
        0009-perf-x86-rapl-Remove-the-global-variable-rapl_msrs.patch
        0010-perf-x86-rapl-Add-per-core-energy-counter-support-fo.patch
        0011-perf-x86-rapl-Remove-the-unused-function-cpu_to_rapl.patch)

export KBUILD_BUILD_HOST=archlinux
export KBUILD_BUILD_USER=$pkgbase
export KBUILD_BUILD_TIMESTAMP="$(date -Ru${SOURCE_DATE_EPOCH:+d @$SOURCE_DATE_EPOCH})"

prepare(){
  cd ${srcdir}/linux-$_pkgver

  local src
  for src in "${source[@]}"; do
    src="${src%%::*}"
    src="${src##*/}"
    [[ $src = *.patch ]] || continue
    msg "Applying patch $src..."
    patch -Np1 < "../$src"
  done

  plain ""

  # Copy the config file first
  msg "Copy the config file first..."
  cp "${srcdir}"/config .config

  sleep 2s

  plain ""

  #  # Remove gcc-plugin if gcc version = 13.0.0
  #  if [[ "$_gccversion" = "13.0.0" ]]; then
  #
  #    msg "Remove GCC_PLUGINS"
  #    scripts/config --disable CONFIG_HAVE_GCC_PLUGINS
  #    scripts/config --disable CONFIG_GCC_PLUGINS
  #
  #    sleep 2s
  #    plain ""
  #  fi

  # Set LTO with CLANG/LLVM

  if [[ "$_compiler" = "2" ]]; then

    msg "Enable THIN LTO"
    scripts/config --enable CONFIG_LTO
    scripts/config --enable CONFIG_LTO_CLANG
    scripts/config --enable CONFIG_ARCH_SUPPORTS_LTO_CLANG
    scripts/config --enable CONFIG_ARCH_SUPPORTS_LTO_CLANG_THIN
    scripts/config --disable CONFIG_LTO_NONE
    scripts/config --enable CONFIG_HAS_LTO_CLANG
    scripts/config --disable CONFIG_LTO_CLANG_FULL
    scripts/config --enable CONFIG_LTO_CLANG_THIN
    scripts/config --enable CONFIG_HAVE_GCC_PLUGINS

    #msg "Enable FULL LTO"
    #scripts/config --enable CONFIG_LTO
    #scripts/config --enable CONFIG_LTO_CLANG
    #scripts/config --enable CONFIG_ARCH_SUPPORTS_LTO_CLANG
    #scripts/config --enable CONFIG_ARCH_SUPPORTS_LTO_CLANG_THIN
    #scripts/config --disable CONFIG_LTO_NONE
    #scripts/config --enable CONFIG_HAS_LTO_CLANG
    #scripts/config --enable CONFIG_LTO_CLANG_FULL
    #scripts/config --disable CONFIG_LTO_CLANG_THIN
    #scripts/config --enable CONFIG_HAVE_GCC_PLUGINS

    #msg "Disable LTO"
    #scripts/config --enable CONFIG_LTO_NONE

    sleep 2s
    plain ""
  fi

  msg "Set Font"
  scripts/config --disable CONFIG_FONTS
  scripts/config --enable CONFIG_FONT_8x8
  scripts/config --enable CONFIG_FONT_8x16

  sleep 2s

  plain ""

  # Supress depmod
  msg "Supress depmod..."
  sed -i '2iexit 0' scripts/depmod.sh

  sleep 2s

  plain ""

  # Setting localversion
  msg "Setting localversion..."
  # --save-scmversion as been removed in upstream
  # https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/scripts/setlocalversion?h=v6.3-rc1&id=f6e09b07cc12a4d104bb19fe7566b0636f60c413
  # scripts/setlocalversion --save-scmversion
  echo "-${pkgbase}" > localversion

  plain ""

  # Config
  msg "make olddefconfig..."
  make ARCH=${ARCH} ${BUILD_FLAGS[*]} olddefconfig

  plain ""

  make -s kernelrelease > version
  msg "Prepared $pkgbase version $(<version)"

  plain ""
}

build(){
  cd ${srcdir}/linux-$_pkgver

  msg "make all"
  make ARCH=${ARCH} ${BUILD_FLAGS[*]} KCFLAGS="-O2 -pipe -march=znver2 -mtune=znver2 -fstack-protector-strong" -j$(nproc) all
  msg "make -C tools/bpf/bpftool vmlinux.h feature-clang-bpf-co-re=1"
  make ARCH=${ARCH} ${BUILD_FLAGS[*]} KCFLAGS="-O2 -pipe -march=znver2 -mtune=znver2 -fstack-protector-strong" -j$(nproc) -C tools/bpf/bpftool vmlinux.h feature-clang-bpf-co-re=1
}

_package(){
  pkgdesc='The Linux kernel and modules - With some improvement patches'
  depends=(
    coreutils
    initramfs
    kmod
  )
  optdepends=(
    'wireless-regdb: to set the correct wireless channels of your country'
    'linux-firmware: firmware images needed for some devices'
  )
  provides=(
    KSMBD-MODULE
    VIRTUALBOX-GUEST-MODULES
    WIREGUARD-MODULE
  )
  replaces=(
    virtualbox-guest-modules-arch
    wireguard-arch
  )

  cd ${srcdir}/linux-$_pkgver

  local kernver="$(<version)"
  local modulesdir="${pkgdir}"/usr/lib/modules/${kernver}

  msg "Installing boot image..."
  # systemd expects to find the kernel here to allow hibernation
  # https://github.com/systemd/systemd/commit/edda44605f06a41fb86b7ab8128dcf99161d2344
  install -Dm644 "$(make -s image_name)" "$modulesdir/vmlinuz"

  # Used by mkinitcpio to name the kernel
  echo "$pkgbase" | install -Dm644 /dev/stdin "$modulesdir/pkgbase"

  msg "Installing modules..."
  ZSTD_CLEVEL=19 make ARCH=${ARCH} ${BUILD_FLAGS[*]} INSTALL_MOD_PATH="${pkgdir}"/usr INSTALL_MOD_STRIP=1 -j$(nproc) modules_install

  # remove build and source links
  msg "Remove build dir and source dir..."
  rm -rf "$modulesdir"/{source,build}
}

_package-headers(){
  pkgdesc="Headers and scripts for building modules for the $pkgbase package"
  depends=("${pkgbase}" pahole)

  cd ${srcdir}/linux-$_pkgver

  local builddir="$pkgdir"/usr/lib/modules/"$(<version)"/build

  msg "Installing build files..."
  install -Dt "$builddir" -m644 .config Makefile Module.symvers System.map *localversion* version vmlinux tools/bpf/bpftool/vmlinux.h
  install -Dt "$builddir/kernel" -m644 kernel/Makefile
  install -Dt "$builddir/arch/x86" -m644 arch/x86/Makefile
  cp -t "$builddir" -a scripts

  # required when STACK_VALIDATION is enabled
  install -Dt "$builddir/tools/objtool" tools/objtool/objtool

  # required when DEBUG_INFO_BTF_MODULES is enabled
  if [ -f tools/bpf/resolve_btfids/resolve_btfids ]; then
    install -Dt "$builddir/tools/bpf/resolve_btfids" tools/bpf/resolve_btfids/resolve_btfids
  fi

  msg "Installing headers..."
  cp -t "$builddir" -a include
  cp -t "$builddir/arch/x86" -a arch/x86/include
  install -Dt "$builddir/arch/x86/kernel" -m644 arch/x86/kernel/asm-offsets.s

  install -Dt "$builddir/drivers/md" -m644 drivers/md/*.h
  install -Dt "$builddir/net/mac80211" -m644 net/mac80211/*.h

  # https://bugs.archlinux.org/task/13146
  install -Dt "$builddir/drivers/media/i2c" -m644 drivers/media/i2c/msp3400-driver.h

  # https://bugs.archlinux.org/task/20402
  install -Dt "$builddir/drivers/media/usb/dvb-usb" -m644 drivers/media/usb/dvb-usb/*.h
  install -Dt "$builddir/drivers/media/dvb-frontends" -m644 drivers/media/dvb-frontends/*.h
  install -Dt "$builddir/drivers/media/tuners" -m644 drivers/media/tuners/*.h

  # https://bugs.archlinux.org/task/71392
  install -Dt "$builddir/drivers/iio/common/hid-sensors" -m644 drivers/iio/common/hid-sensors/*.h

  msg "Installing Kconfig files..."
  find . -name 'Kconfig*' -exec install -Dm644 {} "$builddir/{}" \;

  msg "Removing unneeded architectures..."
  local arch
  for arch in "$builddir"/arch/*/; do
    [[ $arch = */x86/ ]] && continue
    msg2 "Removing $(basename "$arch")"
    rm -r "$arch"
  done

  msg "Removing documentation..."
  rm -r "$builddir/Documentation"

  msg "Removing broken symlinks..."
  find -L "$builddir" -type l -printf 'Removing %P\n' -delete

  msg "Removing loose objects..."
  find "$builddir" -type f -name '*.o' -printf 'Removing %P\n' -delete

  msg "Stripping build tools..."
  local file
  while read -rd '' file; do
    case "$(file -Sib "$file")" in
      application/x-sharedlib\;*)      # Libraries (.so)
        strip -v $STRIP_SHARED "$file" ;;
      application/x-archive\;*)        # Libraries (.a)
        strip -v $STRIP_STATIC "$file" ;;
      application/x-executable\;*)     # Binaries
        strip -v $STRIP_BINARIES "$file" ;;
      application/x-pie-executable\;*) # Relocatable binaries
        strip -v $STRIP_SHARED "$file" ;;
    esac
  done < <(find "$builddir" -type f -perm -u+x ! -name vmlinux -print0)

  msg "Stripping vmlinux..."
  strip -v $STRIP_STATIC "$builddir/vmlinux"

  msg "Adding symlink..."
  mkdir -p "$pkgdir/usr/src"
  ln -sr "$builddir" "$pkgdir/usr/src/$pkgbase"
}

sha256sums=('30909eb2e0434dce97a93cd97ed0dfab7688a124bc3ebc3ecf6c776de09ccc0b'
            '09bc22332affedcdf96cfa7b4ff3dcf1d087d1bde818b9929f5ad1102bc4f775'
            '2dd41feb40495348e83f9d774a6ce2b9672621601215990a79c136040fd65091'
            'd3ee8b341a389a6ef9c614876862924c3c0aff2f1ee2e67b90e06a5a39778683'
            '56bb7873a1a9abdcec0797709cefb486f7e00e9a792c00be4f390b2408669c9d'
            '74d12e96b8ce056a5f1b4fd10cf3f4b671eb3d50d4124cd8fa7a81c83b55ae1e'
            '994514f16122c25e6b8debf79aab539f92ad3f25f94729197912f250eaf75a11'
            '57b0e324bbb1c3017899b76cdeb01ce4670599378017c47852787996d63189ef'
            'e96ca0986eee226aa74501cc400363d38e8355040ac0d6b2d2be009cd2210c02'
            'fb7daf2046c9ad11aa8409eb3f0f7ca53b8de216f2efce9390940a441831dfa3'
            '9d9dbd0f7288fc0508d650e5b35f3d3c329416ff5fce19b6c2ba27a0932ef661'
            '428a323e29c3944956ba08611b2569e51e74142e52e6b924ce312207b1a824a7'
            '3480c98c5b4416e6dadf5d5f935dc9a1b50c38f949228089d7ee06f83169ae50'
            'c323e50d0bcb336186ceca83eeae8a75f9598e4f8a765cd2ae7f3df2e1a3f4cc'
            '2fe247a57584fb1b1e3188503a0f6fd28aa7ddceffbb2350d344062f0f0e6131'
            '3f87680763d1db945205ea10492c1d1d081882b52b2b4db5c9c5d44a7704f9d4'
            '1d0d797b283ae72ed38d8c7d0691172f9c4e1201e3d2573403936b571dffc6e3'
            'caa0a2dfd2374bb5a9ed6a784bf3987caa27f65bc0ef43788a503f9932ddfe67'
            '37842271915562e4ab6e1edae833545644aa09509dfebd6e8a5ddc3b1d8c6bce'
            '3db50e53e9ec604b0076e12f4af04b7ef067704a4f45fe0bec88309604532b9f'
            '8759e49e691eb48913e0f4dbc814f99f943f9796e7e38a98b381d3f3fd5a0469')

pkgname=($pkgbase $pkgbase-headers)
for _p in "${pkgname[@]}"; do
  eval "package_$_p() {
    $(declare -f "_package${_p#$pkgbase}")
    _package${_p#$pkgbase}
  }"
done

# vim:set ts=8 sts=2 sw=2 et:
