# Maintainer: Alynx Zhou <alynx.zhou@gmail.com>
pkgname=gnome-shell-extension-simple-net-speed
pkgver=18
pkgrel=1
pkgdesc="GNOME Shell extension to show network speed."
arch=('any')
url="https://github.com/biji/simplenetspeed"
license=('GPL')
depends=('gnome-shell')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz")
sha512sums=("f37332509a7ea96c705c9eaac7e2b70acc22e8debfcdbc61f617b2d787a27d74f281add715c5b75d01eff116c15e9b2d7bc4681eda2ae85f255c1a6775eb5d20")

package() {
    _uuid="simplenetspeed@biji.extension"
    _reponame="simplenetspeed"

    install -d "${pkgdir}/usr/share/gnome-shell/extensions/${_uuid}"
    cd "${srcdir}/${_reponame}-${pkgver}"
    cp -a * "${pkgdir}/usr/share/gnome-shell/extensions/${_uuid}"
}

