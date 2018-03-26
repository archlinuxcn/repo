# Maintainer: TJM <tommy.mairo@gmail.com>
# Contributor: Yijian Chen <dastudiodirector@gmail.com>
# Contributor: Giovanni Scafora <giovanni@archlinux.org>
# Contributor: Henrik Ronellenfitsch <searinox@web.de>
# Contributor: Alessio Sergi <sergi.alessio {at} gmail.com>
# Contributor: Dario 'Dax' Vilardi <dax [at] deelab [dot] org>
# Contributor: Anatol Pomozov <anatol.pomozov@gmail.com>
pkgname=amule-dlp-git
pkgver=2.3.2.r10453.4f2254308
pkgrel=1
pkgdesc="An eMule-like client for ed2k p2p network with DLP patch"
arch=('i686' 'x86_64')
url="https://github.com/persmule/amule-dlp"
license=('GPL')
depends=('wxgtk' 'gd' 'geoip' 'libupnp' 'crypto++>=6.0.0' 'libsm' 'boost-libs')
conflicts=('amule' 'amule-dlp' 'amule-dlp-hg')
makedepends=('git' 'boost')
optdepends=('antileech')
install=amule.install
provides=('amule' 'amule-dlp')
source=("git+https://github.com/persmule/amule-dlp.git#commit=4f22543087008d29a58a579aff2aab1262b5a5fa"
        'amuled.systemd'
        'amuleweb.systemd'
		'crypto++.patch')
sha256sums=('SKIP'
            '6dbdd1ad1c3c3d8637b8f4cbd5416f39c8e4277a2f8498577b08bf6cda8dbca9'
            'f4f43b1154ddccc9036a4291a58c6715f097b171fec62ea7aead0c9d9fa654f2'
			'de425a5763a90d2b4302a22299a8d57e2a32bd83c6c427a012a42deaac9378a2')

pkgver() {
  cd "${srcdir}/amule-dlp"
  printf "2.3.2.r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

prepare(){
  cd "${srcdir}/amule-dlp"
  patch -p1 -i ../crypto++.patch 
  cp src/aMule.xpm amule.xpm
}

build() {
  cd "${srcdir}/amule-dlp"

  ./autogen.sh
  ./configure \
	  --prefix=/usr \
	  --mandir=/usr/share/man \
	  --disable-debug \
	  --enable-amule-daemon \
	  --enable-amulecmd \
	  --enable-amule-gui \
	  --enable-webserver \
	  --enable-cas \
	  --enable-wxcas \
	  --enable-alc \
	  --enable-alcc \
	  --enable-geoip \
	  --enable-upnp \
	  --with-denoise-level=3 \
	  --enable-nls \
	  --enable-optimize \
	  --enable-mmap \
	  --enable-ccache \
	  --with-boost \
	  --with-wxversion=3.0

  make 
}

package() {
  cd "${srcdir}/amule-dlp"

  make DESTDIR=${pkgdir} install

  install -D -m644 "${srcdir}/amuled.systemd" "${pkgdir}/usr/lib/systemd/system/amuled.service"
  install -D -m644 "${srcdir}/amuleweb.systemd" "${pkgdir}/usr/lib/systemd/system/amuleweb.service"
}
