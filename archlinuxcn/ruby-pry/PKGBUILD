# Maintainer: Mario Finelli <mario at finel dot li>
# Contributor: Artem Vorotnikov <artem at vorotnikov dot me>

_gemname=pry
pkgname=ruby-$_gemname
pkgver=0.14.1
pkgrel=2
pkgdesc="An IRB alternative and runtime developer console"
arch=(any)
url=https://github.com/pry/pry
license=(MIT)
depends=(ruby ruby-coderay ruby-method_source)
checkdepends=(ruby-bundler ruby-rake ruby-rspec)
makedepends=(git rubygems ruby-rdoc)
options=(!emptydirs)
source=(git+https://github.com/pry/pry.git?tag=v${pkgver}
        disable-broken-test.patch)
sha256sums=('SKIP'
            'ea965f6849b4757d8dd0099422da406139af847071a20f10e76366e8d6c576e7')

prepare() {
  cd ${_gemname}
  sed -i 's|~>|>=|g' ${_gemname}.gemspec

  # https://github.com/pry/pry/issues/2216
  patch -p1 -N -i "${srcdir}/disable-broken-test.patch"
}

build() {
  cd ${_gemname}
  gem build ${_gemname}.gemspec
}

check() {
  cd ${_gemname}

  # we need to set an EDITOR environment variable or subject.editor is nil
  EDITOR=testing rake spec
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

  rm -rf "$pkgdir/$_gemdir/cache"

  install -Dm0644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
  install -Dm0644 README.md "$pkgdir/usr/share/doc/$pkgname/README.md"
  install -Dm0644 CHANGELOG.md "$pkgdir/usr/share/doc/$pkgname/CHANGELOG.md"
}

# vim: set ts=2 sw=2 et:
