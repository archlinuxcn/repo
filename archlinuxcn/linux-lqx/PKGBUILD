# Maintainer: Piotr Gorski <lucjan.lucjanov@gmail.com> PGP-Key: BDB26C5A
# Contributor: shivik <> PGP-Key: 761E423C
# Contributor: Michael Duell <mail@akurei.me> PGP-Key: 6EE23EBE
# A special thanks to Steven Barrett for very important suggestions
# Contributor: Jan Alexander Steffens (heftig) <jan.steffens@gmail.com>
# Contributor: Tobias Powalowski <tpowa@archlinux.org>
# Contributor: Thomas Baechler <thomas@archlinux.org>

### BUILD OPTIONS
# Set these variables to ANYTHING that is not null to enable them

### Tweak kernel options prior to a build via nconfig
_makenconfig=

### Tweak kernel options prior to a build via menuconfig
_makemenuconfig=

### Tweak kernel options prior to a build via xconfig
_makexconfig=

### Tweak kernel options prior to a build via gconfig
_makegconfig=

# Compile ONLY used modules to VASTLY reduce the number of modules built
# and the build time.
#
# To keep track of which modules are needed for your specific system/hardware,
# give module_db script a try: https://aur.archlinux.org/packages/modprobed-db
# This PKGBUILD read the database kept if it exists
#
# More at this wiki page ---> https://wiki.archlinux.org/index.php/Modprobed-db
_localmodcfg=

# Use the current kernel's .config file
# Enabling this option will use the .config of the RUNNING kernel rather than
# the ARCH defaults. Useful when the package gets updated and you already went
# through the trouble of customizing your config options.  NOT recommended when
# a new kernel is released, but again, convenient for package bumps.
_use_current=

### Selecting the CPU scheduler
# ATTENTION - one of three predefined values should be selected!
# 'bmq' - select 'BitMap Queue CPU scheduler'
# 'pds' - select 'Priority and Deadline based Skip list multiple queue CPU scheduler'
# 'none' - select 'Completely Fair Scheduler'
_projectc='pds'

### Enable htmldocs (increases compile time)
_htmldocs_enable=

### Do not edit below this line unless you know what you're doing

# pkgname=('linux-lqx' 'linux-lqx-headers' 'linux-lqx-docs')
_major=6.13
_srcname=linux-${_major}
_lqxpatchname=liquorix-package
_lqxpatchrel=8
_lqxpatchver=${_lqxpatchname}-${_major}-${_lqxpatchrel}
pkgbase=linux-lqx
pkgver=6.13.8.lqx3
pkgrel=1
pkgdesc='Linux Liquorix'
url='https://liquorix.net/'
arch=(x86_64)
license=(GPL-2.0-only)
makedepends=(
  bc
  cpio
  gettext
  git
  libelf
  pahole
  perl
  python
  tar
  xz
  zstd
)

if [ -n "$_htmldocs_enable" ]; then
  makedepends+=(
    graphviz
    imagemagick
    python-sphinx
    texlive-latexextra
    xmlto
  )
fi

options=(
  !debug
  !strip
)
#_lucjanpath="https://raw.githubusercontent.com/sirlucjan/kernel-patches/master/${_major}"
_lucjanpath="https://gitlab.com/sirlucjan/kernel-patches/raw/master/${_major}"

source=("https://cdn.kernel.org/pub/linux/kernel/v6.x/${_srcname}.tar.xz"
        "https://cdn.kernel.org/pub/linux/kernel/v6.x/${_srcname}.tar.sign"
        "https://github.com/damentz/${_lqxpatchname}/archive/${_major}-${_lqxpatchrel}.tar.gz")
validpgpkeys=(
    'ABAF11C65A2970B130ABE3C479BE3E4300411886' # Linus Torvalds
    '647F28654894E3BD457199BE38DBBDC86092693E' # Greg Kroah-Hartman
)
sha512sums=('1137e6440132b0958f89165440e99208f82b204e7245ae69dc9c808df97d13ce8f58136db92407e0e93394fa7f6283ec7a34597c6e92a5b6d9025e0960357957'
            'SKIP'
            '0ed175ef6eae6bd25ae4f926272f87329f541add3df8aac94f49eff1a2c76757abfec1f2ca8bf4942bd090921e2ef9e130018762d4c6dc94dddf19e3468044ce')



export KBUILD_BUILD_HOST=archlinux
export KBUILD_BUILD_USER=$pkgbase
export KBUILD_BUILD_TIMESTAMP="$(date -Ru${SOURCE_DATE_EPOCH:+d @$SOURCE_DATE_EPOCH})"

