# Maintainer: Mark Wagie <mark dot wagie at proton dot me>
pkgname=apostrophe
pkgver=3.0
pkgrel=1
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
  'webkitgtk-6.0'
)
makedepends=(
  'gobject-introspection'
  'meson'
)
optdepends=(
  'mathjax: for formula preview'
  'texlive-bin: for the pdftex module'
  'ttf-fira-mono: recommended Mono font'
  'ttf-fira-sans: recommended Sans font'
)
source=("https://gitlab.gnome.org/World/apostrophe/-/archive/v$pkgver/$pkgname-v$pkgver.tar.gz"
        '0001-Use-system-font.patch'
        '2-rm-reveal-check.patch')
sha256sums=('5f06a923ab2bffa16ba623f05b7ac67ea75b49891cee99048c157a15dae29f19'
            'e909c05f259a874afd5e414fd13b0f162972e59c61c23e6d619e502254fcd4fe'
            'a3e2eea5fca084f53fd6d0f9e61ace8e14b4c83d9c2f1d5ea74c8589c8c10b8f')

prepare() {
  cd "$pkgname-v$pkgver"

  # Bug 1953395 - Apostrophe can't export to HTML
  sed -i 's|/app/share/fonts/FiraSans-Regular.ttf|/usr/share/fonts/OTF/FiraSans-Regular.otf|' \
    data/media/css/web/base.css
  sed -i 's|/app/share/fonts/FiraMono-Regular.ttf|/usr/share/fonts/OTF/FiraMono-Regular.otf|' \
    data/media/css/web/base.css

  # W: hidden-file-or-dir
  rm apostrophe/.pylintrc

  # Use system monospace & sans font instead of hard dependency on Fira Mono / Fira Sans
  patch -Np1 -i "$srcdir/0001-Use-system-font.patch"

  ## TODO Find a way to package reveal.js
  patch meson.build < "$srcdir/2-rm-reveal-check.patch"
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
}
