# Maintainer: Kimiblock Moe

pkgname=zen-browser-bitwarden
pkgver=2026.9.3
pkgrel=1
pkgdesc='Bitwarden browser extension for Zen'
arch=('any')
url='https://github.com/bitwarden/clients'
license=('GPL-3.0-or-later')
groups=('zen-browser-addons')
pkgdesc='Bitwarden browser extension for Firefox'
makedepends=('nodejs-lts-krypton' 'npm' 'unzip' 'zip' 'git' corepack)
source=("${pkgname}::git+https://github.com/bitwarden/clients.git#tag=browser-v${pkgver}")
b2sums=('2101574c10fd97ed9e658d832536118bb5113144d66f397e289365e797adee52f35489ed335367cb83968b3b02ed5ac86226e6ce05ed2e4745df71c055b01ae6')

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
