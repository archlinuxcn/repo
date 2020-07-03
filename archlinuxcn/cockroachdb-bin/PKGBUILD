# Maintainer:  Dimitris Kiziridis <ragouel at outlook dot com>
# Contributor: Konrad Tegtmeier <konrad.tegtmeier+aur@gmail.com>
# Contributor: Marcel O'Neil <marcel@marceloneil.com>

pkgname=cockroachdb-bin
pkgver=20.1.3
pkgrel=1
pkgdesc='An open source, survivable, strongly consistent, scale-out SQL database'
arch=('x86_64')
url='https://www.cockroachlabs.com'
license=('Apache' 'custom:BSL' 'custom:CCL')
conflicts=('cockroachdb')
provides=('cockroachdb')
depends=('glibc')
source=("${pkgname}-${pkgver}.tgz::https://binaries.cockroachdb.com/cockroach-v${pkgver}.linux-amd64.tgz"
        "LICENSE::https://raw.githubusercontent.com/cockroachdb/cockroach/v${pkgver}/LICENSE"
        'cockroach.service'
        'cockroach.default'
        'cockroach.sysusers'
        'cockroach.tmpfiles')
sha256sums=('8290c06f123ba1018f1c8702d3b66c774d5f93a78086550028473af838a22828'
            '8a2fba9d26592ff3538f44c96d1b894ef44649058b4d04f3fda49518a9c4ae11'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP')

package() {
  # generate shell completion
  "${srcdir}/cockroach-v${pkgver}.linux-amd64/cockroach" \
  gen autocomplete bash --out "${srcdir}/cockroach.bash"
  "${srcdir}/cockroach-v${pkgver}.linux-amd64/cockroach" \
  gen autocomplete zsh --out "${srcdir}/cockroach.zsh"

  # generate man pages
  "${srcdir}/cockroach-v${pkgver}.linux-amd64/cockroach" \
  gen man --path "${srcdir}/man"

  # binary
  install -Dm755 "${srcdir}/cockroach-v${pkgver}.linux-amd64/cockroach" "${pkgdir}/usr/bin/cockroach"

  # user/group & owned directories
  install -Dm644 "${srcdir}/cockroach.sysusers" "${pkgdir}/usr/lib/sysusers.d/cockroach.conf"
  install -Dm644 "${srcdir}/cockroach.tmpfiles" "${pkgdir}/usr/lib/tmpfiles.d/cockroach.conf"

  # services & runtime
  install -Dm644 "${srcdir}/cockroach.service" "${pkgdir}/usr/lib/systemd/system/cockroach.service"
  install -Dm644 "${srcdir}/cockroach.default" "${pkgdir}/etc/default/cockroach"

  # man pages
  install -d "${pkgdir}/usr/share/man/man1/"
  install -m644 "${srcdir}"/man/*.1 "${pkgdir}/usr/share/man/man1/"

  # shell completion
  install -Dm644 cockroach.bash "${pkgdir}/usr/share/bash-completion/completions/cockroach"
  install -Dm644 cockroach.zsh  "${pkgdir}/usr/share/zsh/site-functions/_cockroach"

  # licenses
  install -Dm644 "${srcdir}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}