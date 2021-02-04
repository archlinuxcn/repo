# Maintainer: JGH <jghodd(at)gmail(dot)com>

_pkgbase=uvesafb
pkgname=uvesafb-dkms
pkgver=1.0.4
pkgrel=1
_v86d=v86d
_v86dver=0.1.10
pkgdesc="uvesafb dkms driver and v86d userspace helper for uvesafb that runs x86 code in an emulated environment"
arch=('i686' 'x86_64')
url="https://github.com/jghodd/uvesafb-dkms"
license=('GPL2')
depends=('glibc' 'dkms>=2.2.0.3+git151023-5')
makedepends=('git')
options=('!makeflags')
provides=("v86d")
replaces=("v86d")
#conflicts=("v86d")

source=("git://github.com/jghodd/uvesafb-dkms.git#tag=$pkgname-$pkgver"
        "git://github.com/mjanusz/v86d.git#tag=$_v86d-$_v86dver"
        v86d_install
        v86d_hook
        'dkms.conf'
        modprobe.uvesafb)

md5sums=(SKIP
         SKIP
         '66ab32602ab29cc5635eaac7f3e42283'
         '5f75b8bc4a7ddf595014591e5db263cb'
         '39fa4b6d261d4fb44d21f45dc8a5390c'
         '2d7cc8dc6a41916a13869212d0191147')

build() {
  cd "$_v86d"
  ./configure --with-x86emu
  # we only need /usr/include/video/uvesafb.h
  make KDIR=/usr
}

package() {
  # Copy dkms.conf
  install -Dm644 dkms.conf "${pkgdir}"/usr/src/${_pkgbase}-${pkgver}/dkms.conf

  # Set name and version
  sed -e "s/@_PKGBASE@/${_pkgbase}/" \
      -e "s/@PKGVER@/${pkgver}/" \
      -i "${pkgdir}"/usr/src/${_pkgbase}-${pkgver}/dkms.conf

  # Copy sources (including Makefile)
  cp -r ${pkgname}/src ${pkgname}/Makefile \
        "${pkgdir}"/usr/src/${_pkgbase}-${pkgver}/

  install -D -m644 "v86d_install" "$pkgdir/usr/lib/initcpio/install/v86d"
  install -D -m644 "v86d_hook" "$pkgdir/usr/lib/initcpio/hooks/v86d"
  install -D -m644 "modprobe.uvesafb" "$pkgdir/usr/lib/modprobe.d/uvesafb.conf"

  # Install v86d to pkgdir
  cd "${_v86d}"
  make DESTDIR="$pkgdir" install

  # usrmove
  cd "$pkgdir"
  mv sbin usr/bin
}
