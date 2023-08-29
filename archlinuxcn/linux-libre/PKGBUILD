# Maintainer : Daniel Bermond <dbermond@archlinux.org>
# Contributor: Jonas Heinrich <onny@project-insanity.org>
# Contributor: André Silva <emulatorman@riseup.net>
# Contributor: Márcio Silva <coadde@riseup.net>
# Contributor (Parabola): Nicolás Reynolds <fauno@kiwwwi.com.ar>
# Contributor (Parabola): Sorin-Mihai Vârgolici <smv@yobicore.org>
# Contributor (Parabola): Michał Masłowski <mtjm@mtjm.eu>
# Contributor (Parabola): Luke Shumaker <lukeshu@sbcglobal.net>
# Contributor (Parabola): Luke R. <g4jc@openmailbox.org>

# Based on linux package

_replacesarchkernel=('linux%') # '%' gets replaced with kernel suffix
_replacesoldkernels=() # '%' gets replaced with kernel suffix
_replacesoldmodules=() # '%' gets replaced with kernel suffix

pkgbase=linux-libre
pkgver=6.3.3
pkgrel=1
pkgdesc='Linux-libre'
rcnver=5.18.12
rcnrel=armv7-x8
url='https://linux-libre.fsfla.org/'
arch=(i686 x86_64 armv7h)
license=(GPL2)
makedepends=(
  bc
  cpio
  gettext
  git
  libelf
  pahole
  perl
  tar
  xz

  # htmldocs
  graphviz
  imagemagick
  python-sphinx
  texlive-latexextra
  xmlto
)
makedepends_armv7h=(uboot-tools vboot-utils dtc) # required by linux-libre-chromebook
options=('!strip')
_srcname=linux-6.3
source=(
  "https://linux-libre.fsfla.org/pub/linux-libre/releases/${_srcname##*-}-gnu/linux-libre-${_srcname##*-}-gnu.tar.xz"{,.sign}
  "https://linux-libre.fsfla.org/pub/linux-libre/releases/$pkgver-gnu/patch-${_srcname##*-}-gnu-$pkgver-gnu.xz"{,.sign}
  "https://repo.parabola.nu/other/linux-libre/logos/logo_linux_"{clut224.ppm,vga16.ppm,mono.pbm}{,.sig}
  config.i686 config.x86_64 config.armv7h    # the main kernel config files
  linux-armv7h.preset                        # armv7h preset file for mkinitcpio ramdisk
  "kernel"{.its,.keyblock,_data_key.vbprivk} # files for signing Chromebooks kernels

  # maintain the TTY over USB disconnects
  # http://www.coreboot.org/EHCI_Gadget_Debug
  0001-usb-serial-gadget-no-TTY-hangup-on-USB-disconnect-WI.patch
  # fix Atmel maXTouch touchscreen support
  # https://labs.parabola.nu/issues/877
  # http://www.fsfla.org/pipermail/linux-libre/2015-November/003202.html
  0002-fix-Atmel-maXTouch-touchscreen-support.patch
  # Arch Linux patches
  0001-ZEN-Add-sysctl-and-CONFIG-to-disallow-unprivileged-C.patch
  0002-drm-amd-display-Have-Payload-Properly-Created-After-.patch
)
source_i686=(
  # avoid using zstd compression in ultra mode (exhausts virtual memory)
  no-ultra-zstd.patch
)
source_armv7h=(
  # RCN patch (CM3 firmware deblobbed and bloatware removed)
  #"https://repo.parabola.nu/other/rcn-libre/patches/$rcnver/rcn-libre-$rcnver-$rcnrel.patch"{,.sig}
  # Arch Linux ARM patches
  0001-ARM-atags-add-support-for-Marvell-s-u-boot.patch
  0002-ARM-atags-fdt-retrieve-MAC-addresses-from-Marvell-bo.patch
  0003-fix-mvsdio-eMMC-timing.patch
  0004-net-smsc95xx-Allow-mac-address-to-be-set-as-a-parame.patch
  0005-set-default-cubietruck-led-triggers.patch
  0006-exynos4412-odroid-set-higher-minimum-buck2-regulator.patch
  0007-USB-Armory-MkII-support.patch
  # ChromiumOS patch
  # https://labs.parabola.nu/issues/2372
  0001-CHROMIUM-block-partitions-efi-Add-support-for-IGNORE.patch
)
validpgpkeys=(
  '474402C8C582DAFBE389C427BCB7CF877E7D47A7' # Alexandre Oliva
  '6DB9C4B4F0D8C0DC432CF6E4227CA7C556B2BA78' # David P.
)
b2sums=('03c5869a2b432207208d002a3a8b55f42751dc2b50642fcd9ca982cc8da05c7965d359202e49e1418b0ff74307fdeb91d9f41f3293815bc4e508a43104ec1e92'
        'SKIP'
        'cff40934db0b5da1624718bab083fc7e99418ee1f134fbb5d52f47927e32198fdc5117d1e8464dc86f504ce8dc1ad924dff6eb87f7cf844ef7b35861aa2a40c8'
        'SKIP'
        '73fee2ae5cb1ffd3e6584e56da86a8b1ff6c713aae54d77c0dab113890fc673dc5f300eb9ed93fb367b045ece8fa80304ff277fe61665eccf7b7ce24f0c045eb'
        'SKIP'
        'd02a1153a4285b32c774dca4560fe37907ccf30b8e487a681b717ed95ae9bed5988875c0a118938e5885ae9d2857e53a6f216b732b6fa3368e3c5fe08c86382c'
        'SKIP'
        '580911af9431c066bbc072fd22d5e2ef65f12d8358cec5ff5a4f1b7deebb86cef6b5c1ad631f42350af72c51d44d2093c71f761234fb224a8b9dbb3b64b8201d'
        'SKIP'
        'efb4265f5e7554b8daa8ab0ae727ee2dbb53ed685956f6e41a548ff297e4dabd9a6e8a61a74af697fd6253c3a79a01d25cf30a6f4f4c3b9d12835228e7481e05'
        'e0047e808c4f2c4659df36e16a5b3ef9f77853950f9ae572b5cfc77d6b28144636d7a8524ef628c51725bdce629f5e1126eddec24189650e103462493bcbc585'
        '5760e0879cf71dfc1c9bdd557829f28437909e701fa566cc3575a52785c81ac70d634ec929833ac01aea111bbae6ba402add738dc86623b32bcc3b523d43f60f'
        'af69176b1117b94e56b043e97b0bd5873a2974a6a2fd52b102d0ffdca440ff68cfb241d6c4d4ef453cc8c220c236b739bad232e53fd500ce7672fa6e5ba87383'
        'f2d309c1d0a347539a8095223085691a9be228934b2258feb4872784f6cf6c2cc741426e4e755d63128ee57c284eddb13e0c719d4b5f8e101722e4cca4eb3ad5'
        'eeed12b2ab60c3d3aad598a1d44b4f23560d818e8fe1ef143f857c8e176652df53501b192ade7d4d915d425fff818b2a232d46bae0d3a0f46b8959e614e0ede2'
        'aaa4e28a31967cc3a7fe25a86ba35fdfa210cd8b1a9cc96298349cbf01d60cdf146ee519d6803d05b175873f1b3367e47194a178db7ed97c802e59b38f8c303c'
        'c2214154c36900e311531bfe68184f31639f5c50fed23bc3803a7f18439b7ff258552a39f02fed0ea92f10744e17a6c55cef0ef1a98187f978fe480fb3dddc14'
        '0c7ceba7cd90087db3296610a07886f337910bad265a32c052d3a703e6eb8e53f355ab9948d72d366408d968d8ee7435084dd89bef5ed0b69355fd884c2cd468'
        '25b35ceabee03a287f21e7de5907fa760ad63e2e5125ee2c42fb8e4427c5fca1bd62be0bef32a1d46b649b513bb3f892337cc1413768440fe9e9613c51d0f8e3'
        '9c7f23cc063ab6c8878e2785bf415320df1e41687db3e35e99286416d59f4c923b1a8bcf6cd0e51d9e689b063c49451bb765d18b47b9139990c8f5b01710783b')
