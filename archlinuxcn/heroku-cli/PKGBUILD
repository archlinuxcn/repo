# Maintainer: Sampson Crowley <sampsonsprojects@gmail.com>
# Contributor: Rhys Kenwell <redrield+aur@gmail.com>
# Github Contributor: Michael Herold <https://github.com/michaelherold>

pkgname=heroku-cli
pkgver=7.42.13
pkgrel=4
_builddir=cli-$pkgver-$pkgrel
pkgdesc="a tool for creating and managing Heroku apps from the command line"
arch=('any')
url="https://devcenter.heroku.com/articles/heroku-cli"
license=('custom' 'ISC')
depends=('nodejs')
# makedepends=('npm')
optdepends=('git: Deploying to Heroku')
conflicts=('heroku-client-standalone' 'heroku-toolbelt' 'ruby-heroku')
source=("https://storage.googleapis.com/arch-package-files/heroku-cli-v$pkgver-$pkgrel.tar.xz")
sha256sums=('a81a43dd1dfcee006c5d6dd996a16c84365f6b45f1da77508862883bd672d98c')
sha512sums=('2d9390bee6826dc2f371098a43d5a014ec369ea12f5efa042d60150b19a82bc5a2b76a2914502d26acc277487424833e887702eb15bac56a94fda26a8f30fb20')
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
