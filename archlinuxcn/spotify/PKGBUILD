# Maintainer: Ashley Whetter <(firstname) @ awhetter.co.uk>
# Co-Maintainer: NicoHood <archlinux {cat} nicohood {dog} de>
# PGP ID: 97312D5EB9D7AE7D0BD4307351DAE9B7C1AE9161
# Contributor: Eothred <yngve.levinsen@gmail.com>

pkgname=spotify
pkgver=1.1.10.546
epoch=1
_commit=ge08ef575
_ver_x86_64=19
#_ver_i686=10
pkgrel=4
pkgdesc='A proprietary music streaming service'
arch=('x86_64')
license=('custom')
url='https://www.spotify.com'
depends=('alsa-lib>=1.0.14' 'gtk2' 'libsystemd' 'libxss' 'desktop-file-utils' 'openssl' 'nss' 'at-spi2-atk')
depends_x86_64=('libcurl-gnutls')
depends_i686=('libcurl-compat')
optdepends=('ffmpeg-compat-57: Adds support for playback of local files'
            'zenity: Adds support for importing local files'
            'libnotify: Desktop notifications')
options=('!strip')

# http://repository.spotify.com/dists/stable/Release
# http://repository.spotify.com/dists/stable/non-free/binary-amd64/Packages
# http://repository.spotify.com/dists/stable/non-free/binary-i386/Packages
# http://repository.spotify.com/dists/stable/Release.gpg
source=('spotify.protocol'
        'LICENSE'
        "${pkgname}-${pkgver}-Release::http://repository.spotify.com/dists/stable/Release"
        "${pkgname}-${pkgver}-Release.sig::http://repository.spotify.com/dists/stable/Release.gpg")
source_x86_64=("${pkgname}-${pkgver}-x86_64.deb::http://repository.spotify.com/pool/non-free/s/spotify-client/spotify-client_${pkgver}.${_commit}-${_ver_x86_64}_amd64.deb"
               "${pkgname}-${pkgver}-x86_64-Packages::http://repository.spotify.com/dists/stable/non-free/binary-amd64/Packages")
# source_i686=("${pkgname}-${pkgver}-i686.deb::http://repository.spotify.com/pool/non-free/s/spotify-client/spotify-client_${pkgver}.${_commit}-${_ver_i686}_i386.deb"
#              "${pkgname}-${pkgver}-i686-Packages::http://repository.spotify.com/dists/stable/non-free/binary-i386/Packages")
sha512sums=('999abe46766a4101e27477f5c9f69394a4bb5c097e2e048ec2c6cb93dfa1743eb436bde3768af6ba1b90eaac78ea8589d82e621f9cbe7d9ab3f41acee6e8ca20'
            '2e16f7c7b09e9ecefaa11ab38eb7a792c62ae6f33d95ab1ff46d68995316324d8c5287b0d9ce142d1cf15158e61f594e930260abb8155467af8bc25779960615'
            'SKIP'
            'SKIP')
sha512sums_x86_64=('f004083eee00600a51e50d7dee03846293b5ccd6966786e91055564c7963917b9aaa917de41f299a0f5b7baecea5f466fb37722b8631743ff2ca15f43851f5f4'
                   '39074e57abb9a647b4b27cc09bf91dd80a16589c8503b17061c23277b7718e778834bb79c168c771b9615d9e247f1ce9c5c597a10db905874a5d5c79f1109856')
validpgpkeys=('931FF8E79F0876134EDDBDCCA87FF9DF48BF1C90'
              '2EBF997C15BDA244B6EBF5D84773BD5E130D1D45') # Spotify <tux@spotify.com>

# Spotify uses different names for the arch
if [ "${CARCH}" = "i686" ]; then
    _SPOTIFY_ARCH=i386
else
    _SPOTIFY_ARCH=amd64
fi

prepare() {
    # Validate hashes from the PGP signed "Release" file
    echo "$(grep non-free/binary-${_SPOTIFY_ARCH}/Packages ${pkgname}-${pkgver}-Release | tail -n 2 | head -n 1 | awk '{print $1}') ${pkgname}-${pkgver}-${CARCH}-Packages" \
        > "${pkgname}-${pkgver}-${CARCH}-Packages.sha256"
    sha256sum -c "${pkgname}-${pkgver}-${CARCH}-Packages.sha256"

    echo "$(grep SHA512 ${pkgname}-${pkgver}-${CARCH}-Packages | head -n 1 | awk '{print $2}') ${pkgname}-${pkgver}-${CARCH}.deb" \
        > "${pkgname}-${pkgver}-${CARCH}.deb.sha512"
    sha512sum -c "${pkgname}-${pkgver}-${CARCH}.deb.sha512"
}

package() {
    cd "${srcdir}"

    tar -xzf data.tar.gz -C "${pkgdir}"

    install -Dm644 "${pkgdir}"/usr/share/spotify/spotify.desktop "${pkgdir}"/usr/share/applications/spotify.desktop
    install -Dm644 "${pkgdir}"/usr/share/spotify/icons/spotify-linux-512.png "${pkgdir}"/usr/share/pixmaps/spotify-client.png

    for size in 22 24 32 48 64 128 256 512; do
        install -Dm644 "${pkgdir}/usr/share/spotify/icons/spotify-linux-$size.png" \
            "${pkgdir}/usr/share/icons/hicolor/${size}x${size}/apps/spotify.png"
    done

    # Move spotify binary to its proper location
    mkdir -p "${pkgdir}"/opt/spotify
    mv "${pkgdir}/usr/share/spotify" "${pkgdir}/opt/"

    # Symlink spotify binary which is located in /opt
    ln -sf /opt/spotify/spotify "${pkgdir}/usr/bin/spotify"

    # Copy protocol file for KDE
    install -Dm644 "${srcdir}/spotify.protocol" "${pkgdir}/usr/share/kservices5/spotify.protocol"

    # Install license
    # https://www.spotify.com/legal/end-user-agreement
    install -Dm 644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"

    # Fix permissions
    chmod -R go-w "${pkgdir}"
}
