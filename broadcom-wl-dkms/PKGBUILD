# Maintainer: Andrey Vihrov <andrey.vihrov at gmail.com>
# Contributor: Frank Vanderham <twelve.eighty (at) gmail.>
# Contributor: USA-RedDragon (AUR)

pkgname=broadcom-wl-dkms
pkgver=6.30.223.271
pkgrel=8
pkgdesc="Broadcom 802.11 Linux STA wireless driver"
arch=('i686' 'x86_64')
url="https://www.broadcom.com/support/802.11"
license=('custom')
depends=('dkms')
optdepends=('linux-headers: build modules against the Arch kernel'
            'linux-lts-headers: build modules against the LTS kernel'
            'linux-zen-headers: build modules against the ZEN kernel'
            'linux-grsec-headers: build modules against the GRSEC kernel')
conflicts=('broadcom-wl')
install=broadcom-wl-dkms.install
source=('broadcom-wl-dkms.conf'
        'dkms.conf.in'
        '001-null-pointer-fix.patch'
        '002-rdtscl.patch'
        '003-linux47.patch')
source_i686=("http://www.broadcom.com/docs/linux_sta/hybrid-v35-nodebug-pcoem-${pkgver//./_}.tar.gz")
source_x86_64=("http://www.broadcom.com/docs/linux_sta/hybrid-v35_64-nodebug-pcoem-${pkgver//./_}.tar.gz")
sha256sums=('b97bc588420d1542f73279e71975ccb5d81d75e534e7b5717e01d6e6adf6a283'
            'c59c3ccf5238fe93cc671e6fa2f6614c0bfec073dc79bfda4d14e3a5be96eac8'
            '32e505a651fdb9fd5e4870a9d6de21dd703dead768c2b3340a2ca46671a5852f'
            '4ea03f102248beb8963ad00bd3e36e67519a90fa39244db065e74038c98360dd'
            '30ce1d5e8bf78aee487d0f3ac76756e1060777f70ed1a9cf95215c3a52cfbe2e')
sha256sums_i686=('4f8b70b293ac8cc5c70e571ad5d1878d0f29d133a46fe7869868d9c19b5058cd')
sha256sums_x86_64=('5f79774d5beec8f7636b59c0fb07a03108eef1e3fd3245638b20858c714144be')

prepare() {
  sed -i -e "/BRCM_WLAN_IFNAME/s:eth:wlan:" src/wl/sys/wl_linux.c

  patch -p1 < 001-null-pointer-fix.patch
  patch -p1 < 002-rdtscl.patch
  patch -p1 < 003-linux47.patch

  sed -e "s/@PACKAGE_VERSION@/${pkgver}/" dkms.conf.in > dkms.conf
}

package() {
  local dest="${pkgdir}/usr/src/${pkgname/-dkms/}-${pkgver}"

  mkdir -p "${dest}"
  cp -a src lib Makefile dkms.conf "${dest}"
  chmod a-x "${dest}/lib/LICENSE.txt" # Ships with executable bits set

  install -D -m 0644 broadcom-wl-dkms.conf "${pkgdir}/usr/lib/modprobe.d/broadcom-wl-dkms.conf"

  local lic="${pkgdir}/usr/share/licenses/${pkgname}"
  mkdir -p "${lic}"
  ln -rs "${dest}/lib/LICENSE.txt" "${lic}/LICENSE.shipped"
  sed -n -e '/Copyright/,/SOFTWARE\./{s/^ \* //;p}' src/wl/sys/wl_linux.c > "${lic}/LICENSE.module"
}

# vim:set ts=2 sw=2 et:
