# Maintainer: bpozdena <https://github.com/bpozdena>

pkgname=onedrivegui-git
_pkgname=OneDriveGUI
pkgver=1.1.0alpha5.r2.g9f9df60
pkgrel=1
pkgdesc="A simple GUI for OneDrive Linux client, with multi-account support."
url="https://github.com/bpozdena/${_pkgname}"
license=("GPL-3.0-or-later")
depends=("pyside6" "python-requests" "onedrive-abraunegg" "qt6-webengine")
makedepends=("git")
conflicts=("onedrivegui")
provides=("onedrivegui")
arch=("any")
source=("git+${url}.git" "onedrivegui.desktop")
sha256sums=('SKIP'
            'c531f57c3c8424f265c0aad2e93260eab071d066d75de2f7eebb47e41c644267')

pkgver(){
    cd "${_pkgname}/"
    git describe --tags --long | sed 's/v//;s/-/.r/;s/-/./g'
}

package(){
    cd "${_pkgname}/"

    install -d "${pkgdir}/usr/lib/${_pkgname}/"
    install -d "${pkgdir}/usr/bin/"
    cp -r src/{resources,ui} "${pkgdir}/usr/lib/${_pkgname}/"

    install -Dm644 "src/resources/images/${_pkgname}.png" -t "${pkgdir}/usr/share/icons/hicolor/48x48/apps/"
    install -Dm644 "${srcdir}/onedrivegui.desktop" -t "${pkgdir}/usr/share/applications/"
    install -Dm755 "src/${_pkgname}.py" -t "${pkgdir}/usr/lib/${_pkgname}/"
    ln -sf "/usr/lib/${_pkgname}/${_pkgname}.py" "${pkgdir}/usr/bin/onedrivegui"
}
