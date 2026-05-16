# Maintainer: Gavin Luo <lunt.luo@gmail.com>

pkgname=rime-wanxiang-gram-zh-hans
pkgver=20260517.004732
pkgrel=1
epoch=2
pkgdesc="万象词库中文语法模型"
arch=(any)
license=('CC-BY-4.0')
url="https://github.com/amzxyz/RIME-LMDG"
source=("wanxiang-lts-zh-hans.${pkgver}.gram::${url}/releases/download/LTS/wanxiang-lts-zh-hans.gram")
sha256sums=('aa1f5b1c7cc3f913c28f8a4f7094132ed9c8b557051bdb17faaf797bb4e7266d')

package_rime-wanxiang-gram-zh-hans() {
    replaces=(rime-lmdg)

    install -Dm664 "${srcdir}/wanxiang-lts-zh-hans.${pkgver}.gram" "${pkgdir}"/usr/share/rime-data/wanxiang-lts-zh-hans.gram
}
