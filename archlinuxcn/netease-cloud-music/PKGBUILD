# Maintainer: kXuan <kxuanobj at gmail dot com>
# Contribuor: Peter Cai <peter at typeblog dot net>

pkgname=netease-cloud-music
pkgver=1.2.1
_pkgdate=20190428
pkgrel=6
pkgdesc="Netease Cloud Music, converted from .deb package"
arch=("x86_64")
url="https://music.163.com/"
license=('custom')
depends=('gtk2' 'gtk3' 'vlc')
source=(
	"https://d1.music.126.net/dmusic/netease-cloud-music_${pkgver}_amd64_ubuntu_${_pkgdate}.deb"
	"https://music.163.com/html/web2/service.html"
    "patch.c"
    "exclude.list"
    "netease-cloud-music.bash"
)
sha256sums=('1ee9f02842e6c2c8c79c48b2e932074f9c213a8eb4238e5e63f20438562fecbb'
            'cf307fee4be224223ed8cf5af5e8708960683564cd05c53108fa3c382c029a0e'
            'a92650cfd889b1d5c3192adc0785627721f1c60dbfe08a35f124f6f5cc9613dc'
            '0c470e76741c549e5530b2e57d57281eaf198fd56ca3590f664154365b744cf9'
            'b11bd6ab4abcc375850668f54a4912948875ad9f9b93cfc24f89de16ec1e8ea7')

DLAGENTS=("https::/usr/bin/curl -A 'Mozilla' -fLC - --retry 3 --retry-delay 3 -o %o %u")

build() {
  cd ${srcdir}
  cc -O2 -fPIC -shared -I /usr/include/vlc/plugins/ -o libnetease-patch.so patch.c
}

package() {
  cd ${srcdir}
  tar -xf data.tar.xz -C ${pkgdir} --exclude-from=exclude.list
  install -D -m644 service.html ${pkgdir}/usr/share/licenses/$pkgname/license.html
  install -D -m755 libnetease-patch.so ${pkgdir}/opt/netease/netease-cloud-music/libnetease-patch.so
  install -D -m755 netease-cloud-music.bash ${pkgdir}/opt/netease/netease-cloud-music/netease-cloud-music.bash
}
