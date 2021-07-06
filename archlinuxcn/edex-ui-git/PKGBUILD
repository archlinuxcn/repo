# Maintainer: Lucas Malandrino <lucas.malandrino@gmail.com>
# Co-maintainer & author of the original software: Gabriel "Squared" Saillard <gabriel@saillard.dev>
pkgname='edex-ui-git'
_pkgname='edex-ui'
pkgver=2.2.8.pre
pkgrel=1
pkgdesc="A cross-platform, customizable science fiction terminal emulator with advanced monitoring & touchscreen support."
arch=('i686' 'x86_64' 'armv7h' 'aarch64')
url='https://github.com/GitSquared/edex-ui'
license=('GPL3')
depends=('gtk3'
         'libxss'
         'nss')
makedepends=('npm'
             'git'
             'python'
             'rsync')
conflicts=('edex-ui')
provides=('edex-ui')
install="edex-ui.install"
source=("git+https://github.com/GitSquared/edex-ui.git#branch=master")
sha256sums=('SKIP')

pkgver() {
    cd "${srcdir}/${_pkgname}"

    # echo $(head -n 4 package.json | tail -n 1 | sed 's/  "version": "//;s/",//;s/-/./g').$(git log -n 1 --oneline | head -c 7)
    echo $(head -n 4 package.json | tail -n 1 | sed 's/  "version": "//;s/",//;s/-/./g')
}

build() {
    cd "${_pkgname}"

    npm install

    # Build tarball with electron-builder
    npm run prebuild-linux
    ${srcdir}/${_pkgname}/node_modules/.bin/electron-builder -l pacman -p never
    npm run postbuild-linux
}

package() {
    cd "${_pkgname}"

    # Extract the package made by electron-builder
    # It's not pretty but blame electron
    tar xf ./dist/eDEX-UI-linux-*.pacman -C "${pkgdir}"
    cd "${pkgdir}"

    # Garbage made by electron-builder
    rm -f "${pkgdir}/.INSTALL" "${pkgdir}/.MTREE" "${pkgdir}/.PKGINFO"

    chmod 755 "${pkgdir}/opt/eDEX-UI/edex-ui"
}
