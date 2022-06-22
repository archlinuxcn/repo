# Maintainer: Xuanrui Qi <me@xuanruiqi.com>
# Contributor: Jean Lucas <jean@4ray.co>
# Contributor: José Luis Lafuente <jl@lafuente.me>
# Contributor: Michael Louis Thaler <michael.louis.thaler@gmail.com>

pkgname=watchman
pkgver=4.9.0
pkgrel=6
pkgdesc="An inotify-based file watching and job triggering command line utility"
url="https://facebook.github.io/watchman/"
arch=('i686' 'x86_64')
license=('Apache')
depends=('pcre' 'systemd' 'python')
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/facebook/watchman/archive/v${pkgver}.tar.gz"
        "${pkgname}.tmpfiles" "python3.patch" "autogen.patch")
sha256sums=('1f6402dc70b1d056fffc3748f2fdcecff730d8843bb6936de395b3443ce05322'
            '2b061865e10578a0477b9c7991a00594bc839c846b98896e93c75743dbf6a379'
            '8aa32e37aef329e0873425d25e370d25b7aa0731f104a645737f1111f64a5a9e'
            '1a86a52a434c034b4478af88f2789a1791e826f9ca4f1e8b1c421923b2dc2447')

prepare() {
  cd ${pkgname}-${pkgver}
  patch -Np1 -i "${srcdir}"/autogen.patch
  autoupdate
  ./autogen.sh

  patch -Np1 -i "${srcdir}"/python3.patch
}

build() {
  cd ${pkgname}-${pkgver}
  ./configure --prefix=/usr --disable-statedir --enable-lenient
  make
}

check() {
  cd ${pkgname}-${pkgver}
  # TODO: fix segfault in test
  #make check
}

package() {
  cd ${pkgname}-${pkgver}
  # Docs available online only; see https://github.com/facebook/watchman/issues/30
  make DESTDIR="${pkgdir}" install

  install -Dm 644 "${srcdir}"/${pkgname}.tmpfiles "${pkgdir}"/usr/lib/tmpfiles.d/${pkgname}.conf
}

# vim:set ts=2 sw=2 et:
