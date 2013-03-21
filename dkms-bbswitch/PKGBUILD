# Maintainer: Lekensteyn <lekensteyn@gmail.com>
# Contributor: Samsagax <samsagax@gmail.com>

pkgname=dkms-bbswitch
_modname=bbswitch
pkgver=0.6
pkgrel=1
pkgdesc="kernel module allowing to switch dedicated graphics card on Optimus laptops, dkms version"
arch=(any)
url=("http://github.com/Bumblebee-Project/bbswitch")
license=('GPL')
provides=('bbswitch')
conflicts=('bbswitch' 'bbswitch-git')
depends=('dkms')
source=("https://github.com/Bumblebee-Project/bbswitch/archive/v${pkgver}.tar.gz" 'dkms.conf.in')
md5sums=('c5496e3225c8e70d02a24bfd8a50faf6'
         '262c8a723584860fa86f8e5fc8a4889a')
install=dkms-bbswitch.install

package() {
  cd ${srcdir}/${_modname}-${pkgver}
  install -dm755 "${pkgdir}/usr/src/${_modname}-${pkgver}/"
  for i in "${srcdir}/${_modname}-${pkgver}/"{Makefile,bbswitch.c}; do
    install -D -m644 "${i}" "${pkgdir}/usr/src/${_modname}-${pkgver}/"
  done
  sed "s/#MODULE_VERSION#/${pkgver}/" "${srcdir}/dkms.conf.in" > "${pkgdir}/usr/src/${_modname}-${pkgver}/dkms.conf"
}
