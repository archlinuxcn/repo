# Maintainer: Shengyu Zhang <la@archlinuxcn.org>
# Contributor: Carsten Feuls <archlinux@carstenfeuls.de>

_gemname=jekyll
pkgname=$_gemname
pkgver=3.8.3
pkgrel=1
pkgdesc='A simple, blog aware, static site generator.'
arch=('any')
url='https://github.com/jekyll/jekyll'
license=('MIT')
depends=('ruby>=2.1.0'
    'ruby-addressable>=2.4' 'ruby-addressable<3.0'
    'ruby-colorator>=1.0' 'ruby-colorator<=2.0'
    'ruby-jekyll-sass-converter>=1.0' 'ruby-jekyll-sass-converter<2.0'
    'ruby-jekyll-watch>=2.0' 'ruby-jekyll-watch<3.0'
    'ruby-kramdown>=1.14' 'ruby-kramdown<2.0'
    'ruby-liquid>=4.0' 'ruby-liquid<5.0'
    'ruby-mercenary>=0.3.3' 'ruby-mercenary<0.4'
    'ruby-pathutil>=0.9' 'ruby-pathutil<1.0'
    'ruby-rouge>1.7' 'ruby-rouge<4.0'
    'ruby-safe_yaml>=1.0' 'ruby-safe_yaml<2.0'
    'ruby-i18n>=0.7' 'ruby-i18n<1.0'
    'ruby-concurrent-ruby>=1.0' 'ruby-concurrent-ruby<2.0' # missing dependency for ruby-i18n
    'ruby-em-websocket>=0.5' 'ruby-em-websocket<1.0'
    'ruby-ruby_dep' # missing dependency for ruby-listen
    )
optdepends=('ruby-jekyll-paginate'
    'ruby-jekyll-gist'
    'ruby-jekyll-feed'
    )
provides=("$pkgname=$pkgver" "ruby-jekyll")
conflicts=('ruby-jekyll')
replaces=('ruby-jekyll')
options=(!emptydirs)
source=(https://rubygems.org/downloads/$_gemname-$pkgver.gem)
noextract=($_gemname-$pkgver.gem)
sha512sums=('3b1b486dcae67a92751f410c4984b25355abf6a04b445b8c6e17f102b9a8ee47a7ef143ea2f54afa3a537a92b7a28ec75383581eb018dd73bcd055aafec58ecf')

package() {
  local _gemdir="$(ruby -e'puts Gem.default_dir')"
  gem install --ignore-dependencies --no-user-install -i "$pkgdir/$_gemdir" -n "$pkgdir/usr/bin" $_gemname-$pkgver.gem
  rm "$pkgdir/$_gemdir/cache/$_gemname-$pkgver.gem"
  install -D -m644 "$pkgdir/$_gemdir/gems/$_gemname-$pkgver/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
