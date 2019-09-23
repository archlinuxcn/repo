# Maintainer: Shengyu Zhang <la@archlinuxcn.org>
# Co-Maintainer: Bjoern Franke <bjo+aur@schafweide.org>
# Co-Maintainer: Bert Peters <bert+aur@bertptrs.nl>
# Contributor: Carsten Feuls <archlinux@carstenfeuls.de>

_gemname=jekyll
pkgname=$_gemname
pkgver=4.0.0
pkgrel=1
pkgdesc='A simple, blog aware, static site generator.'
arch=('any')
url='https://github.com/jekyll/jekyll'
license=('MIT')
depends=('ruby>=2.1.0'
    'ruby-addressable>=2.4'
    'ruby-colorator>=1.0'
    'ruby-jekyll-sass-converter>=2.0'
    'ruby-sassc' # actually a missing dependency of ruby-jekyll-sass-converter
    'ruby-jekyll-watch>=2.0'
    'ruby-kramdown>=2.1.0'
    'ruby-liquid>=4.0' 'ruby-liquid<5.0'
    'ruby-mercenary>=0.3.3' 'ruby-mercenary<0.4'
    'ruby-pathutil>=0.9' 'ruby-pathutil<1.0'
    'ruby-rouge>1.7' 'ruby-rouge<4.0'
    'ruby-safe_yaml>=1.0' 'ruby-safe_yaml<2.0'
    'ruby-i18n>=1'
    'ruby-em-websocket>=0.5' 'ruby-em-websocket<1.0'
    'ruby-kramdown-parser-gfm'
    'ruby-terminal-table'
    )
optdepends=(
    'ruby-minima: Default theme for Jekyll'
    'ruby-jekyll-paginate'
    'ruby-jekyll-gist'
    'ruby-jekyll-feed'
    )
provides=("$pkgname=$pkgver" "ruby-jekyll")
conflicts=('ruby-jekyll')
replaces=('ruby-jekyll')
options=(!emptydirs)
source=(https://rubygems.org/downloads/$_gemname-$pkgver.gem)
noextract=($_gemname-$pkgver.gem)
sha256sums=('4a1dc48895d525bfb98cd562bf03ab6dd2727b5795360877c90e12670b9fec3a')

package() {
  local _gemdir="$(ruby -e'puts Gem.default_dir')"
  gem install --ignore-dependencies --no-user-install -i "$pkgdir/$_gemdir" -n "$pkgdir/usr/bin" $_gemname-$pkgver.gem
  rm "$pkgdir/$_gemdir/cache/$_gemname-$pkgver.gem"
  install -D -m644 "$pkgdir/$_gemdir/gems/$_gemname-$pkgver/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
