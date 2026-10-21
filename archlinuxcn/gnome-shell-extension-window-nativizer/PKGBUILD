# Maintainer: Gavin Luo <lunt.luo@gmail.com>

pkgname=gnome-shell-extension-window-nativizer
pkgver=0.11.1
pkgrel=1
pkgdesc='Seamlessly nativize non-native applications into the GNOME desktop'
arch=('any')
url='https://github.com/everyx/gnome-shell-extension-window-nativizer'
license=('GPL-2.0-or-later')
depends=('gnome-shell>=50' 'dconf')
makedepends=('gnome-shell' 'gettext' 'pnpm' 'nodejs')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/refs/tags/v${pkgver}.tar.gz")
b2sums=('cf5ced2ee3d1cdc1fe4968ad37c99b2558025eecc21c93877a8a2745fa9f53ced738b7448a84bc7d34dbeda83e8fff2258182c5b5a8ca19a6289d62a7bdc8fdd')

build() {
    cd "${pkgname}-${pkgver}"

    pnpm install --prod --ignore-scripts
    pnpm run build
}

package() {
    cd "${pkgname}-${pkgver}"

    local _uuid='window-nativizer@everyx.github.io'
    local _ext_dir="${pkgdir}/usr/share/gnome-shell/extensions/${_uuid}"

    install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}/"

    install -d "${_ext_dir}"
    bsdtar --uid 0 --gid 0 -xf "dist/${_uuid}.shell-extension.zip" -C "${_ext_dir}"

    install -Dm644 "${_ext_dir}/schemas/"*.gschema.xml -t "${pkgdir}/usr/share/glib-2.0/schemas/"
    rm -rf "${_ext_dir}/schemas"

    mv "${_ext_dir}/locale" "${pkgdir}/usr/share/locale"
}