b2sums_i686=('165ab9dd8cedeaae5327accc1581c19cf0be55f923b03feb889cad3351b74c7c4cd3d3c206938e5152bfe1d947513dea8f630f8f5544099ec13d16d254725c40')
b2sums_armv7h=('73ecc5862c6b4aef7b163c1992004273fbf791b82c75a8602e3def311f682f2b866124c0bfde90d03c7c76bb8b5853bdb9daad6ee2ab0908f4145cda476b8286'
               '15f7b70b5d153e9336006aba873a78f94d91b8df5e1939041f12e678bb9cfbdda2e362001068a07c044ce606cf0d4d2e625002df9c569c914f7ac248d4d3e8ad'
               '6219cec826bc543000ab87cf35dcc713f0635519cf79e75888b213a5e2d1f728e59e70df7fd842dda6e40494bf9cafa9f87368cb75b338c5a157a0adcf583512'
               '66d6cff292962c4c8bbea62b2240c4c53c0c514f9e99864be9244cb846c505e1bedd800ca1347b80883543035d20573b06796e5bacbace6e829880695ffca781'
               'e1d0949abbde146d68cddab53944c0391210fb4ac632a78788ec729dea834cb82698c8beef203608eee5323a07ecd566b9813552498e9ac659942060713c4549'
               '56fdf81b439b6b94e63acfb18d61f90298dc4e29fc65efd4dcf41ae950e87f287f48b42b2be15f4ea0cf7a6d39df3c0ef882cf37b2474e91cc2985fb6cdd1089'
               'd00505c1ac57fd4b53bdb0d9a2172168a23d6082111695c679aeae58e8e749f5b2ef27ce1bc47b0d5fdd81fac792c57d9b45f125a3315b64297b146f727ac467'
               '741ad7ffc9e8200657315fc4111066b2477cde35ecdc5e73976457f17106f80d148d86bf97b92c523fef1cc5a26ddb867d16330f592f2aa4d886be596bedc8df')

