# Maintainer: Carsten Feuls <archlinux@carstenfeuls.de>

_gemname=jekyll-sass-converter
pkgname=ruby-$_gemname
pkgver=1.4.0
pkgrel=1
pkgdesc='A basic Sass converter for Jekyll.'
arch=(any)
url='https://github.com/jekyll/jekyll-sass-converter'
license=(MIT)
depends=('ruby' 'ruby-sass')
options=(!emptydirs)
source=(https://rubygems.org/downloads/$_gemname-$pkgver.gem)
noextract=($_gemname-$pkgver.gem)
sha512sums=('cda8b113c433e6ca7fa1a019e63473d6d1adb77f885e1fa09cece8d360772f3985802383bbb24e9e9f7e9ab1728462243249d0e5cf93e95d4b5eb1f3df446ab8')

package() {
  local _gemdir="$(ruby -e'puts Gem.default_dir')"
  gem install --ignore-dependencies --no-user-install -i "$pkgdir/$_gemdir" -n "$pkgdir/usr/bin" $_gemname-$pkgver.gem
  rm "$pkgdir/$_gemdir/cache/$_gemname-$pkgver.gem"
}
