# Maintainer: Mario Finelli <mario at finel dot li>
# Contributor: carstene1ns <arch carsten-teibes de> - http://git.io/ctPKG
# Contributor: Artem Vorotnikov <artem@vorotnikov.me>

_gemname=rb-fsevent
pkgname=ruby-$_gemname
pkgver=0.10.3
pkgrel=1
pkgdesc='Very simple & usable FSEvents API.'
arch=('i686' 'x86_64')
url='http://rubygems.org/gems/rb-fsevent'
license=('MIT')
depends=('ruby')
makedepends=('ruby-rdoc')
source=("https://rubygems.org/downloads/$_gemname-$pkgver.gem")
noextract=("$_gemname-$pkgver.gem")
sha256sums=('a8f78186feb55bb98579b5e0f8dd925ececfde1b5c2496e5e932997ff999a1d2')
options=(!emptydirs)

package() {
  local _gemdir="$(ruby -e'puts Gem.default_dir')"

  gem install \
    --ignore-dependencies \
    --no-user-install \
    -i "$pkgdir/$_gemdir" \
    -n "$pkgdir/usr/bin" \
    $_gemname-$pkgver.gem

  rm "$pkgdir/$_gemdir/cache/$_gemname-$pkgver.gem"

  install -Dm0644 "$pkgdir/$_gemdir/gems/$_gemname-$pkgver/LICENSE.txt" \
    "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
