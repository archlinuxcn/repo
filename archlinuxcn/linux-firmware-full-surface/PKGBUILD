# Maintainer: Peter Cai <peter@typeblog.net>
# Thanks: Frans-Willem Hardijzer <fw@hardijzer.nl>

_pkgname=linux-firmware
pkgbase=linux-firmware-full-surface
pkgname=(
  linux-firmware-full-surface-pro-3
  linux-firmware-full-surface-pro-4
  linux-firmware-full-surface-pro-2017
  linux-firmware-full-surface-pro-6
  linux-firmware-full-surface-studio
  linux-firmware-full-surface-laptop
  linux-firmware-full-surface-laptop-2
  linux-firmware-full-surface-book
  linux-firmware-full-surface-book-2
  linux-firmware-full-surface-book-2-1793
  linux-firmware-full-surface-go
)
_commit=efd2c1cc375cff1c17b4259d99a7fee240c3b510 # master
_jakeday_commit=5d21cc824c9b41e65f92fdebcbcccd2181b9393f
_core_repo_ver=20190313.efd2c1c # Update this on each release to correspond to linux-firmware of core
_last_updated=20190320
pkgver=20190320.efd2c1.5d21cc
pkgrel=1
pkgdesc="Firmware files for Linux, patched for surface"
makedepends=('git' 'unzip')
arch=('any')
url="http://git.kernel.org/?p=linux/kernel/git/firmware/linux-firmware.git;a=summary"
license=('GPL2' 'GPL3' 'custom')
options=(!strip)
source=(
  "git+https://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git#commit=${_commit}"
  "git+https://github.com/jakeday/linux-surface.git#commit=${_jakeday_commit}"
)
md5sums=('SKIP'
         'SKIP')

pkgver() {
  echo ${_last_updated}.${_commit:0:6}.${_jakeday_commit:0:6}
}

prepare() {
  cd "${srcdir}/${_pkgname}"
}

build() {
  cd "${srcdir}/${_pkgname}"
}

package_orig() {
  provides=("linux-firmware=${_core_repo_ver}")
  conflicts=('linux-firmware'
             'linux-firmware-git'
             ${pkgname/full-/}
             'kernel26-firmware'
             'ar9170-fw'
             'iwlwifi-1000-ucode'
             'iwlwifi-3945-ucode'
             'iwlwifi-4965-ucode'
             'iwlwifi-5000-ucode'
             'iwlwifi-5150-ucode'
             'iwlwifi-6000-ucode'
             'rt2870usb-fw'
             'rt2x00-rt61-fw'
             'rt2x00-rt71w-fw')

  cd "${srcdir}/${_pkgname}"

  make DESTDIR="${pkgdir}" FIRMWAREDIR=/usr/lib/firmware install
  rm "${pkgdir}/usr/lib/firmware/"{Makefile,README,configure,GPL-3}

  install -d "${pkgdir}/usr/share/licenses/${_pkgname}"
  install -Dm644 LICEN* WHENCE "${pkgdir}/usr/share/licenses/linux-firmware/"

  # Trigger a microcode reload for configurations not using early updates
  install -d "${pkgdir}/usr/lib/tmpfiles.d"
  echo 'w /sys/devices/system/cpu/microcode/reload - - - - 1' \
    >"${pkgdir}/usr/lib/tmpfiles.d/${_pkgname}.conf"
}

package_linux-firmware-surface-common() {
  install -d "${pkgdir}/usr/lib/firmware/mrvl"
  unzip -o "${srcdir}/linux-surface/firmware/mrvl_firmware.zip" -d "${pkgdir}/usr/lib/firmware/mrvl/"
  install -d "${pkgdir}/usr/lib/firmware/mwlwifi"
  unzip -o "${srcdir}/linux-surface/firmware/mwlwifi_firmware.zip" -d "${pkgdir}/usr/lib/firmware/mwlwifi/"
}

package_linux-firmware-full-surface-pro-3() {
  package_orig
  install -d "${pkgdir}/usr/lib/firmware/i915"
  unzip -o "${srcdir}/linux-surface/firmware/i915_firmware_bxt.zip" -d "${pkgdir}/usr/lib/firmware/i915/"
  package_linux-firmware-surface-common
}

package_linux-firmware-full-surface-pro-4() {
  package_orig
  install -d "${pkgdir}/usr/lib/firmware/intel/ipts"
  unzip -o "${srcdir}/linux-surface/firmware/ipts_firmware_v78.zip" -d "${pkgdir}/usr/lib/firmware/intel/ipts/"
  install -d "${pkgdir}/usr/lib/firmware/i915"
  unzip -o "${srcdir}/linux-surface/firmware/i915_firmware_skl.zip" -d "${pkgdir}/usr/lib/firmware/i915/"
  package_linux-firmware-surface-common
}

package_linux-firmware-full-surface-pro-2017() {
  package_orig
  install -d "${pkgdir}/usr/lib/firmware/intel/ipts"
  unzip -o "${srcdir}/linux-surface/firmware/ipts_firmware_v102.zip" -d "${pkgdir}/usr/lib/firmware/intel/ipts/"
  install -d "${pkgdir}/usr/lib/firmware/i915"
  unzip -o "${srcdir}/linux-surface/firmware/i915_firmware_kbl.zip" -d "${pkgdir}/usr/lib/firmware/i915/"
  package_linux-firmware-surface-common
}

