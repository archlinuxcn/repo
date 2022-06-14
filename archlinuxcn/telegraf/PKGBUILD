# Maintainer: "Amhairghin" Oscar Garcia Amor (https://ogarcia.me)
# Contributor: Nicolas Leclercq <nicolas.private@gmail.com>
# Contributor: Adam S Levy <adam@aslevy.com>


pkgname=telegraf
pkgver=1.23.0
pkgrel=1
pkgdesc='Plugin-driven server agent for reporting metrics into InfluxDB'
arch=('i686' 'x86_64' 'armv6h' 'armv7h' 'aarch64')
url='http://influxdb.org/'
license=('MIT')
depends=('glibc')
makedepends=('go' 'git')
options=('!lto')
backup=('etc/telegraf/telegraf.conf')
install="${pkgname}.install"
source=("https://github.com/influxdata/${pkgname}/archive/v${pkgver}/${pkgname}-v${pkgver}.tar.gz"
        "${pkgname}.install"
        "${pkgname}.service"
        "${pkgname}.sysusers"
        "${pkgname}.tmpfiles")
b2sums=('256a0da38293507175a1583a49ca861d5d713b04f2bd659addb7ec74a140695ca920d9a19ad3de97730da4c29429c63acd3c171b01563deef8137a808708abb6'
        'a99e279fa6057b64b8a531922b9ce249fccea86b777686966932b6101923aaa9bacfe51d14dd2ef3168217b0d2d76fd06ce8ff50ae27d19fee69fcad975a83a9'
        'a0ea1bf213d10a6186993a48e6a8ca0ab70e3a949d85d0f7b881baeea3d051d05596863f1cef28ad83b0d2bc976a101014d7c04ae17a3ce2b98ce73b2b205826'
        'aac77720058d91abbe0ad28dadeb429a812e94c970c29491d787f039aece4a6401e8d52aa8c31b439771e8c31aed97cd822f1d4730eaa86fdff7140a0f45e143'
        '16df3d7a60cf88f979c48983e0bba099cc6c270f173b5caf9716c51b5545cf4d6494141d8e068e8ab39dacb6f3e6ca54c30aea619854ac752d804244b5a1cc21')

prepare() {
  cd "${pkgname}-${pkgver}"
  mkdir -p build/
}

build() {
  cd "${pkgname}-${pkgver}"
  export CGO_CPPFLAGS="${CPPFLAGS}"
  export CGO_CFLAGS="${CFLAGS}"
  export CGO_CXXFLAGS="${CXXFLAGS}"
  export GOFLAGS="-buildmode=pie -trimpath -mod=readonly -modcacherw"
  _LDFLAGS="-X main.goos=$(go env GOOS) -X main.goarch=$(go env GOARCH) -X main.version=${pkgver} -X main.branch=tag-${pkgver} -X main.commit=tag-${pkgver} -extldflags ${LDFLAGS}"
  go build -o build -ldflags="${_LDFLAGS}" "./cmd/telegraf"
}

package() {
  # binary
  install -D -m755 "${srcdir}/${pkgname}-${pkgver}/build/telegraf" \
    "${pkgdir}/usr/bin/telegraf"

  # configuration files
  install -dD -m755 "${pkgdir}/etc/telegraf/telegraf.d"
  "${srcdir}/${pkgname}-${pkgver}/build/telegraf" -sample-config > \
    "${pkgdir}/etc/telegraf/telegraf.conf"

  # license
  install -Dm644 "${srcdir}/${pkgname}-${pkgver}/LICENSE" \
    "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"

  # service
  install -D -m644 "${srcdir}/${pkgname}.service" \
    "${pkgdir}/usr/lib/systemd/system/${pkgname}.service"

  # systemd user and home directory
  install -D -m644 "${srcdir}/${pkgname}.sysusers" \
    "${pkgdir}/usr/lib/sysusers.d/${pkgname}.conf"
  install -D -m644 "${srcdir}/${pkgname}.tmpfiles" \
    "${pkgdir}/usr/lib/tmpfiles.d/${pkgname}.conf"
}
