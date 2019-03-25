# Maintainer: Horo a.k.a KenOokamiHoro <horo at yoitsu dot moe>
# Contributor: end222 <pabloorduna98 at gmail dot com>
# Cotributor: Jean Lucas <jean at 4ray dot co>
# Contributor: sekret, mail=$(echo c2VrcmV0QHBvc3Rlby5zZQo= | base64 -d)

pkgname=tor-browser-dev-zh-cn
pkgver=8.5a9
_language='zh-CN'
pkgrel=1
pkgdesc="(Simplified Chinese version) Tor Browser is +1 for privacy and -1 for mass surveillance"
arch=('i686' 'x86_64')
url="https://www.torproject.org/projects/torbrowser.html.en"
license=('GPL')
depends=('gtk2' 'mozilla-common' 'libxt' 'startup-notification' 'mime-types'
         'dbus-glib' 'alsa-lib' 'desktop-file-utils' 'hicolor-icon-theme'
         'libvpx' 'icu' 'libevent' 'nss' 'hunspell' 'sqlite')
optdepends=('zenity: simple dialog boxes'
            'kdebase-kdialog: KDE dialog boxes'
            'gst-plugins-good: h.264 video'
            'gst-libav: h.264 video'
            'libpulse: PulseAudio audio driver'
            'libnotify: GNOME dialog boxes')
source_i686=("https://dist.torproject.org/torbrowser/${pkgver}/tor-browser-linux32-${pkgver}_${_language}.tar.xz"{,.asc})
source_x86_64=("https://dist.torproject.org/torbrowser/${pkgver}/tor-browser-linux64-${pkgver}_${_language}.tar.xz"{,.asc})
source+=(${pkgname}.desktop
         ${pkgname}.png
         ${pkgname}.sh)
validpgpkeys=('EF6E286DDA85EA2A4BA7DE684E2C6E8793298290'
	            'A4300A6BC93C0877A4451486D1483FA6C3C07136')
noextract_i686=("tor-browser-linux32-${pkgver}_${_language}.tar.xz")
noextract_x86_64=("tor-browser-linux64-${pkgver}_${_language}.tar.xz")

package() {
  cd ${srcdir}

  sed -i \
    -e "s|REPL_NAME|${pkgname}|g" \
    -e "s|REPL_VERSION|${pkgver}|g" \
    -e "s|REPL_LANGUAGE|${_language}|g" \
    ${pkgname}.sh

  sed -i \
    -e "s|REPL_LANGUAGE|${_language}|g" \
    -e "s|REPL_COMMENT|${pkgdesc}|g" \
    -e "s|REPL_NAME|${pkgname}|g" \
    ${pkgname}.desktop

  install -Dm 0644 ${pkgname}.desktop \
    ${pkgdir}/usr/share/applications/${pkgname}.desktop
  install -Dm 0644 ${pkgname}.png \
    ${pkgdir}/usr/share/pixmaps/${pkgname}.png
  install -Dm 0755 ${pkgname}.sh ${pkgdir}/usr/bin/${pkgname}

  if [ "$CARCH" == "i686" ]; then
    install -Dm 0644 tor-browser-linux32-${pkgver}_${_language}.tar.xz \
      ${pkgdir}/opt/${pkgname}/tor-browser-linux32-${pkgver}_${_language}.tar.xz
  else
    install -Dm 0644 tor-browser-linux64-${pkgver}_${_language}.tar.xz \
      ${pkgdir}/opt/${pkgname}/tor-browser-linux64-${pkgver}_${_language}.tar.xz
  fi
}
sha256sums=('13d2e1fe85a9a08e9f66116f3c2d6f1e5d37e07d2ad8b08ae4f01890e864a722'
            '13267084e2b6dd1dbbb93f685d61da4cb48184a76a1c06a42ecc575855e24c57'
            'ce19dd89a8ecd9289136f97f0122b7301bdda9bcf0208f4277817e23ea9a95d8')
sha256sums_i686=('248c8cc376aca08e0aa4f6cc47a05939fd64466057ebcc391d81d8790f7ac362'
                 'SKIP')
sha256sums_x86_64=('5a79147b5a4a52d444e203a8c7dfcf0f6282d76490be3d2ccd4c334d95787c22'
                   'SKIP')
sha512sums=('5127d8ce8b5ad873b7ca7bbff5f4dfcee152f75f1bfbe0e9539c11fdbbc36357fcb1fdec621e379c705fe9f2b4a0303deb36e09bea309919c2c463da05aa17cf'
            'f37300061b8202ff60df035be8df4f1fe83f0b864062d59c1b49a0c1e3669d44dc4dd5d007c3f4620d5f57f8d8f9ca929c029be48b47a54fbab270a8ad554a7e'
            'b8e1a9e1f8ea12518a953854a98580acb1d144c5cf6351d977b4e92d7ffb2fa1b77e14f71b10ee761989ad1bd471147fe1c4ab4413d4fa072bc5b1e4f9a63742')
sha512sums_i686=('de1b9cde71b9d37fb69d1be83384f2a67fce00e84035a72ce5b3337508e44f8f029dd70be0cbce6a8d1508a7338a458b79ec6672378d946a1bbbf7c6adfe45e2'
                 'SKIP')
sha512sums_x86_64=('9155cf553197c27990729bbc1e74dbe638df543bee43263f75a5c1fc228f3978f493e769813301502e5a39ce0bd1e745a29673934a51104373db3cab1bba13ee'
                   'SKIP')
