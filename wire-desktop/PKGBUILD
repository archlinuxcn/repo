# Maintainer: Conor Anderson <conor@conr.ca>
# Maintainer: Maxim Baz <$pkgname at maximbaz dot com>

pkgname=wire-desktop
pkgver=3.5.2881
pkgrel=2
pkgdesc='End-to-end encrypted messenger with file sharing, voice calls and video conferences'
arch=('x86_64')
url='https://wire.com/'
license=('GPL3')
depends=('electron' 'xdg-utils')
makedepends=('cargo' 'npm' 'python2' 'git' 'yarn')
optdepends=('hunspell-en_US: for English spellcheck support'
            'emoji-font: colorful emoji')
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/wireapp/${pkgname}/archive/linux/$pkgver.tar.gz"
        "${pkgname}"
        "${pkgname}.desktop")
sha256sums=('4216cd9c3a2c4920aec2f3c967181b04bfafdb1b47e526a8e823911cce704da1'
            '13f0829f0995269e7bdf5db683d048d36ae8af8cf16030a581e6386d83aae03a'
            'cc9056cecff2aa49a9ce9c8376d57ec8c7c2cb8174f7966b5cdccbeb2e3751ea')

build() {
  cd "${pkgname}-linux-${pkgver}"
  yarn
  yarn build:ts
  npx grunt 'linux-other'
}

package() {
  # Place files
  install -d "${pkgdir}/usr/lib/${pkgname}"
  cp -a "${pkgname}-linux-${pkgver}"/wrap/dist/linux-unpacked/resources/app/* "${pkgdir}/usr/lib/${pkgname}"

  # Place launcher script
  install -Dm755 -t "${pkgdir}/usr/bin/" "${pkgname}"

  # Place desktop entry and icon
  desktop-file-install -m 644 --dir "${pkgdir}/usr/share/applications/" "${pkgname}.desktop"
  local res
  for res in 32x32 256x256; do
    install -Dm644 "${pkgname}-linux-${pkgver}/resources/icons/${res}.png" "${pkgdir}/usr/share/icons/hicolor/${res}/apps/${pkgname}.png"
  done

  # Spellcheck dictionaries
  rm -rf "${pkgdir}/usr/lib/${pkgname}/node_modules/spellchecker/vendor/hunspell_dictionaries"
  ln -s "/usr/share/hunspell" "${pkgdir}/usr/lib/${pkgname}/node_modules/spellchecker/vendor/hunspell_dictionaries"

  # Place license files
  local license
  for license in "LICENSE.electron.txt" "LICENSES.chromium.html"; do
    install -Dm644 "${pkgname}-linux-${pkgver}/wrap/dist/linux-unpacked/${license}" "${pkgdir}/usr/share/licenses/${pkgname}/${license}"
  done
}
