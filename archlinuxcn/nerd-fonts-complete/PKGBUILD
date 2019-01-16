# Maintainer: Super Bo <supernbo at gmail dot com>
# Contributor: glider <samtron1412 {at} gmail {dot} com>
# Contributor: devopsdeluxe <dan.ray.beste@gmail.com>

pkgname='nerd-fonts-complete'
pkgver=2.0.0
pkgrel=5
pkgdesc='
Iconic font aggregator, collection, and patcher. 40+ patched fonts, over 3,600
glyph/icons, includes popular collections such as Font Awesome & fonts such as
Hack'
arch=('any')
url='https://github.com/ryanoasis/nerd-fonts'
license=('MIT')
depends=('fontconfig' 'xorg-font-utils')
conflicts=('nerd-fonts-git' 'nerd-fonts-complete-mono-glyphs')
install="${pkgname}.install"
source=(
  "${pkgname/-complete}-${pkgver}.tar.xz::https://gitlab.com/devopsdeluxe/nerd-fonts-aur/raw/v${pkgver}/release/NerdFonts.tar.xz"
  "https://raw.githubusercontent.com/ryanoasis/nerd-fonts/v${pkgver}/LICENSE"
  "https://raw.githubusercontent.com/ryanoasis/nerd-fonts/v${pkgver}/bin/scripts/lib/i_all.sh"
  "https://raw.githubusercontent.com/ryanoasis/nerd-fonts/v${pkgver}/bin/scripts/lib/i_dev.sh"
  "https://raw.githubusercontent.com/ryanoasis/nerd-fonts/v${pkgver}/bin/scripts/lib/i_fa.sh"
  "https://raw.githubusercontent.com/ryanoasis/nerd-fonts/v${pkgver}/bin/scripts/lib/i_fae.sh"
  "https://raw.githubusercontent.com/ryanoasis/nerd-fonts/v${pkgver}/bin/scripts/lib/i_iec.sh"
  "https://raw.githubusercontent.com/ryanoasis/nerd-fonts/v${pkgver}/bin/scripts/lib/i_linux.sh"
  "https://raw.githubusercontent.com/ryanoasis/nerd-fonts/v${pkgver}/bin/scripts/lib/i_material.sh"
  "https://raw.githubusercontent.com/ryanoasis/nerd-fonts/v${pkgver}/bin/scripts/lib/i_oct.sh"
  "https://raw.githubusercontent.com/ryanoasis/nerd-fonts/v${pkgver}/bin/scripts/lib/i_ple.sh"
  "https://raw.githubusercontent.com/ryanoasis/nerd-fonts/v${pkgver}/bin/scripts/lib/i_pom.sh"
  "https://raw.githubusercontent.com/ryanoasis/nerd-fonts/v${pkgver}/bin/scripts/lib/i_seti.sh"
  "https://raw.githubusercontent.com/ryanoasis/nerd-fonts/v${pkgver}/bin/scripts/lib/i_weather.sh"
)
sha256sums=(
  '6e203ec84af9f55959141025a96ad3788c8edc7777b7dbcc1fafa600214c1213'
  'd2a29823384e9194a87936ccad495c764c2ef733b29bfa6f72a1d65803ce02e5'
  '036361c808c84242b819ba24246f205b283ae51ba5d5d3304848f999a3ff0622'
  '254f32ceca71d36afee8ddbcd2c98a5de06ab7d7579f03e693987501bef6476b'
  'f3d00c7188f9499911c8215483cb9b430fa1873f531fa57fd30ca20f0cad5314'
  '09cfd8e5748c6401ee2bae24b95eb1c98cb7f7a4200c6337b741084612091b1c'
  'f0fe3eac3a979610153ca60611954cf4baba133e1268f395e2f61a8b800d26dd'
  '3406824f07f7b92757d88356f9f3d89e2270eae0f2862205e7ed1eb8bd294eaf'
  'cddb161c6b4a3ec5f4e4d1723ebc9ce0bea6da572bbb940999a05eaf9ad52d74'
  '67ab5c4bb0d4d057c4d6cd34075a8643f6f845977a2c57d56f05ac931b2f54f0'
  'd94a7c8ede808826258ed651f040bf4d3904fbf81c722692359b5ca5f30d6135'
  '50be7ad9d955a05ba56badabde7992cf5277cc2ccb2348af3293a517bfaefe9d'
  '3245d4859e7c4fe311e79599a406af84564c079d0ba5f36d3a458ee646ca5aac'
  'ced3b935d4f4a04e98da215862de6b6ab4282669fd20ff0b039c913b2f322dec'
)

package() {
  local -r libdir="${pkgdir}/usr/lib/${pkgname}"
  local -r licensedir="${pkgdir}/usr/share/licenses/${pkgname}"
  local -r otfdir="${pkgdir}/usr/share/fonts/${pkgname}/otf"
  local -r ttfdir="${pkgdir}/usr/share/fonts/${pkgname}/ttf"

  # otf:
  install -d -m 755 "${otfdir}"
  while read -r font; do
    install -m 644 "${font}" "${otfdir}"
  done < <(find NerdFonts -name "*.otf")

  # ttf:
  install -d -m 755 "${ttfdir}"
  while read -r font; do
    install -m 644 "${font}" "${ttfdir}"
  done < <(find NerdFonts -name "*.ttf")

  # Scripts:
  install -d -m 755 "${libdir}"
  while read -r script; do
    install -m 644 "${script}" "${libdir}"
  done < <(find "${srcdir}" -maxdepth 1 -name "i_*.sh")

  install -d -m 755 "${licensedir}"
  install -m 644 LICENSE "${licensedir}"
}

# vim: ts=2 sw=2 et:
