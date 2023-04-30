# Maintainer: zhullyb <zhullyb [at] outlook dot com>
# Contributor: weearc <q19981121 [at] 163 dot com>
pkgname=motrix
_pkgname=Motrix
pkgver=1.8.14
pkgrel=1
epoch=
pkgdesc="A full-featured download manager (release version)"
arch=("x86_64")
url="https://github.com/agalwood/Motrix"
license=('MIT')
groups=()
depends=('gtk3' 'libxcb' 'electron')
makedepends=('npm' 'yarn' "nodejs")
checkdepends=()
optdepends=()
provides=()
conflicts=('motrix-git')
replaces=()
backup=()
options=()
install=
changelog=
source=("motrix.desktop"
    "motrix"
    "Motrix.tar.gz"::"https://github.com/agalwood/Motrix/archive/v${pkgver}.tar.gz")
noextract=()
sha256sums=('af5092a2a599bd23c13303ad1e7b745992a7af141278d13abe4297ca50a77bd8'
            '52a8f1ae5916a91aa1c9f1749e06777b4457bd9f5a03749c9fcd97e7d0801a71'
            '3b709583403c84e597feeee78a9fee7211e46972dfaf8e2075b7a278eb54f74c')
validpgpkeys=()

#_ensure_local_nvm() {
    # let's be sure we are starting clean
#    which nvm >/dev/null 2>&1 && nvm deactivate && nvm unload
#    export NVM_DIR="${srcdir}/.nvm"

    # The init script returns 3 if version specified
    # in ./.nvrc is not (yet) installed in $NVM_DIR
    # but nvm itself still gets loaded ok
#    source /usr/share/nvm/init-nvm.sh || [[ $? != 1 ]]
#}

prepare() {
    mv ${_pkgname}-${pkgver} ${_pkgname}
#    _ensure_local_nvm
#    nvm install 14
}

build() {
    cd ${_pkgname}/
#    _ensure_local_nvm
    export YARN_CACHE_FOLDER="${srcdir}/yarn_cache"
    yarn
    yarn run build:dir
}

package() {

    install -Dm 644 ${srcdir}/${_pkgname}/release/linux-unpacked/resources/app.asar ${pkgdir}/usr/lib/${pkgname}/app.asar
    install -Dm 755 ${srcdir}/${_pkgname}/release/linux-unpacked/resources/engine/aria2c ${pkgdir}/usr/lib/${pkgname}/engine/aria2c
    install -Dm 644 ${srcdir}/${_pkgname}/release/linux-unpacked/resources/engine/aria2.conf ${pkgdir}/usr/lib/${pkgname}/engine/aria2.conf

    # binary wrapper
    install -Dm 775 ${srcdir}/motrix ${pkgdir}/usr/bin/${pkgname}

    # desktop enrty
    install -Dm 644 ${srcdir}/motrix.desktop ${pkgdir}/usr/share/applications/${pkgname}.desktop

    # icons
    install -Dm 644 ${srcdir}/${_pkgname}/build/256x256.png ${pkgdir}/usr/share/icons/${pkgname}.png
}
