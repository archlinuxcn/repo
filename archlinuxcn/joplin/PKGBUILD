# Maintainer: Alfredo Palhares <alfredo at palhares dot me>
# Contributor: Mark Wagie <mark dot wagie at tutanota dot com>

# Please contribute to:
# https://github.com/masterkorp/joplin-pkgbuild

pkgname=joplin
pkgver=1.0.224
pkgrel=1
pkgdesc="A note taking and to-do application with synchronization capabilities"
arch=('x86_64' 'i686')
depends=('gtk3' 'libexif' 'libgsf' 'libjpeg-turbo' 'libwebp' 'libxss' 'nodejs'
         'nss' 'orc')
makedepends=('git' 'npm' 'python' 'rsync')
optdepends=('libappindicator-gtk3: for tray icon')
url="https://joplinapp.org/"
license=('MIT')
source=("${pkgname}.desktop" "${pkgname}-desktop.sh" "${pkgname}.sh"
        "${pkgname}-${pkgver}.tar.gz::https://github.com/laurent22/joplin/archive/v${pkgver}.tar.gz")
sha256sums=('f915b42c3c35b22fc9bd1525953be2363319edfa2e95288f87edfb2833ec45f1'
            '41bfdc95a6ee285eb644d05eb3bded72a83950d4720c3c8058ddd3c605cd625d'
            '5245da6f5f647d49fbe044b747994c9f5a8e98b3c2cd02757dd189426a677276'
            '80af12d00730fe2150ce766658f417fa39f829a99048256ca7e86dba27d069ca')

build() {
  # Remove husky (git hooks) from dependencies
  cd "${srcdir}/${pkgname}-${pkgver}"
  sed -i '/"husky": ".*"/d' package.json

  # Force Lang
  # INFO: https://github.com/alfredopalhares/joplin-pkgbuild/issues/25
  export LANG=en_US.utf8

  # npm complains for missing execa package - force to install it
  npm install --cache "${srcdir}/npm-cache" execa
  npm install --cache "${srcdir}/npm-cache"

  # CliClient
  cd "${srcdir}/${pkgname}-${pkgver}/CliClient"
  npm install --cache "${srcdir}/npm-cache"

  # Electron App
  cd "${srcdir}/${pkgname}-${pkgver}/ElectronClient"
  npm install --cache "${srcdir}/npm-cache"
  npm run dist

}

package() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  install -d ${pkgdir}/usr/share/{${pkgname},${pkgname}-cli}
  cp -R CliClient/build/* "${pkgdir}/usr/share/${pkgname}-cli"
  cp -R CliClient/node_modules "${pkgdir}/usr/share/${pkgname}-cli"
  cp -R ElectronClient/dist/linux-unpacked/* "${pkgdir}/usr/share/${pkgname}"

  install -Dm755 ${srcdir}/${pkgname}-desktop.sh "${pkgdir}/usr/bin/${pkgname}-desktop"
  install -m755 ${srcdir}/${pkgname}.sh "${pkgdir}/usr/bin/${pkgname}"

  install -Dm644 ${srcdir}/${pkgname}.desktop -t "${pkgdir}/usr/share/applications"

  install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"

  # Remove unneeded architecture files
  rm -rf "${pkgdir}/usr/share/${pkgname}/resources/app/node_modules/7zip-bin-linux"/arm*
}
