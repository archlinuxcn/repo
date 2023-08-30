# Maintainer: George Rawlinson <grawlinson@archlinux.org>

pkgname=lemmy-ui
pkgver=0.18.4
pkgrel=3
pkgdesc='The official web app for lemmy'
arch=('any')
url='https://github.com/LemmyNet/lemmy-ui'
license=('AGPL3')
depends=('nodejs' 'lemmy')
makedepends=('git' 'yarn' 'python')
backup=('etc/lemmy/lemmy-ui.env')
_commit='fd8d45282926f7d3e1e2df37e5656243386a4a05'
source=(
  "$pkgname::git+https://github.com/LemmyNet/lemmy-ui#commit=$_commit"
  'git+https://github.com/LemmyNet/lemmy-translations.git'
  'systemd.service'
  'tmpfiles.conf'
  'config.env'
)
b2sums=('SKIP'
        'SKIP'
        '45a104b346e866fdefd84e581eb2b1bb8d8e0aef2193a4a7996fc3d6f0541edb3da0bca766af487efea9760a6c655a1577d3cc901dee54ad0a0fd73182476a04'
        'ba5c683c5a71ceae18b009c7177def65de4311ecebed9d7d1e5d75e09aadb3d8b7ff2e5007d1eb23bdd3a2c389e581dc88c2131d492eaa8245269d75d63e07a7'
        '2d498b293181523feecff185cb8592dd5af90ed482755232b5ef7dc143dca2de4808073315c7d638e051ab4513464b8c8440d69d2f345de67d220b7c1b0009c2')

pkgver() {
  cd "$pkgname"
  git describe --tags | sed 's/^v//'
}

prepare() {
	cd "$pkgname"

  # setup submodules
  git submodule init
  git config submodule.lemmy-translations.url ../lemmy-translations
  git -c protocol.file.allow=always submodule update

  # set UI version
  sed -i "s/unknown version/$pkgver/" src/shared/version.ts
}

build() {
	cd "$pkgname"

  yarn install
  yarn build:prod
}

package() {
  # systemd integration
  install -vDm644 config.env "$pkgdir/etc/lemmy/$pkgname.env"
  install -vDm644 systemd.service "$pkgdir/usr/lib/systemd/system/$pkgname.service"
  install -vDm644 tmpfiles.conf "$pkgdir/usr/lib/tmpfiles.d/$pkgname.conf"

	cd "$pkgname"

  install -vd "$pkgdir/usr/share/$pkgname"
  cp -R dist node_modules "$pkgdir/usr/share/$pkgname"
}
