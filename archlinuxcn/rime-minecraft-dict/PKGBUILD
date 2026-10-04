# Maintainer: Kimiblock Moe
pkgname=rime-minecraft-dict
pkgver=26.3
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
sha256sums=('c5f95feea04558230448918aec786b964946ce4c6b77eaa550aa26869521f099')

function package(){
	install -Dm644 "${srcdir}/rime-minecraft-dict/minecraft_en.dict.yaml" \
		"${pkgdir}/usr/share/rime-data/minecraft_pinyin.dict.yaml"
	install -Dm644 "${srcdir}/rime-minecraft-dict/minecraft_cn_ext.dict.yaml" \
		"${pkgdir}/usr/share/rime-data/minecraft_pinyin.dict.yaml"
	install -Dm644 "${srcdir}/rime-minecraft-dict/minecraft_cn.dict.yaml" \
		"${pkgdir}/usr/share/rime-data/minecraft_pinyin.dict.yaml"
}
