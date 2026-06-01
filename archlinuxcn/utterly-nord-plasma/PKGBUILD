# Maintainer: Cryolitia PukNgae <cryolitia at gmail dot com>
# Maintainer: Yiyao Yu <yuydevel at protonmail dot com>
# Author: Himprakash Deka <himprakashd at gmail dot com>

pkgname=utterly-nord-plasma
pkgver=3.3
pkgrel=2
pkgdesc='A Slick and Modern Global theme for KDE Plasma utilizing the Nord Color Palette with transparency and blur in UI '
url='https://github.com/HimDek/Utterly-Nord-Plasma'
_commit='ae0de9d555b518226627b2d10ee5df4a18073c60'
arch=('any')
license=('GPL-2.0-or-later')
depends=('bash' 'kirigami' 'libplasma' 'plasma-workspace' 'qt6-5compat' 'qt6-declarative')
makedepends=('git')
optdepends=('kvantum: kvantum application style',
            'konsole: konsole color scheme'
            'sddm: sddm login theme'
            'utterly-round-plasma-style: complementing kwin style')
source=("${pkgname}::git+${url}.git#commit=${_commit}")
sha256sums=('SKIP')
_theme_base='Utterly-Nord'

_package_and_rename() {
  local _src="$1"
  local _dst="$2"
  mkdir -p "${_dst}"
  cd "${_src}"
  find -type f -exec \
    install -Dm 644 '{}' "${_dst}/{}" \;
}

package() {
  cd "${srcdir}/${pkgname}"

  # colors
  mkdir -p "${pkgdir}/usr/share/color-schemes/"
  install -Dm 644 *.colors "${pkgdir}/usr/share/color-schemes/"

  # Konsole
  mkdir -p "${pkgdir}/usr/share/konsole/"
  install -Dm 644 *.colorscheme "${pkgdir}/usr/share/konsole/"

  # look-and-feel
  _package_and_rename \
    "${srcdir}/${pkgname}/look-and-feel" \
    "${pkgdir}/usr/share/plasma/look-and-feel/${_theme_base}"

  _package_and_rename \
    "${srcdir}/${pkgname}/look-and-feel-solid" \
    "${pkgdir}/usr/share/plasma/look-and-feel/${_theme_base}-Solid"

  _package_and_rename \
    "${srcdir}/${pkgname}/look-and-feel-light" \
    "${pkgdir}/usr/share/plasma/look-and-feel/${_theme_base}-Light"

  _package_and_rename \
    "${srcdir}/${pkgname}/look-and-feel-light-solid" \
    "${pkgdir}/usr/share/plasma/look-and-feel/${_theme_base}-Light-Solid"

  # wallpaper
  _package_and_rename \
    "${srcdir}/${pkgname}/wallpaper" \
    "${pkgdir}/usr/share/wallpapers/${_theme_base}"

  # kvantum
  _package_and_rename \
    "${srcdir}/${pkgname}/kvantum" \
    "${pkgdir}/usr/share/Kvantum/${_theme_base}"

  _package_and_rename \
    "${srcdir}/${pkgname}/kvantum-solid" \
    "${pkgdir}/usr/share/Kvantum/${_theme_base}-Solid"

  _package_and_rename \
    "${srcdir}/${pkgname}/kvantum-light" \
    "${pkgdir}/usr/share/Kvantum/${_theme_base}-Light"

  _package_and_rename \
    "${srcdir}/${pkgname}/kvantum-light-solid" \
    "${pkgdir}/usr/share/Kvantum/${_theme_base}-Light-Solid"

  # sddm
  _package_and_rename \
    "${srcdir}/${pkgname}/sddm" \
    "${pkgdir}/usr/share/sddm/themes/${_theme_base}"

}

# vim:set et ts=2 sw=2 tw=79:
