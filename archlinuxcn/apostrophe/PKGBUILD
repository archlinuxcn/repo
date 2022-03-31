# Maintainer: Mark Wagie <mark dot wagie at tutanota dot com>
pkgname=apostrophe
pkgver=2.6.2
pkgrel=1
pkgdesc="A distraction free Markdown editor for GNU/Linux made with GTK+"
arch=('any')
url="https://world.pages.gitlab.gnome.org/apostrophe"
license=('GPL3')
depends=('gspell' 'libhandy>=1.6' 'otf-fira-mono' 'otf-fira-sans' 'python-cairo'
         'python-gobject' 'python-levenshtein' 'python-pyenchant' 'python-pypandoc'
         'python-regex' 'python-setuptools' 'webkit2gtk')
makedepends=('meson' 'gobject-introspection' 'sassc')
optdepends=('texlive-latexextra: for the pdftex module'
            'mathjax: for formula preview')
checkdepends=('appstream-glib')
changelog="$pkgname-NEWS"
source=("https://gitlab.gnome.org/World/apostrophe/-/archive/v$pkgver/$pkgname-v$pkgver.tar.gz")
sha256sums=('b06ca4593ceb21bcd7f9734e41ba3fb69f632b5ab24afcdc66500d18d242c068')

prepare() {
  cd "$pkgname-v$pkgver"

  # Bug 1953395 - Apostrophe can't export to HTML
  sed -i 's|/app/share/fonts/FiraSans-Regular.ttf|/usr/share/fonts/mozilla-fira/FiraSans-Regular.otf|' \
    data/media/css/web/base.css
  sed -i 's|/app/share/fonts/FiraMono-Regular.ttf|/usr/share/fonts/mozilla-fira/FiraMono-Regular.otf|' \
    data/media/css/web/base.css

  # W: hidden-file-or-dir
  rm apostrophe/.pylintrc
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
