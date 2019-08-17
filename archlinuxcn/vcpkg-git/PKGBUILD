# Maintainer: Honghao Li <hh.li99@outlook.com>
# Maintainer: Michael Yang <ohmyarchlinux@pm.me>

pkgname=vcpkg-git
pkgver=r9094.300e21d59
pkgrel=1
pkgdesc='VC++ Pcakaging Tool'
arch=('x86_64')
url='https://github.com/Microsoft/vcpkg'
license=('MIT')
makedepends=('git' 'cmake>=3.3.0' 'ninja')
conflicts=('vcpkg')
provides=('vcpkg')
source=('git+https://github.com/Microsoft/vcpkg.git'
        'vcpkg.sh'
        'vcpkg-git.install')
sha512sums=('SKIP'
            '9028f5f3f6915894f69924e49cddaee3cb670d39c03b56599d858cf278ca0f2e977363a2682d9a12a837d18508050f7009c1e61c4e572045d24a2bf93658fbc6'
            '9b113b12b9005193fa59b60dd33f5a589897b166bc0611ff18a6437727b922decaf0a26cec40aaa4a9a52bfb76a7dd7b3ecd7401f9dfe89a1684aaf7649427f6')
install=${pkgname}.install

pkgver() {
  cd vcpkg
  printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

prepare() {
  mkdir build
  touch vcpkg/.vcpkg-root
}

build() {
  cd build
  ../vcpkg/bootstrap-vcpkg.sh -useSystemBinaries
  cp ../vcpkg/vcpkg .
}

package() {
  cd "${srcdir}"
  install -dm755 "${pkgdir}/usr/bin"
  install -Dm755 "vcpkg.sh" "${pkgdir}/usr/bin/vcpkg"

  install -dm755 "${pkgdir}/usr/share/licenses"
  install -Dm644 "vcpkg/LICENSE.txt" "${pkgdir}/usr/share/licenses/vcpkg-git/LICENSE.txt"

  install -dm755 "${pkgdir}/usr/share/vcpkg"
  install -dm755 "${pkgdir}/var/cache/vcpkg"
  cp --preserve=mode -r vcpkg/{docs,ports,scripts,triplets,CHANGELOG.md,.vcpkg-root} "${pkgdir}/usr/share/vcpkg"
  install -Dm755 "build/vcpkg" "${pkgdir}/usr/share/vcpkg/vcpkg"

}
