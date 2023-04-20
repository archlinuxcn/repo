# Maintainer: Xuanwo <xuanwo@archlinuxcn.org>
# Contributor: Bader <Bad3r@pm.me>
# Acknowledgment: Borrowed a lot from logseq-desktop-git, thank @pychuang
pkgname=logseq-desktop
pkgver=0.9.3
pkgrel=1
pkgdesc="A privacy-first, open-source platform for knowledge sharing and management."
arch=("x86_64")
url="https://logseq.com"
license=('AGPL3')
makedepends=("git" "yarn" "npm" "clojure" "nodejs>=16")
provides=("${pkgname}")
conflicts=("${pkgname}-git" "${pkgname}-bin")
source=(
    "${pkgname}-${pkgver}.zip::https://github.com/logseq/logseq/archive/refs/tags/${pkgver}.zip"
    "build.patch"
    "${pkgname}.desktop"
    "${pkgname}.install"
    "${pkgname}.sh"
)
sha256sums=('f412388fad41023db7a426f7cb6c8b35dc40d7365a549c2e08769152e7e31f1f'
            'b26c6ed39e2635e08a0df83d92883e670b75b02ed1c2c279044909c04edf8fc2'
            'd7ec65e2e92c967a1be865f90a7c242402dbf6ee8c45c863bdbad73aab0af2f4'
            'ad9bb5c0c7f9df5686201ed13c3f5566dcec65357bce33a7d143f160b59a9988'
            'a6412899c57cc0369cb11af547b561b00de84cc4aa4d656f4fa5ea3385cfef2e')

prepare() {
    cd "$srcdir/logseq-${pkgver}"

    # patch :parallel-build true in shadow-cljs.edn
    patch -p1 -i "${srcdir}/build.patch"

    # download required js modules
    yarn install

    # create and sync files to folder `static`
    yarn gulp:build

    # go to folder `static` and download required js modules in static
    cd "${srcdir}/logseq-${pkgver}/static"
    yarn install

    # go back to the top-level folder and download clojure dependencies
    cd "${srcdir}/logseq-${pkgver}"
    clojure -P -M:cljs
}

build() {
    cd "${srcdir}/logseq-${pkgver}"

    # build
    yarn cljs:release

    # packaging javescript files to an executable
    cd "${srcdir}/logseq-${pkgver}/static"
    yarn electron-forge package
}

package() {
    # important files are under static/out/Logseq-linux-x64
    cd "${srcdir}/logseq-${pkgver}/static/out/Logseq-linux-x64"

    # create destination folder and copy files
    mkdir -p "${pkgdir}/opt/${pkgname}"
    cp -a -r -u --verbose ./ "${pkgdir}/opt/${pkgname}"

    # create a soft link to the executable
    mkdir -p "${pkgdir}/usr/bin"
    # User flag aware launcher
    install -m755 ${srcdir}/logseq-desktop.sh "${pkgdir}/usr/bin/logseq"

    # create license folder and make soft links to actual license
    mkdir -p "${pkgdir}/usr/share/licenses/${pkgname}"
    ln -s "/opt/${pkgname}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}"
    ln -s "/opt/${pkgname}/LICENSES.chromium.html" "${pkgdir}/usr/share/licenses/${pkgname}"

    # install readme and additional license file (the top-level AGPL3)
    cd "${srcdir}/logseq-${pkgver}"
    install -Dm644 "README.md" -t "${pkgdir}/usr/share/doc/${pkgname}"
    install -Dm644 "LICENSE.md" -t "${pkgdir}/usr/share/licenses/${pkgname}"

    # copy xdg desktop files
    cd "${srcdir}"
    mkdir -p "${pkgdir}/usr/share/applications"
    install -Dm644 "${pkgname}.desktop" -t "${pkgdir}/usr/share/applications"
}
