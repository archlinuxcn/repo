# Maintainer: edward-p <edward At edward-p Dot xyz>

pkgname=proxmark3-iceman-git
pkgver=6915.bfec7648
pkgrel=1
pkgdesc=pkgdesc='RRG / Iceman repo - Proxmark3 RDV4.0 and other Proxmark3 platforms.'
arch=('x86_64')
url='https://github.com/RfidResearchGroup/proxmark3'
license=('GPL2')
depends=('libusb' 'perl')
makedepends=('git' 'arm-none-eabi-gcc' 'arm-none-eabi-newlib')
provides=('proxmark3' 'proxmark3-iceman')
conflicts=('proxmark3' 'proxmark3-iceman')
replaces=($pkgname'-generic' $pkgname'-rdv4')
source=("$pkgname::git+https://github.com/RfidResearchGroup/proxmark3.git")
sha512sums=('SKIP')
install=proxmark3-iceman-git.install

pkgver() {
  cd $pkgname
  echo $(git rev-list --count HEAD).$(git rev-parse --short HEAD)
}

prepare() {
  export PM3_DOC_PATH="/usr/share/doc/proxmark3"
  export PM3_SHARE_PATH="/usr/share/proxmark3"
  export PM3_BIN_PATH="/usr/bin"
  export UDEV_PREFIX="/usr/lib/udev/rules.d"
}

build() {
  cd "${srcdir}/${pkgname}"
  mkdir "firmware"
  # Build firmware and recovery for pm3rdv4
  make PLATFORM=PM3RDV4 PLATFORM_EXTRAS=BTADDON fullimage recovery
  mv "armsrc/obj/fullimage.elf" "firmware/fullimage-rdv4.elf"
  mv "recovery/proxmark3_recovery.bin" "firmware/proxmark3_recovery-rdv4.bin"

  make clean

  # Build firmware and recovery for generic pm3 and other targets
  make PLATFORM=PM3OTHER all

  mv "armsrc/obj/fullimage.elf" "firmware/fullimage-generic.elf"
  mv "recovery/proxmark3_recovery.bin" "firmware/proxmark3_recovery-generic.bin"

}

package() {
  cd "${srcdir}/${pkgname}"
  
  # Install firmwares
  mv "tools/simmodule/SIM011.sha512.txt" "firmware/"
  mv "tools/simmodule/SIM011.BIN" "firmware/"
  mv "bootrom/obj/bootrom.elf" "firmware/"
  for file in $(ls firmware); do
    install -Dm 644 "firmware/$file" "${pkgdir}/$PM3_SHARE_PATH/firmware/$file"
  done

  # Install executables
  install -Dm 755 "client/proxmark3" "${pkgdir}/$PM3_BIN_PATH/proxmark3"
  #install -Dm 755 "proxmark3.sh" "${pkgdir}/$PM3_BIN_PATH/p3"
  install -Dm 755 "client/flasher" "${pkgdir}/$PM3_BIN_PATH/proxmark3-flasher"
  #install -Dm 755 "flash-all.sh" "${pkgdir}/$PM3_BIN_PATH/pm3-flash-all"
  #install -Dm 755 "flash-bootrom.sh" "${pkgdir}/$PM3_BIN_PATH/pm3-flash-bootrom"
  #install -Dm 755 "flash-fullimage.sh" "${pkgdir}/$PM3_BIN_PATH/pm3-flash-fullimage"

  # Install tools
  install -Dm 755 "tools/mfkey/mfkey32" "${pkgdir}/$PM3_SHARE_PATH/tools/mfkey32"
  install -Dm 755 "tools/mfkey/mfkey32v2" "${pkgdir}/$PM3_SHARE_PATH/tools/mfkey32v2"
  install -Dm 755 "tools/mfkey/mfkey64" "${pkgdir}/$PM3_SHARE_PATH/tools/mfkey64"
  install -Dm 755 "tools/nonce2key/nonce2key" "${pkgdir}/$PM3_SHARE_PATH/tools/nonce2key"
  install -Dm 755 "client/pm3_eml2lower.sh" "${pkgdir}/$PM3_SHARE_PATH/tools/pm3_eml2lower.sh"
  install -Dm 755 "client/pm3_eml2upper.sh" "${pkgdir}/$PM3_SHARE_PATH/tools/pm3_eml2upper.sh"
  install -Dm 755 "client/pm3_mfdread.py" "${pkgdir}/$PM3_SHARE_PATH/tools/pm3_mfdread.py"
  install -Dm 755 "client/pm3_mfd2eml.py" "${pkgdir}/$PM3_SHARE_PATH/tools/pm3_mfd2eml.py"
  install -Dm 755 "client/pm3_eml2mfd.py" "${pkgdir}/$PM3_SHARE_PATH/tools/pm3_eml2mfd.py"
  install -Dm 755 "tools/findbits.py" "${pkgdir}/$PM3_SHARE_PATH/tools/findbits.py"
  install -Dm 755 "tools/rfidtest.pl" "${pkgdir}/$PM3_SHARE_PATH/tools/rfidtest.pl"
  install -Dm 755 "tools/xorcheck.py" "${pkgdir}/$PM3_SHARE_PATH/tools/xorcheck.py"
  cp -a "tools/jtag_openocd" "${pkgdir}/$PM3_SHARE_PATH/"
  
  # Install udev rules
  install -Dm 644 "driver/77-pm3-usb-device-blacklist.rules" "${pkgdir}/$UDEV_PREFIX/77-pm3-usb-device-blacklist.rules"

  # Install others
  cp -a "client/lualibs" "${pkgdir}/$PM3_SHARE_PATH/"
  cp -a "client/luascripts" "${pkgdir}/$PM3_SHARE_PATH/"

  cp -a "client/resources" "${pkgdir}/$PM3_SHARE_PATH/"

  cp -a "traces" "${pkgdir}/$PM3_SHARE_PATH/"
  install -dm 755 "${pkgdir}/$PM3_DOC_PATH"
  cp -a doc/* "${pkgdir}/$PM3_DOC_PATH/"
  cp -a "client/dictionaries" "${pkgdir}/$PM3_SHARE_PATH/"
}
