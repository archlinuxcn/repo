# Maintainer: Alynx Zhou <alynx.zhou@gmail.com>
pkgname=gnome-shell-extension-simple-net-speed
pkgver=21
pkgrel=1
pkgdesc="GNOME Shell extension to show network speed."
arch=('any')
url="https://github.com/biji/simplenetspeed"
license=('GPL')
depends=('gnome-shell')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz")
sha512sums=('0b708c55774e963093c10bcf6fc494f403150df30001b822df3827f48da5c6fc26786e6ead445e49256815d622df629d321b8366fe1f9787be01db07099e4b06')

package() {
    _uuid="simplenetspeed@biji.extension"
    _reponame="simplenetspeed"

    install -d "${pkgdir}/usr/share/gnome-shell/extensions/${_uuid}"
    cd "${srcdir}/${_reponame}-${pkgver}"
    cp -a * "${pkgdir}/usr/share/gnome-shell/extensions/${_uuid}"
}

