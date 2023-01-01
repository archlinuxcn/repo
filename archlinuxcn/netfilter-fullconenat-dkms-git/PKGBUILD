# Maintainer: Edward Pacman <edward@edward-p.xyz>

pkgname=netfilter-fullconenat-dkms-git
pkgver=r88.74c5e6f
pkgrel=1
pkgdesc="A kernel module that turns MASQUERADE into full cone SNAT"
arch=('any')
url="https://github.com/llccd/netfilter-full-cone-nat"
license=('GPL2')
depends=('dkms')
makedepends=('git')
optdepends=('iptables-fullconenat: iptables with FULLCONENAT')
provides=('netfilter-fullconenat')
conflicts=('netfilter-fullconenat')
source=("netfilter-fullconenat-dkms.conf"
        "dkms.conf"
        "Kbuild"
        "${pkgname}::git+https://github.com/llccd/netfilter-full-cone-nat.git"
      )
sha256sums=('a17dfdf1fd046219daeacc60065e3a81c80c2eb2cfdf6d8068278c509577f571'
            'd6823506b2c9e99b282d29270b0001de946dfe48462056b80aa9b564d67f7642'
            '7ff12ad066a68c65f23fc7e01654ca459ce3458172e3dce30f42553fa44dd7c2'
            'SKIP')

prepare(){
  cd "$srcdir/${pkgname}"
}

pkgver() {
  cd "$srcdir/${pkgname}"
  ( set -o pipefail
    git describe --long 2>/dev/null | sed 's/\([^-]*-g\)/r\1/;s/-/./g' ||
    printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
  )
}

package() {
  # Install modules-load.conf
  install -Dm644 netfilter-fullconenat-dkms.conf "${pkgdir}/usr/lib/modules-load.d/netfilter-fullconenat-dkms.conf"
  # Install Kbuild
  install -Dm644 Kbuild "${pkgdir}/usr/src/${pkgname}-${pkgver}/Kbuild"
  # Install dkms.conf
  install -Dm644 dkms.conf "${pkgdir}/usr/src/${pkgname}-${pkgver}/dkms.conf"
  
  # Install sources (including Makefile)
  install -Dm644 ${pkgname}/xt_FULLCONENAT.c "${pkgdir}/usr/src/${pkgname}-${pkgver}/xt_FULLCONENAT.c"

  # Set name and version
  sed -e "s/@PKGNAME@/${pkgname}/" \
      -e "s/@PKGVER@/${pkgver}/" \
      -i "${pkgdir}"/usr/src/${pkgname}-${pkgver}/dkms.conf
}
