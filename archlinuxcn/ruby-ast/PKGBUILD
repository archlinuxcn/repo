# Maintainer: Michael Nussbaum <michaelnussbaum08@gmail.com>

_gemname=ast
pkgname=ruby-$_gemname
pkgver=2.4.2
pkgrel=1
pkgdesc="A library for working with Abstract Syntax Trees"
arch=('any')
url="https://whitequark.github.io/ast/"
license=('MIT')
depends=('ruby')
makedepends=('ruby-rdoc')
source=(https://rubygems.org/downloads/${pkgname#*-}-${pkgver}.gem)
sha256sums=('1e280232e6a33754cde542bc5ef85520b74db2aac73ec14acef453784447cc12')
noextract=("${pkgname#*-}-$pkgver.gem")

package() {
  local _gemdir="$(ruby -e'puts Gem.default_dir')"
  gem install --ignore-dependencies --no-user-install -i "$pkgdir/$_gemdir" "$_gemname-$pkgver.gem"
}
