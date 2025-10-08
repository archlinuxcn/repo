# Maintainer: Kimiblock Moe

pkgname=rime-moe-pinyin-git
pkgver=4.2.r15.g291b65a
pkgrel=2
epoch=1
pkgdesc="moeOS RIME 全拼方案. 简洁, 现代."
arch=('any')
url="https://github.com/Kimiblock/moeOS-pinyin"
license=('GPL-3.0-or-later')
depends=("rime-pinyin-moegirl" "rime-pinyin-zhwiki")
provides=('rime-moe-pinyin')
conflicts=('rime-moe-pinyin')
source=(
	pinyin::"git+https://github.com/Kimiblock/moeOS-pinyin.git")
sha256sums=('SKIP')
makedepends=("git" "git-lfs")

function pkgver() {
	cd "${srcdir}/pinyin"
	git describe --long --tags | sed 's/^v//;s/\([^-]*-g\)/r\1/;s/-/./g'
}

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


