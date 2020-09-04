# Maintainer: Sampson Crowley <sampsonsprojects@gmail.com>
# Contributor: Rhys Kenwell <redrield+aur@gmail.com>
# Github Contributor: Michael Herold <https://github.com/michaelherold>

pkgname=heroku-cli
pkgver=7.42.13
_builddir=cli-${pkgver}
pkgrel=2
pkgdesc="a tool for creating and managing Heroku apps from the command line"
arch=('x86_64' 'armv7h')
url="https://devcenter.heroku.com/articles/heroku-cli"
license=('custom' 'ISC')
depends=('nodejs')
# makedepends=('npm')
optdepends=('git: Deploying to Heroku')
conflicts=('heroku-client-standalone' 'heroku-toolbelt' 'ruby-heroku')
# source=("https://cli-assets.heroku.com/heroku-v$pkgver/heroku-v$pkgver-linux-x86.tar.xz")
# source_armv7h=("https://cli-assets.heroku.com/heroku-v$pkgver/heroku-v$pkgver-linux-arm.tar.xz")
source_x86_64=("https://storage.googleapis.com/arch-package-files/heroku-v$pkgver-linux-x64.tar.xz")
source_armv7h=("https://storage.googleapis.com/arch-package-files/heroku-v$pkgver-linux-arm.tar.xz")
sha256sums_x86_64=('9313870e71d8a6737a6cf5d7f4c94a350128db97ec8648b90e8f2d53bda9e92b')
sha256sums_armv7h=('decfbc9e407cf3e965907cc134610b72e7a67972ba57f3bbe28178c84686f539')
sha512sums_x86_64=('bf2945f3faed1ae54bc51407782e3288d7024808acb4e0be0a7b55e0b61b99f4a4b8be7a66d9d97584d5994f23a39f7a6df8079ec71f8ee1dfd2feec8b7dab3c')
sha512sums_armv7h=('51cdcf09d04a8854eb6b9ee301a1e67d87d6e9b881c2f7672a7e7fe491beb63e8ac73b5736ebb81a457e8a5f9bc6c4a8f34711c53217df86037f5cb03b7f8058')
# noextract=("heroku-v$pkgver-linux-x64.tar.xz" "heroku-v$pkgver-linux-arm.tar.xz")
# noextract_armv7h=("heroku-v$pkgver-linux-x64.tar.xz" "heroku-v$pkgver-linux-arm.tar.xz")
options=('!strip')
provides=('heroku' 'heroku-cli')

prepare() {
  # remove packaged node binary and fall back to whatever node is on the PATH
  rm -f "$srcdir/heroku/bin/heroku"
  rm -f "$srcdir/heroku/bin/heroku.cmd"
  rm -f "$srcdir/heroku/bin/node"
}

package() {
  # https://cli-assets.heroku.com/linux-arm
  # https://cli-assets.heroku.com/linux-x64

  install -dm755 "$pkgdir/usr/lib/heroku"
  install -dm755 "$pkgdir/usr/bin"
  install -dm755 "$pkgdir/usr/share/licenses/$pkgname"

  herokulibdir="$pkgdir/usr/lib"
  for foundherokudir in $(find "$srcdir/heroku" -mindepth 1 -type d) ; do
    herokuinstalldir="${foundherokudir/$srcdir/$herokulibdir}"
    install -dm755 "$herokuinstalldir"
  done

  for foundherokufile in $(find "$srcdir/heroku" -mindepth 1 -type f) ; do
    herokuinstallperm=$(stat -c "%a" "$foundherokufile")
    herokuinstallfile="${foundherokufile/$srcdir/$herokulibdir}"
    install -Dm$herokuinstallperm "$foundherokufile" "$herokuinstallfile"
  done

  ln -sf "../../../lib/heroku/LICENSE" "$pkgdir/usr/share/licenses/$pkgname"
  ln -sf "../../lib/heroku/bin/run" "$pkgdir/usr/bin/heroku"
}
