# Maintainer: Heddxh <g311571057 at gmail dot com>
pkgname=fcitx5-ff14
pkgver=2024.03.12
pkgrel=1
pkgdesc="Final Fantasy XIV dictionary for fcitx5"
arch=(any)
url="https://github.com/heddxh/fcitx5-ff14"
license=('MIT')
depends=(fcitx5)
source=("https://github.com/heddxh/fcitx5-ff14/releases/download/2024.03.12/ff14.dict"
    "https://github.com/heddxh/fcitx5-ff14/raw/main/LICENSE")
sha256sums=('a900fe76eb4b0ff6cf29bed80b67400b5962fbd421cb3ef1f2d2acf6948785f9'
    'bdf13e21e04fcb85f9d4ee1ad80c5ba47aeb9121c49cdac2e356f4340a2eba08')
validpgpkeys=()

package() {
    install -Dm644 ff14.dict -t "$pkgdir/usr/share/fcitx5/pinyin/dictionaries/"
    install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
