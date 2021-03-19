# Maintainer: Ashley Whetter <(firstname) @ awhetter.co.uk>
# Co-Maintainer: NicoHood <archlinux {cat} nicohood {dog} de>
# PGP ID: 97312D5EB9D7AE7D0BD4307351DAE9B7C1AE9161
# Contributor: Eothred <yngve.levinsen@gmail.com>

pkgname=spotify
pkgver=1.1.55.494
epoch=1
_commit=gca75f788
pkgrel=1
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

# NOTE: We switched from stable to testing on 18th march, as the spotify
# stable repository is always outdated. Testing seems to be in sync with snap:
# https://snapcraft.io/spotify
# http://repository.spotify.com/dists/testing/Release
# http://repository.spotify.com/dists/testing/non-free/binary-amd64/Packages
# http://repository.spotify.com/dists/testing/Release.gpg
source=('spotify.protocol'
        'LICENSE'
        "${pkgname}-${pkgver}-Release::http://repository.spotify.com/dists/testing/Release"
        "${pkgname}-${pkgver}-Release.sig::http://repository.spotify.com/dists/testing/Release.gpg")
source_x86_64=("${pkgname}-${pkgver}-x86_64.deb::http://repository.spotify.com/pool/non-free/s/spotify-client/spotify-client_${pkgver}.${_commit}_amd64.deb"
               "${pkgname}-${pkgver}-x86_64-Packages::http://repository.spotify.com/dists/testing/non-free/binary-amd64/Packages")
sha512sums=('999abe46766a4101e27477f5c9f69394a4bb5c097e2e048ec2c6cb93dfa1743eb436bde3768af6ba1b90eaac78ea8589d82e621f9cbe7d9ab3f41acee6e8ca20'
            '2e16f7c7b09e9ecefaa11ab38eb7a792c62ae6f33d95ab1ff46d68995316324d8c5287b0d9ce142d1cf15158e61f594e930260abb8155467af8bc25779960615'
            'SKIP'
            'SKIP')
sha512sums_x86_64=('95938ac1170c8cccb9fde836659e84b82391513bbd55d228d496bb3562b0e5ea567b4956aeacf379e76e4569e4b6d5060a5f21db0ce76c0a6908b2f4323d7fd6'
                   'e202d266a57dc4ad5300aaa1336e920bb1cd56c1814542aaf2ff113265fb0bd565ad686502bed2b9a23a9229511055b9967f426c93da788e1a6c65ef89a98bb5')
validpgpkeys=('8FD3D9A8D3800305A9FFF259D1742AD60D811D58') # Spotify <tux@spotify.com>
# Old Keys:
# 931FF8E79F0876134EDDBDCCA87FF9DF48BF1C90
# 2EBF997C15BDA244B6EBF5D84773BD5E130D1D45

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
