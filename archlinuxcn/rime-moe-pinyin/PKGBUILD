# Maintainer: Kimiblock Moe

pkgname=rime-moe-pinyin
pkgver=5.1
pkgrel=1
pkgdesc="moeOS RIME 全拼方案. 简洁, 现代."
arch=('any')
url="https://github.com/Kimiblock/moeOS-pinyin"
license=('GPL-3.0-or-later')
depends=("rime-pinyin-moegirl" "rime-pinyin-zhwiki")
provides=('rime-moe-pinyin')
source=(
	pinyin::"git+https://github.com/Kimiblock/moeOS-pinyin.git#tag=${pkgver}")
sha256sums=('0e5706f2f7ecfee3987edcb1e59b7c239719545629c0efd2cc421ecdca419927')
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


