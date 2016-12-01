# Maintainer: Carsten Feuls <archlinux@carstenfeuls.de>

_gemname=jekyll-watch
pkgname=ruby-$_gemname
pkgver=1.3.1
pkgrel=1
pkgdesc='Rebuild your Jekyll site when a file changes with the `--watch` switch.'
arch=('any')
url='https://github.com/jekyll/jekyll-watch'
license=('MIT')
depends=('ruby-listen>3.0')
options=(!emptydirs)
source=(https://rubygems.org/downloads/$_gemname-$pkgver.gem)
noextract=($_gemname-$pkgver.gem)
sha512sums=('b47930117f502b701da54cc99ca8686f26d53a009758a17b03f9148381dd355b4e3b29e447e31b644226ce0757a2dc070cee0285180c5fdd34c52751e1ddfbd5')

package() {
  local _gemdir="$(ruby -e'puts Gem.default_dir')"
  gem install --ignore-dependencies --no-user-install -i "$pkgdir/$_gemdir" -n "$pkgdir/usr/bin" $_gemname-$pkgver.gem
  rm "$pkgdir/$_gemdir/cache/$_gemname-$pkgver.gem"
}
