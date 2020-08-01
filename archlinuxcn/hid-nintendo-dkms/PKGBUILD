# Maintainer: nicman23
_pkgbase=hid-nintendo
pkgname=${_pkgbase}-dkms
pkgver=2.0
pkgrel=2
pkgdesc="hid-nintendo Driver (DKMS)"
arch=('any')
url="https://github.com/nicman23/dkms-hid-nintendo"
license=('GPLv2')
depends=('dkms' 'bc')
provides=('hid-nintendo')
source=("https://github.com/nicman23/dkms-hid-nintendo/archive/$pkgver.tar.gz"
        "dkms.conf")
md5sums=('e2aae4a69b4f63255181318189e68774'
         '7dee3612b857c0aeb9de37977ed64d36')

package() {
  mkdir -p "${pkgdir}"/usr/src/${_pkgbase}-${pkgver}/
  chmod 755 "${pkgdir}"/usr/src/${_pkgbase}-${pkgver}/

  cp -r dkms-hid-nintendo*/* "${pkgdir}"/usr/src/${_pkgbase}-${pkgver}/
  install -Dm644 dkms.conf "${pkgdir}"/usr/src/${_pkgbase}-${pkgver}/dkms.conf
  sed -e "s/@_PKGBASE@/${_pkgbase}/" \
      -e "s/@PKGVER@/${pkgver}/" \
      -i "${pkgdir}"/usr/src/${_pkgbase}-${pkgver}/dkms.conf
}
