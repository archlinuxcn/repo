#!/bin/bash
# Maintainer: Kimiblock Moe

pkgname=(cinny-web)
pkgbase=cinny
pkgver=4.12.7
pkgrel=1
pkgdesc='Yet another matrix client — web version'
arch=(any)
license=(AGPL-3.0-or-later)
depends=()
url=https://github.com/cinnyapp/cinny
#makedepends=(npm git yarn)
makedepends=(npm yarn)
#source=("git+https://github.com/cinnyapp/cinny#tag=v${pkgver}")
source=(
	cinny-${pkgver}.tar.gz::"https://github.com/cinnyapp/cinny/archive/refs/tags/v${pkgver}.tar.gz"
)
sha512sums=('53a1c4693369245de2ed34acc145950e9421e67ac982e3e21678c2b58802ed83dba6da0352003e7d083a186be8274e61282193abe661cf46b8c900da24a65ea7')

function prepare() {
	NODE_OPTIONS="--max_old_space_size=4096"
	cd "cinny-${pkgver}"
	#yarn
	npm install --legacy-peer-deps
}

build() {
	if [ ! ${cinnyBase} ]; then
		cinnyBase='/'
	fi
	sed -i "s|/|${cinnyBase}|g" "${srcdir}"/"cinny-${pkgver}"/build.config.ts
	cd "cinny-${pkgver}"
	NODE_OPTIONS="--max_old_space_size=4096"
	#yarn dist
	#yarn run build
	npm run build
}

package_cinny-web() {
	url=https://github.com/cinnyapp/cinny
	NODE_OPTIONS="--max_old_space_size=4096"
	backup=('etc/webapps/cinny/config.json')
	cd "cinny-${pkgver}"
	install -d "$pkgdir/usr/share/webapps/$pkgbase"
	cp -r dist/* "$pkgdir/usr/share/webapps/$pkgbase"
	install -d "$pkgdir/etc/webapps/$pkgbase"
	mv "${pkgdir}/usr/share/webapps/$pkgbase/config.json" \
		"${pkgdir}/etc/webapps/$pkgbase/config.json"
	ln -sfr "${pkgdir}/etc/webapps/$pkgbase/config.json" \
		"${pkgdir}/usr/share/webapps/$pkgbase/config.json"
}
