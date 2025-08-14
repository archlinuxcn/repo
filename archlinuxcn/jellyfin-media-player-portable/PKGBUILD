# Maintainer: Kimiblock Moe

pkgname=jellyfin-media-player-portable
pkgver=1.12.0
pkgrel=1
epoch=1
pkgdesc="Jellyfin Desktop. Sandboxed to prevent dGPU wakeup."
arch=('x86_64')
url="https://github.com/Kraftland/portable"
license=('GPL-3.0-or-later')
groups=()
provides=(jellyfin-media-player)
options=(!debug !strip)
#depends=("portable")
conflicts=("jellyfin-media-player")

optdepends=()

makedepends+=(jellyfin-media-player)

checkdepends=()

source=(
	portable-config
	jellyfin-media-player.sh
	jellyfin-media-player.desktop
)


md5sums=('886c7336ab017afd8d2d9a3acbbb18e8'
         'a0fd049fc174d7a0942a5488cdefc7a2'
         'd82778df35e3aca815ba3a75a2d267e1')

function prepare() {
	pacman -Ql jellyfin-media-player >file.list
}

function package() {
	depends=("portable" mpv  libcec  sdl2  p8-platform  protobuf  qt5-webengine  qt5-x11extras  qt5-quickcontrols)
	while IFS= read -r line; do
		file="$(echo "$line" | awk '{print $2}')"
		if [[ -d ${file} ]]; then
			echo "Omitting Directory"
		else
			install -Dm755 "${file}" "${pkgdir}/${file}"
		fi
	done < file.list
	rm -f "${pkgdir}/usr/share/applications"/*
	install -Dm755 \
		"${pkgdir}/usr/bin/jellyfinmediaplayer" \
		"${pkgdir}/usr/lib/portable/overlay-usr/jellyfinmediaplayer"
	rm -f "${pkgdir}/usr/bin"/*
	install -Dm644 portable-config \
		"${pkgdir}/usr/lib/portable/info/org.jellyfin.jellyfin-media-player/config"
	install -Dm755 "jellyfin-media-player.sh" \
		"${pkgdir}/usr/bin/jellyfin-media-player-portable"
	install -Dm644 "jellyfin-media-player.desktop" "${pkgdir}/usr/share/applications/org.jellyfin.jellyfin-media-player.desktop"
	echo '''[Desktop Entry]
Type=Application
Name=Jellyfin
GenericName=Stub for MPRIS
Icon=com.github.iwalton3.jellyfin-media-player
TryExec=portable
Exec=env _portableConfig="org.jellyfin.jellyfin-media-player" portable -- %u
Terminal=false
NoDisplay=true''' >"${pkgdir}/usr/share/applications/jellyfin.desktop"
}
