# Maintainer: Gavin Luo <lunt.luo@gmail.com>

pkgname=gnome-shell-extension-window-nativizer
pkgver=0.10.0
pkgrel=1
pkgdesc='Seamlessly nativize non-native applications into the GNOME desktop'
arch=('any')
url='https://github.com/everyx/gnome-shell-extension-window-nativizer'
license=('GPL-2.0-or-later')
depends=('gnome-shell>=50' 'dconf')
makedepends=('gnome-shell' 'gettext' 'pnpm')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/refs/tags/v${pkgver}.tar.gz")
b2sums=('e4b9b8066aa18e60ab9e0291eb84285510cc871214ddba63ac058048fdde86f2b2436dffbbdade7de1883e237a6d93357e1e53900ca798b35b454407dc4cbc00')

build() {
    cd "${pkgname}-${pkgver}"

    pnpm install --prod --ignore-scripts
    pnpm run pack
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
