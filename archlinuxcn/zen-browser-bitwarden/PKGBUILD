# Maintainer: Kimiblock Moe

pkgname=zen-browser-bitwarden
pkgver=2025.11.1
pkgrel=1
pkgdesc='Bitwarden browser extension for Zen'
arch=('any')
url='https://github.com/bitwarden/clients'
license=('GPL-3.0-or-later')
groups=('zen-browser-addons')
pkgdesc='Bitwarden browser extension for Firefox'
makedepends=('nodejs-lts-krypton' 'npm' 'unzip' 'zip' 'git' corepack)
source=("${pkgname}::git+https://github.com/bitwarden/clients.git#tag=browser-v${pkgver}")
b2sums=('b7d86e71bb209fa16c703158459463946185e7512d94d2dd507a64ef7ee54cfbe8925d582816470526ce85a136b8662712ee26d6bc4716188c8661d752e1487f')

prepare() {
  cd "${srcdir}/zen-browser-bitwarden"
  npm ci
}

build() {
  cd "${srcdir}/zen-browser-bitwarden/apps/browser"
  npm run dist:firefox
}

check() {
	cd "${srcdir}/zen-browser-bitwarden/apps/browser"
  npm run test
}

package() {
  install -Dm644 "${srcdir}/zen-browser-bitwarden/apps/browser/dist/dist-firefox.zip" "${pkgdir}/usr/lib/zen-browser/browser/extensions/{446900e4-71c2-419f-a6a7-df9c091e268b}.xpi"
}
