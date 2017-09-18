# Contributor: Bug <bug2000@gmail.com>
# Maintainer: Bug <bug2000@gmail.com>
pkgname=xpra-winswitch
pkgver=2.1.2
pkgrel=1
pkgdesc="Modified version of xpra by Winswitch"
arch=('i686' 'x86_64')
url='http://xpra.org/'
license=('GPL2')
depends=('python2' 'pygtk' 'libxtst' 'python2-pillow' 'python2-lz4'
         'ffmpeg' 'libvpx' 'xf86-video-dummy' 'libxkbfile'
         'python2-numpy' 'rencode' 'python2-opengl'
         'python2-gtkglext' 'python-lz4' 'python-opengl')
optdepends=('x264: Codec' 'python2-dbus: dbus features'
            'python2-pycups: Printing support' 'python2-netifaces: mdns'
            'python2-cryptography: Cryptography'
            'python-cryptography: Cryptography')
conflicts=('parti-all')
provides=('parti-all')
makedepends=('python2-setuptools' 'cython2' 'uglify-js')
backup=('etc/xpra/xpra.conf' 'etc/xpra/xorg.conf'
#        'etc/xpra/cuda.conf' 'etc/xpra/nvenc.keys'
        'etc/xpra/conf.d/05_features.conf'
        'etc/xpra/conf.d/10_network.conf'
        'etc/xpra/conf.d/12_ssl.conf'
        'etc/xpra/conf.d/15_file_transfers.conf'
        'etc/xpra/conf.d/16_printing.conf'
        'etc/xpra/conf.d/20_sound.conf'
        'etc/xpra/conf.d/30_picture.conf'
        'etc/xpra/conf.d/35_webcam.conf'
        'etc/xpra/conf.d/40_client.conf'
        'etc/xpra/conf.d/42_client_keyboard.conf'
        'etc/xpra/conf.d/50_server_network.conf'
        'etc/xpra/conf.d/55_server_x11.conf'
        'etc/xpra/conf.d/60_server.conf'
        'etc/xpra/conf.d/65_proxy.conf'
        'etc/pam.d/xpra')
source=("https://xpra.org/src/xpra-$pkgver.tar.xz")
sha256sums=('16462cd3ee7e982eabdc411dad524db563f49395d5c1d5f0df479efa8c76ae28')

build() {
  cd ${srcdir}/xpra-$pkgver
  export pkgdir
  #python2 setup.py build
  CFLAGS="$CFLAGS -fno-strict-aliasing" python2 setup.py build --without-enc_x265
}

package() {
  cd ${srcdir}/xpra-$pkgver
  python2 setup.py install --root=${pkgdir} --without-enc_x265
  mkdir -p ${pkgdir}/usr/lib/sysusers.d
}
