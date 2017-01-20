# Maintainer: wenLiangcan <boxeed at gmail dot com>

pkgname=electronic-wechat-git
_pkgname=electronic-wechat
pkgver=1.4.0.43.gb18ff6d
pkgrel=1
pkgdesc="An Electron application for WeChat"
arch=('any')
url="https://github.com/geeeeeeeeek/wechat-electron/"
license=('MIT')
depends=('electron' 'xdg-utils')
makedepends=('git' 'npm' 'sed' 'gcc')
provides=("${_pkgname}")
conflicts=("${_pkgname}")
source=('git+https://github.com/geeeeeeeeek/electronic-wechat.git')
sha1sums=('SKIP')
_desktop="${_pkgname}.desktop"

pkgver() {
    cd "${srcdir}/${_pkgname}"
    git describe --tags --long | sed 's/^v//;s/-/./g'
}

prepare() {
    cat > ${_desktop} << EOF
[Desktop Entry]
Type=Application
Name=Electronic WeChat
Comment=A better WeChat client on Mac OS X and Linux.
Exec=/usr/bin/${_pkgname}
Icon=/usr/share/${_pkgname}/assets/icon.png
Categories=Network;InstantMessaging;Application;
Terminal=false
StartupNotify=true
Version=${pkgver}
EOF

    cat > "${_pkgname}.sh" << EOF
#!/usr/bin/env sh
electron /usr/share/${_pkgname}/ \$*
EOF
}

build() {
    cd "${_pkgname}"
    sed -i 's/^.*"electron".*$//;s/^.*"electron-packager".*$//' package.json
    npm install --production
}

package() {
    cd "${_pkgname}"

    find ./{'assets','node_modules','src','package.json'} -type f -exec install -Dm644 {} \
        "${pkgdir}/usr/share/${_pkgname}/{}" \;

    install -Dm644 LICENSE.md "${pkgdir}/usr/share/licenses/${_pkgname}/LICENSE"

    install -Dm644 "${srcdir}/${_desktop}" "${pkgdir}/usr/share/applications/${_desktop}"
    install -Dm755 "${srcdir}/${_pkgname}.sh" "${pkgdir}/usr/bin/${_pkgname}"
}

