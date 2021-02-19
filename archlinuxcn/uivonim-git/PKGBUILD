# Maintainer: Shengyu Zhang <la@archlinuxcn.org>

_pkgname=uivonim
pkgname=${_pkgname}-git
pkgver=v0.28.0.24.gd23b6ea
pkgrel=1
pkgdesc="A Neovim GUI designed for programming"
arch=('x86_64')
license=('AGPL')
url="https://glitchtron.org/veonim/"
makedepends=('npm' 'git')
depends=('neovim')
optdepends=()
source=("git+https://github.com/smolck/${_pkgname}"
        "${_pkgname}.sh"
        "${_pkgname}.desktop")

sha256sums=('SKIP'
            '8de71b3528e4f40b77d114080a1bb7a2ade4ad73dd6f9799c2cb640d78209af2'
            '17ab49bb6e0f74bc11052554cd0a8f341d772a993fe821143b256bad01d55d4f')

pkgver() {
    cd ${_pkgname}
    git describe --tags | sed 's/-/./g'
}

build() {
    cd ${_pkgname}
    npm ci
    npm run build
    npm run package
}

package() {
    cd ${_pkgname}

    install -d ${pkgdir}/opt
    cp -R dist/linux-unpacked "${pkgdir}/opt/${_pkgname}"
    install -Dm755 ${srcdir}/${_pkgname}.sh "${pkgdir}/usr/bin/${_pkgname}"
    install -Dm644 ${srcdir}/${_pkgname}/art/icon.png "${pkgdir}/usr/share/icons/hicolor/512x512/apps/${_pkgname}.png"
    install -Dm644 ${srcdir}/${_pkgname}.desktop "${pkgdir}/usr/share/applications/${_pkgname}.desktop"
}
