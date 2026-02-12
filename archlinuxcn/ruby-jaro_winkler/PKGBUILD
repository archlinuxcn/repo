# Maintainer: Mario Finelli <mario at finel dot li>

_gemname=jaro_winkler
pkgname=ruby-${_gemname}
pkgver=1.7.0
pkgrel=1
pkgdesc="Ruby & C implementation of Jaro-Winkler distance algorithm"
arch=(i686 x86_64)
depends=(ruby)
makedepends=(rubygems ruby-rdoc)
checkdepends=(ruby-rake ruby-rake-compiler ruby-minitest)
url=https://github.com/tonytonyjan/jaro_winkler
license=(MIT)
options=(!emptydirs)
source=($pkgname-$pkgver.tar.gz::${url}/archive/v$pkgver/$_gemname-$pkgver.tar.gz)
sha256sums=('28e1885960fa0556a604a1361893a88e0f3f581eef80ff3133e92d8702bc2b56')

build() {
  cd ${_gemname}-${pkgver}
  local _gemdir="$(gem env gemdir)"

  gem build "${_gemname}.gemspec"

  gem install \
    --local \
    --verbose \
    --ignore-dependencies \
    --no-user-install \
    --install-dir "tmp_install/${_gemdir}" \
    --bindir "tmp_install/usr/bin" \
    "${_gemname}-${pkgver}.gem"

  # remove unrepreducible files
  rm --force --recursive --verbose \
    "tmp_install/${_gemdir}/cache/" \
    "tmp_install/${_gemdir}/gems/${_gemname}-${pkgver}/vendor/" \
    "tmp_install/${_gemdir}/doc/${_gemname}-${pkgver}/ri/ext/"

  find "tmp_install/${_gemdir}/gems/" \
    -type f \
    \( \
      -iname "*.o" -o \
      -iname "*.c" -o \
      -iname "*.so" -o \
      -iname "*.time" -o \
      -iname "gem.build_complete" -o \
      -iname "Makefile" \
    \) \
    -delete

  find "tmp_install/${_gemdir}/extensions/" \
    -type f \
    \( \
      -iname "mkmf.log" -o \
      -iname "gem_make.out" \
    \) \
    -delete
}

check() {
  cd ${_gemname}-${pkgver}
  local _gemdir="$(gem env gemdir)"
  GEM_HOME="tmp_install/${_gemdir}" rake
}

package() {
  cd ${_gemname}-${pkgver}

  cp --archive --verbose tmp_install/* "${pkgdir}"

  install -v -Dm0644 LICENSE.txt "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
  install -v -Dm0644 README.md "$pkgdir/usr/share/doc/$pkgname/README.md"
  install -v -Dm0644 CHANGELOG.md "$pkgdir/usr/share/doc/$pkgname/CHANGELOG.md"
}

# vim: set ts=2 sw=2 et:
