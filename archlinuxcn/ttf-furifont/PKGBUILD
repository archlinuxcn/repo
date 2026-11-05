# Maintainer: Vita Yuzu <vita.yuzupon@gmail.com>
pkgbase=ttf-furifont
pkgname=(ttf-furifont-hiragana ttf-furifont-romaji)
pkgver=0.7.0
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
sha256sums=('141e54d8f23c55ad8c0cede8d4ac44cfc25c86f9784049418ef276aba32fd74a'
            'be69b38af8b568f44a2f77b66990f0c45854425f0129dce8686f921362c0fef4'
            '080122c2d78b17b865b418671925015e6f64d28e1ccc3b47a06a108cb085b4d3'
            '5f281e32faa7d71a345d5392e9933cd36b4f06024ba4f8e3f6389c18e6230a68'
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