package_linux-firmware-full-surface-pro-6() {
  package_orig
  install -d "${pkgdir}/usr/lib/firmware/intel/ipts"
  unzip -o "${srcdir}/linux-surface/firmware/ipts_firmware_v102.zip" -d "${pkgdir}/usr/lib/firmware/intel/ipts/"
  install -d "${pkgdir}/usr/lib/firmware/i915"
  unzip -o "${srcdir}/linux-surface/firmware/i915_firmware_kbl.zip" -d "${pkgdir}/usr/lib/firmware/i915/"
  package_linux-firmware-surface-common
}

package_linux-firmware-full-surface-studio() {
  package_orig
  install -d "${pkgdir}/usr/lib/firmware/intel/ipts"
  unzip -o "${srcdir}/linux-surface/firmware/ipts_firmware_v76.zip" -d "${pkgdir}/usr/lib/firmware/intel/ipts/"
  install -d "${pkgdir}/usr/lib/firmware/i915"
  unzip -o "${srcdir}/linux-surface/firmware/i915_firmware_skl.zip" -d "${pkgdir}/usr/lib/firmware/i915/"
  package_linux-firmware-surface-common
}

package_linux-firmware-full-surface-laptop() {
  package_orig
  install -d "${pkgdir}/usr/lib/firmware/intel/ipts"
  unzip -o "${srcdir}/linux-surface/firmware/ipts_firmware_v79.zip" -d "${pkgdir}/usr/lib/firmware/intel/ipts/"
  install -d "${pkgdir}/usr/lib/firmware/i915"
  unzip -o "${srcdir}/linux-surface/firmware/i915_firmware_kbl.zip" -d "${pkgdir}/usr/lib/firmware/i915/"
  package_linux-firmware-surface-common
}

package_linux-firmware-full-surface-laptop-2() {
  package_orig
  install -d "${pkgdir}/usr/lib/firmware/intel/ipts"
  unzip -o "${srcdir}/linux-surface/firmware/ipts_firmware_v79.zip" -d "${pkgdir}/usr/lib/firmware/intel/ipts/"
  install -d "${pkgdir}/usr/lib/firmware/i915"
  unzip -o "${srcdir}/linux-surface/firmware/i915_firmware_kbl.zip" -d "${pkgdir}/usr/lib/firmware/i915/"
  package_linux-firmware-surface-common
}

package_linux-firmware-full-surface-book() {
  package_orig
  install -d "${pkgdir}/usr/lib/firmware/intel/ipts"
  unzip -o "${srcdir}/linux-surface/firmware/ipts_firmware_v76.zip" -d "${pkgdir}/usr/lib/firmware/intel/ipts/"
  install -d "${pkgdir}/usr/lib/firmware/i915"
  unzip -o "${srcdir}/linux-surface/firmware/i915_firmware_skl.zip" -d "${pkgdir}/usr/lib/firmware/i915/"
  package_linux-firmware-surface-common
}

package_linux-firmware-full-surface-book-2() {
  package_orig
  install -d "${pkgdir}/usr/lib/firmware/intel/ipts"
  unzip -o "${srcdir}/linux-surface/firmware/ipts_firmware_v137.zip" -d "${pkgdir}/usr/lib/firmware/intel/ipts/"
  install -d "${pkgdir}/usr/lib/firmware/i915"
  unzip -o "${srcdir}/linux-surface/firmware/i915_firmware_kbl.zip" -d "${pkgdir}/usr/lib/firmware/i915/"
  install -d "${pkgdir}/usr/lib/firmware/nvidia/gp108"
  unzip -o "${srcdir}/linux-surface/firmware/nvidia_firmware_gp108.zip" -d "${pkgdir}/usr/lib/firmware/nvidia/gp108/"
  install -d "${pkgdir}/usr/lib/firmware/nvidia/gv100"
  unzip -o "${srcdir}/linux-surface/firmware/nvidia_firmware_gv100.zip" -d "${pkgdir}/usr/lib/firmware/nvidia/gv100/"
  package_linux-firmware-surface-common
}

package_linux-firmware-full-surface-book-2-1793() {
  package_orig
  install -d "${pkgdir}/usr/lib/firmware/intel/ipts"
  unzip -o "${srcdir}/linux-surface/firmware/ipts_firmware_v101.zip" -d "${pkgdir}/usr/lib/firmware/intel/ipts/"
  install -d "${pkgdir}/usr/lib/firmware/i915"
  unzip -o "${srcdir}/linux-surface/firmware/i915_firmware_kbl.zip" -d "${pkgdir}/usr/lib/firmware/i915/"
  install -d "${pkgdir}/usr/lib/firmware/nvidia/gp108"
  unzip -o "${srcdir}/linux-surface/firmware/nvidia_firmware_gp108.zip" -d "${pkgdir}/usr/lib/firmware/nvidia/gp108/"
  install -d "${pkgdir}/usr/lib/firmware/nvidia/gv100"
  unzip -o "${srcdir}/linux-surface/firmware/nvidia_firmware_gv100.zip" -d "${pkgdir}/usr/lib/firmware/nvidia/gv100/"
  package_linux-firmware-surface-common
}

package_linux-firmware-full-surface-go() {
  package_orig
  install -d "${pkgdir}/usr/lib/firmware/intel/ath10k"
  unzip -o "${srcdir}/linux-surface/firmware/ath10k_firmware.zip" -d "${pkgdir}/usr/lib/firmware/intel/ath10k/"
  package_linux-firmware-surface-common
}

# vim:set ts=2 sw=2 et:

