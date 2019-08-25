# Maintainer: Shengyu Zhang <la@archlinuxcn.org>
# Co-Maintainer: Bjoern Franke <bjo+aur@schafweide.org>
# Contributor: Carsten Feuls <archlinux@carstenfeuls.de>

_gemname=jekyll
pkgname=$_gemname
pkgver=3.8.6
pkgrel=4
pkgdesc='A simple, blog aware, static site generator.'
arch=('any')
url='https://github.com/jekyll/jekyll'
license=('MIT')
depends=('ruby>=2.1.0'
    'ruby-addressable>=2.4' 'ruby-addressable<3.0'
    'ruby-colorator>=1.0' 'ruby-colorator<=2.0'
    'ruby-jekyll-sass-converter-1>=1.0' 'ruby-jekyll-sass-converter-1<2.0'
    'ruby-jekyll-watch>=2.0' 'ruby-jekyll-watch<3.0'
    'ruby-kramdown-1>=1.14' 'ruby-kramdown-1<2.0'
    'ruby-liquid>=4.0' 'ruby-liquid<5.0'
    'ruby-mercenary>=0.3.3' 'ruby-mercenary<0.4'
    'ruby-pathutil>=0.9' 'ruby-pathutil<1.0'
    'ruby-rouge>1.7' 'ruby-rouge<4.0'
    'ruby-safe_yaml>=1.0' 'ruby-safe_yaml<2.0'
    'ruby-i18n>=0.7' 'ruby-i18n<1.0'
    'ruby-em-websocket>=0.5' 'ruby-em-websocket<1.0'
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
sha512sums=('9b54f3c06373ff515c3f190645a231538b3045a5d39b568defc4977434a52812a1cfa1f9ec836b0b7376d1d0290ca17a55b69b3039203aa8f99df8e9b66c56e3')

package() {
  local _gemdir="$(ruby -e'puts Gem.default_dir')"
  gem install --ignore-dependencies --no-user-install -i "$pkgdir/$_gemdir" -n "$pkgdir/usr/bin" $_gemname-$pkgver.gem
  rm "$pkgdir/$_gemdir/cache/$_gemname-$pkgver.gem"
  install -D -m644 "$pkgdir/$_gemdir/gems/$_gemname-$pkgver/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
