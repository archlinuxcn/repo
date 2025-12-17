# Maintainer: Kimiblock Moe
pkgname=rime-minecraft-dict
pkgver=1.21.11.1
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
sha256sums=('91e407209fa7b901085eded4c2a0eff0dc5c473bb2c6fd676a69d2e77d3bfcb7')

function package(){
	install -Dm644 "${srcdir}/rime-minecraft-dict/minecraft_en.dict.yaml" \
		"${pkgdir}/usr/share/rime-data/minecraft_pinyin.dict.yaml"
	install -Dm644 "${srcdir}/rime-minecraft-dict/minecraft_cn_ext.dict.yaml" \
		"${pkgdir}/usr/share/rime-data/minecraft_pinyin.dict.yaml"
	install -Dm644 "${srcdir}/rime-minecraft-dict/minecraft_cn.dict.yaml" \
		"${pkgdir}/usr/share/rime-data/minecraft_pinyin.dict.yaml"
}
