# Maintainer: Kimiblock Moe

pkgname=zen-browser-bitwarden
pkgver=2025.9.0
pkgrel=1
pkgdesc='Bitwarden browser extension for Zen'
arch=('any')
url='https://github.com/bitwarden/clients'
license=('GPL-3.0-or-later')
groups=('zen-browser-addons')
pkgdesc='Bitwarden browser extension for Firefox'
makedepends=('nodejs' 'npm' 'unzip' 'zip' 'git')
source=("${pkgname}::git+https://github.com/bitwarden/clients.git#tag=browser-v${pkgver}")
b2sums=('50ca4103b2401e950a6f9f18b047076179a8ea2b81937769865fee4a9797314b6f3f787e4aef1b3b58146250a9775855e37fe0656acf436f012aabe1214874b7')

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
