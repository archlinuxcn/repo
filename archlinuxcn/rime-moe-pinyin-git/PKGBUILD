# Maintainer: Kimiblock Moe

pkgname=rime-moe-pinyin-git
pkgver=20250831.151631
pkgrel=1
pkgdesc="moeOS RIME 全拼方案. 简洁, 现代."
arch=('any')
url="https://github.com/Kimiblock/moeOS-pinyin"
license=('GPL-3.0-or-later')
depends=("rime-pinyin-moegirl" "rime-pinyin-zhwiki")
provides=('rime-moe-pinyin')
conflicts=('rime-moe-pinyin')
source=(
	pinyin::"git+https://github.com/Kimiblock/moeOS-pinyin.git"
	wanxiang-lts-zh-hans.gram::"https://github.com/Kimiblock/moeOS-pinyin/raw/refs/heads/master/rime-data/others/LMDG/wanxiang-lts-zh-hans.gram")
sha256sums=('SKIP'
            '28a34da7f25ae6edbb9906abd9aecb4cf31f0ec004709a23bf602fc1630cafb6')
makedepends=("git" "git-lfs")

function prepare() {
	cd pinyin
	git submodule update --init --depth 1 --remote
}

function package() {
	cd pinyin
	mkdir -p "${pkgdir}/usr/share"
	cp "${srcdir}/pinyin/rime-data" -r "${pkgdir}/usr/share"
	install -Dm644 "${srcdir}/pinyin/default.yaml" "${pkgdir}/usr/share/moeOS-Docs/ibus-rime.conf.d/default.yaml"
	for dir in $(ls "${pkgdir}/usr/share/rime-data/others"); do
		rm -rf "${pkgdir}/usr/share/rime-data/others/${dir}/.git"
	done
	install -Dm644 "${srcdir}/wanxiang-lts-zh-hans.gram" "${pkgdir}/usr/share/rime-data/others/LMDG/wanxiang-lts-zh-hans.gram"
	chmod -R 755 "${pkgdir}/usr/share/rime-data"
}


