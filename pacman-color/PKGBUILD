# Contributor: JokerBoy <jokerboy at punctweb dot ro>
# Contributor: vogo <vogo(at)seznam(dot)cz>

pkgname=pacman-color
pkgver=4.0.3
pkgrel=5
pkgdesc="A color patched command-line frontend for libalpm (Pacman)"
arch=('i686' 'x86_64' 'armv6h')
url="http://www.archlinux.org/pacman/"
license=('GPL')
depends=('pacman>=4.0' 'pacman<4.1')
backup=('etc/pacman.d/color.conf')
source=("ftp://ftp.archlinux.org/other/pacman/pacman-${pkgver}.tar.gz"
        '0001-Add-conflict-for-replacing-owned-empty-directory.patch'
        '0002-Check-empty-subdirectory-ownership.patch'
        '0003-Ensure-pre_upgrade-scriptlet-gets-old-package-version.patch'
        "${pkgname}-${pkgver}.patch"
        'color.conf')
md5sums=('387965c7125e60e5f0b9ff3b427fe0f9'
         '1a9b79788640907a2b34e8671cacc94a'
         'a9ddd43891bed364e1e97d27b2887bf1'
         '2e8cbf55a94b1954b167c5dee6b62317'
         '185e6a488b1aa14db4a54b71eb5e5e29'
         '47665f5054196c20ba0dd280a8d4c5e1')

build() {
  cd "pacman-${pkgver}"
  patch -p1 -i "${srcdir}/0001-Add-conflict-for-replacing-owned-empty-directory.patch"
  patch -p1 -i "${srcdir}/0002-Check-empty-subdirectory-ownership.patch"
  patch -p1 -i "$srcdir/0003-Ensure-pre_upgrade-scriptlet-gets-old-package-version.patch"
  patch -p1 -i "${srcdir}/${pkgname}-${pkgver}.patch"

  ./configure \
      --prefix=/usr \
      --sysconfdir=/etc \
      --localstatedir=/var \
      --disable-doc
  make
}

package() {
  # install pacman-color && color.conf
  install -Dm755 "pacman-${pkgver}/src/pacman/.libs/pacman" "${pkgdir}/usr/bin/pacman-color"
  install -Dm644 'color.conf' "${pkgdir}/etc/pacman.d/color.conf"
}
