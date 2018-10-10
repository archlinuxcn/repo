# Maintainer: Mario Finelli <mario at finel dot li>
# Contributor: Artem Vorotnikov <artem at vorotnikov dot me>

_gemname=coderay
pkgname=ruby-$_gemname
pkgver=1.1.2
pkgrel=2
pkgdesc='Fast syntax highlighting for selected languages.'
arch=(any)
url='http://coderay.rubychan.de'
license=(MIT)
depends=(ruby)
makedepends=(rubygems ruby-rdoc)
options=(!emptydirs)
source=(https://rubygems.org/downloads/$_gemname-$pkgver.gem)
noextract=($_gemname-$pkgver.gem)
sha256sums=('9efc1b3663fa561ccffada890bd1eec3a5466808ebc711ab1c5d300617d96a97')

package() {
  local _gemdir="$(ruby -e'puts Gem.default_dir')"

  gem install \
    --ignore-dependencies \
    --no-user-install \
    -i "$pkgdir/$_gemdir" \
    -n "$pkgdir/usr/bin" \
    $_gemname-$pkgver.gem

  rm "$pkgdir/$_gemdir/cache/$_gemname-$pkgver.gem"

  install -Dm0644 "$pkgdir/$_gemdir/gems/$_gemname-$pkgver/MIT-LICENSE" \
    "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
