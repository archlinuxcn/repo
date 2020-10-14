# Maintainer: Alynx Zhou <alynx.zhou@gmail.com>
pkgname=gnome-shell-extension-simple-net-speed
pkgver=19
pkgrel=1
pkgdesc="GNOME Shell extension to show network speed."
arch=('any')
url="https://github.com/biji/simplenetspeed"
license=('GPL')
depends=('gnome-shell')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz")
sha512sums=('11df78cf9a7d0b9d0b7914a08fefded60bb0c072de73fe3185e812c4442d9ad8149d279f5e93f2a526822c376643b1455e42c0026e9b5212e3b4742f6cca732c')

package() {
    _uuid="simplenetspeed@biji.extension"
    _reponame="simplenetspeed"

    install -d "${pkgdir}/usr/share/gnome-shell/extensions/${_uuid}"
    cd "${srcdir}/${_reponame}-${pkgver}"
    cp -a * "${pkgdir}/usr/share/gnome-shell/extensions/${_uuid}"
}