_replacesarchkernel=("${_replacesarchkernel[@]/\%/${pkgbase#linux-libre}}")
_replacesoldkernels=("${_replacesoldkernels[@]/\%/${pkgbase#linux-libre}}")
_replacesoldmodules=("${_replacesoldmodules[@]/\%/${pkgbase#linux-libre}}")

case "$CARCH" in
  i686|x86_64) KARCH=x86;;
  armv7h) KARCH=arm;;
esac

export KBUILD_BUILD_HOST=archlinux
export KBUILD_BUILD_USER=$pkgbase
export KBUILD_BUILD_TIMESTAMP="$(date -Ru${SOURCE_DATE_EPOCH:+d @$SOURCE_DATE_EPOCH})"

_make() {
  test -s version
  make KERNELRELEASE="$(<version)" "$@"
}

prepare() {
  cd $_srcname

  if [ "${_srcname##*-}" != "$pkgver" ]; then
    echo "Applying upstream patch..."
    patch -Np1 < "../patch-${_srcname##*-}-gnu-$pkgver-gnu"
  fi

  echo "Adding freedo as boot logo..."
  install -m644 -t drivers/video/logo \
    ../logo_linux_{clut224.ppm,vga16.ppm,mono.pbm}

  echo "Setting version..."
  echo "-$pkgrel" > localversion.10-pkgrel
  echo "${pkgbase#linux-libre}" > localversion.20-pkgname
  make defconfig
  make -s kernelrelease > version
  make mrproper

  if [ "$CARCH" = "armv7h" ]; then
    local src_armv7h
    for src_armv7h in "${source_armv7h[@]}"; do
      src_armv7h="${src_armv7h%%::*}"
      src_armv7h="${src_armv7h##*/}"
      [[ $src_armv7h = *.patch ]] || continue
      echo "Applying patch $src_armv7h..."
      patch -Np1 < "../$src_armv7h"
    done
  fi

  if [ "$CARCH" = "i686" ]; then
    local src_i686
    for src_i686 in "${source_i686[@]}"; do
      src_i686="${src_i686%%::*}"
      src_i686="${src_i686##*/}"
      [[ $src_i686 = *.patch ]] || continue
      echo "Applying patch $src_i686..."
      patch -Np1 < "../$src_i686"
    done
  fi

  local src
  for src in "${source[@]}"; do
    src="${src%%::*}"
    src="${src##*/}"
    [[ $src = *.patch ]] || continue
    echo "Applying patch $src..."
    patch -Np1 < "../$src"
  done

  echo "Setting config..."
  cp ../config.$CARCH .config
  _make olddefconfig
  diff -u ../config.$CARCH .config || :

  echo "Prepared $pkgbase version $(<version)"
}

build() {
  cd $_srcname
  _make htmldocs all
}

