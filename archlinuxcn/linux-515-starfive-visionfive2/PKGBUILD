# Maintainer: Estela ad Astra <i@estela.cn>

pkgbase=linux-515-starfive-visionfive2
_variant=VF2 #5.15-VF2-xxx-x
pkgver=2.10.4
epoch=1 #Change to use ver from StarFive's SDK
pkgrel=3
_tag=VF2_v${pkgver}
_desc='Linux 5.15 for StarFive RISC-V VisionFive 2 Board'
_srcname=linux-$_tag
url="https://github.com/starfive-tech/linux/"
arch=(riscv64)
license=(GPL2)
makedepends=(bc libelf pahole cpio perl tar xz)
options=('!strip')
source=("https://github.com/starfive-tech/linux/archive/refs/tags/${_tag}.tar.gz"
  "0001-csr-fix.patch::https://github.com/torvalds/linux/commit/6df2a016c0c8a3d0933ef33dd192ea6606b115e3.diff"
  "0002-realloc-fix.patch::https://github.com/torvalds/linux/commit/52a9dab6d892763b2a8334a568bd4e2c1a6fde66.diff"
  "0003-constify-struct-dh.patch" #Modified from https://github.com/torvalds/linux/commit/215bebc8c6ac438c382a6a56bd2764a2d4e1da72.diff"
  "0004-tda998x.patch"
  "0005-pahole-flags.patch"
  'config'
  'linux.preset'
  '90-linux.hook')

sha256sums=('5614f50f29fd4aa56525e0b002b5b03ef4109ef92484aab6747516efd2fb213b'
            '3459b3799b7f9b7d6129ca8996c40d6a12f89127fe54b4af99ec9512b711dced'
            '26c03a99bb0f90e334289726f041f454ca9c54f2bbd553bff7ee5ab042f64775'
            '10d29b13ebccd1ea836e89338f6e88874dd6bb80cd01324527cc3ea7108cd65f'
            'f3bc5d054cde348d9bcb2f7eb2be7c3421e60e55efdc2c849f8058ab8e6b9c7a'
            '5d7e122d49915adae57e7453082860950dc62d599602438e2f1d0ca226710c9b'
            'b365069f42eaaf78ef4155b8526f3b6165f5bfe1a0ad7489f785d2ce2da77436'
            '57acae869144508c5600d6c8f41664f073f731c40cad2c58d2a1d55240495ddb'
            '5308a6dcabff290c627cab5c9db23c739eddbf7aa8a4984468ed59e6a5250702')

if [ $(uname -m) != riscv64 ]; then
  shopt -s expand_aliases
  alias make="make ARCH=riscv CROSS_COMPILE=riscv64-linux-gnu-"
  alias strip=riscv64-linux-gnu-strip
  CFLAGS="-march=rv64gc -mabi=lp64d -O2 -pipe -fno-plt -fexceptions \
          -Wp,-D_FORTIFY_SOURCE=2 -Wformat -Werror=format-security \
          -fstack-clash-protection"
fi

prepare() {
  cd $_srcname

  local src
  for src in $(ls ../); do
    [[ $src = *.patch ]] || continue
    echo "Applying patch $src..."
    patch -Np1 <"../$src"
  done

  echo "Setting version..."
  scripts/setlocalversion --save-scmversion
  echo "-${_variant}" >localversion.10-variant
  echo "-${pkgver}" >localversion.20-pkgver
  echo "-$pkgrel" >localversion.30-pkgrel

  echo "Setting config..."
  cp ../config .config
  make olddefconfig
  #make starfive_visionfive2_defconfig
  cp .config ../../config.new

  make -s kernelrelease >version
  echo "Prepared $pkgbase version $(<version)"
}

build() {
  cd $_srcname
  make all
}

_package() {
  pkgdesc="The $_desc kernel and modules"
  depends=(coreutils kmod mkinitcpio)
  optdepends=('wireless-regdb: to set the correct wireless channels of your country'
    'linux-firmware: firmware images needed for some devices')
  provides=("linux=${pkgver}" "WIREGUARD-MODULE")
  conflicts=('linux')

  cd $_srcname
  local kernver="$(<version)"
  local modulesdir="$pkgdir/usr/lib/modules/$kernver"

  echo "Installing boot image..."
  install -Dm644 "arch/riscv/boot/Image.gz" "$modulesdir/vmlinuz"
  install -Dm644 "arch/riscv/boot/Image.gz" "$pkgdir/boot/vmlinuz"

  echo "Installing modules..."
  make INSTALL_MOD_PATH="$pkgdir/usr" INSTALL_MOD_STRIP=1 modules_install

  echo "Installing dtbs..."
  make INSTALL_DTBS_PATH="$pkgdir/usr/share/dtbs/$kernver" dtbs_install
  make INSTALL_DTBS_PATH="$pkgdir/boot/dtbs/" dtbs_install

  # remove build links
  rm "$modulesdir"/build

  install -Dm644 ../linux.preset "${pkgdir}/etc/mkinitcpio.d/linux.preset"
  install -Dm644 ../90-linux.hook "${pkgdir}/usr/share/libalpm/hooks/90-linux.hook"

}

_package-headers() {
  pkgdesc="Headers and scripts for building modules for the $_desc kernel"
  depends=(pahole)
  provides=("linux-headers=${pkgver}")
  conflicts=('linux-headers')

  cd $_srcname
  local builddir="$pkgdir/usr/lib/modules/$(<version)/build"

  echo "Installing build files..."
  install -Dt "$builddir" -m644 .config Makefile Module.symvers System.map \
    version vmlinux
  install -Dt "$builddir/kernel" -m644 kernel/Makefile
  install -Dt "$builddir/arch/riscv" -m644 arch/riscv/Makefile
  cp -t "$builddir" -a scripts

  # required when DEBUG_INFO_BTF_MODULES is enabled
  cp --parents -r -t "$builddir/" tools/bpf/resolve_btfids

  echo "Installing headers..."
  cp -t "$builddir" -a include
  cp -t "$builddir/arch/riscv" -a arch/riscv/include
  install -Dt "$builddir/arch/riscv/kernel" -m644 arch/riscv/kernel/asm-offsets.s

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
    [[ $arch = */riscv/ ]] && continue
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
    application/x-sharedlib\;*) # Libraries (.so)
      strip -v $STRIP_SHARED "$file" ;;
    application/x-archive\;*) # Libraries (.a)
      strip -v $STRIP_STATIC "$file" ;;
    application/x-executable\;*) # Binaries
      strip -v $STRIP_BINARIES "$file" ;;
    application/x-pie-executable\;*) # Relocatable binaries
      strip -v $STRIP_SHARED "$file" ;;
    esac
  done < <(find "$builddir" -type f -perm -u+x ! -name vmlinux -print0)

  echo "Adding symlink..."
  mkdir -p "$pkgdir/usr/src"
  ln -sr "$builddir" "$pkgdir/usr/src/$pkgbase"
}

pkgname=("$pkgbase" "$pkgbase-headers")
for _p in "${pkgname[@]}"; do
  eval "package_$_p() {
    $(declare -f "_package${_p#$pkgbase}")
    _package${_p#$pkgbase}
  }"
done

# vim:set ts=8 sts=2 sw=2 et:
