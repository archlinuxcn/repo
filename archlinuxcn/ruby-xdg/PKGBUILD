# Maintainer: Filipe Nascimento <flipee at tuta dot io>
# Contributor: Luca Cesari < luca AT cesari DOT me>

_gemname=xdg
pkgname=ruby-xdg
pkgver=5.1.1
pkgrel=1
pkgdesc="Provides a Ruby implementation of the XDG Base Directory Specification"
arch=('any')
url="https://www.alchemists.io/projects/xdg"
license=('Apache')
depends=('ruby' 'ruby-rdoc')
options=(!emptydirs)
source=("http://rubygems.org/downloads/xdg-$pkgver.gem")
noextract=("xdg-$pkgver.gem")
sha256sums=('3d050ea585c0d1fdb69bbb9ee58858edbd7ad6e6db830391e08b174eddbe4b15')

package() {
    local _gemdir
    _gemdir="$(ruby -e 'puts Gem.default_dir')"
    gem install --ignore-dependencies --no-user-install -i "$pkgdir/$_gemdir" -n "$pkgdir/usr/bin" $_gemname-$pkgver.gem
    rm "$pkgdir/$_gemdir/cache/$_gemname-$pkgver.gem"
}
