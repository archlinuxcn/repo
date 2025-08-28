# Maintainer: Kimiblock Moe

pkgname=zen-browser-bitwarden
pkgver=2025.8.2
pkgrel=1
pkgdesc='Bitwarden browser extension for Zen'
arch=('any')
url='https://github.com/bitwarden/clients'
license=('GPL-3.0-or-later')
groups=('zen-browser-addons')
pkgdesc='Bitwarden browser extension for Firefox'
makedepends=('nodejs' 'npm' 'unzip' 'zip' 'git')
source=("${pkgname}::git+https://github.com/bitwarden/clients.git#tag=browser-v${pkgver}")
b2sums=('9610037a4f3e7d679b5e21d9d010186ca2270394a8d0ab66793c59cf0638500a935c712103e457bf0d1f3b274020b598f1b77679c5c49a670fa091fae89fc734')

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
