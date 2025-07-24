# Maintainer: Kimiblock Moe

pkgname=firefox-portable
pkgver=141.0
pkgrel=1
epoch=1
pkgdesc="Firefox sandboxed by portable"
arch=('any')
url="https://github.com/Kraftland/portable"
license=('GPL-3.0-or-later')
groups=()
options=(!debug !strip)
depends=("firefox" "portable")

optdepends=()

makedepends+=()

checkdepends=()

source=(
	portable-config
	firefox.sh
	firefox.desktop
)


md5sums=('c4a91aae851117c60742624c1b64a7c9'
         'e9286af04e5d107b38523c92f9c68c76'
         '2f74e3e788705621db286bb25fcabdee')

function package() {
	install -Dm644 portable-config \
		"${pkgdir}/usr/lib/portable/info/org.mozilla.firefox/config"
	install -Dm755 "firefox.sh" \
		"${pkgdir}/usr/bin/firefox-portable"
	install -Dm644 "firefox.desktop" "${pkgdir}/usr/share/applications/org.mozilla.firefox.desktop"
	install -d "${pkgdir}/usr/share/libalpm/hooks"

	echo '''[Action]
When = PostTransaction
Exec = /usr/bin/ln "-sfr" "/usr/bin/firefox-portable" "/usr/bin/firefox"
Depends = firefox
Description = Configuring Firefox for Portable

[Trigger]
Operation = Install
Operation = Upgrade
Type = Path
Target = usr/bin/firefox-portable
Target = usr/bin/firefox''' >"${pkgdir}/usr/share/libalpm/hooks/firefox-portable.hook"
        echo '''[Action]
When = PostTransaction
Exec = /usr/bin/rm "-f" "/usr/share/applications/firefox.desktop"
Depends = firefox
Description = Configuring Firefox for Portable

[Trigger]
Operation = Install
Operation = Upgrade
Type = Path
Target = usr/bin/firefox-portable
Target = usr/bin/firefox''' >"${pkgdir}/usr/share/libalpm/hooks/firefox-portable-desktop.hook"
}
