# Maintainer: Kewl <xrjy@nygb.rh.bet(rot13)>
# Maintainer: Adam Nielsen <malvineous@shikadi.net>

pkgname='etc-update'
pkgdesc="CLI to interactively merge .pacnew in /etc"
pkgver=2.3.60
pkgrel=1
arch=('any')
url="https://wiki.gentoo.org/wiki/Handbook:X86/Portage/Tools#etc-update"
license=('GPL')
depends=('bash')
makedepends=('git')
backup=("etc/etc-update.conf")
source=("https://github.com/gentoo/portage/archive/portage-${pkgver}.tar.gz")
md5sums=('462a5d39b80df196dc0731ff95f851ee')

package() {
  install -Dm 0755 "portage-portage-${pkgver}/bin/${pkgname}" "${pkgdir}/usr/bin/${pkgname}"
  install -Dm 0644 "portage-portage-${pkgver}/cnf/${pkgname}.conf" "${pkgdir}/etc/${pkgname}.conf"
}
