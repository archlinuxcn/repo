# Maintainer: Frederik Schwan <frederik dot schwan at linux dot com>

pkgname=gitea
pkgver=1.5.1
pkgrel=1
pkgdesc='Git with a cup of tea, forked from Gogs. Is a Self Hosted Git Service in the Go Programming Language.'
arch=('x86_64' 'i686' 'arm' 'armv6h' 'armv7h' 'aarch64')
url='http://gitea.io'
license=('MIT')
depends=('git')
makedepends=('go' 'go-bindata')
optdepends=('sqlite: SQLite support'
            'mariadb: MariaDB support'
            'postgresql: PostgreSQL support'
            'pam: Authentication via PAM support'
            'redis: Redis support'
            'memcached: MemCached support'
            'openssh: GIT over SSH support')
conflicts=('gitea-git' 'gitea-git-dev')
backup=('etc/gitea/app.ini')
source=(https://github.com/go-gitea/gitea/archive/v${pkgver}.tar.gz
        gitea.tmpfiles
        gitea.service
        app.ini)
sha512sums=('16d10d98caf377d3bd5b4933316290e853a8fc46f5fdb3c206b9607750b5bdbdfd5c50bf8dd59906d7476d0e9211a67332eb4b780d8d37cdfb1c0bc3141ceed7'
            'c5fa7ae2e251ef86f002b001b9c46528f5a39e118ec56bd72e69ae62e9674bd5ffd2b2762e078fdf16c6ae8991c18b33b91a16e4cc9922744bfab5bc3377c079'
            '485f627daee2eebbd081f44bce5686eb2ee373a0fb24616fa1940d275caf1a192b29ef20b236a99f5ace99922dbb19cdc0db39b761fa8002d6f4bebe625ae8db'
            '3d8439ad48621a4a87634588377d133ae13a9ce30830d140beee1d69e3d4d40f6c47df663e97620d88c42e892c7fc0845f4091574c6314bed53fd20c7416b949')

prepare() {
  mkdir -p "${srcdir}/src/code.gitea.io"
  mv "${srcdir}/${pkgname}-${pkgver}" "${srcdir}/src/code.gitea.io/${pkgname}"
}

build() {
  cd ${srcdir}/src/code.gitea.io/${pkgname}
  GOPATH="${srcdir}" make clean generate
  GOPATH="${srcdir}" EXTRA_GOFLAGS="-gcflags all=-trimpath=${srcdir} -asmflags all=-trimpath=${srcdir}" \
  make LDFLAGS="-X \"main.Version=${pkgver}\" -X \"main.Tags=\$(TAGS)\"" GOFLAGS="-v" TAGS="bindata sqlite tidb pam" build
}

package() {
  install -dm 750 "${pkgdir}/var/lib/gitea/"
  install -dm 750 "${pkgdir}/var/lib/gitea/"{attachments,data,indexer,repos,tmp}
  install -dm 750 "${pkgdir}/var/log/gitea/"
  install -dm 775 "${pkgdir}/etc/gitea/"

  install -Dm755 "${srcdir}/src/code.gitea.io/${pkgname}/${pkgname}" "${pkgdir}/usr/bin/${pkgname}"
  install -Dm644 "${srcdir}/src/code.gitea.io/${pkgname}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
  install -Dm660 "${srcdir}/app.ini" "${pkgdir}/etc/gitea/app.ini"

  install -Dm644 "${srcdir}/gitea.tmpfiles" "${pkgdir}/usr/lib/tmpfiles.d/gitea.conf"
  install -Dm644 "${srcdir}/gitea.service" "${pkgdir}/usr/lib/systemd/system/${pkgname}.service"
}
