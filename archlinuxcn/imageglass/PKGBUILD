pkgname="imageglass"
_pkgver="10.0.0.314-beta-1"
pkgver=${_pkgver//-/_}
pkgrel=1
pkgdesc="lightweight, versatile image viewer"
url="https://imageglass.org"
license=('GPL-3.0-only')
arch=('x86_64')

depends=(
  'fontconfig'
  'glibc'
  'hicolor-icon-theme'
  'libgomp'
)
makedepends=(
  'dotnet-sdk'
  'git'
)

options=('!strip' '!debug')
_pkgsrc="$pkgname-$pkgver"
_pkgext="tar.gz"
source=(
  "${pkgname}"::"git+https://github.com/d2phap/ImageGlass.git#tag=$_pkgver"
  'imageglass.desktop'
)
sha256sums=('72c1473abea880eaa50de0435a0a9a1d0ac12ed6c14cbf6467ae6c1c62844926'
            'b31814a355395b002b8bd2dedc9107f5c288a56998df6e9894379900b6a7c560')
build() {
  cd "$srcdir/${pkgname}/v10/"
  dotnet publish ImageGlass.Linux/ImageGlass.Linux.csproj \
    -c Release \
    -r linux-x64 \
    -p:Platform=x64 \
    -p:PublishAot=true \
    -p:PublishSingleFile=true \
    -p:PublishTrimmed=true \
    -o ./artifacts/publish/linux-x64 \
    --self-contained true
}

package() {
  cd "$srcdir/${pkgname}/v10/artifacts/publish/linux-x64"
  for file in ImageGlass libHarfBuzzSharp.so libSkiaSharp.so Magick.Native-Q8-OpenMP-x64.dll.so; do
    install -Dm755 "$file" "$pkgdir/usr/lib/$pkgname/$file"
  done
  install -dm755 "$pkgdir/usr/bin"
  ln -s "/usr/lib/$pkgname/ImageGlass" "$pkgdir/usr/bin/$pkgname"
  # copy resources
  cp -r "$srcdir/${pkgname}/v10/assets/resources/"* "$pkgdir/usr/lib/$pkgname/"
  # install desktop file and icon
  install -Dm644 "$srcdir/$pkgname.desktop" "$pkgdir/usr/share/applications/$pkgname.desktop"
  install -Dm644 "$srcdir/${pkgname}/v10/assets/Logo.svg" "$pkgdir/usr/share/icons/hicolor/scalable/apps/$pkgname.svg"
  install -Dm644 "$srcdir/${pkgname}/v10/assets/Logo512.png" "$pkgdir/usr/share/icons/hicolor/512x512/apps/$pkgname/$pkgname.png"
}