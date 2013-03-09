# Maintainer: jarda-wien <xstej70@gmail.com>
# Former maintainer: Jason Melton <jason.melton@gmail.com>
# Contributor: Atilla ÖNTAŞ <tarakbumba@gmail.com>

pkgname=dkms-nvidia
_pkgname=nvidia
pkgver=313.26
pkgrel=1
pkgdesc="NVIDIA dynamic kernel module (DKMS) drivers for kernel26."
arch=(i686 x86_64)
url="http://www.nvidia.com/"
license=(custom)
depends=("dkms" "nvidia-utils=${pkgver}")
#optdepends=("nvidia-utils=${pkgver}")
provides=("nvidia=${pkgver}")
conflicts=("nvidia")
install="${pkgname}.install"
options=(!strip)

if [ "$CARCH" = "i686" ]; then
	_arch='x86'
	_pkg="NVIDIA-Linux-${_arch}-${pkgver}"
  source=("ftp://download.nvidia.com/XFree86/Linux-${_arch}/${pkgver}/${_pkg}.run")
  md5sums=('3c2f5138d0fec58b27e26c5b37d845b8')
elif [ "$CARCH" = "x86_64" ]; then
	_arch='x86_64'
	_pkg="NVIDIA-Linux-${_arch}-${pkgver}-no-compat32"
  source=("ftp://download.nvidia.com/XFree86/Linux-${_arch}/${pkgver}/${_pkg}.run")
  md5sums=('2d35124fa5a4b009f170fe893b5d07e3')
fi

source[1]="dkms.conf"
md5sums[1]='8f8c618c1fff3b3b4dea38dfe17fa4de'

#source[2]='conftest_new.diff'
#md5sums[2]='b391ae9ad430caecd3c353e3edda5979'

build() {
	cd $srcdir
	sh ${_pkg}.run --extract-only
#	patch -p1 < conftest_new.diff
}

package() 
{
 	mkdir -p                                ${pkgdir}/usr/src/${_pkgname}-${pkgver}
 	cp -a       ${srcdir}/${_pkg}/kernel/*  ${pkgdir}/usr/src/${_pkgname}-${pkgver}
	cp          ${srcdir}/dkms.conf         ${pkgdir}/usr/src/${_pkgname}-${pkgver}

  install -d -m755 $pkgdir/etc/modprobe.d
  echo "blacklist nouveau" >> $pkgdir/etc/modprobe.d/nouveau_blacklist.conf
}
