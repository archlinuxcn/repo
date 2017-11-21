# Maintainer: Shengyu Zhang <la@archlinuxcn.org>
# Contributor: Carsten Feuls <archlinux@carstenfeuls.de>

_gemname=jekyll
pkgname=$_gemname
pkgver=3.6.2
pkgrel=1
pkgdesc='A simple, blog aware, static site generator.'
arch=(any)
url='https://github.com/jekyll/jekyll'
license=(MIT)
depends=('ruby>=2.1.0'
    'ruby-addressable>=2.4' 'ruby-addressable<3.0'
    'ruby-colorator>=1.0' 'ruby-colorator<=2.0'
    'ruby-jekyll-sass-converter>=1.0' 'ruby-jekyll-sass-converter<2.0'
    'ruby-jekyll-watch>=1.1' 'ruby-jekyll-watch<2.0'
    'ruby-kramdown>=1.14' 'ruby-kramdown<2.0'
    'ruby-liquid>=4.0' 'ruby-liquid<5.0'
    'ruby-mercenary>=0.3.3' 'ruby-mercenary<0.4'
    'ruby-pathutil>=0.9' 'ruby-pathutil<1.0'
    'ruby-rouge>1.7' 'ruby-rouge<3'
    'ruby-safe_yaml>=1.0' 'ruby-safe_yaml<2.0'
    )
provides=("$pkgname=$pkgver")
conflicts=('ruby-jekyll')
replace=('ruby-jekyll')
options=(!emptydirs)
source=(https://rubygems.org/downloads/$_gemname-$pkgver.gem)
noextract=($_gemname-$pkgver.gem)
sha512sums=('2c212347648cb8f4fe08b06cd248545f9669b25b98ff2784e4e4a79f6e1966ddd538bfc89e2beec68f5a1e2237281bb65a3de511192a22cb18bf78c9843e4f41')

package() {
  local _gemdir="$(ruby -e'puts Gem.default_dir')"
  gem install --ignore-dependencies --no-user-install -i "$pkgdir/$_gemdir" -n "$pkgdir/usr/bin" $_gemname-$pkgver.gem
  rm "$pkgdir/$_gemdir/cache/$_gemname-$pkgver.gem"
  install -D -m644 "$pkgdir/$_gemdir/gems/$_gemname-$pkgver/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
