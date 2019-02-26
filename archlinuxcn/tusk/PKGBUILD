# Maintainer: suthernfriend <public@janpeterkoenig.com>
# Contributor: RPDiep
# Contributor: Hugo Barrera <hugo@barrera.io>
# Contributor: liberodark

pkgname=tusk
pkgver=0.22.0
pkgrel=1
pkgdesc="Refined Evernote desktop app"
arch=('x86_64')
url="https://github.com/klaussinani/tusk"

license=('MIT')
makedepends=('npm')
depends=('xdg-utils' 'electron')

source=(
    "$pkgname-$pkgver.tar.gz::https://github.com/klaussinani/tusk/archive/v${pkgver}.tar.gz"
    "$pkgname.desktop"
    "$pkgname.png"
)

sha256sums=(
    '9e45f45d208e2aa1404500c6b0104a43cd402c21e1000f83a42dc2e22b738f01'
    'b72cfcd35a727cb982f82d9f97f9e4330e81fbc70af47d1bc7f5baa7837a29f3'
    '2e8e1f13a86bd4a8fdbd2a4a69cde6b09e035b31352ad60f5a81d61a7abfe5bf'
)

build() {
    cd $srcdir/$pkgname-$pkgver
    npm install --cache "${srcdir}/npm-cache"
    node ./node_modules/electron-builder/out/cli/cli.js build -l dir --x64
}

package() {
    cd "$srcdir/$pkgname-${pkgver}/dist/linux-unpacked"
    install -Dm644 -t "${pkgdir}/usr/lib/${pkgname}" ./*.pak ./*.dat ./*.bin
    install -Dm644 -t "${pkgdir}/usr/lib/${pkgname}/locales" ./locales/*
    install -Dm644 -t "${pkgdir}/usr/lib/${pkgname}/resources" ./resources/*
    install -Dm755 -t "${pkgdir}/usr/lib/${pkgname}" ./libffmpeg.so
    install -Dm755 -t "${pkgdir}/usr/lib/${pkgname}" ./${pkgname}
    
    # electron is required for several libs, so we use the libnode.so provided by electron itself
    ln -sf "/usr/lib/electron/libnode.so" "${pkgdir}/usr/lib/${pkgname}/libnode.so"
    install -dm755 "${pkgdir}/usr/bin"
    ln -sf "/usr/lib/${pkgname}/${pkgname}" "${pkgdir}/usr/bin/${pkgname}"
    
    # licenses
    cd "${srcdir}/$pkgname-${pkgver}"
    install -Dm644 "./license.md" "${pkgdir}/usr/share/licenses/$pkgname/LICENSE"
    cd "$srcdir/$pkgname-${pkgver}/dist/linux-unpacked"
    install -Dm644 -t "${pkgdir}/usr/share/licenses/${pkgname}" ./LICENSE*
    install -Dm644 "${srcdir}/${pkgname}.desktop" "${pkgdir}/usr/share/applications/${pkgname}.desktop"
    install -Dm644 "${srcdir}/${pkgname}.png" "${pkgdir}/usr/share/pixmaps/${pkgname}.png"
}
