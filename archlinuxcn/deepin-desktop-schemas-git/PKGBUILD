# Maintainer: DingYuan Zhang <justforlxz@gmail.com>

pkgname=deepin-desktop-schemas-git
pkgver=5.6.0.13.r2.g4ff5aba
pkgrel=1
pkgdesc='GSettings deepin desktop-wide schemas'
arch=('any')
url="https://github.com/linuxdeepin/deepin-desktop-schemas"
license=('GPL3')
depends=('dconf' 'deepin-gtk-theme' 'deepin-icon-theme' 'deepin-sound-theme')
makedepends=('git' 'python' 'go' 'golang-deepin-lib')
conflicts=('deepin-artwork-themes' 'deepin-desktop-schemas')
replaces=('deepin-artwork-themes' 'deepin-desktop-schemas')
provides=('deepin-desktop-schemas')
groups=('deepin-git')
source=('git://github.com/linuxdeepin/deepin-desktop-schemas'
        https://github.com/linuxdeepin/deepin-desktop-schemas/commit/bf0c4e43f6b6d508ddd346c2d1e865dae9ae947d.patch)
sha512sums=('SKIP'
            'be13e501baf0517da19618011219b53d633a4186840b20b24d134e5d667c4ab1b6b716c09c78faf802b32ecf3f6f6e5e2f84744a5919b28645f002739d07ea82')

pkgver() {
    cd deepin-desktop-schemas
    git describe --long --tags | sed 's/\([^-]*-g\)/r\1/;s/-/./g'
}

prepare() {
  export GOPATH="$srcdir/build:/usr/share/gocode"
  cd deepin-desktop-schemas
  # disable swap-sched
  patch -Rp1 -i ../bf0c4e43f6b6d508ddd346c2d1e865dae9ae947d.patch
  # fix default background url
  sed -i "s#^picture-uri.*#picture-uri='file:///usr/share/backgrounds/deepin/desktop.jpg'#" overrides/common/com.deepin.wrap.gnome.desktop.override
}

build() {
  export CGO_CPPFLAGS="${CPPFLAGS}"
  export CGO_CFLAGS="${CFLAGS}"
  export CGO_CXXFLAGS="${CXXFLAGS}"
  export CGO_LDFLAGS="${LDFLAGS}"
  export GOFLAGS="-buildmode=pie -trimpath -mod=readonly -modcacherw"

  cd deepin-desktop-schemas
  make ARCH=x86
}

check() {
  cd deepin-desktop-schemas
  make test
}

package() {
  cd deepin-desktop-schemas
  make DESTDIR="$pkgdir" install
}
