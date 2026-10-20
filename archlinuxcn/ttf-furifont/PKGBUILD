# Maintainer: Vita Yuzu <vita.yuzupon@gmail.com>
pkgbase=ttf-furifont
pkgname=(ttf-furifont-hiragana ttf-furifont-romaji)
pkgver=0.6.1
pkgrel=2
pkgdesc='Japanese variable fonts with built-in furigana'
arch=('any')
url='https://furifont.antfu.me'
license=('OFL-1.1')
provides=('ttf-font')
_release="https://github.com/antfu/furifont/releases/download/v${pkgver}"
source=(
  "FurifontSansVF-${pkgver}.ttf::${_release}/FurifontSansVF.ttf"
  "FurifontSerifVF-${pkgver}.ttf::${_release}/FurifontSerifVF.ttf"
  "FurifontSansRomajiVF-${pkgver}.ttf::${_release}/FurifontSansRomajiVF.ttf"
  "FurifontSerifRomajiVF-${pkgver}.ttf::${_release}/FurifontSerifRomajiVF.ttf"
  "OFL-${pkgver}.txt::${_release}/OFL.txt"
  "DATA-LICENSE-${pkgver}.md::${_release}/DATA-LICENSE.md"
)
sha256sums=('9d86d5f2893803d910ac1667e886881a4475e2132066b9f03e03440776b4bbe5'
            'd63c8c0849c6ca92b4e63bf5f3d69e66fa6087e44abc58ef8ff357e083e12bf3'
            '4113e8977a64ea1f9af47c59cce2da53f505b222de2234c7b1a40918bfbe6bb8'
            'ff44113025ac06d3d83c3c1a1366fd094c25f196389828426f13afb8b26860ae'
            'fcac737e761ec63dbfbdce11030a1780161920d80315edba9c8beff1c2bac5a2'
            '28989f9dfb9ee3d81f814efdf7d0c1d0bb750ba45ea1d908c93260dfd920f607')

package_ttf-furifont-hiragana() {
  pkgdesc='Furifont Sans and Serif variable fonts with hiragana furigana'

  install -Dm644 "FurifontSansVF-${pkgver}.ttf" \
    "${pkgdir}/usr/share/fonts/TTF/FurifontSansVF.ttf"
  install -Dm644 "FurifontSerifVF-${pkgver}.ttf" \
    "${pkgdir}/usr/share/fonts/TTF/FurifontSerifVF.ttf"

  install -Dm644 "OFL-${pkgver}.txt" \
    "${pkgdir}/usr/share/licenses/${pkgname}/OFL.txt"
  install -Dm644 "DATA-LICENSE-${pkgver}.md" \
    "${pkgdir}/usr/share/licenses/${pkgname}/DATA-LICENSE.md"
}

package_ttf-furifont-romaji() {
  pkgdesc='Furifont Sans and Serif variable fonts with romaji furigana'

  install -Dm644 "FurifontSansRomajiVF-${pkgver}.ttf" \
    "${pkgdir}/usr/share/fonts/TTF/FurifontSansRomajiVF.ttf"
  install -Dm644 "FurifontSerifRomajiVF-${pkgver}.ttf" \
    "${pkgdir}/usr/share/fonts/TTF/FurifontSerifRomajiVF.ttf"

  install -Dm644 "OFL-${pkgver}.txt" \
    "${pkgdir}/usr/share/licenses/${pkgname}/OFL.txt"
  install -Dm644 "DATA-LICENSE-${pkgver}.md" \
    "${pkgdir}/usr/share/licenses/${pkgname}/DATA-LICENSE.md"
}
