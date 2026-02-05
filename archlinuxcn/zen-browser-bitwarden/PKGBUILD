# Maintainer: Kimiblock Moe

pkgname=zen-browser-bitwarden
pkgver=2026.1.0
pkgrel=1
pkgdesc='Bitwarden browser extension for Zen'
arch=('any')
url='https://github.com/bitwarden/clients'
license=('GPL-3.0-or-later')
groups=('zen-browser-addons')
pkgdesc='Bitwarden browser extension for Firefox'
makedepends=('nodejs-lts-krypton' 'npm' 'unzip' 'zip' 'git' corepack)
source=("${pkgname}::git+https://github.com/bitwarden/clients.git#tag=browser-v${pkgver}")
b2sums=('27486f0f403b153865687435f594e78433b5fa6483f3b13292ee22cec4afade32199d69a31ef6de3bcecb17d64c5a90bafa57cea1e55117c2886f9fc723b1308')

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
