# Maintainer: Andreas Baumann <mail@andreasbaumann.cc>
# Contributor: Andreas Radke <andyrtr@archlinux.org>

pkgbase=linux-lts515
pkgver=5.15.107
pkgrel=1
pkgdesc='LTS Linux 5.15.x'
url="https://www.kernel.org/"
arch=(x86_64 pentium4 i686 i486)
license=(GPL2)
makedepends=(
  bc libelf pahole cpio perl tar xz
  xmlto python-sphinx python-sphinx_rtd_theme graphviz imagemagick texlive-latexextra
)
options=('!strip')
_srcname=linux-$pkgver
source=(
  https://cdn.kernel.org/pub/linux/kernel/v${pkgver%%.*}.x/${_srcname}.tar.{xz,sign}
  config         # the main kernel config file
  0001-ZEN-Add-sysctl-and-CONFIG-to-disallow-unprivileged-C.patch
  0002-PCI-Add-more-NVIDIA-controllers-to-the-MSI-masking-q.patch
  0003-iommu-intel-do-deep-dma-unmapping-to-avoid-kernel-fl.patch
  0004-Bluetooth-btintel-Fix-bdaddress-comparison-with-garb.patch
  0005-lg-laptop-Recognize-more-models.patch
)
validpgpkeys=(
  'ABAF11C65A2970B130ABE3C479BE3E4300411886'  # Linus Torvalds
  '647F28654894E3BD457199BE38DBBDC86092693E'  # Greg Kroah-Hartman
)
# https://www.kernel.org/pub/linux/kernel/v5.x/sha256sums.asc
sha256sums=('19370e769045681f52cceedb14ecda97e89b1b058133a0c8ad45d35ffbc5afa8'
            'SKIP'
            '53c67354cf91a7dafb964485a5496b208dffdc55436828e7b155b3f6f2e651b6'
            '3b5cfc9ca9cf778ea2c4b619b933cda26519969df2d764b5a687f63cf59974cd'
            'c175fbb141c3cec013c799f694d88310375ac5456042f6a4a1adc7667836d786'
            '8357f000b2b622e73dcfd41c2bad42b5e99fffe8f7ee64f774aa771f86cef43c'
            '5c1ee81fdd5818442af6081de987f9c1a9ce3c8d183566b3dfc19a8433aa3dde'
            '067e8995fcd6f6ed25e0253e9374c0e179a000c154da3e59ce62634945ac5be9')

export KBUILD_BUILD_HOST=archlinux
export KBUILD_BUILD_USER=$pkgbase
export KBUILD_BUILD_TIMESTAMP="$(date -Ru${SOURCE_DATE_EPOCH:+d @$SOURCE_DATE_EPOCH})"

prepare() {
  cd $_srcname

  echo "Setting version..."
  scripts/setlocalversion --save-scmversion
  echo "-$pkgrel" > localversion.10-pkgrel
  echo "${pkgbase#linux}" > localversion.20-pkgname

  local src
  for src in "${source[@]}"; do
    src="${src%%::*}"
    src="${src##*/}"
    [[ $src = *.patch ]] || continue
    echo "Applying patch $src..."
    patch -Np1 < "../$src"
  done

  echo "Setting config..."
  cp ../config .config
  make olddefconfig
  diff -u ../config .config || :

  make -s kernelrelease > version
  echo "Prepared $pkgbase version $(<version)"
}

build() {
  cd $_srcname
  make htmldocs all
}

_package() {
  pkgdesc="The $pkgdesc kernel and modules"
  depends=(coreutils kmod initramfs)
  optdepends=('wireless-regdb: to set the correct wireless channels of your country'
              'linux-firmware: firmware images needed for some devices')
  provides=(VIRTUALBOX-GUEST-MODULES WIREGUARD-MODULE KSMBD-MODULE)
  replaces=(wireguard-lts)

  cd $_srcname
  local kernver="$(<version)"
  local modulesdir="$pkgdir/usr/lib/modules/$kernver"

  echo "Installing boot image..."
  # systemd expects to find the kernel here to allow hibernation
  # https://github.com/systemd/systemd/commit/edda44605f06a41fb86b7ab8128dcf99161d2344
  install -Dm644 "$(make -s image_name)" "$modulesdir/vmlinuz"

  # Used by mkinitcpio to name the kernel
  echo "$pkgbase" | install -Dm644 /dev/stdin "$modulesdir/pkgbase"

  echo "Installing modules..."
  make INSTALL_MOD_PATH="$pkgdir/usr" INSTALL_MOD_STRIP=1 \
    DEPMOD=/doesnt/exist modules_install  # Suppress depmod

  # remove build and source links
  rm "$modulesdir"/{source,build}
}

