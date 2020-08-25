# Maintainer: Sampson Crowley <sampsonsprojects@gmail.com>
# Contributor: Rhys Kenwell <redrield+aur@gmail.com>
# Github Contributor: Michael Herold <https://github.com/michaelherold>

pkgname=heroku-cli
pkgver=7.42.8
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
sha256sums=('96994967ecf268cb5d91830a7204fb0fc9803a066ab67d2a22de8dcf521e78ee')
sha512sums=('f320f6246a4d7397ad7111fe573c6e9b9c8bfb600195754c1dc8e7b645ca21ec51b862b87f6cb932cd623dcbdc0bf71ecebc3b5002821de7d7c0f59da804b019')
noextract=("heroku-$pkgver.tgz")
options=('!strip')

package() {
  npm install -g --user root --prefix "$pkgdir/usr" --cache "$srcdir/npm-cache" heroku-$pkgver.tgz
  mkdir -p "$pkgdir/usr/share/licenses/$pkgname"
  ln -s "../../../lib/node_modules/heroku/LICENSE" "$pkgdir/usr/share/licenses/$pkgname"

  # npm makes some directories world writable
  find "$pkgdir/usr" -type d -exec chmod 755 '{}' +

  # package files should always be owned by root:root
  chown -hR root:root "$pkgdir/usr"
}
