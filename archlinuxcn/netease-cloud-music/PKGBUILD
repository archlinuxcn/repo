# Maintainer: Peter Cai <peter at typeblog dot net>
pkgname=netease-cloud-music
pkgver=1.2.1
_pkgdate=20190428
pkgrel=1
pkgdesc="Netease Cloud Music, converted from .deb package"
arch=("x86_64")
url="http://music.163.com/"
license=('custom')
depends=()
source=(
	"http://d1.music.126.net/dmusic/netease-cloud-music_${pkgver}_amd64_ubuntu_${_pkgdate}.deb"
	"http://music.163.com/html/web2/service.html"
)
md5sums=('1f47c7dc3d9ce46da8099e539ee8a74d'
         'SKIP')

package() {
  cd ${srcdir}
  tar -xvf data.tar.xz -C ${pkgdir}
  install -D -m644 service.html ${pkgdir}/usr/share/licenses/$pkgname/license.html
}
