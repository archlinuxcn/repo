# Maintainer : Christian Rebischke <Chris.Rebischke@archlinux.org>
# Contributor:dront78 <dront78@gmail.com>
pkgname=systemtap
pkgver=3.2
pkgrel=4
pkgdesc="provides infrastructure to simplify the gathering of information about the running system."
url="http://sourceware.org/systemtap/"
arch=('x86_64' 'i686')
license=('GPL')
depends=('elfutils' 'nss' 'python2')
makedepends=('python2-setuptools' 'xmlto')
optdepends=('sqlite3: for storing results in a database')
source=("${pkgname}-${pkgver}.tar.gz::https://sourceware.org/systemtap/ftp/releases/${pkgname}-${pkgver}.tar.gz"
        "${pkgname}-${pkgver}.tar.gz.asc::https://sourceware.org/systemtap/ftp/releases/${pkgname}-${pkgver}.tar.gz.asc"
        'stp_remove_install_hooks.patch'
        'fixes-for-gcc-8.patch'
        'fix-timers-for-4.15-kernel.patch'
        )
sha512sums=('6036ed1b5189fd3fcfdeeaa526a3539ac632d0b687a063b5e3424e8f613bfc2c8d079742b0262b547128e97e30e4beb61898b23761657aee519e61346ac92e94'
            'SKIP'
            '1d2758e9f875e06d08d37679587454fb43e025aa83ceeb405b1bc8d3277476502f2d67cf9e8383cc4c63ae545d7d0e9ebaab814f880b2f53bba47bef4afcd537'
            '970d83ace43909e5a1bfc4112d78dd913af6d59e4b8dc8c4461370b022092b0cdb6830427b52bcf5b7409ff6d7c79dab778e53398ba65de71bd4a270c66a2d3a'
            '3cbf261cf34df23454e0a9aa4566664241b8bcf4b44a28617cce483d0f24632b9fcd4ac8b37f488e736d0ce02308fb67e7b4dd52f6349a9010e2390d8c94190d'
            )
install='systemtap.install'
validpgpkeys=('5D38116FA4D3A7CC77E378D37E83610126DCC2E8')

prepare() {
  cd "${pkgname}-${pkgver}"
  patch -Np1 -i "${srcdir}/stp_remove_install_hooks.patch"
  patch -Np1 -i "${srcdir}/fixes-for-gcc-8.patch"
  patch -Np1 -i "${srcdir}/fix-timers-for-4.15-kernel.patch"
  autoreconf -i
}
build() {
  cd "${pkgname}-${pkgver}"
  ./configure \
    --prefix=/usr \
    --sysconfdir=/etc \
    --libexecdir=/usr/lib/"${pkgname}" \
    --libdir=/usr/lib/"${pkgname}" \
    --mandir=/usr/share/man/ \
    --localstatedir=/var \
    --enable-pie \
    --disable-docs \
    --enable-htmldocs
  make
}

package() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  make DESTDIR="${pkgdir}" install
  rmdir "${pkgdir}/var/run/stap-server/"
  rmdir "${pkgdir}/var/run/"
}

