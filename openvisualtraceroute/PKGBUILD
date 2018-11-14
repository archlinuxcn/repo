# Maintainer: Jake <aur@ja-ke.tech>

pkgname=openvisualtraceroute
_short_pkgname=ovtr
pkgver=1.7.1
pkgrel=1
pkgdesc="Open source cross-platform Java Visual Traceroute"
arch=('i686' 'x86_64')
license=('LGPLv3')
url="http://sourceforge.net/projects/openvisualtrace"
depends=('java-runtime' 'traceroute')
source=("http://downloads.sourceforge.net/project/openvisualtrace/${pkgver}/OpenVisualTraceRoute${pkgver}.zip"
        "ovtr"
        "ovtr.desktop")
sha256sums=('196054d50a15975dca18dca51308bbb2ccdc454d153cd6137612fad67d541617'
            '8eb4f3ad755ce5c0ec8a85331cd291da71d70d5325cf2ad5133aca9e736c8e1d'
            'af0cef38105d65182c261067577f8ff68bf50e71d4d2f4fc7fe8e0ba4472d22f')

if [ "$CARCH" = "i686" ]; then
  _arch="x86"
elif [ "$CARCH" = "x86_64" ]; then
  _arch="x64"
fi

package() {
  cd "${srcdir}/OpenVisualTraceRoute${pkgver}"

  install -d -m755 "${pkgdir}/usr/bin"
  install -d -m755 "${pkgdir}/usr/share/OpenVisualTraceRoute"
  install -d -m755 "${pkgdir}/usr/share/OpenVisualTraceRoute/"{lib,native/linux/${_arch},resources}

  cp -rPf "resources/"* "${pkgdir}/usr/share/OpenVisualTraceRoute/resources"
  cp -rPf "native/linux/${_arch}/"*.so "${pkgdir}/usr/share/OpenVisualTraceRoute/native/linux/${_arch}"
  cp -rPf "lib/"*.jar "${pkgdir}/usr/share/OpenVisualTraceRoute/lib"

  install -m755 "${srcdir}/${_short_pkgname}" "${pkgdir}/usr/bin/${_short_pkgname}"
  install -m755 "ovtr_run_as_root.sh" "${pkgdir}/usr/share/OpenVisualTraceRoute/"
  install -m755 "org.leo.traceroute.jar" "${pkgdir}/usr/share/OpenVisualTraceRoute/"
  
  install -d -m755 "${pkgdir}/usr/lib"
  ln -s /usr/lib/libpcap.so.1 ${pkgdir}/usr/lib/libpcap.so.0.8
  
  install -D -m644 "${srcdir}/${_short_pkgname}.desktop" "${pkgdir}/usr/share/applications/${_short_pkgname}.desktop"
  install -D -m644 "resources/icon.png" "$pkgdir/usr/share/pixmaps/${_short_pkgname}.png"
}

# vim:set ts=2 sw=2 et:
