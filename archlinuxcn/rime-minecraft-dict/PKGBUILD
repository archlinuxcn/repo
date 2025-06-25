# Maintainer: Kimiblock Moe
pkgname=rime-minecraft-dict
pkgver=1.21.6
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
sha256sums=('63abf09c08ea3d2ed5535a0205aa64be3b1e574bddc827cd919f747c5d1c8de2')

function package(){
	install -Dm644 "${srcdir}/rime-minecraft-dict/minecraft_en.dict.yaml" \
		"${pkgdir}/usr/share/rime-data/minecraft_pinyin.dict.yaml"
	install -Dm644 "${srcdir}/rime-minecraft-dict/minecraft_cn_ext.dict.yaml" \
		"${pkgdir}/usr/share/rime-data/minecraft_pinyin.dict.yaml"
	install -Dm644 "${srcdir}/rime-minecraft-dict/minecraft_cn.dict.yaml" \
		"${pkgdir}/usr/share/rime-data/minecraft_pinyin.dict.yaml"
}
