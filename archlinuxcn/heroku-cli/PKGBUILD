# Maintainer: Sampson Crowley <sampsonsprojects@gmail.com>
# Contributor: Rhys Kenwell <redrield+aur@gmail.com>

pkgname=heroku-cli
pkgver=7.35.1
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
sha256sums=('64996ba1bf2acbdf86cb2e3087e3e0339f84874318cdd96a9b1c6415d75bcff0')
sha512sums=('2f19b5166433d411016508cb620a8411ea5fff2c6467f5ff173904075bd9653679a6af95c9185b06f8f1a4d5b92ba4de19c349b4a5ec51d156adc03bee895fc1')
noextract=("heroku-$pkgver.tgz")
options=('!strip')

package() {
  npm install -g --user root --prefix "$pkgdir/usr" heroku-$pkgver.tgz
  mkdir -p "$pkgdir/usr/share/licenses/$pkgname"
  ln -s "../../../lib/node_modules/heroku/LICENSE" "$pkgdir/usr/share/licenses/$pkgname"

  # npm makes some directories world writable
  find "$pkgdir/usr" -type d -exec chmod 755 '{}' +
}
