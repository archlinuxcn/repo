# Maintainer: Andrey Vihrov <andrey.vihrov at gmail.com>
# Contributor: Frank Vanderham <twelve.eighty (at) gmail.>

pkgname=broadcom-wl-dkms
pkgver=6.30.223.271
pkgrel=2
pkgdesc="Broadcom 802.11 Linux STA wireless driver"
arch=('i686' 'x86_64')
url="https://www.broadcom.com/support/?gid=1"
license=('custom')
depends=('dkms')
optdepends=('linux-headers: If running standard kernel, otherwise find matching headers for your kernel')
conflicts=('broadcom-wl')
backup=('etc/modprobe.d/broadcom-wl-dkms.conf')
install=broadcom-wl-dkms.install
source=('broadcom-wl-dkms.conf'
        'dkms.conf.in')
source_i686=("https://www.broadcom.com/docs/linux_sta/hybrid-v35-nodebug-pcoem-${pkgver//./_}.tar.gz")
source_x86_64=("https://www.broadcom.com/docs/linux_sta/hybrid-v35_64-nodebug-pcoem-${pkgver//./_}.tar.gz")
sha256sums=('b97bc588420d1542f73279e71975ccb5d81d75e534e7b5717e01d6e6adf6a283'
            'c59c3ccf5238fe93cc671e6fa2f6614c0bfec073dc79bfda4d14e3a5be96eac8')
sha256sums_i686=('4f8b70b293ac8cc5c70e571ad5d1878d0f29d133a46fe7869868d9c19b5058cd')
sha256sums_x86_64=('5f79774d5beec8f7636b59c0fb07a03108eef1e3fd3245638b20858c714144be')

prepare() {
  cd "${srcdir}"

  sed -e "s/@PACKAGE_VERSION@/${pkgver}/" dkms.conf.in > dkms.conf

  sed -i -e "/BRCM_WLAN_IFNAME/s:eth:wlan:" src/wl/sys/wl_linux.c
}

package() {
  cd "${srcdir}"

  local dest="${pkgdir}/usr/src/${pkgname/-dkms/}-${pkgver}"

  mkdir -p "${dest}"
  cp -RL src lib Makefile dkms.conf "${dest}"
  chmod a-x "${dest}/lib/LICENSE.txt" # Ships with executable bits set

  mkdir -p "${pkgdir}/usr/share/licenses/${pkgname}"
  ln -rs "${dest}/lib/LICENSE.txt" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"

  install -D -m 644 broadcom-wl-dkms.conf "${pkgdir}/etc/modprobe.d/broadcom-wl-dkms.conf"
}

# vim:set ts=2 sw=2 et:
