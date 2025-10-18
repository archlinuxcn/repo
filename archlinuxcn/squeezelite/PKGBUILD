# Maintainer: Fabio 'Lolix' Loli <fabio.loli@disroot.org> -> https://github.com/FabioLolix
# Contributor: Christian Hesse <mail@eworm.de
# Contributor: Mika Fischer <mika.fischer@zoopnet.de>

pkgname=squeezelite
pkgver=2.0.0.1524
pkgrel=1
pkgdesc="Lightweight headless squeezebox emulator"
arch=(x86_64 i686 armv7h aarch64)
url="https://github.com/ralph-irving/squeezelite"
license=(GPL-3.0-or-later)
depends=(glibc alsa-lib faad2 flac libmad libvorbis mpg123 libsoxr ffmpeg libavformat.so)
makedepends=(git)
install=${pkgname}.install
_commit=db51a7b16934f41b72437394bf8114c3a85e0a91 #micro 1524
source=("git+https://github.com/ralph-irving/squeezelite.git#commit=${_commit}"
        'squeezelite.service'
        'conffile')
sha256sums=('10a7a0a71048a85d3a3ce4da54852a72eded9fe7a69fdde9dcd3e296537cd439'
            '9bffedd1d119e6b8643007c8e3ca674266100fb091e4c1458893a42388d4e90e'
            'f0753a1cbd0194119226587ff9c12257438674d9b8e0179d22f0d5461ad3a70a')

pkgver() {
  cd "${srcdir}/squeezelite"

  _maj=$(cat squeezelite.h|grep "#define MAJOR_VERSION" | awk '{print $3}' | sed 's/\"//g;s/-/_/g')
  _min=$(cat squeezelite.h|grep "#define MINOR_VERSION" | awk '{print $3}' | sed 's/\"//g;s/-/_/g')
  _mic=$(cat squeezelite.h|grep "#define MICRO_VERSION" | awk '{print $3}' | sed 's/\"//g;s/-/_/g')

  printf "${_maj}.${_min}.${_mic}"
}

build() {
  cd "${srcdir}/squeezelite"
  export LDFLAGS="${LDFLAGS} -lasound -lpthread -lm -lrt"
  export OPTS="${OPTS} -DDSD -DRESAMPLE -DVISEXPORT -DFFMPEG -DLINKALL"
  make
}

package() {
  cd "${srcdir}/squeezelite"

  install -m0755 -D squeezelite "${pkgdir}/usr/bin/squeezelite"
  install -Dm644 ../conffile "${pkgdir}/etc/squeezelite.conf.default"
  install -Dm644 ../squeezelite.service -t "${pkgdir}/usr/lib/systemd/system/"
  install -Dm644 doc/squeezelite.1 -t "${pkgdir}/usr/share/man/man1/"
  install -Dm644 LICENSE.txt -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
