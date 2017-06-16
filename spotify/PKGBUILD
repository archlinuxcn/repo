# Maintainer: Ashley Whetter <(firstname) @ awhetter.co.uk>
# Contributor: Eothred <yngve.levinsen@gmail.com>

pkgname=spotify
pkgver=1.0.55.487
_anotherpkgver=.g256699aa
_amd64_pkgrel=16
_i386_pkgrel=16
pkgrel=2
pkgdesc="A proprietary music streaming service"
arch=('x86_64' 'i686')
license=('custom:"Copyright (c) 2006-2010 Spotify Ltd"')
url="http://www.spotify.com"
options=('!strip' '!upx')

source=('spotify'
'spotify.protocol'
'LICENSE')
sha256sums=('989920e9360cadc1a8103b8c04acf0c87cb7911eb9a09dddb0cf4708d6249d34'
            'af54f3b90cac46fa100b3f919a9225d10d847617d24aa9af3d832e7689f482c3'
            '4e8bea31ca27e16cac9c9dcd8f6ec27e1f82b45de86d6fee7a1e77e23f884b92')
sha256sums_x86_64=('20073ba6fdf7d960361d4cb2afa6453e7a2108bd84df8f9cdf2cdf7225a83027')
sha256sums_i686=('183f87b930b75d85ecb34cef2b26b0355a3a18ffa38e0e0a476bfb190972b74d')

source_x86_64=("http://repository.spotify.com/pool/non-free/s/spotify-client/spotify-client_${pkgver}${_anotherpkgver}-${_amd64_pkgrel}_amd64.deb")

source_i686=("http://repository.spotify.com/pool/non-free/s/spotify-client/spotify-client_${pkgver}${_anotherpkgver}-${_i386_pkgrel}_i386.deb")

depends=("alsa-lib>=1.0.14" "gconf" "gtk2" "glib2" "nss" "libsystemd" "libxtst" "libx11" "libxss" "openssl-1.0" "libcurl-compat" "desktop-file-utils" "rtmpdump")
optdepends=('ffmpeg0.10: Adds support for playback of local files'
'zenity: Adds support for importing local files'
)

package() {
	cd "${srcdir}"

	tar -xzf data.tar.gz -C "${pkgdir}"

	install -D "${pkgdir}"/usr/share/spotify/spotify.desktop "${pkgdir}"/usr/share/applications/spotify.desktop
	install -D "${pkgdir}"/usr/share/spotify/icons/spotify-linux-512.png "${pkgdir}"/usr/share/pixmaps/spotify-client.png

	for size in 22 24 32 48 64 128 256 512; do
		install -D "${pkgdir}/usr/share/spotify/icons/spotify-linux-$size.png" \
			"${pkgdir}/usr/share/icons/hicolor/${size}x${size}/apps/spotify.png"
	done

	chmod -R go-w "${pkgdir}"/usr

	# Bin Script
	rm "${pkgdir}"/usr/bin/spotify
	install -Dm755 "${srcdir}/spotify" "${pkgdir}/usr/bin/spotify"

	# Copy protocol file for KDE
	install -Dm644 "${srcdir}/spotify.protocol" "${pkgdir}/usr/share/kservices5/spotify.protocol"

	# License
	install -D -m644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
