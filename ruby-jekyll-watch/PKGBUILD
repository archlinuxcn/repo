# Maintainer: Carsten Feuls <archlinux@carstenfeuls.de>

_gemname=jekyll-watch
pkgname=ruby-$_gemname
pkgver=1.5.0
pkgrel=1
pkgdesc='Rebuild your Jekyll site when a file changes with the `--watch` switch.'
arch=('any')
url='https://github.com/jekyll/jekyll-watch'
license=('MIT')
depends=('ruby-listen>3.0')
options=(!emptydirs)
source=(https://rubygems.org/downloads/$_gemname-$pkgver.gem)
noextract=($_gemname-$pkgver.gem)
sha512sums=('8eda8def17883354aa5ecf89f68e8553e664f228dc4b82b0e888c66c6c247592817b8462907d9e69200532a2211d032e3669e5760a3e816f1dd118eea70ca834')

package() {
  local _gemdir="$(ruby -e'puts Gem.default_dir')"
  gem install --ignore-dependencies --no-user-install -i "$pkgdir/$_gemdir" -n "$pkgdir/usr/bin" $_gemname-$pkgver.gem
  rm "$pkgdir/$_gemdir/cache/$_gemname-$pkgver.gem"
}
