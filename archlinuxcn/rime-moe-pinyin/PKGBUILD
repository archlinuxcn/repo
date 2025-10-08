# Maintainer: Kimiblock Moe

pkgname=rime-moe-pinyin
pkgver=5.0
pkgrel=1
pkgdesc="moeOS RIME 全拼方案. 简洁, 现代."
arch=('any')
url="https://github.com/Kimiblock/moeOS-pinyin"
license=('GPL-3.0-or-later')
depends=("rime-pinyin-moegirl" "rime-pinyin-zhwiki")
provides=('rime-moe-pinyin')
source=(
	pinyin::"git+https://github.com/Kimiblock/moeOS-pinyin.git#tag=${pkgver}")
sha256sums=('9ce6ea934b06ddbf44416a9022510e97bf21812cca212d1859372c17e5b0c8f2')
makedepends=("git" "git-lfs")

function prepare() {
	cd pinyin
	git submodule update --init --depth 1 --remote
	./release.sh
}

function package() {
	cd pinyin
	mkdir -p "${pkgdir}/usr/share"
	cp "${srcdir}/pinyin/rime-data" -r "${pkgdir}/usr/share"
	install -Dm644 "${srcdir}/pinyin/default.yaml" "${pkgdir}/usr/share/moeOS-Docs/ibus-rime.conf.d/default.yaml"
	chmod -R 755 "${pkgdir}/usr/share/rime-data"
}


