# Maintainer: Jerry Xiao <aur@mail.jerryxiao.cc>

_id=ocaahdebbfolfmndjeplogmgcagdmblk
pkgname=chromium-extension-web-store
pkgver=1.5.4.3
pkgrel=2
pkgdesc="chromium web store extension (for ungoogled-chromium)"
arch=('any')
url="https://github.com/NeverDecaf/chromium-web-store"
license=('MIT')
optdepends=("ungoogled-chromium")
source=("${pkgname}-${pkgver}.crx::${url}/releases/download/v${pkgver}/Chromium.Web.Store.crx")
noextract=("${pkgname}-${pkgver}.crx")
sha256sums=('e593bf206d40a7b947d87a84c208f3967e0e8b9a2ac4d278c07cb1a21f996532')
install=chromium-extension-web-store.install

prepare() {
    # Create extension json
    cat << EOF > "${_id}".json
{
    "external_crx": "/usr/lib/${pkgname}/${pkgname}-${pkgver}.crx",
    "external_version": "${pkgver}"
}
EOF
}

package() {
    install -Dm644 -t "${pkgdir}/usr/share/chromium/extensions/" "${_id}.json"
    install -Dm644 -t "${pkgdir}/usr/lib/${pkgname}/" "${pkgname}-${pkgver}.crx"
}
