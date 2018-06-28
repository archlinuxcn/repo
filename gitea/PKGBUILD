# Maintainer: Frederik Schwan <frederik dot schwan at linux dot com>

pkgname=gitea
pkgver=1.4.3
pkgrel=1
pkgdesc='Git with a cup of tea, forked from Gogs. Is a Self Hosted Git Service in the Go Programming Language.'
arch=('x86_64' 'i686' 'arm' 'armv6h' 'armv7h' 'aarch64')
url='http://gitea.io'
license=('MIT')
depends=('git')
makedepends=('go')
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
sha512sums=('24498b418b9ddb14da5568a206e1fa0831c5789e0b64207f413c3b86e2a855052f7af80d3cb80549eaae6944e22af271c00f6308c66487c3be0dccf55a17976a'
            '042199a7c692a7a2b344f1af3bc1c84b8dea2e2609634e4cbf2d7d7964c23508d7cad772a39de50a1116bd8d85b597c9988dd3ef398a26c2df8189f3aa9f40ee'
            '485f627daee2eebbd081f44bce5686eb2ee373a0fb24616fa1940d275caf1a192b29ef20b236a99f5ace99922dbb19cdc0db39b761fa8002d6f4bebe625ae8db'
            '3d8439ad48621a4a87634588377d133ae13a9ce30830d140beee1d69e3d4d40f6c47df663e97620d88c42e892c7fc0845f4091574c6314bed53fd20c7416b949')

prepare() {
  mkdir -p "${srcdir}/src/code.gitea.io"
  ln -s "${srcdir}/${pkgname}-${pkgver}" "${srcdir}/src/code.gitea.io/${pkgname}"
  sed -i -e "s/\"main.Version.*$/\"main.Version=${pkgver}\"/" "${srcdir}/${pkgname}-${pkgver}/Makefile"
}

build() {
  cd ${srcdir}/src/code.gitea.io/${pkgname}
  GOPATH="${srcdir}" PATH="${PATH}:${GOPATH}/bin/" make DESTDIR="${pkgdir}" TAGS="sqlite tidb pam" clean generate build
}

package() {
  install -Dm644 "${srcdir}/gitea.tmpfiles" "${pkgdir}/usr/lib/tmpfiles.d/gitea.conf"

  install -dm 750 "${pkgdir}/var/lib/gitea/"
  install -dm 750 "${pkgdir}/var/lib/gitea/"{repos,tmp,attachments,data,indexer,conf}
  install -dm 750 "${pkgdir}/var/log/gitea/"
  install -dm 775 "${pkgdir}/etc/gitea/"

  install -Dm755 "${srcdir}/src/code.gitea.io/${pkgname}/${pkgname}" "${pkgdir}/usr/bin/${pkgname}"
  install -Dm644 "${srcdir}/gitea.service" "${pkgdir}/usr/lib/systemd/system/${pkgname}.service"
  install -Dm644 "${srcdir}/src/code.gitea.io/${pkgname}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
  install -Dm660 "${srcdir}/app.ini" "${pkgdir}/etc/gitea/app.ini"

  cp -r "${srcdir}/src/code.gitea.io/${pkgname}/"{templates,options,public} "${pkgdir}/var/lib/${pkgname}"
  cp -r "${srcdir}/src/code.gitea.io/${pkgname}/options/locale" "${pkgdir}/var/lib/${pkgname}/conf"
}
