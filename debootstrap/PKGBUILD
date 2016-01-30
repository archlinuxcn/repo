# Maintainer: Jan Dolinar <dolik.rce@gmail.com>
# Contributor: Abakus <java5 at arcor dot de>
# Contributor: Michael Lass <bevan@bi-co.net>
pkgname=debootstrap
pkgver=1.0.78
pkgrel=1
pkgdesc="A tool used to create a Debian base system from scratch, without requiring the availability of dpkg or apt"
arch=('any')
license=('GPL')
url="https://tracker.debian.org/pkg/debootstrap"
depends=('wget')
optdepends=( 'debian-archive-keyring: checking Debian release signatures'
             'ubuntu-keyring: checking Ubuntu release signatures'
             'gnupg1:  checking Debian and Ubuntu release signatures' )
backup=(usr/share/debootstrap/arch)
source=("http://ftp.debian.org/debian/pool/main/d/${pkgname}/${pkgname}_${pkgver}_all.deb")
md5sums=('c437ae4757f7a1b8b8d9576b1e0fb21d')

package(){
  tar -xzf "${srcdir}/data.tar.gz" -C "${pkgdir}/"

  # move the executables to /usr/bin
  mv "${pkgdir}/usr/sbin" "${pkgdir}/usr/bin"

  # patch the path to use Debian defaults (prevents error in chrooted environment)
  sed -i 's|export PATH|export PATH="/usr/local/bin:/usr/bin:/bin:/usr/local/sbin:/usr/sbin:/sbin:/opt/java/jre/bin:/usr/bin/vendor_perl:/usr/bin/core_perl"|' ${pkgdir}/usr/bin/debootstrap

  # doesn't work with gpg 2.x, patch to point to gpg1v
  sed 's/gpgv/gpg1v/g;' -i "${pkgdir}/usr/bin/debootstrap" "${pkgdir}/usr/share/debootstrap/functions"

  # write architecture configuration
  case "$CARCH" in
    "i686")    echo "i386" ;;
    "x86_64")  echo "amd64" ;;
    "armv7h")  echo "armhf" ;;
    *)         error "Unknown architecture '$CARCH'" && false
  esac > "${pkgdir}/usr/share/debootstrap/arch"
}
