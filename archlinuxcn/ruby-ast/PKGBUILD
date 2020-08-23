# Maintainer: Michael Nussbaum <michaelnussbaum08@gmail.com>

_gemname=ast
pkgname=ruby-$_gemname
pkgver=2.4.1
pkgrel=1
pkgdesc="A library for working with Abstract Syntax Trees"
arch=('any')
url="https://whitequark.github.io/ast/"
license=('MIT')
depends=('ruby')
makedepends=('ruby-rdoc')
source=(https://rubygems.org/downloads/${pkgname#*-}-${pkgver}.gem)
sha256sums=('4a54905a05a3ae848ec67d81a79625b77b92feb91090ab46a2bdcaff193264d0')
noextract=("${pkgname#*-}-$pkgver.gem")

package() {
  local _gemdir="$(ruby -e'puts Gem.default_dir')"
  gem install --ignore-dependencies --no-user-install -i "$pkgdir/$_gemdir" "$_gemname-$pkgver.gem"
}
