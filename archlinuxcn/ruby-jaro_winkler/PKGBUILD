# Maintainer: Mario Finelli <mario at finel dot li>

_commit=13c427010b8065c11f6ea917195b99502d4d8f67 # no tag for v1.6.1
_gemname=jaro_winkler
pkgname=ruby-${_gemname}
pkgver=1.6.1
pkgrel=1
pkgdesc="Ruby & C implementation of Jaro-Winkler distance algorithm"
arch=(i686 x86_64)
depends=(ruby)
makedepends=(rubygems ruby-rdoc)
checkdepends=(ruby-rake ruby-rake-compiler ruby-minitest)
url=https://github.com/tonytonyjan/jaro_winkler
license=(MIT)
options=(!emptydirs)
source=(https://github.com/tonytonyjan/jaro_winkler/archive/$_commit/$_gemname-$pkgver.tar.gz)
sha256sums=('c9047bd6b4fbaf80aca29b922daf4d952519a07544fb7b18b07a44b7ff0fe505')

build() {
  cd ${_gemname}-${_commit}
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
  cd ${_gemname}-${_commit}
  local _gemdir="$(gem env gemdir)"
  GEM_HOME="tmp_install/${_gemdir}" rake
}

package() {
  cd ${_gemname}-${_commit}

  cp --archive --verbose tmp_install/* "${pkgdir}"

  install -v -Dm0644 LICENSE.txt "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
  install -v -Dm0644 README.md "$pkgdir/usr/share/doc/$pkgname/README.md"
  install -v -Dm0644 CHANGELOG.md "$pkgdir/usr/share/doc/$pkgname/CHANGELOG.md"
}

# vim: set ts=2 sw=2 et:
