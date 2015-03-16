# Maintainer: Sam Stuewe <halosghost at archlinux dot info>
# Contributor: Humbert Julien <julroy67 [AT] gmail.com>
_hgname=lugaru
pkgname="${_hgname}hd-hg"
pkgver=550.2aac6aa9913f
pkgrel=2
pkgdesc="An open-source third-persion action game featuring a unique close-range combat system"
arch=('i686' 'x86_64')
license=('GPL' 'CCPL:cc-by-sa' 'custom')
url='https://bitbucket.org/osslugaru/lugaru'
depends=('sdl' 'openal' 'libjpeg' 'libpng' 'libvorbis')
makedepends=('mercurial' 'gcc-libs' 'sdl' 'openal' 'cmake' 'libjpeg' 'libpng' 'libvorbis')
source=("${_hgname}::hg+https://bitbucket.org/osslugaru/${_hgname}"
        "${_hgname}.launcher"
        "${_hgname}.desktop")
sha256sums=('SKIP'
            'f0868d415e18d5199b2c99980cfdf89311a1214c010206c98d7cf7f1e50c1096'
            'aa7e7615d5c9d8f7bf02265bb392cadfa6e479d2fc2ff4f8972de4a0769bd6d5')

pkgver() {
    cd "${_hgname}"
    echo "$(hg identify -n).$(hg identify -i)"
}

build() {
    cd "${_hgname}"
	cmake ./ -DCMAKE_BUILD_TYPE=Release -DLUGARU_INSTALL_PREFIX=/opt/LugaruHD
	make
}

package() {
    cd "${_hgname}"
    make PREFIX=/usr DESTDIR="${pkgdir}" install

    cd "${srcdir}"
	install -Dm755 "${_hgname}.launcher" "${pkgdir}/usr/bin/${_hgname}"
	install -Dm644 "${_hgname}/Source/win-res/${_hgname//l/L}.png" "${pkgdir}/usr/share/pixmaps/${_hgname//l/L}.png"
	install -Dm644 "${_hgname}.desktop" "${pkgdir}/usr/share/applications/${_hgname}.desktop"

	install -Dm644 "${_hgname}/CONTENT-LICENSE.txt" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
