# Maintainer: zxp19821005 <zxp19821005 at 163 dot com>
# Maintainer: Yurii Kolesnykov <root@yurikoles.com>
# based on aur electron8-bin: Tom Vincent <http://tlvince.com/contact/>
_projectname=electron
_major=13
_pkgname="${_projectname}${_major}"
pkgname="${_pkgname}"-bin
_pkgver="${_major}.6.9"
pkgver="${_pkgver/-/.}"
pkgrel=2
pkgdesc="Build cross platform desktop apps with web technologies - binary version ${_major}"
arch=(
	'aarch64'
	'armv7h'
	'i686' 
	'x86_64'
)
url='https://electronjs.org'
_ghurl="https://github.com/electron/electron"
license=(
    'MIT'
    'LicenseRef-custom'
)
provides=(
    "${_pkgname}=${pkgver}"
)
conflicts=("${_pkgname}")
depends=(
	'alsa-lib'
	'gtk3'
	'nss'
)
optdepends=(
    'kde-cli-tools: file deletion support (kioclient5)'
    'libappindicator-gtk3: StatusNotifierItem support'
    'pipewire: WebRTC desktop sharing under Wayland'
    'trash-cli: file deletion support (trash-put)'
    "xdg-utils: open URLs with desktop's default (xdg-email, xdg-open)"
)
source_aarch64=(
    "${_pkgname}-chromedriver-${pkgver}-aarch64.zip::${_ghurl}/releases/download/v${_pkgver}/chromedriver-v${_pkgver}-linux-arm64.zip"
    "${_pkgname}-${pkgver}-aarch64.zip::${_ghurl}/releases/download/v${_pkgver}/electron-v${_pkgver}-linux-arm64.zip"
)
source_armv7h=(
    "${_pkgname}-chromedriver-${pkgver}-armv7h.zip::${_ghurl}/releases/download/v${_pkgver}/chromedriver-v${_pkgver}-linux-armv7l.zip"
    "${_pkgname}-${pkgver}-armv7h.zip::${_ghurl}/releases/download/v${_pkgver}/electron-v${_pkgver}-linux-armv7l.zip"
)
source_i686=(
    "${_pkgname}-chromedriver-${pkgver}-i686.zip::${_ghurl}/releases/download/v${_pkgver}/chromedriver-v${_pkgver}-linux-ia32.zip"
    "${_pkgname}-${pkgver}-i686.zip::${_ghurl}/releases/download/v${_pkgver}/electron-v${_pkgver}-linux-ia32.zip"
)
source_x86_64=(
    "${_pkgname}-chromedriver-${pkgver}-x86_64.zip::${_ghurl}/releases/download/v${_pkgver}/chromedriver-v${_pkgver}-linux-x64.zip"
    "${_pkgname}-${pkgver}-x86_64.zip::${_ghurl}/releases/download/v${_pkgver}/electron-v${_pkgver}-linux-x64.zip"
)
sha256sums_aarch64=('44a13d95354cfc253ac1b7dea5c4343e36f661f1a696d2d64856b0dd7e63e878'
                    'cb570f77e46403a75b99740c41b297154f057dc3b9aa75fd235dccc5619972cf')
sha256sums_armv7h=('2e21640e4fa73eaffe9f4623aa2cb7d82ffb1b2f55475b63a071456d3439a000'
                   'e70cf80ac17850f3291c19a89235c59a7a6e0c791e7965805872ce584479c419')
sha256sums_i686=('025d17fa3335588c19500040fe2ab24d4337e2014c5a9d293270c5d6c1577228'
                 '7c31b60ee0e1d9966b8cf977528ace91e10ce25bb289a46eabbcf6087bee50e6')
sha256sums_x86_64=('4e96c1c807eadc39eea479d742a553367752ccab6e078e20b89c1b344d0f6ae9'
                   '5e29701394041ba2acd8a9bb042d77967c399b8fe007d7ffbd1d3e6bfdb9eb8a')
package() {
    install -dm755 "${pkgdir}/usr/lib/${_pkgname}/"
    find . -mindepth 1 -maxdepth 1 -type f ! -name "*.zip" ! -name "LICENSE*" -exec cp -r --no-preserve=ownership --preserve=mode -t "${pkgdir}/usr/lib/${_pkgname}/." {} +
    for _folder in 'locales' 'resources'; do
        cp -r --no-preserve=ownership --preserve=mode "${_folder}/" "${pkgdir}/usr/lib/${_pkgname}/${_folder}/"
    done
    chmod u+s "${pkgdir}/usr/lib/${_pkgname}/chrome-sandbox"
    install -dm755 "${pkgdir}/usr/bin"
    ln -nfs "/usr/lib/${_pkgname}/${_projectname}" "${pkgdir}/usr/bin/${_pkgname}"
   
    for _license in 'LICENSE' 'LICENSES.chromium.html'; do
        install -Dm644 "${_license}" "${pkgdir}/usr/share/licenses/${pkgname}/${_license}"
    done
}