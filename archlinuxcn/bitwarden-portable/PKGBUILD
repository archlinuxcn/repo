# Maintainer: Kimiblock Moe
pkgname=bitwarden-portable
pkgver=2025.8.0
pkgrel=1
pkgdesc="Zen Browser sandboxed by portable"
arch=('any')
url="https://github.com/Kraftland/portable"
license=(GPL-3.0-or-later)
groups=()
options=(!debug !strip)

makedepends+=(git)

depends=(
	"portable"
	"electron"
)

optdepends=()

provides=(bitwarden)
conflicts=(bitwarden)

makedepends+=(
	"bitwarden"
)

checkdepends=()

source=(
	portable-config
	start.sh
	desktop.file
	)

function prepare() {
	pacman -Ql bitwarden >file.list
}

function package() {
	while IFS= read -r line; do
		file="$(echo "$line" | awk '{print $2}')"
		if [[ -d ${file} ]]; then
			echo "Omitting Directory"
		else
			install -Dm755 "${file}" "${pkgdir}/${file}"
		fi
	done < file.list
	install -Dm755 \
		portable-config \
		"${pkgdir}/usr/lib/portable/info/com.bitwarden.desktop/config"
	rm "${pkgdir}/usr/share/applications"/*
	rm "${pkgdir}/usr/bin"/*
	install -Dm755 \
		"${srcdir}/start.sh" \
		"${pkgdir}/usr/bin/bitwarden"
	install -Dm644 \
		"${srcdir}/desktop.file" \
		"${pkgdir}/usr/share/applications/com.bitwarden.desktop.desktop"
}
sha256sums=('c2a4000cd5384646e757735e31fbbe3ef6b222939a414119879f5ad0e79b5dd1'
            'ea40d1cfc92687162bd430c1daa030e6deefd8a45ccfb5ccc7ce2ccd014f7654'
            'e0804985439a2798667326c15d176c79a9c186bda5a4843636a3a61a90a8c366')
