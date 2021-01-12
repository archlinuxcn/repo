# Maintainer: buckket <buckket@cock.li>
# Co-maintainer: leothrix <ty at tjll dot net>
# Contributor: FadeMind <fademind@gmail.com>
# Contributor: Richard Weber <old-box at outlook dot com>
# Contributor: Benjamin Hedrich <kiwisauce at pagenotfound dot de>
# Contributor: Thomas Jost <schnouki at schnouki dot net>
# Contributor: Tomas Strand <tomas at fik1 dot net>
# Contributor: Neil Shephard <nshephard at gmail dot com>

### NOTICE
### libspotify is EOL, sources are taken from https://mopidy.github.io/libspotify-archive/
### Checksums have not changed.
###
### SPOTIFY DEVS STATEMENT
###
### Please note that we have removed the LibSpotify binaries from our website in an effort to phase out the usage of this deprecated library.
### LibSpotify has been considered deprecated since 2015 and will be shut down in 2017, so we want to ensure that all developers’ efforts and
### attention are focused on newer and better APIs that we actively support and maintain. These APIs include the Web API, iOS and Android SDKs,
### and upcoming embedded libraries for Windows, Mac OS X and Linux. More information regarding upcoming libraries will be provided in the coming months.
###
###
### Source: https://is.gd/z6waBx
###
###

pkgname=libspotify
pkgver=12.1.51
pkgrel=8
pkgdesc="C API package allowing third-party developers to write applications that utilize the Spotify music streaming service"
arch=("i686" "x86_64" "armv6h" "armv7h")
url="https://mopidy.github.io/libspotify-archive/"
license=('custom')
depends=('glibc')

if [ "$CARCH" == "x86_64" ]; then SPOTIFY_ARCH="x86_64"; fi
if [ "$CARCH" == "i686" ]  ; then SPOTIFY_ARCH="i686"  ; fi
if [ "$CARCH" == "armv7h" ]; then SPOTIFY_ARCH="armv7" ; fi
if [ "$CARCH" == "armv6h" ]; then
    SPOTIFY_ARCH="armv6-bcm2708hardfp"
    pkgver=12.1.103
fi

source_x86_64=("https://mopidy.github.io/libspotify-archive/${pkgname}-${pkgver}-Linux-${SPOTIFY_ARCH}-release.tar.gz")
source_i686=("https://mopidy.github.io/libspotify-archive/${pkgname}-${pkgver}-Linux-${SPOTIFY_ARCH}-release.tar.gz")
source_armv6h=("https://mopidy.github.io/libspotify-archive/${pkgname}-${pkgver}-Linux-${SPOTIFY_ARCH}-release.tar.gz")
source_armv7h=("https://mopidy.github.io/libspotify-archive/${pkgname}-${pkgver}-Linux-${SPOTIFY_ARCH}-release.tar.gz")

md5sums_x86_64=('83efddcc195d6ff12b24c97c767a5e45')
sha256sums_x86_64=('43a14e0732ba6ae30078fac105d0e2998d04d5f5c396a4968386bc4e22491058')
md5sums_i686=('04735b890da0b1fc7f1f14e68a5293de')
sha256sums_i686=('941ab4ba10bcd6ec4e96127afd095a39e11bc955de0882734c97e4f588b155ae')
md5sums_armv6h=('bf9afc8c7b966841735734b248f9c7a7')
sha256sums_armv6h=('d658e6c1978fb46cf33376eb8367a51d024f4014f21beac1dd264532bcc54b24')
md5sums_armv7h=('eb7e98849b3bb6d364fa74034602afbf')
sha256sums_armv7h=('ad27b6c5aee5382b66b39bfea3b1752076b7abcc445979ce25c1ec9d7ff3aeda')

build() {
    cd "${srcdir}/${pkgname}-${pkgver}-Linux-${SPOTIFY_ARCH}-release"

    # Don't do stupid things from a Makefile
    msg2 "Patching Makefile..."
    sed -i 's/ldconfig//' Makefile
}

package() {
    cd "${srcdir}/${pkgname}-${pkgver}-Linux-${SPOTIFY_ARCH}-release"

    make prefix="$pkgdir/usr" install

    # Install documentation
    cp -R share "$pkgdir"/usr/share
    mkdir -p "$pkgdir"/usr/share/man
    mv "$pkgdir"/usr/share/man3 "$pkgdir"/usr/share/man/man3

    # Correct pkgconfig file
    sed -e s:PKG_PREFIX:/usr:g \
          < lib/pkgconfig/libspotify.pc \
          > "$pkgdir"/usr/lib/pkgconfig/libspotify.pc

    # Custom license
    install -Dm644 LICENSE licenses.xhtml "$pkgdir"/usr/share/doc/libspotify
    mkdir -p "$pkgdir"/usr/share/licenses/libspotify
    ln -s ../../doc/libspotify/LICENSE "$pkgdir"/usr/share/licenses/libspotify/LICENSE
}
