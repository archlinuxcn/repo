# Maintainer: George Rawlinson <grawlinson@archlinux.org>

pkgname=lemmy-ui
pkgver=0.16.3
pkgrel=1
pkgdesc="The official web app for lemmy"
arch=('any')
url="https://github.com/LemmyNet/lemmy-ui"
license=('AGPL3')
depends=('nodejs')
makedepends=('git' 'yarn' 'python')
_commit='de5552f87048aee88f9450ff3e840aa778c4b3ca'
source=(
  "$pkgname::git+https://github.com/LemmyNet/lemmy-ui#commit=$_commit"
  'git+https://github.com/LemmyNet/lemmy-translations.git'
)
b2sums=('SKIP' 'SKIP')

pkgver() {
  cd "$pkgname"
  git describe --tags | sed 's/^v//'
}

prepare() {
	cd "$pkgname"

  # setup submodules
  git submodule init
  git config submodule.lemmy-translations.url ../lemmy-translations
  git submodule update

  # set UI version
  sed -i "s/unknown version/$pkgver/" src/shared/version.ts
}

build() {
	cd "$pkgname"

  yarn install
  yarn build:prod
}

package() {
	cd "$pkgname"

  install -vd "$pkgdir/usr/share/$pkgname"
  cp -R dist/* node_modules "$pkgdir/usr/share/$pkgname"
}
