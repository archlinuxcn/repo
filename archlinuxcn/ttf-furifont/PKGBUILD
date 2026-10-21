# Maintainer: Vita Yuzu <vita.yuzupon@gmail.com>
pkgbase=ttf-furifont
pkgname=(ttf-furifont-hiragana ttf-furifont-romaji)
pkgver=0.6.2
pkgrel=1
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
sha256sums=('5cd36ebcd9e9562351e01a8f06c9a0cccd2df610181f4d3e7a22381b7879c323'
            'fd73120b5a040cfe5313dad5453026bd7adb88a86f54f7a83468f2bc895289ea'
            'cdcdd8755df054ed5bbb136c0b754cbbfd1a372b099c08bf55b364c4957b9fa4'
            '5fa534373326e40ac1b18bde9a56565fb2801dfedb1ddfa857a41376d4d48a1c'
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
