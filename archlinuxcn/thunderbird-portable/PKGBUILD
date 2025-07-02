# Maintainer: Kimiblock Moe

pkgname=thunderbird-portable
pkgver=139.0.2
pkgrel=1
epoch=1
pkgdesc="Thunderbird sandboxed by portable"
arch=('any')
url="https://github.com/Kraftland/portable"
license=('GPL-3.0-or-later')
groups=()
options=(!debug !strip)
depends=("thunderbird" "portable")

optdepends=()

makedepends+=()

checkdepends=()

source=(
	portable-config
	thunderbird.sh
	thunderbird.desktop
)


md5sums=('ea5929c2da88108fa43a4d7a7c566050'
         'ad98beaed27a3b529c9ceb5038a6e987'
         '8f09e1dba74deb4e4efab78d0b13d315')

function package() {
	install -Dm644 portable-config \
		"${pkgdir}/usr/lib/portable/info/org.mozilla.thunderbird/config"
	install -Dm755 "thunderbird.sh" \
		"${pkgdir}/usr/bin/thunderbird-portable"
	install -Dm644 "thunderbird.desktop" "${pkgdir}/usr/share/applications/org.mozilla.thunderbird.desktop"
	install -d "${pkgdir}/usr/share/libalpm/hooks"

	echo '''[Action]
When = PostTransaction
Exec = /usr/bin/ln "-sfr" "/usr/bin/thunderbird-portable" "/usr/bin/thunderbird"
Depends = thunderbird
Description = Configuring Thunderbird for Portable

[Trigger]
Operation = Install
Operation = Upgrade
Type = Path
Target = usr/bin/thunderbird-portable
Target = usr/bin/thunderbird''' >"${pkgdir}/usr/share/libalpm/hooks/thunderbird-portable.hook"
        echo '''[Action]
When = PostTransaction
Exec = /usr/bin/rm "-f" "/usr/share/applications/org.mozilla.Thunderbird.desktop"
Depends = thunderbird
Description = Configuring Thunderbird for Portable

[Trigger]
Operation = Install
Operation = Upgrade
Type = Path
Target = usr/bin/thunderbird-portable
Target = usr/bin/thunderbird''' >"${pkgdir}/usr/share/libalpm/hooks/thunderbird-portable-desktop.hook"
}

