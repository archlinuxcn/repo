# Maintainer: Mahdi Sarikhani <mahdisarikhani@outlook.com>
# Contributor: Anna <morganamilo@gmail.com>

pkgname=superproductivity
_name=super-productivity
pkgver=16.6.0
pkgrel=1
pkgdesc="An advanced todo list app with timeboxing and time tracking capabilities"
arch=('x86_64')
url="https://super-productivity.com"
license=('MIT')
_electron=electron38
depends=('bash' "${_electron}" 'gcc-libs' 'glibc' 'hicolor-icon-theme')
makedepends=('nvm')
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/johannesjo/super-productivity/archive/v${pkgver}.tar.gz"
        "${pkgname}.desktop"
        "${pkgname}.sh")
sha256sums=('6c82d9e58c7dbcbb22b2e00be1c2d5dfea26c35ccb0dc359edb41ace3c851099'
            'a8945d93cacbe189b538da601b3f6ace0588c3b126236e763e8f2010005513bb'
            'f9ca69e16223b3dcfa0d8ae9dbbff231255482d85f0d72ddcc5033dac890741e')

prepare() {
    source /usr/share/nvm/init-nvm.sh
    sed -i "s/@ELECTRON@/${_electron}/" "${pkgname}.sh"

    cd "${_name}-${pkgver}"
    export ELECTRON_SKIP_BINARY_DOWNLOAD=1
    nvm install
    npm install
}

build() {
    cd "${_name}-${pkgver}"
    npm run build
    npx electron-builder --linux --dir \
        -c.electronDist="/usr/lib/${_electron}" \
        -c.electronVersion="$(cat /usr/lib/${_electron}/version)"
}

package() {
    cd "${_name}-${pkgver}"
    install -Dm644 .tmp/app-builds/linux-unpacked/resources/app.asar -t "${pkgdir}/usr/lib/${pkgname}"
    cp -r .tmp/app-builds/linux-unpacked/resources/app.asar.unpacked "${pkgdir}/usr/lib/${pkgname}"
    install -Dm755 "${srcdir}/${pkgname}.sh" "${pkgdir}/usr/bin/${pkgname}"
    install -Dm644 "${srcdir}/${pkgname}.desktop" -t "${pkgdir}/usr/share/applications"
    for i in 16 32 48 64 128 256 512 1024; do
        install -Dm644 "build/icons/${i}x${i}.png" "${pkgdir}/usr/share/icons/hicolor/${i}x${i}/apps/${pkgname}.png"
    done
    install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
