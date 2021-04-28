# Maintainer: Jonas Heinrich <onny@project-insanity.org>
# Contributor: Jonas Heinrich <onny@project-insanity.org>
# Contributor: Sergej Pupykin <pupykin.s+arch@gmail.com>

pkgname=nextcloud-app-calendar-git
epoch=1
pkgver=2.1.1.r441.g902994dd
pkgrel=1
pkgdesc="Calendar app for nextcloud"
arch=('any')
url="http://nextcloud.com"
license=('AGPL')
depends=('nextcloud')
# Using older node.js due to https://github.com/sass/node-sass/issues/3077
makedepends=('nodejs-lts-fermium' 'npm' 'composer' 'git')
conflicts=('nextcloud-app-calendar')
provides=('nextcloud-app-calendar')
options=('!strip')
source=("git+https://github.com/nextcloud/calendar.git")
sha512sums=('SKIP')

pkgver() {
  cd "calendar"
  git describe --long | sed 's/\([^-]*-g\)/r\1/;s/-beta/beta/g;s/-rc/rc/g;s/-/./g' | cut -d "v" -f2
}

build() {
  cd "${srcdir}/calendar"
  # -j1 so that `npm install` runs before other steps
  make -j1 dev-setup build-js-production composer-init
}

package() {
  cd "${srcdir}/calendar"

  install -Ddm755 "$pkgdir"/usr/share/webapps/nextcloud/apps/calendar
  # Upstream `appstore` target now creates tarball from a separate cloned repo
  cp -dr --no-preserve=ownership CHANGELOG.md appinfo css img js l10n lib templates vendor \
    "$pkgdir"/usr/share/webapps/nextcloud/apps/calendar
}
