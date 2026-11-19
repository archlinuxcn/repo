# Maintainer: Gavin Luo <lunt.luo@gmail.com>

pkgname=gnome-shell-extension-window-nativizer
pkgver=0.12.0
pkgrel=1
pkgdesc='Seamlessly nativize non-native applications into the GNOME desktop'
arch=('any')
url='https://github.com/everyx/gnome-shell-extension-window-nativizer'
license=('GPL-2.0-or-later')
depends=('gnome-shell>=50' 'dconf')
makedepends=('gnome-shell' 'gettext' 'pnpm' 'nodejs')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/refs/tags/v${pkgver}.tar.gz")
b2sums=('cbf8417174283caf26d1aaa16f2874a499dbef26abc736590b06cb5ad5a49bdd3b90e6b4426834b8e580b7e6225948632a1cbf8c721a249d1ac353e83df9508f')

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
