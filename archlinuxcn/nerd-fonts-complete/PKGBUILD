# Maintainer:Francois Menning <f.menning@pm.me>
# Contributor: Super Bo <supernbo at gmail dot com>
# Contributor: glider <samtron1412 {at} gmail {dot} com>
# Contributor: devopsdeluxe <dan.ray.beste@gmail.com>

_gitname='nerd-fonts'
pkgname='nerd-fonts-complete'
pkgver=2.1.0
pkgrel=2
pkgdesc='Iconic font aggregator, collection, & patcher. 3,600+ icons, 50+ patched fonts.'
arch=('any')
url='https://github.com/ryanoasis/nerd-fonts'
license=('MIT')
depends=('fontconfig' 'xorg-font-utils')
conflicts=('nerd-fonts-git' 'nerd-fonts-complete-mono-glyphs')
source=(
  'fix-installer-font-dir.patch'
  "${_gitname}-${pkgver}.tar.gz::https://github.com/ryanoasis/nerd-fonts/archive/v${pkgver}.tar.gz"
)
sha256sums=('ccf93b108044a87bfb29c3f836d2ce4d5bdb1829702e532a69ccb4ab4aecaceb'
            'a084ca91a174b547bab4523507824c76aa91ebcf38f9256a4ffd181813f87bd8')

prepare () {
  cd "$srcdir/$_gitname-$pkgver"

  patch -Np1 -i "$srcdir"/fix-installer-font-dir.patch
}

build() {
  cd "$srcdir/$_gitname-$pkgver"

  bash install.sh \
    --quiet \
    --clean \
    --otf \
    --complete
}

package() {
  cd "$srcdir/$_gitname-$pkgver"

  # Prepare destination directories
  libdir="${pkgdir}/usr/lib/${pkgname}"
  otfdir="${pkgdir}/usr/share/fonts/${pkgname}/OTF"
  ttfdir="${pkgdir}/usr/share/fonts/${pkgname}/TTF"

  install -dm755 "${libdir}"
  install -dm755 "${otfdir}"
  install -dm755 "${ttfdir}"

  # Install fonts
  install -m644 release/NerdFonts/*.otf "${otfdir}"
  install -m644 release/NerdFonts/*.ttf "${ttfdir}"

  # Install scripts
  install -m644 bin/scripts/lib/*.sh "${libdir}"

  # Install license
  install -dm755 "${pkgdir}/usr/share/licenses/${pkgname}"
  install -m644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