prepare() {
  cd $_srcname

  ### Set package version variables
  _abiname="$(cat ${srcdir}/${_lqxpatchver}/linux-liquorix/debian/config/defines | grep 'abiname:' | sed -r 's/abiname:\s*//')"
  _minor="$(echo "$_abiname" | cut -f1 -d -)"
  _patchrel="$(echo "$_abiname" | cut -f2 -d -)"

  ### Add Liquorix patches
  local _patchfolder="${srcdir}/${_lqxpatchver}/linux-liquorix/debian/patches"
  grep -P '^(zen|lqx)/' "$_patchfolder/series" | while IFS= read -r line
  do
    echo "Patching sources with $line"
    patch -Np1 -i "$_patchfolder/$line"
  done

  ### Setting version
  echo "Setting version..."
  echo "-$pkgrel" > localversion.10-pkgrel
  echo "${pkgbase#linux}" > localversion.20-pkgname

  ### Patching sources
  for p in $(find ../../ -maxdepth 1 -name '*.patch'); do
    echo "Applying patch $p..."
    patch -Np1 -i "$p"
  done

  ### Setting config
  echo "Setting config..."
  cat ${srcdir}/${_lqxpatchver}/linux-liquorix/debian/config/kernelarch-x86/config-arch-64 >./.config
  make olddefconfig
  diff -u ${srcdir}/${_lqxpatchver}/linux-liquorix/debian/config/kernelarch-x86/config-arch-64 .config || :

  ### Prepared version
  make -s kernelrelease > version
  echo "Prepared $pkgbase version $(<version)"

  ### Optionally use running kernel's config
	# code originally by nous; http://aur.archlinux.org/packages.php?ID=40191
	if [ -n "$_use_current" ]; then
		if [[ -s /proc/config.gz ]]; then
			echo "Extracting config from /proc/config.gz..."
			# modprobe configs
			zcat /proc/config.gz > ./.config
		else
			warning "Your kernel was not compiled with IKCONFIG_PROC!"
			warning "You cannot read the current config!"
			warning "Aborting!"
			exit
		fi
	fi

  ### Selecting the CPU scheduler
	if [ "$_projectc" = "bmq" ]; then
		echo "Selecting BMQ CPU scheduler..."
		scripts/config -e CONFIG_SCHED_BMQ
		scripts/config -d CONFIG_SCHED_PDS
	elif [ "$_projectc" = "pds" ]; then
		echo "Selecting PDS CPU scheduler..."
		scripts/config -d CONFIG_SCHED_BMQ
		scripts/config -e CONFIG_SCHED_PDS
	elif [ "$_projectc" = "none" ]; then
		echo "Selecting Completely Fair Scheduler..."
		scripts/config -d CONFIG_SCHED_ALT
	else
		if [ -n "$_projectc" ]; then
			error "The value $_projectc is invalid. Choose the correct one again."
		else
			error "The value is empty. Choose the correct one again."
		fi
		error "Selecting the CPU scheduler failed!"
		exit
	fi

  ### Optionally load needed modules for the make localmodconfig
  # See https://aur.archlinux.org/packages/modprobed-db
  if [ -n "$_localmodcfg" ]; then
    if [ -f $HOME/.config/modprobed.db ]; then
      echo "Running Steven Rostedt's make localmodconfig now"
      make LSMOD=$HOME/.config/modprobed.db localmodconfig
    else
      echo "No modprobed.db data found"
      exit
    fi
  fi

  ## Use DWARF5 debug info for Arch
  echo "Upgrading debug info from toolchain default to DWARF v5..."
  scripts/config -e CONFIG_DEBUG_INFO_DWARF5

  ## Use Arch Wiki TOMOYO configuration: https://wiki.archlinux.org/title/TOMOYO_Linux#Installation_2
  echo "Replacing Debian TOMOYO configuration with upstream Arch Linux..."
  scripts/config --set-str CONFIG_SECURITY_TOMOYO_POLICY_LOADER      "/usr/bin/tomoyo-init"
  scripts/config --set-str CONFIG_SECURITY_TOMOYO_ACTIVATION_TRIGGER "/usr/lib/systemd/systemd"

  ## Add landlock for pacman sandbox support
  echo "Adding 'landlock' to CONFIG_LSM for pacman sandbox support"
  scripts/config --set-str CONFIG_LSM "landlock,lockdown,yama,bpf"

  ### Running make nconfig
	[[ -z "$_makenconfig" ]] ||  make nconfig

  ### Running make menuconfig
	[[ -z "$_makemenuconfig" ]] || make menuconfig

  ### Running make xconfig
	[[ -z "$_makexconfig" ]] || make xconfig

  ### Running make gconfig
	[[ -z "$_makegconfig" ]] || make gconfig

  ### Save configuration for later reuse
	cat .config > "${startdir}/config.last"
}

