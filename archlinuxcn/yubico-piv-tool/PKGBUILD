# Maintainer: travisghansen <travisghansen@yahoo.com>

pkgname=yubico-piv-tool
pkgver=2.1.0
pkgrel=2
pkgdesc="Tool to interact with the PIV applet on a YubiKey NEO"
arch=('armv7h' 'i686' 'x86_64')
license=('GPL3')
depends=('pcsclite' 'openssl')
makedepends=('check' 'cmake' 'gengetopt' 'help2man')
url=https://developers.yubico.com/yubico-piv-tool/
source=(
 "https://developers.yubico.com/yubico-piv-tool/Releases/${pkgname}-${pkgver}.tar.gz"
 "https://developers.yubico.com/yubico-piv-tool/Releases/${pkgname}-${pkgver}.tar.gz.sig"
)
md5sums=('fda6c27ae459185e5a0f119a5a3d5de0'
         'SKIP')
validpgpkeys=('0A3B0262BCA1705307D5FF06BCA00FD4B2168C0A'
              '20EE325B86A81BCBD3E56798F04367096FBA95E8'
              'B70D62AA6A31AD6B9E4F9F4BDC8888925D25CA7A'
              'FF8AF719AE5828181B894D831CE39268A0973948'
              'B6042E2BD1FDBC2BCA8588B2FF8D3B45B7B875A9'
              '8D0B4EBA9345254BCEC0E843514F078FF4AB24C3'
              '57A9DEED4C6D962A923BB691816F3ED99921835E'
              '268583B64786F50F807456DA8CED3A80D41C0DCB'
              '1D7308B0055F5AEF36944A8F27A9C24D9588EA0F'
              '355C8C0186CC96CBA49F9CD8DAA17C2953914D9D'
              '9E885C0302F9BB9167529C2D5CBA11E6ADC7BCD1'
              '7FBB6186957496D58C751AC20E777DD85755AA4A'
              'EE90AE0D19774C8386628FAAB428949EF7914718'
              '9AA9BDB11BB1B99A21285A330664A76954265E8C'
              'DCB904FAB343CFA719076EF79EA90242958E0658')
options=(!libtool)

build() {
  cmake -B build -S "${pkgname}-${pkgver}" \
      -DCMAKE_BUILD_TYPE='None' \
      -DCMAKE_INSTALL_PREFIX='/usr' \
      -Wno-dev
  make -C build
}

package() {
  DESTDIR="${pkgdir}" make install -C build
}
