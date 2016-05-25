# Maintainer: Justin Wong <justin.w.xd at gmail dot com>
pkgname=netease-cloud-music
pkgver=0.9.0_2
pkgrel=2
pkgdesc="Netease Cloud Music, converted from .deb package"
arch=("x86_64")
url="http://music.163.com/"
license=('EULA')
depends=("alsa-lib" "glibc" "libdbus"
	"gcc-libs" "gdk-pixbuf2" "glib2" "gtk2" "nss" 
	"qt5-base" "qt5-multimedia" "qt5-x11extras" "sqlite" "taglib"
	"libxss" "zlib" "gstreamer0.10-ugly-plugins"
	"gst-plugins-ugly" "gst-plugins-good"
)
source=(
	"http://s1.music.126.net/download/pc/${pkgname}_${pkgver/_/-}_amd64.deb"
	"http://security.ubuntu.com/ubuntu/pool/main/o/openssl/libssl1.0.0_1.0.2g-1ubuntu4.1_amd64.deb"
	"http://archive.ubuntu.com/ubuntu/pool/universe/libc/libcue/libcue1_1.4.0-1_amd64.deb"
	"https://music.163.com/html/web2/service.html"
	"netease-cloud-music"
)
noextract=(
	"libssl1.0.0_1.0.2g-1ubuntu4.1_amd64.deb"
	"libcue1_1.4.0-1_amd64.deb"
)
md5sums=('24c44fe5e71e69cd7ac252c2ce611270'
         '0542b3182cef57f91f0c1dd3e03e6995'
         '51920df6edb60d9ef5e4e9f3ae3be0d6'
		 'SKIP'
         '849fa0561f7713aa062c1fc4cbc269e3')

prepare() {
	tar -xvf data.tar.xz
	(mkdir -p libcue && cd libcue && ar xf ../libcue1_1.4.0-1_amd64.deb && tar xf data.tar.gz)
	(mkdir -p libssl && cd libssl && ar xf ../libssl1.0.0_1.0.2g-1ubuntu4.1_amd64.deb && tar xf data.tar.xz)
}

package() {
  cd ${srcdir}
  cp -aR usr ${pkgdir}
  mkdir -p ${pkgdir}/usr/share/licenses/netease-cloud-music/
  install -m644 service.html ${pkgdir}/usr/share/licenses/netease-cloud-music/license.html
  install -m755 libcue/usr/lib/libcue.so.1.0.4 ${pkgdir}/usr/lib/netease-cloud-music/libcue.so.1
  install -m755 libssl/lib/x86_64-linux-gnu/libcrypto.so.1.0.0 ${pkgdir}/usr/lib/netease-cloud-music/libcrypto.so.1.0.0
  install -m755 libssl/lib/x86_64-linux-gnu/libssl.so.1.0.0 ${pkgdir}/usr/lib/netease-cloud-music/libssl.so.1.0.0
  install -m755 netease-cloud-music ${pkgdir}/usr/bin/netease-cloud-music
}