_package-headers() {
  pkgdesc="Headers and scripts for building modules for the $pkgdesc kernel"
  depends=(pahole)

  cd $_srcname
  local builddir="$pkgdir/usr/lib/modules/$(<version)/build"

  echo "Installing build files..."
  install -Dt "$builddir" -m644 .config Makefile Module.symvers System.map \
    localversion.* version vmlinux
  install -Dt "$builddir/kernel" -m644 kernel/Makefile
  install -Dt "$builddir/arch/x86" -m644 arch/x86/Makefile
  cp -t "$builddir" -a scripts

  # required when STACK_VALIDATION is enabled
  install -Dt "$builddir/tools/objtool" tools/objtool/objtool

  # required when DEBUG_INFO_BTF_MODULES is enabled
  install -Dt "$builddir/tools/bpf/resolve_btfids" tools/bpf/resolve_btfids/resolve_btfids

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
    case "$(file -bi "$file")" in
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

pkgname=("$pkgbase" "$pkgbase-headers" "$pkgbase-docs")
for _p in "${pkgname[@]}"; do
  eval "package_$_p() {
    $(declare -f "_package${_p#$pkgbase}")
    _package${_p#$pkgbase}
  }"
done

# vim:set ts=8 sts=2 sw=2 et:

if [ "${CARCH}" = "i486" -o  "${CARCH}" = "i686" -o "${CARCH}" = "pentium4" ]; then

  # use 32-bit configuration files per subarchitecture instead of main config file
  source_pentium4=('config.pentium4')
  source_i686=('config.i686')
  source_i486=('config.i486')
  # fail if upstream's .config changes
  for ((i=0; i<${#sha256sums[@]}; i++)); do
    if [ "${sha256sums[${i}]}" = '53c67354cf91a7dafb964485a5496b208dffdc55436828e7b155b3f6f2e651b6' ]; then
      sha256sums_pentium4=('0c9e8525c759f0c3f1bb395d3b8fdf697aa28aae139707491bd4a57f40640f9e')
      sha256sums_i686=('8350099d1ff6a209b0008817b324cbf4256003de9e50d1bb6302825c49ba429d')
      sha256sums_i486=('fec0298fe19b73f24b4fa587b0184650604023af3f60cf482c85e0d5c8e870b9')
    fi
  done

  # copy architecture specific config file, not default 'config'
  eval "$(
    declare -f prepare | \
      sed '
        s,\.\./config,../config.$CARCH,
      '
  )"

  # patch architecture when copying the kernel Makefile
  eval "$(
    declare -f package_linux-lts515-headers | \
      sed '
        \,/tools/objtool" ,d
        \,arch/x86/Makefile, {
          a \
          install -t "${builddir}/arch/x86" -m644 arch/x86/Makefile_32.cpu
        }
      '
  )"

  # avoid using zstd compression in ultra mode (exhausts virtual memory)
  source+=('no-ultra-zstd.patch')
  sha256sums+=('3997ce6033fdf950a9960f1db720b38c47b1a2e06ab75fc6712c154f596e7c47')
  # upstream prepare() does already do the *.patch patching

  # temporarily disabled documentation due to sphinx_rtd_theme (FS32#163)
  pkgname=(
    $(
      printf '%s\n' "${pkgname[@]}" | \
        grep -v '^\$pkgbase-docs'
    )
  )
  eval "$(
    declare -f build | \
      sed '
        s/\bhtmldocs\b//
      '
  )"
  makedepends=(${makedepends[@]//python-sphinx_rtd_theme/})
  makedepends=(${makedepends[@]//python-sphinx/})
  makedepends=(${makedepends[@]//graphviz/})
  makedepends=(${makedepends[@]//imagemagick/})
  makedepends=(${makedepends[@]//texlive-latexextra/})
fi
