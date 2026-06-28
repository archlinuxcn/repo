# Maintainer: Qi Meng <qi_meng0206@outlook.com>
pkgname=7zip-zstd
pkgver=26.02
pkgrel=1
_pkgver=1.5.7-R1
_srcname="7-Zip-zstd-${pkgver}-v${_pkgver}"
pkgdesc="File archiver for extremely high compression (With Zstandard support)"
arch=('x86_64' 'aarch64')
url="https://github.com/mcmilk/7-Zip-zstd"
license=('LGPL-2.1-or-later' 'BSD-3-Clause' 'LicenseRef-UnRAR')
depends=('glibc' 'gcc-libs' 'sh')
makedepends=('uasm')
provides=('p7zip' '7zip')
conflicts=('p7zip' '7zip')
replaces=('p7zip')
source=("${url}/archive/refs/tags/v${pkgver}-v${_pkgver}.tar.gz")
sha256sums=('bf226fe3ca98383bc085ff0215758625d488b02da229b4df0ac5962f05bc97b0')

prepare() {
  cd "$_srcname"
  sed -i 's/-Werror//g' CPP/7zip/7zip_gcc.mak
}

build() {
  cd "$_srcname"
  
  local _platform_flags=()
  case $CARCH in
    x86_64)  _platform_flags=(PLATFORM=x64 IS_X64=1 MY_ASM=uasm USE_ASM=1) ;;
    aarch64) _platform_flags=(PLATFORM=arm64 IS_ARM64=1 MY_ASM=uasm USE_ASM=1) ;;
  esac

  local _components=(
    Bundles/Alone
    Bundles/Alone7z
    Bundles/Format7zF
    Bundles/SFXCon
    UI/Console
  )

  for component in "${_components[@]}"; do
    msg2 "Building $component..."
    make -C "CPP/7zip/$component" -f ../../cmpl_gcc.mak \
      "${_platform_flags[@]}" \
      LFLAGS_STRIP= \
      CC="cc $CFLAGS $CPPFLAGS $LDFLAGS" \
      CXX="g++ $CXXFLAGS $CPPFLAGS $LDFLAGS"
  done
}

package() {
  cd "$_srcname"

  install -Dt "$pkgdir/usr/lib/7zip" \
    CPP/7zip/Bundles/Alone/b/g/7za \
    CPP/7zip/Bundles/Alone7z/b/g/7zr \
    CPP/7zip/Bundles/Format7zF/b/g/7z.so \
    CPP/7zip/UI/Console/b/g/7z
  
  install -Dm644 CPP/7zip/Bundles/SFXCon/b/g/7zCon "$pkgdir/usr/lib/7zip/7zCon.sfx"

  local _prog
  for _prog in 7za 7zr 7z; do
    printf '#!/bin/sh\nexec /usr/lib/7zip/%s "$@"\n' "$_prog" \
      | install -D /dev/stdin "$pkgdir/usr/bin/$_prog"
  done

  install -Dm644 -t "$pkgdir/usr/share/licenses/$pkgname" DOC/{,unRar}License.txt
  install -Dm644 -t "$pkgdir/usr/share/doc/$pkgname" DOC/{Methods,readme}.txt
}
