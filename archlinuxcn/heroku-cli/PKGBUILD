# Maintainer: Sampson Crowley <sampsonsprojects@gmail.com>
# Contributor: Rhys Kenwell <redrield+aur@gmail.com>
# Github Contributor: Michael Herold <https://github.com/michaelherold>

pkgname=heroku-cli
pkgver=7.42.6
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
sha256sums=('afc4183006267e39fb5ff8d6ea5e11f5cf0f606bd1183189ceb13099ae4d4abd')
sha512sums=('f43f8fa699436e7ebf4b14d2612f2a9ea4f8da01f75d75e1411822fdec4535ea4c04cde7d2ac208d1b68d518180b6cf1cf66e3296942009c8c14f800b15023e2')
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
