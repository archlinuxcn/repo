# Maintainer: Mark Wagie <mark dot wagie at proton dot me>
pkgname=apostrophe
pkgver=3.0
pkgrel=2
_reveal_ver=5.1.0
pkgdesc="A distraction free Markdown editor for GNU/Linux made with GTK+"
arch=('any')
url="https://world.pages.gitlab.gnome.org/apostrophe"
license=('GPL-3.0-or-later')
depends=(
  'gtksourceview5'
  'libadwaita'
  'libspelling'
  'python-cairo'
  'python-chardet'
  'python-gobject'
  'python-levenshtein'
  'python-pyenchant'
  'python-pypandoc'
  'python-regex'
  'python-setuptools'
  'ttf-fira-mono'
  'ttf-fira-sans'
  'webkitgtk-6.0'
)
makedepends=(
  'gobject-introspection'
  'meson'
)
optdepends=(
  'mathjax: for formula preview'
  'texlive-bin: for the pdftex module'
)
source=("https://gitlab.gnome.org/World/apostrophe/-/archive/v$pkgver/$pkgname-v$pkgver.tar.gz"
        "https://github.com/hakimel/reveal.js/archive/${_reveal_ver}/reveal.js-${_reveal_ver}.tar.gz"
        'embed-reveal.patch')
sha256sums=('5f06a923ab2bffa16ba623f05b7ac67ea75b49891cee99048c157a15dae29f19'
            'ddc83539ec50583eac9a972e88f892971b37c44e70dd0c08be069e2688684b71'
            'd9f140a58a2f65395450a4907263b8c925d6186f90c59e37cc378141be695f5c')

prepare() {
  cd "$pkgname-v$pkgver"
  mkdir -p "$pkgname/libs/reveal.js"
  cp -r "$srcdir/reveal.js-${_reveal_ver}"/* "$pkgname/libs/reveal.js"

  # Point Meson to the reveal.js files
  patch meson.build < "$srcdir/embed-reveal.patch"
}

build() {
  arch-meson "$pkgname-v$pkgver" build
  meson compile -C build
}

check() {
  meson test -C build --print-errorlogs
}

package() {
  meson install -C build --destdir "$pkgdir"

  install -d "$pkgdir/usr/share/$pkgname/libs/reveal.js"
  cp -r "reveal.js-${_reveal_ver}"/* "$pkgdir/usr/share/$pkgname/libs/reveal.js"
}