_package() {
  pkgdesc="The $pkgdesc kernel and modules"
  depends=(
    coreutils
    initramfs
    kmod
  )
  optdepends=(
    'wireless-regdb: to set the correct wireless channels of your country'
    'linux-libre-firmware: firmware images needed for some devices'
  )
  provides=(
    KSMBD-MODULE "LINUX-ABI_VERSION=$pkgver"
    VIRTUALBOX-GUEST-MODULES
    WIREGUARD-MODULE
  )

  cd $_srcname
  local modulesdir="$pkgdir/usr/lib/modules/$(<version)"

  echo "Installing boot image..."
  # systemd expects to find the kernel here to allow hibernation
  # https://github.com/systemd/systemd/commit/edda44605f06a41fb86b7ab8128dcf99161d2344
  install -Dm644 "$(_make -s image_name)" "$modulesdir/vmlinuz"

  # Used by mkinitcpio to name the kernel
  echo "$pkgbase" | install -Dm644 /dev/stdin "$modulesdir/pkgbase"

  echo "Installing modules..."
  _make INSTALL_MOD_PATH="$pkgdir/usr" INSTALL_MOD_STRIP=1 \
    DEPMOD=/doesnt/exist modules_install  # Suppress depmod

  # remove build and source links
  rm "$modulesdir"/{source,build}

  if [ "$CARCH" = "armv7h" ]; then
    echo "Installing device tree binaries..."
    _make INSTALL_DTBS_PATH="$pkgdir/boot/dtbs/$pkgbase" dtbs_install

    # armv7h presets only work with ALL_kver=$(<version)
    backup=("etc/mkinitcpio.d/$pkgbase.preset")
    echo "Installing mkinitcpio preset..."
    sed "s|%PKGBASE%|$pkgbase|g;s|%KERNVER%|$(<version)|g" ../linux-armv7h.preset \
      | install -Dm644 /dev/stdin "$pkgdir/etc/mkinitcpio.d/$pkgbase.preset"
  fi
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
  install -Dt "$builddir/arch/$KARCH" -m644 arch/$KARCH/Makefile
  if [ "$CARCH" = "i686" ]; then
    install -Dt "$builddir/arch/$KARCH" -m644 arch/$KARCH/Makefile_32.cpu
  fi
  cp -t "$builddir" -a scripts

  # required when STACK_VALIDATION is enabled
  if [[ -e tools/objtool/objtool ]]; then
    install -Dt "$builddir/tools/objtool" tools/objtool/objtool
  fi

  # required when DEBUG_INFO_BTF_MODULES is enabled
  if [[ -e tools/bpf/resolve_btfids/resolve_btfids ]]; then
    install -Dt "$builddir/tools/bpf/resolve_btfids" tools/bpf/resolve_btfids/resolve_btfids
  fi

  echo "Installing headers..."
  cp -t "$builddir" -a include
  cp -t "$builddir/arch/$KARCH" -a arch/$KARCH/include
  install -Dt "$builddir/arch/$KARCH/kernel" -m644 arch/$KARCH/kernel/asm-offsets.s

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
    [[ $arch = */$KARCH/ ]] && continue
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

_package-chromebook() {
  pkgdesc="$pkgdesc kernel sign for Veyron Chromebooks"
  depends=(linux-libre=$pkgver)
  install=$pkgbase-chromebook.install

  cd $_srcname

  cp ../kernel.its .
  mkimage -D "-I dts -O dtb -p 2048" -f kernel.its kernel.signed
  dd if=/dev/zero of=bootloader.bin bs=512 count=1
  echo 'console=tty0 init=/sbin/init root=PARTUUID=%U/PARTNROFF=1 rootwait rw noinitrd' > cmdline

  echo "Creating kernel sign..."
  vbutil_kernel \
    --pack vmlinux.kpart \
    --version 1 \
    --vmlinuz kernel.signed \
    --arch arm \
    --keyblock ../kernel.keyblock \
    --signprivate ../kernel_data_key.vbprivk \
    --config cmdline \
    --bootloader bootloader.bin

  echo "Installing kernel sign..."
  mkdir -p "$pkgdir/boot"
  cp vmlinux.kpart "$pkgdir/boot"
}

pkgname=(
  "$pkgbase"
  "$pkgbase-headers"
  "$pkgbase-docs"
)
[ "$CARCH" = "armv7h" ] && pkgname+=("$pkgbase-chromebook")
for _p in "${pkgname[@]}"; do
  eval "package_$_p() {
    $(declare -f "_package${_p#$pkgbase}")
    _package${_p#$pkgbase}
  }"
done

# vim:set ts=8 sts=2 sw=2 et:
