# Maintainer: Super Bo <supernbo at gmail dot com>
# Maintainer: glider <samtron1412 {at} gmail {dot} com>
pkgname='nerd-fonts-complete'
pkgver=2.0.0
pkgrel=1
pkgdesc="collection of over 20 patched fonts (complete variant) for \
         powerline, devicons, and vim-devicons: includes Droid Sans, \
         Meslo, AnonymousPro, ProFont, Inconsolta, and many more"
arch=('any')
url='https://github.com/ryanoasis/nerd-fonts'
license=('MIT')
depends=('fontconfig' 'xorg-font-utils')
conflicts=('nerd-fonts-git' 'nerd-fonts-complete-mono-glyphs')
install="${pkgname}.install"
source=(
  "${pkgname}-${pkgver}.tar.gz::https://github.com/ryanoasis/nerd-fonts/archive/v${pkgver}.tar.gz"
  'https://raw.githubusercontent.com/ryanoasis/nerd-fonts/v2.0.0/install.sh'
  'arch-friendly-installer.patch'
)
sha256sums=(
  '0d5939042eff3b2d9b81ee2a871b3d2c046cbc6781f20ae87cdecfc1833e7bc8'
  '0e2cdb9d4c84e8b697f32c77f0b5cae2a2fa8ba93ae60ca852c06a34fc14395c'
  'd7073412a8d8402c6f1278dc15432edeec56092d1e47fd435741eda66919e57d'
)

package() {
  cd "${pkgname/-complete}-${pkgver}"

  cp ../install.sh .
  patch install.sh < ../arch-friendly-installer.patch
  export pkgdir

  # otf:
  ./install.sh --clean --install-to-system-path --quiet --otf
  install -d -m 755 "${pkgdir}/usr/share/fonts/NerdFonts/otf"
  for otf in "${pkgdir}/usr/share/fonts/NerdFonts/"*.otf; do
    install -m 644 "${otf}" "${pkgdir}/usr/share/fonts/NerdFonts/otf"
  done

  # ttf:
  ./install.sh --install-to-system-path --quiet --ttf
  install -d -m 755 "${pkgdir}/usr/share/fonts/NerdFonts/ttf"
  for ttf in "${pkgdir}/usr/share/fonts/NerdFonts/"*.ttf; do
    install -m 644 "${ttf}" "${pkgdir}/usr/share/fonts/NerdFonts/ttf"
  done

  # Cleanup:
  rm "${pkgdir}/usr/share/fonts/NerdFonts/"*.otf
  rm "${pkgdir}/usr/share/fonts/NerdFonts/"*.ttf
  mv "${pkgdir}/usr/share/fonts/NerdFonts" "${pkgdir}/usr/share/fonts/${pkgname}"
}

# vim: ts=2 sw=2 et:
