# Maintainer: Shen-Ta Hsieh <ibmibmibm(at)gmail(dot)com>
# Contributor: Shen-Ta Hsieh <ibmibmibm(at)gmail(dot)com>

_pkgbase=r8125
pkgname=(r8125 r8125-dkms)
pkgver=9.003.05
pkgrel=1
pkgdesc="r8125 kernel driver for linux"
arch=('x86_64')
url="https://www.realtek.com/"
license=('GPL2')
makedepends=(linux-headers)
source=("https://github.com/ibmibmibm/r8125/archive/${pkgver}.tar.gz"
        'dkms.conf')
sha256sums=('75196ec98afcefbb6706307104d32131a27abba24ac333633790264968d548d6'
            '7a6b42b6ebbd76ae3c40e10f824c2dae88448fab3ba074916b3be5c2b4bef448')

build() {
  _kernver=$(</usr/src/linux/version)

  tar -xf "${pkgver}.tar.gz"
  cd "${_pkgbase}-${pkgver}"/src
  make -C "/lib/modules/${_kernver}/build" M="$(pwd)" modules
}

package_r8125() {
  # Install
  _kernver=$(</usr/src/linux/version)

  msg2 "Starting make install..."
  install -Dt "${pkgdir}/usr/lib/modules/${_kernver}/extramodules" -m644 "${_pkgbase}-${pkgver}/src/r8125.ko"
  find "${pkgdir}" -name '*.ko' -exec gzip -n {} +
}

package_r8125-dkms() {
  pkgdesc="r8125 kernel driver sources for linux"
  depends=('dkms')
  optdepends=('linux-headers: Build the module for Arch kernel'
              'linux-lts-headers: Build the module for LTS Arch kernel')
  provides=("8125=$pkgver")
  conflicts+=(r8125)
  # Copy dkms.conf
  install -Dm644 dkms.conf "${pkgdir}"/usr/src/${_pkgbase}-${pkgver}/dkms.conf

  # Set name and version
  sed -e "s/@_PKGBASE@/${_pkgbase}/" \
      -e "s/@PKGVER@/${pkgver}/" \
      -i "${pkgdir}"/usr/src/${_pkgbase}-${pkgver}/dkms.conf

  # Copy sources (including Makefile)
  cp -r ${_pkgbase}-${pkgver}/* "${pkgdir}"/usr/src/${_pkgbase}-${pkgver}/
}
