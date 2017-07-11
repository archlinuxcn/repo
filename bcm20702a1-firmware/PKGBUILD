# Maintainer: Sonic-Y3k <sonic.y3k@googlemail.com>
# Contributor: Christopher Reimer <archlinux@tjbp.net>
# Contributor: Christoph Hoopmann <christophhoopmann@gmail.com>

pkgbase=bcm20702a1-firmware
pkgname=('bcm4335c0-firmware' 'bcm4350c5-firmware' 'bcm4356a2-firmware' 'bcm20702a1-firmware' 'bcm20702b0-firmware' 'bcm20703a1-firmware' 'bcm43142a0-firmware')
pkgver=1201710
pkgrel=8
arch=('any')
pkgdesc="Broadcom bluetooth firmware."
url="http://asus.com"
license=("Custom")
makedepends=('bluez-utils')
source=("http://dlcdnet.asus.com/pub/ASUS/wireless/USB-BT400/DR_USB_BT400_${pkgver}_Windows.zip"
        "filelist.txt")
sha256sums=('a84889e296add13cae389524b790133519666826ba899c6f82cd6528a80fefcb'
            '03c49bf2e59cf341723ff40a23335c35c432a7c14f652aefae2060d8048624a9')

build() {
  cd "${srcdir}"

  while read p; do
    filename=$(echo $p|awk -F':' '{print $3}'|sed 's% %%g')
    bcm=$(echo $filename|awk -F'_' '{print $1}')
    vid=$(echo $p|awk -F':' '{print tolower($1)}')
    pid=$(echo $p|awk -F':' '{print tolower($2)}')
    hex2hcd "$srcdir/Win10_USB-BT400_DRIVERS/Win10_USB-BT400_Driver_Package/64/$filename" -o "$bcm-$vid-$pid.hcd"
  done < "${srcdir}/filelist.txt"
}

package_bcm4335c0-firmware() {
  pkgdesc="Broadcom bluetooth firmware for BCM4335C0 based devices."
  
  cd "${srcdir}"
  mkdir -p ${pkgdir}/usr/lib/firmware/brcm
  
  for i in BCM4335C0-*.hcd; do
    install -m644 "${srcdir}/$i" "${pkgdir}/usr/lib/firmware/brcm/$i"
  done
}

package_bcm4350c5-firmware() {
  pkgdesc="Broadcom bluetooth firmware for BCM4350C5 based devices."
  conflicts=('bcm4350-firmware')

  cd "${srcdir}"
  mkdir -p ${pkgdir}/usr/lib/firmware/brcm
  
  for i in BCM4350C5-*.hcd; do
    install -m644 "${srcdir}/$i" "${pkgdir}/usr/lib/firmware/brcm/$i"
  done
}

package_bcm4356a2-firmware() {
  pkgdesc="Broadcom bluetooth firmware for BCM4356A2 based devices."

  cd "${srcdir}"
  mkdir -p ${pkgdir}/usr/lib/firmware/brcm
  
  for i in BCM4356A2-*.hcd; do
    install -m644 "${srcdir}/$i" "${pkgdir}/usr/lib/firmware/brcm/$i"
  done
}

package_bcm20702a1-firmware() {
  pkgdesc="Broadcom bluetooth firmware for BCM20702A1 based devices."
  conflicts=('bt-dw1560-firmware')

  cd "${srcdir}"
  mkdir -p ${pkgdir}/usr/lib/firmware/brcm
  
  for i in BCM20702A1-*.hcd; do
    install -m644 "${srcdir}/$i" "${pkgdir}/usr/lib/firmware/brcm/$i"
  done
}

package_bcm20702a0-firmware() {
  pkgdesc="Broadcom bluetooth firmware for BCM20702A0 based devices."

  cd "${srcdir}"
  mkdir -p ${pkgdir}/usr/lib/firmware/brcm
  
  for i in BCM20702A0-*.hcd; do
    install -m644 "${srcdir}/$i" "${pkgdir}/usr/lib/firmware/brcm/$i"
  done
}

package_bcm20702b0-firmware() {
  pkgdesc="Broadcom bluetooth firmware for BCM20702B0 based devices."

  cd "${srcdir}"
  mkdir -p ${pkgdir}/usr/lib/firmware/brcm
  
  for i in BCM20702B0-*.hcd; do
    install -m644 "${srcdir}/$i" "${pkgdir}/usr/lib/firmware/brcm/$i"
  done
}

package_bcm20703a1-firmware() {
  pkgdesc="Broadcom bluetooth firmware for BCM20703A1 based devices."

  cd "${srcdir}"
  mkdir -p ${pkgdir}/usr/lib/firmware/brcm
  
  for i in BCM20703A1-*.hcd; do
    if [ "$i" == "BCM20703A1-0a5c-6410.hcd" ]; then
      install -m644 "${srcdir}/$i" "${pkgdir}/usr/lib/firmware/brcm/BCM-0a5c-6410.hcd"
    else
      install -m644 "${srcdir}/$i" "${pkgdir}/usr/lib/firmware/brcm/$i"
    fi
  done
}

package_bcm43142a0-firmware() {
  pkgdesc="Broadcom bluetooth firmware for BCM43142A0 based devices."

  cd "${srcdir}"
  mkdir -p ${pkgdir}/usr/lib/firmware/brcm
  
  for i in BCM43142A0-*.hcd; do
    install -m644 "${srcdir}/$i" "${pkgdir}/usr/lib/firmware/brcm/$i"
  done
}

