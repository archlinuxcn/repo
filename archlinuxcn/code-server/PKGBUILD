# Maintainer: Colin Adler <colin@coder.com>
# Maintainer: Asher <ash@coder.com>
# Maintainer: cdrci <joe+cdrci@coder.com>
# Contributor: Joe Previte <joe@coder.com>
# Contributor: Teffen Ellis <teffen@coder.com>
# Contributor: Anmol <anmol@coder.com>

pkgname=code-server
pkgver=4.131.0
pkgrel=1
pkgdesc="VS Code in the browser"
arch=("x86_64" "aarch64")
url="https://github.com/coder/code-server"
license=(MIT)
depends=(glibc)
source=(
  "$pkgname-$pkgver-user.service::https://raw.githubusercontent.com/cdr/code-server/v$pkgver/ci/build/code-server-user.service"
  "$pkgname-$pkgver@.service::https://raw.githubusercontent.com/cdr/code-server/v$pkgver/ci/build/code-server@.service"
)
release_name="code-server-${pkgver}-linux"
source_x86_64=(
  "${url}/releases/download/v$pkgver/$release_name-amd64.tar.gz"
)
source_aarch64=(
  "${url}/releases/download/v$pkgver/$release_name-arm64.tar.gz"
)
sha512sums=('7040df09c7404a56dbbb32e09d04ead3b622773520feae19c6710656cef46ca5d79b1972bfebb931e309e495d041b9938cd6a51c39fc0f8f6133dfe711be9280'
            'ab8e679c05f6184f163dccf0651e8c1fac22a29ae583148f8c93b6930ece27cdff45a48b425e8b15b8c8ce749015680a3ae8225b7e8037979ff3d228f396f629')
sha512sums_x86_64=('4d7125e002b9e2d95a4960c5ed783e40066985e33302103e0f68283209106d84ffaaff6dd35471be98c03b50de67c34af02a835b274606fa298e5d9e54a07111')
sha512sums_aarch64=('118b213b864e527858437ef984bf309ae6de613e3fdcbddb9cff782f20f5b73a79c193da6116f9984ce091713217d71cd5fa3f95de269492d897d4ee1783e357')
package() {
  if [[ ${CARCH} == x86_64 ]]; then
    release_name+=-amd64
  else
    release_name+=-arm64
  fi

  mkdir -p "$pkgdir/usr/lib"
  cp -a "$release_name" "$pkgdir/usr/lib/$pkgname"

  mkdir -p "$pkgdir/usr/bin"
  ln -s "/usr/lib/$pkgname/bin/$pkgname" "$pkgdir/usr/bin/$pkgname"

  mkdir -p "$pkgdir/usr/lib/systemd/system"
  cp -aL "$pkgname-$pkgver@.service" "$pkgdir/usr/lib/systemd/system/$pkgname@.service"

  mkdir -p "$pkgdir/usr/lib/systemd/user"
  cp -aL "$pkgname-$pkgver-user.service" "$pkgdir/usr/lib/systemd/user/$pkgname.service"

  mkdir -p "$pkgdir/usr/share/licenses"
  cp -a "$release_name/LICENSE" "$pkgdir/usr/share/licenses/$pkgname"
}
