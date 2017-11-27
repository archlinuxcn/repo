# Maintainer: David Birks <david@tellus.space>
# Contributor: Jean Lucas <jean at 4ray dot co>
# Contributor: Jonas Heinrich <onny at project-insanity dot org>

pkgname=tor-messenger-bin
pkgver=0.5.0b1
pkgrel=2
_language="en-US"
pkgdesc="Chat program that sends all traffic over Tor"
arch=("i686" "x86_64")
url="https://trac.torproject.org/projects/tor/wiki/doc/TorMessenger"
license=("MIT")
source_i686=("https://dist.torproject.org/tormessenger/${pkgver}/tor-messenger-linux32-${pkgver}_${_language}.tar.xz")
source_x86_64=("https://dist.torproject.org/tormessenger/${pkgver}/tor-messenger-linux64-${pkgver}_${_language}.tar.xz")
source+=(tor-messenger.desktop
         tor-messenger.png
         tor-messenger.sh)
sha256sums_i686=("f7c1a7b0d4f26193ca2635412c426846c801f2445890381c4c8d3f0e87c83345")
sha256sums_x86_64=("2fc64e0ebd80b307ede57733028b90f62d8d7c6b9e4bafbe80955cf235ad3fb1")
sha256sums+=("f0df8e7237c295d81a991ba72e59cbbc7e3ade6d49f5178ed4aa226f8b7d5da0"
             "967353473d53da791bfb16eaf55e9a95b1d059502e40b0aaae7a1ab297f7d259"
	     "dd817794af9633ef635e24f9994854728914c47814e3dcc1785649529cb87968")

package() {
    cd ${srcdir}

    sed -i \
        -e "s|REPL_VERSION|${pkgver}|g" \
        -e "s|REPL_LANGUAGE|${_language}|g" \
        tor-messenger.sh
    
    install -Dm 0644 tor-messenger.desktop  ${pkgdir}/usr/share/applications/tor-messenger.desktop
    install -Dm 0644 tor-messenger.png      ${pkgdir}/usr/share/pixmaps/tor-messenger.png
    install -Dm 0755 tor-messenger.sh       ${pkgdir}/usr/bin/tor-messenger

    if [ "$CARCH" == "i686" ]; then
      install -Dm 0644 tor-messenger-linux32-${pkgver}_${_language}.tar.xz ${pkgdir}/opt/tor-messenger/tor-messenger-linux32-${pkgver}_${_language}.tar.xz
    else
      install -Dm 0644 tor-messenger-linux64-${pkgver}_${_language}.tar.xz ${pkgdir}/opt/tor-messenger/tor-messenger-linux64-${pkgver}_${_language}.tar.xz
    fi
}
