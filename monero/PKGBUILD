# Maintainer: anonimal <anonimal at getmonero dot org>
# Contributor: redfish <redfish at galactica dot pw>
# Contributor: Onishin <onishin at onishin dot org>

pkgbase=('monero')
pkgname=('monero' 'libmonero-wallet')
pkgver=0.13.0.2
pkgrel=3
pkgdesc="Monero: the secure, private, untraceable currency - release version (includes daemon, wallet and miner)"
license=('custom:Cryptonote')
arch=('x86_64' 'i686' 'armv7h' 'aarch64')
url="https://getmonero.org/"
depends=('boost-libs' 'libunwind' 'openssl' 'readline' 'zeromq' 'pcsclite')
makedepends=('git' 'cmake' 'boost' 'gtest' 'qt5-tools')
provides=('monero' 'libmonero-wallet')
conflicts=('bitmonero-git' 'libmonero-wallet-git')

source=("${pkgname}"::"git+https://github.com/monero-project/monero#tag=v${pkgver}")

sha256sums+=('SKIP')

_monero="${pkgbase}"
_build="build"

prepare()
{
  git -C "${pkgname}" submodule update --init --recursive --force
}

build() {
  cd "${srcdir}/${_monero}"
  CMAKE_FLAGS+=" -DCMAKE_BUILD_TYPE=Release "
  CMAKE_FLAGS+=" -DCMAKE_INSTALL_PREFIX=/usr "
  CMAKE_FLAGS+=" -DBUILD_GUI_DEPS=ON "
  #CMAKE_FLAGS+=" -DCMAKE_LINKER=/usr/bin/ld.gold " # #974 ld segfault on ARM, re-implement if needed
  mkdir -p $_build && cd $_build
  cmake $CMAKE_FLAGS ../
  make
}

# Disable running of tests. Tests should not be needed outside of the development environment.
# Cherry-picking tests that aren't "too long" also defeats the purpose of running tests.
#check() {
#  cd "${srcdir}/${_monero}/${_build}"
#
#  # Temporarily disable some a tests:
#  #  * coretests takes too long (~25000s)
#  #  * libwallet_api_tests fail (Issue #895)
#  #  * unit_tests were run separately above
#  #  * hash-variant2-int-sqrt takes too long
#  CTEST_ARGS+="-E 'core_tests|libwallet_api_tests|unit_tests|hash-variant2-int-sqrt'"
#  echo ">>> NOTE: some tests excluded: $CTEST_ARGS"
#
#  make ARGS="$CTEST_ARGS" test
#}

package_monero() {
  backup=('etc/monerod.conf')
  install=monero.install

  # Uncomment for a debug build
  # options=(!strip debug)
  install -Dm644 "${srcdir}/${_monero}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"

  install -Dm644 "${srcdir}/${_monero}/utils/conf/monerod.conf" "${pkgdir}/etc/monerod.conf"
  install -Dm644 "${srcdir}/${_monero}/utils/systemd/monerod.service" "${pkgdir}/usr/lib/systemd/system/monerod.service"

  install -Dm755 "${srcdir}/${_monero}/build/bin/monero-blockchain-ancestry" "${pkgdir}/usr/bin/monero-blockchain-ancestry"
  install -Dm755 "${srcdir}/${_monero}/build/bin/monero-blockchain-blackball" "${pkgdir}/usr/bin/monero-blockchain-blackball"
  install -Dm755 "${srcdir}/${_monero}/build/bin/monero-blockchain-depth" "${pkgdir}/usr/bin/monero-blockchain-depth"
  install -Dm755 "${srcdir}/${_monero}/build/bin/monero-blockchain-export" "${pkgdir}/usr/bin/monero-blockchain-export"
  install -Dm755 "${srcdir}/${_monero}/build/bin/monero-blockchain-import" "${pkgdir}/usr/bin/monero-blockchain-import"
  install -Dm755 "${srcdir}/${_monero}/build/bin/monero-blockchain-usage" "${pkgdir}/usr/bin/monero-blockchain-usage"

  install -Dm755 "${srcdir}/${_monero}/build/bin/monero-gen-trusted-multisig" "${pkgdir}/usr/bin/monero-gen-trusted-multisig"

  install -Dm755 "${srcdir}/${_monero}/build/bin/monero-wallet-cli" "${pkgdir}/usr/bin/monero-wallet-cli"
  install -Dm755 "${srcdir}/${_monero}/build/bin/monero-wallet-rpc" "${pkgdir}/usr/bin/monero-wallet-rpc"

  install -Dm755 "${srcdir}/${_monero}/build/bin/monerod" "${pkgdir}/usr/bin/monerod"
}

package_libmonero-wallet() {
  # NOTE: this is crucial, otherwise stripping breaks the .a archive:
  # monero-core (GUI) fails to link against it (it can't find symbols
  # that are clearly in the library).
  options=(!strip)

  _stage_dir=stagedir

  cd "${srcdir}/${_monero}/${_build}"

  mkdir -p $_stage_dir
  make DESTDIR=$_stage_dir install

  cd $_stage_dir
  find usr/{include,lib} -type f -exec install -D -m 755 {} ${pkgdir}/{} \;
}
