# Maintainer: Cirk2 <privat+aur at cirk2 dot de> 

pkgbase=sdbus-cpp
pkgname=(${pkgbase} ${pkgbase}-doc)
pkgver=1.2.0
pkgrel=2
pkgdesc="sdbus-c++ is a high-level C++ D-Bus library for Linux designed to provide expressive, easy-to-use API in modern C++"
url="https://github.com/Kistler-Group/sdbus-cpp"
arch=('i686' 'x86_64')
license=('LGPL2.1' 'custom:sdbus-c++ LGPL Exception 1.0')
depends=('systemd-libs' 'expat')
makedepends=('git' 'cmake' 'doxygen' 'systemd')
conflicts=('sdbus-cpp-git')
source=("${pkgbase}::git+https://github.com/Kistler-Group/sdbus-cpp.git#tag=v${pkgver}")
sha256sums=('SKIP')

build() {

    cmake -B build -S "$srcdir/${pkgbase}" \
        -DCMAKE_INSTALL_PREFIX=/ \
        -DCMAKE_BUILD_TYPE='Release' \
        -DBUILD_CODE_GEN=ON \
        -DBUILD_DOXYGEN_DOC=ON

    cmake --build build
    cmake --build build --target doc

    # Install so we can split the packaging up later
    DESTDIR="$srcdir/fakeinstall" cmake --install build

    # Remove references to $srcdir
    find "$srcdir/fakeinstall/usr/share/doc" -name \*.html -print -exec sed \
         -e "s|${srcdir}/sdbus-cpp/include|/usr/include|g" \
         -e "s|${srcdir}/sdbus-cpp||" \
         -i {} \;
}

package_sdbus-cpp() {
  local dir
  install -Dm644 "$srcdir/${pkgbase}/COPYING-LGPL-Exception" "$pkgdir/usr/share/licenses/$pkgbase/LICENSE"

  for dir in lib include bin ; do
    install -dm755 "$pkgdir/usr/$dir"
    cp  -dr --no-preserve=owner "$srcdir/fakeinstall/usr/$dir/"* "$pkgdir/usr/$dir"
  done
}

package_sdbus-cpp-doc() {
  local dir
  for dir in share/doc ; do
    install -dm755 "$pkgdir/usr/$dir"
    cp  -dr --no-preserve=owner "$srcdir/fakeinstall/usr/$dir/"* "$pkgdir/usr/$dir"
  done
}
