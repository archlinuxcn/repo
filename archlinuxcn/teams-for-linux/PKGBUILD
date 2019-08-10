# Maintainer: Fredy García <frealgagu at gmail dot com>
# Contributor: Ivelin Velkov <ivelin dot velkov at gmail dot com>

pkgname=teams-for-linux
pkgver=0.6.0
pkgrel=1
pkgdesc="Unofficial Microsoft Teams client for Linux using Electron."
arch=("aarch64" "armv7h" "i686" "x86_64")
url="https://github.com/IsmaelMartinez/${pkgname}"
license=("GPL3")
depends=("gtk3" "libxss" "nss")
makedepends=("node-gyp" "python2" "yarn")
source=(
  "${pkgname}-${pkgver}.tar.gz::https://github.com/IsmaelMartinez/${pkgname}/archive/v${pkgver}.tar.gz"
  "${pkgname}.desktop"
)
sha256sums=(
  "d9a37c43d89c34d8554eddb26d2735b8492e94f08e2fd31f5e70607e60f98835"
  "f33ab4997c329567bbe172fe77ee6cbced5c5d4354e12ef52a89dd702422fded"
)

build() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  yarn install --non-interactive --pure-lockfile --cache-folder "${srcdir}/yarn-cache"
  if [[ ${CARCH} == "aarch64" ]]; then
    yarn electron-builder build --arm64 --linux dir
  elif [[ ${CARCH} == "armv7h" ]]; then
    yarn electron-builder build --armv7l --linux dir
  elif [[ ${CARCH} == "i686" ]]; then
    yarn electron-builder build --ia32 --linux dir
  elif [[ ${CARCH} == "x86_64" ]]; then
    yarn electron-builder build --x64 --linux dir
  fi
}

package() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  install -dm755 "${pkgdir}/opt" "${pkgdir}/usr/bin"
  cp -r --preserve=mode "${srcdir}/${pkgname}-${pkgver}/dist/linux-unpacked" "${pkgdir}/opt/${pkgname}"
  install -Dm644 "${srcdir}/${pkgname}.desktop" "${pkgdir}/usr/share/applications/${pkgname}.desktop"
  for _file in "${srcdir}/${pkgname}-${pkgver}/build/icons/"*.png
  do
    _filename="$(basename ${_file})"
    install -Dm644 "${_file}" "${pkgdir}/usr/share/icons/hicolor/${_filename%.png}/apps/${pkgname}.png"
  done
  ln -sf "/opt/${pkgname}/${pkgname}" "${pkgdir}/usr/bin/${pkgname}"
}
