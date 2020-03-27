# Maintainer: Sampson Crowley <sampsonsprojects@gmail.com>
# Contributor: Rhys Kenwell <redrield+aur@gmail.com>

pkgname=heroku-cli
pkgver=7.39.0
_builddir=cli-${pkgver}
pkgrel=1
pkgdesc="a tool for creating and managing Heroku apps from the command line"
arch=('x86_64')
url="https://devcenter.heroku.com/articles/heroku-cli"
license=('custom' 'ISC')
depends=('nodejs')
makedepends=('npm')
optdepends=('git: Deploying to Heroku')
conflicts=('heroku-client-standalone' 'heroku-toolbelt' 'ruby-heroku')
source=("https://registry.npmjs.org/heroku/-/heroku-$pkgver.tgz")
sha256sums=('2a722131dc40272205dc4a054e89b760757e13c5a25ff841753e4bd37ee749ad')
sha512sums=('580de291500df90f258284d7743d2475da45e6f5d7b118d2ff257916f770924a93c474708b42c76df941f14bcb5852a9dbc640226945d791081b382e92457bb5')
noextract=("heroku-$pkgver.tgz")
options=('!strip')

package() {
  npm install -g --user root --prefix "$pkgdir/usr" heroku-$pkgver.tgz
  mkdir -p "$pkgdir/usr/share/licenses/$pkgname"
  ln -s "../../../lib/node_modules/heroku/LICENSE" "$pkgdir/usr/share/licenses/$pkgname"

  # npm makes some directories world writable
  find "$pkgdir/usr" -type d -exec chmod 755 '{}' +
}
