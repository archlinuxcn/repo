# Maintainer: Mario Finelli <mario at finel dot li>
# Contributor: Artem Vorotnikov <artem at vorotnikov dot me>

_gemname=coderay
pkgname=ruby-$_gemname
pkgver=1.1.3
pkgrel=1
pkgdesc="Fast syntax highlighting for selected languages"
arch=(any)
url=http://coderay.rubychan.de
license=(MIT)
depends=(ruby)
makedepends=(git rubygems ruby-rdoc)
options=(!emptydirs)
source=(git+https://github.com/rubychan/coderay.git?tag=v${pkgver})
sha256sums=('SKIP')

build() {
  cd ${_gemname}
  RELEASE=true gem build ${_gemname}.gemspec
}

package() {
  cd ${_gemname}
  local _gemdir="$(gem env gemdir)"

  gem install \
    --ignore-dependencies \
    --no-user-install \
    -i "$pkgdir/$_gemdir" \
    -n "$pkgdir/usr/bin" \
    $_gemname-$pkgver.gem

  rm "$pkgdir/$_gemdir/cache/$_gemname-$pkgver.gem"

  install -Dm0644 MIT-LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
