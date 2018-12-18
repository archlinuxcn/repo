# Maintainer: Fredy García <frealgagu at gmail dot com>
# Contributor: Ivelin Velkov <ivelin dot velkov at gmail dot com>

pkgname=teams-for-linux
pkgver=0.1.10
pkgrel=1
pkgdesc="Unofficial Microsoft Teams client for Linux using Electron."
arch=("aarch64" "armv7h" "i686" "x86_64")
url="https://github.com/IsmaelMartinez/${pkgname}"
license=("GPL3")
depends=("gtk3" "libxss" "nss")
makedepends=("yarn")
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/IsmaelMartinez/${pkgname}/archive/v${pkgver}.tar.gz"
        "${pkgname}.desktop")
sha256sums=("9ea2a75087b326d5ace211675f1136bb11cf7e4aa4df231c80db533123ad9442"
            "f33ab4997c329567bbe172fe77ee6cbced5c5d4354e12ef52a89dd702422fded")

build() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  yarn install --non-interactive --pure-lockfile --cache-folder "${srcdir}/yarn-cache"
  if [[ ${CARCH} == "aarch64" ]]; then
    yarn build --arm64 --linux dir
  elif [[ ${CARCH} == "armv7h" ]]; then
    yarn build --armv7l --linux dir
  elif [[ ${CARCH} == "i686" ]]; then
    yarn build --ia32 --linux dir
  elif [[ ${CARCH} == "x86_64" ]]; then
    yarn build --x64 --linux dir
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
  ln -sf "/opt/${pkgname}/${pkgname%-for-linux}" "${pkgdir}/usr/bin/${pkgname}"
}
