# Co-Maintainer: Shengyu Zhang <la@archlinuxcn.org>
# Maintainer: Carsten Feuls <archlinux@carstenfeuls.de>

_gemname=jekyll-watch
pkgname=ruby-$_gemname
pkgver=2.2.1
pkgrel=1
pkgdesc='Rebuild your Jekyll site when a file changes with the `--watch` switch.'
arch=('any')
url='https://github.com/jekyll/jekyll-watch'
license=('MIT')
depends=('ruby-listen>=3.0' 'ruby-listen<4.0' 'ruby-rdoc')
options=(!emptydirs)
source=(https://rubygems.org/downloads/$_gemname-$pkgver.gem)
noextract=($_gemname-$pkgver.gem)
sha512sums=('9f64ee866d844fadbe6ee854e3b893c049abba0a58cc9d0c483fb320557ff557d834ac5b026288f38a8648b1c465253b1e7f9a9d84483c65f889918cd474e811')

package() {
  local _gemdir="$(ruby -e'puts Gem.default_dir')"
  gem install --ignore-dependencies --no-user-install -i "$pkgdir/$_gemdir" -n "$pkgdir/usr/bin" $_gemname-$pkgver.gem
  rm "$pkgdir/$_gemdir/cache/$_gemname-$pkgver.gem"
}
