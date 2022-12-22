# Maintainer: Fredy García <frealgagu at gmail dot com>
# Contributor: Philip Goto <philip.goto@gmail.com>, WithTheBraid <the-one@with-the-braid.cf>

pkgname=flutter
pkgver=3.3.10
pkgrel=1
pkgdesc="A new mobile app SDK to help developers and designers build modern mobile apps for iOS and Android."
arch=("x86_64" "aarch64")
url="https://${pkgname}.dev"
license=("custom" "BSD" "CCPL")
depends=("git" "glu" "java-environment" "libglvnd" "unzip")
optdepends=("android-sdk" "android-studio" "intellij-idea-community-edition" "intellij-idea-ultimate-edition" "ninja" "perl" "python")
makedepends=("python")
backup=("opt/${pkgname}/packages/${pkgname}_test/pubspec.yaml" "opt/${pkgname}/packages/${pkgname}/pubspec.yaml")
options=("!emptydirs")
install="${pkgname}.install"
source=(
  "${pkgname}-${pkgver}.tar.xz::https://storage.googleapis.com/flutter_infra_release/releases/stable/linux/${pkgname}_linux_${pkgver/.hotfix/+hotfix}-stable.tar.xz"
  "${pkgname}.sh"
  "${pkgname}.csh"
)
sha256sums=('d24e83f7a6b829d163feeef1abfcc30869f0c5d1af93e9917426265dad507024'
            '1dea1952d386c43948b9970382c2da5b65b7870684b8ad2ad89124e873aa485a'
            '7ef10d753cfaac52d243549764a793f44f8284a1f4b11715ccd2fa915b026a6f')

build() {
  rm -rf "${srcdir}/${pkgname}/bin/cache" "${srcdir}/${pkgname}/.pub-cache"
  "${srcdir}/${pkgname}/bin/internal/update_dart_sdk.sh"
  "${srcdir}/${pkgname}/bin/flutter" precache
}

package() {
  install -Dm644 "${srcdir}/${pkgname}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
  install -Dm755 "${srcdir}/${pkgname}.sh" "${pkgdir}/etc/profile.d/${pkgname}.sh"
  install -Dm755 "${srcdir}/${pkgname}.csh" "${pkgdir}/etc/profile.d/${pkgname}.csh"
  install -dm755 "${pkgdir}/opt/${pkgname}"
  install -dm755 "${pkgdir}/usr/bin"
  cp -ra "${srcdir}/${pkgname}" "${pkgdir}/opt/"
  find "${pkgdir}/opt/${pkgname}" -type d -exec chmod a+rx {} +
  find "${pkgdir}/opt/${pkgname}" -type f -exec chmod a+r {} +
  # those files *must* be read-write for end-users; not my fault *grumble*
  chmod a+rw "${pkgdir}/opt/${pkgname}/version" "${pkgdir}/opt/${pkgname}/bin/cache/lockfile" "${pkgdir}/opt/${pkgname}/bin/cache/usbmuxd.stamp" "${pkgdir}/opt/${pkgname}/bin/cache/libimobiledevice.stamp"
  ln -s "/opt/${pkgname}/bin/${pkgname}" "${pkgdir}/usr/bin/${pkgname}"
}
