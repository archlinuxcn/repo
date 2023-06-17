# Maintainer: kXuan <kxuanobj at gmail dot com>
# Contribuor: Peter Cai <peter at typeblog dot net>

pkgname=netease-cloud-music
pkgver=1.2.1
_pkgdate=20190428
pkgrel=8
pkgdesc="Netease Cloud Music, converted from .deb package"
arch=("x86_64")
url="https://music.163.com/"
license=('custom')
depends=('gtk2' 'gtk3' 'vlc')
makedepends=(gcc)
source=(
	"https://d1.music.126.net/dmusic/netease-cloud-music_${pkgver}_amd64_ubuntu_${_pkgdate}.deb"
	"https://music.163.com/html/web2/service.html"
    "patch.c"
    "exclude.list"
    "netease-cloud-music.bash"
)
sha256sums=('1ee9f02842e6c2c8c79c48b2e932074f9c213a8eb4238e5e63f20438562fecbb'
            'SKIP'
            '1080edde7cbd3716464598f80dd5c715737775bec9501740295a40c48236b109'
            '45ecec9b94872fac7ef5f07f31ab2d2fbf19412f43d865c6125be194d4ec0c86'
            '3b2c2e2251461d4ee0509ac00d1677d9fff3eaca24f90ef8678efba2c30ae95f')

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
