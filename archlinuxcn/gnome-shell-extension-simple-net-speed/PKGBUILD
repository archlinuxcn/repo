# Maintainer: Alynx Zhou <alynx.zhou@gmail.com>
pkgname=gnome-shell-extension-simple-net-speed
pkgver=23
pkgrel=1
pkgdesc="GNOME Shell extension to show network speed."
arch=('any')
url="https://github.com/biji/simplenetspeed"
license=('GPL')
depends=('gnome-shell')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz")
sha512sums=('d5dc3a72fd309fb2c3882d018eda14f0bc15d59702bd5b0b09424d82a61057d0e72b26aeb11c5cfd4048e0a22951fb6647a5b0b574a7ad31a42eb86cfae841df')

package() {
    _uuid="simplenetspeed@biji.extension"
    _reponame="simplenetspeed"

    install -d "${pkgdir}/usr/share/gnome-shell/extensions/${_uuid}"
    cd "${srcdir}/${_reponame}-${pkgver}"
    cp -a * "${pkgdir}/usr/share/gnome-shell/extensions/${_uuid}"
}

