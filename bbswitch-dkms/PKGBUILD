# Maintainer: Lekensteyn <peter@lekensteyn.nl>
# Contributor: Samsagax <samsagax@gmail.com>

pkgname=bbswitch-dkms
_modname=bbswitch
pkgver=0.8
pkgrel=1
pkgdesc="kernel module allowing to switch dedicated graphics card on Optimus laptops, dkms version"
arch=(any)
url="https://github.com/Bumblebee-Project/bbswitch"
license=('GPL')
provides=('bbswitch')
conflicts=('bbswitch' 'bbswitch-git')
replaces=('dkms-bbswitch')
depends=('dkms')
source=("https://github.com/Bumblebee-Project/bbswitch/archive/v${pkgver}.tar.gz" 'dkms.conf.in')
md5sums=('5b116b31ace3604ddf9d1fc1f4bc5807'
         '262c8a723584860fa86f8e5fc8a4889a')
sha256sums=('76cabd3f734fb4fe6ebfe3ec9814138d0d6f47d47238521ecbd6a986b60d1477'
            '61917827739b518401ec64d842e9e851d070bd28492172d6c22c9031e52de1a1')
install=dkms-bbswitch.install

package() {
  cd ${srcdir}/${_modname}-${pkgver}
  install -dm755 "${pkgdir}/usr/src/${_modname}-${pkgver}/"
  for i in "${srcdir}/${_modname}-${pkgver}/"{Makefile,bbswitch.c}; do
    install -D -m644 "${i}" "${pkgdir}/usr/src/${_modname}-${pkgver}/"
  done
  sed "s/#MODULE_VERSION#/${pkgver}/" "${srcdir}/dkms.conf.in" > "${pkgdir}/usr/src/${_modname}-${pkgver}/dkms.conf"
}
