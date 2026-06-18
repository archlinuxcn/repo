# Maintainer: Kimiblock Moe
pkgname=rime-minecraft-dict
pkgver=26.2
pkgrel=1
pkgdesc="Minecraft dict for RIME"
arch=('any')
url="https://github.com/Kimiblock/rime-minecraft-dict"
license=('GPL-3.0-or-later')
depends=()
makedepends=("git")
provides=('rime-minecraft-dict')
conflicts=('rime-minecraft-dict')
source=("git+https://github.com/Kimiblock/rime-minecraft-dict.git#tag=${pkgver}")
sha256sums=('5cb28424f6e5880ef50f2de02dfb7f84402122bc8361998ffa789a3a244b3be2')

function package(){
	install -Dm644 "${srcdir}/rime-minecraft-dict/minecraft_en.dict.yaml" \
		"${pkgdir}/usr/share/rime-data/minecraft_pinyin.dict.yaml"
	install -Dm644 "${srcdir}/rime-minecraft-dict/minecraft_cn_ext.dict.yaml" \
		"${pkgdir}/usr/share/rime-data/minecraft_pinyin.dict.yaml"
	install -Dm644 "${srcdir}/rime-minecraft-dict/minecraft_cn.dict.yaml" \
		"${pkgdir}/usr/share/rime-data/minecraft_pinyin.dict.yaml"
}
