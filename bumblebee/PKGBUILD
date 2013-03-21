pkgname=bumblebee
pkgver=3.1
pkgrel=2
pkgdesc="Bumblebee brings Optimus Support for Linux Through VirtualGL. You need to install proper drivers separately. Can be used with Nouveau or Nvidia"
arch=('i686' 'x86_64')
depends=('virtualgl' 'libbsd' 'glib2')
optdepends=('xf86-video-nouveau: Nouveau driver' 'nouveau-dri: 3D acceleration features fo Nouveau' 'mesa: 3D acceleration features fo Nouveau'  'bbswitch: switch on/off discrete card' 
'nvidia-utils-bumblebee: Nvidia utils not breaking LibGL' 'nvidia: Nvidia kernel driver')
if [ "$CARCH" = "x86_64" ]; then
     optdepends[${#optdepends[@]}]='lib32-virtualgl: run 32bit applications with optirun'
     optdepends[${#optdepends[@]}]='primus-git: alternative back-end for optirun'
fi
url="http://www.Bumblebee-Project.org"
license=("GPL3")
install='bumblebee.install'
provides=('bumblebee')
backup=('etc/bumblebee/bumblebee.conf' 
    'etc/bumblebee/xorg.conf.nouveau' 
    'etc/bumblebee/xorg.conf.nvidia')
source=("http://www.bumblebee-project.org/${pkgname}-${pkgver}.tar.gz"
    'bumblebeed.in')

build() {
    cd "${srcdir}/${pkgname}-${pkgver}"
    ./configure \
        CONF_DRIVER_MODULE_NVIDIA=nvidia \
        CONF_LDPATH_NVIDIA=/usr/lib/nvidia-bumblebee:/usr/lib32/nvidia-bumblebee \
        CONF_MODPATH_NVIDIA=/usr/lib/nvidia-bumblebee/xorg/,/usr/lib/xorg/modules \
        --prefix=/usr \
        --sysconfdir=/etc
    make
}

package() {
    cd "${srcdir}/${pkgname}-${pkgver}"
    make install DESTDIR="$pkgdir"
    # Install init script
    install -D -m755 "${srcdir}/bumblebeed.in" "${pkgdir}/etc/rc.d/bumblebeed"
    # Install systemd unit
    install -D -m644 "scripts/systemd/bumblebeed.service" "${pkgdir}/usr/lib/systemd/system/bumblebeed.service"    
    # Make bash_completion work
    mv -v "${pkgdir}/etc/bash_completion.d/bumblebee" "${pkgdir}/etc/bash_completion.d/optirun"
}
md5sums=('de515ef51b1e0714c2f1b2a95f83e77e'
         'dc29576a356d3129bbea5d4dd04ab743')
