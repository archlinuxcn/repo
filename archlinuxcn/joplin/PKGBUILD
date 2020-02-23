# Maintainer: Alfredo Palhares <alfredo at palhares dot me>
# Contributor: Mark Wagie <mark dot wagie at tutanota dot com>

# Please contribute to:
# https://github.com/masterkorp/joplin-pkgbuild

pkgname=joplin
pkgver=1.0.179
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
        "${pkgname}-${pkgver}.zip::https://github.com/laurent22/joplin/archive/v${pkgver}.zip")
sha256sums=('ce4435654ee1f6d51d361945f32dd9bf07308f423c3f3c3db147744f203fbc2b'
            '41bfdc95a6ee285eb644d05eb3bded72a83950d4720c3c8058ddd3c605cd625d'
            '5245da6f5f647d49fbe044b747994c9f5a8e98b3c2cd02757dd189426a677276'
            '15c1ff7f42e4639d98c52780830d070d6aa60eea5f04fa6a7568aceca6628e9a')

build() {
  # Remove husky (git hooks) from dependencies
  cd "${srcdir}/${pkgname}-${pkgver}"
  sed -i '/"husky": ".*"/d' package.json

  # Force Lang
  # INFO: https://github.com/alfredopalhares/joplin-pkgbuild/issues/25
  export LANG=en_US.utf8

  # Install dependencies for the Tools used on another projects
  cd "${srcdir}/${pkgname}-${pkgver}/Tools"
  npm install --cache "${srcdir}/npm-cache"

  # Run copyLib and build the typescript
  # INFO: https://github.com/alfredopalhares/joplin-pkgbuild/issues/40
  cd "${srcdir}/${pkgname}-${pkgver}"
  npm install --cache "${srcdir}/npm-cache"
  npm run copyLib
  npm run tsc

  # Build Cli CLient
  cd "${srcdir}/${pkgname}-${pkgver}/CliClient"
  rsync -a --exclude "node_modules/" "${srcdir}/${pkgname}-${pkgver}/CliClient/app/" \
    "${srcdir}/${pkgname}-${pkgver}/CliClient/build"
  rsync -a --delete "${srcdir}/${pkgname}-${pkgver}/ReactNativeClient/locales" \
    "${srcdir}/${pkgname}-${pkgver}/CliClient/build/"
  rsync -a --delete "${srcdir}/${pkgname}-${pkgver}/ReactNativeClient/lib/" \
    "${srcdir}/${pkgname}-${pkgver}/CliClient/build/lib"

  cd "${srcdir}/${pkgname}-${pkgver}/CliClient/build/"
  # NOTE: Manually forcing sqlite 4.0.7 for node v12, remove later on
  npm install --cache "${srcdir}/npm-cache"

  # Electron App
  cd "${srcdir}/${pkgname}-${pkgver}/ElectronClient/app"
  npm install --cache "${srcdir}/npm-cache"

  rsync -a --delete "${srcdir}/${pkgname}-${pkgver}/ReactNativeClient/lib/" \
    "${srcdir}/${pkgname}-${pkgver}/ElectronClient/app/lib/"
  npm run compile
  npm run pack
}

package() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  install -d ${pkgdir}/usr/share/{${pkgname},${pkgname}-cli}
  cp -R CliClient/build/* "${pkgdir}/usr/share/${pkgname}-cli"
  cp -R CliClient/node_modules "${pkgdir}/usr/share/${pkgname}-cli"
  cp -R ElectronClient/app/dist/linux-unpacked/* "${pkgdir}/usr/share/${pkgname}"

  install -Dm755 ${srcdir}/${pkgname}-desktop.sh "${pkgdir}/usr/bin/${pkgname}-desktop"
  install -m755 ${srcdir}/${pkgname}.sh "${pkgdir}/usr/bin/${pkgname}"

  install -Dm644 ${srcdir}/${pkgname}.desktop -t "${pkgdir}/usr/share/applications"

  install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"

  # Remove unneeded architecture files
  rm -rf "${pkgdir}/usr/share/${pkgname}/resources/app/node_modules/7zip-bin-linux"/arm*
}
