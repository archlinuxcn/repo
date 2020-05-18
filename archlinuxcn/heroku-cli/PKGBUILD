# Maintainer: Sampson Crowley <sampsonsprojects@gmail.com>
# Contributor: Rhys Kenwell <redrield+aur@gmail.com>
# Github Contributor: Michael Herold <https://github.com/michaelherold>

pkgname=heroku-cli
pkgver=7.40.0
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
sha256sums=('95d3836e08f666b828e16caeaf59f3d68f7abf608a6510d495d1d6306f29e520')
sha512sums=('1d2b89c81f61c809a0996e9f261361a0c56c8e48212e0b9a4f810f7eac06051fbfa4bf197a46d9a44a6aa9080b010fda9e88e9f862a2fd36a081f0ff78ddadd3')
noextract=("heroku-$pkgver.tgz")
options=('!strip')

package() {
  npm install -g --no-progress --user root --prefix "$pkgdir/usr" --cache "$srcdir/npm-cache" heroku-$pkgver.tgz
  mkdir -p "$pkgdir/usr/share/licenses/$pkgname"
  ln -s "../../../lib/node_modules/heroku/LICENSE" "$pkgdir/usr/share/licenses/$pkgname"

  # npm makes some directories world writable
  find "$pkgdir/usr" -type d -exec chmod 755 '{}' +

  # package files should always be owned by root:root
  chown -hR root:root "$pkgdir/usr"
}