build() {
  cd $_srcname

  make all
  if [ -n "$_htmldocs_enable" ]; then
    make htmldocs
  fi
  make -C tools/bpf/bpftool vmlinux.h feature-clang-bpf-co-re=1
}

_package() {
  pkgdesc="The $pkgdesc kernel and modules"
  depends=(coreutils kmod initramfs)
  optdepends=('wireless-regdb: to set the correct wireless channels of your country'
              'linux-firmware: firmware images needed for some devices'
              'sof-firmware: firmware images needed for Sound Open Firmware capable devices'
              'modprobed-db: Keeps track of EVERY kernel module that has ever been probed - useful for those of us who make localmodconfig'
              'uksmd: Userspace KSM helper daemon')
  provides=(VIRTUALBOX-GUEST-MODULES WIREGUARD-MODULE UKSMD-BUILTIN VHBA-MODULE)

  cd $_srcname
  local modulesdir="$pkgdir/usr/lib/modules/$(<version)"

  echo "Installing boot image..."
  # systemd expects to find the kernel here to allow hibernation
  # https://github.com/systemd/systemd/commit/edda44605f06a41fb86b7ab8128dcf99161d2344
  install -Dm644 "$(make -s image_name)" "$modulesdir/vmlinuz"

  # Used by mkinitcpio to name the kernel
  echo "$pkgbase" | install -Dm644 /dev/stdin "$modulesdir/pkgbase"

  echo "Installing modules..."
  make INSTALL_MOD_PATH="$pkgdir/usr" INSTALL_MOD_STRIP=1 \
    DEPMOD=/doesnt/exist modules_install  # Suppress depmod

  # remove build link
  rm "$modulesdir"/build
}

_package-headers() {
  pkgdesc="Headers and scripts for building modules for the $pkgdesc kernel"
  depends=('linux-lqx' 'pahole')

  cd $_srcname
  local builddir="$pkgdir/usr/lib/modules/$(<version)/build"

  echo "Installing build files..."
  install -Dt "$builddir" -m644 .config Makefile Module.symvers System.map \
    localversion.* version vmlinux tools/bpf/bpftool/vmlinux.h
  install -Dt "$builddir/kernel" -m644 kernel/Makefile
  install -Dt "$builddir/arch/x86" -m644 arch/x86/Makefile
  cp -t "$builddir" -a scripts

  # required when STACK_VALIDATION is enabled
  install -Dt "$builddir/tools/objtool" tools/objtool/objtool

  # required when DEBUG_INFO_BTF_MODULES is enabled
  install -Dt "$builddir/tools/bpf/resolve_btfids" tools/bpf/resolve_btfids/resolve_btfids \
    || true

  echo "Installing headers..."
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

  echo "Installing KConfig files..."
  find . -name 'Kconfig*' -exec install -Dm644 {} "$builddir/{}" \;

  echo "Removing unneeded architectures..."
  local arch
  for arch in "$builddir"/arch/*/; do
    [[ $arch = */x86/ ]] && continue
    echo "Removing $(basename "$arch")"
    rm -r "$arch"
  done

  echo "Removing documentation..."
  rm -r "$builddir/Documentation"

  echo "Removing broken symlinks..."
  find -L "$builddir" -type l -printf 'Removing %P\n' -delete

  echo "Removing loose objects..."
  find "$builddir" -type f -name '*.o' -printf 'Removing %P\n' -delete

  echo "Stripping build tools..."
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

  echo "Stripping vmlinux..."
  strip -v $STRIP_STATIC "$builddir/vmlinux"

  echo "Adding symlink..."
  mkdir -p "$pkgdir/usr/src"
  ln -sr "$builddir" "$pkgdir/usr/src/$pkgbase"
}

_package-docs() {
  pkgdesc="Documentation for the $pkgdesc kernel"
  depends=('linux-lqx')

  cd $_srcname
  local builddir="$pkgdir/usr/lib/modules/$(<version)/build"

  echo "Installing documentation..."
  local src dst
  while read -rd '' src; do
    dst="${src#Documentation/}"
    dst="$builddir/Documentation/${dst#output/}"
    install -Dm644 "$src" "$dst"
  done < <(find Documentation -name '.*' -prune -o ! -type d -print0)

  echo "Adding symlink..."
  mkdir -p "$pkgdir/usr/share/doc"
  ln -sr "$builddir/Documentation" "$pkgdir/usr/share/doc/$pkgbase"
}

pkgname=(
  "$pkgbase"
  "$pkgbase-headers"
  "$pkgbase-docs"
)
for _p in "${pkgname[@]}"; do
  eval "package_$_p() {
    $(declare -f "_package${_p#$pkgbase}")
    _package${_p#$pkgbase}
  }"
done

# vim:set ts=8 sts=2 sw=2 et:
