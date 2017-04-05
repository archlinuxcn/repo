# Maintainer: Brian Bidulock <bidulock@openss7.org>
# Contributo: Jianhui Z <jianhui@outlook.com>
# Contributo: Tau Tsao <realturner at gmail.com>
# Contributor: Tomasz Zok <tomasz.zok [at] gmail.com>
# Contributor: techryda <techryda at silentdome dot com>
# Contributor: Mathias R. <pu154r@overlinux.org>

pkgname=xrdp
pkgver=0.9.2
pkgrel=1
pkgdesc="An open source remote desktop protocol (RDP) server"
url="https://github.com/neutrinolabs/xrdp"
arch=('i686' 'x86_64' 'armv6h')
license=('Apache')
makedepends=('nasm')
depends=('tigervnc' 'libxrandr' 'lame' 'opus' 'fuse')
backup=('etc/xrdp/sesman.ini' 'etc/xrdp/xrdp.ini')
install="${pkgname}.install"
source=("https://github.com/neutrinolabs/xrdp/releases/download/v${pkgver}/xrdp-${pkgver}.tar.gz"
	"arch-config.diff")
md5sums=('afe2f922d2912a19dab1f78c927c204b'
         '4ffed594dcc6ca76553893a807c1645d')

prepare() {
  cd "${pkgname}-${pkgver}"
  patch -Np2 -b -z .orig <../arch-config.diff
  ./bootstrap
}

build() {
  cd "${pkgname}-${pkgver}"
  ./configure --prefix=/usr \
              --sysconfdir=/etc \
              --localstatedir=/var \
              --sbindir=/usr/bin \
              --with-systemdsystemunitdir=/usr/lib/systemd/system \
              --enable-jpeg \
              --enable-tjpeg \
              --enable-fuse \
	      --enable-opus \
	      --enable-rfxcodec \
	      --enable-mp3lame \
	      --enable-pixman \
	      --enable-painter
  make V=0
}

package() {
  cd "${pkgname}-${pkgver}"
  make DESTDIR="$pkgdir" install
  rm -f "$pkgdir"/etc/xrdp/rsakeys.ini
  install -Dm644 COPYING "$pkgdir"/usr/share/licenses/$pkgname/COPYING
}
