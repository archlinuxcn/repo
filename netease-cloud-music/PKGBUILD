# Maintainer: Justin Wong <justin.w.xd at gmail dot com>
pkgname=netease-cloud-music
pkgver=0.9.0
pkgrel=2
pkgdesc="Netease Cloud Music, converted from .deb package"
arch=("x86_64")
url="http://music.163.com/"
license=('EULA')
depends=("alsa-lib" "atk" "glibc" "cairo" "libcups" "libdbus" "expat" "fontconfig"
	"freetype2" "gcc-libs" "gdk-pixbuf2" "glib2" "gtk2" "nspr" "nss" "pango"
	"qt5-base" "qt5-multimedia" "qt5-x11extras" "sqlite" "taglib" "libx11" "libxcursor"
	"libxext" "libxfixes" "libxi" "libxrandr" "libxrender" "libxss" "libxtst" "zlib"
	"gstreamer0.10-ugly-plugins"
)
source=(
	"http://s1.music.126.net/download/pc/${pkgname}_${pkgver}-${pkgrel}_amd64.deb"
	"http://security.ubuntu.com/ubuntu/pool/main/o/openssl/libssl1.0.0_1.0.2g-1ubuntu4.1_amd64.deb"
	"http://nl.archive.ubuntu.com/ubuntu/pool/universe/libc/libcue/libcue1_1.4.0-1_amd64.deb"
	"netease-cloud-music"
)
noextract=(
	"libssl1.0.0_1.0.2g-1ubuntu4.1_amd64.deb"
	"libcue1_1.4.0-1_amd64.deb"
)
md5sums=('24c44fe5e71e69cd7ac252c2ce611270'
         '0542b3182cef57f91f0c1dd3e03e6995'
         '51920df6edb60d9ef5e4e9f3ae3be0d6'
         '849fa0561f7713aa062c1fc4cbc269e3')

prepare() {
	tar -xvf data.tar.xz
	(mkdir -p libcue && cd libcue && ar xf ../libcue1_1.4.0-1_amd64.deb && tar xf data.tar.gz)
	(mkdir -p libssl && cd libssl && ar xf ../libssl1.0.0_1.0.2g-1ubuntu4.1_amd64.deb && tar xf data.tar.xz)
}

package() {
  cd ${srcdir}
  cp -aR usr ${pkgdir}
  install -m755 libcue/usr/lib/libcue.so.1.0.4 ${pkgdir}/usr/lib/netease-cloud-music/libcue.so.1
  install -m755 libssl/lib/x86_64-linux-gnu/libcrypto.so.1.0.0 ${pkgdir}/usr/lib/netease-cloud-music/libcrypto.so.1.0.0
  install -m755 libssl/lib/x86_64-linux-gnu/libssl.so.1.0.0 ${pkgdir}/usr/lib/netease-cloud-music/libssl.so.1.0.0
  install -m755 netease-cloud-music ${pkgdir}/usr/bin/netease-cloud-music
  # cp -aR usr ${pkgdir}
}
