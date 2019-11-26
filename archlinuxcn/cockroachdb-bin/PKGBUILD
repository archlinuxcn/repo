# Maintainer: Konrad Tegtmeier <konrad.tegtmeier+aur@gmail.com>
# Contributor: Marcel O'Neil <marcel@marceloneil.com>

pkgname=cockroachdb-bin
conflicts=('cockroachdb')
provides=('cockroachdb')
pkgver=19.2.1
pkgrel=1
pkgdesc="An open source, survivable, strongly consistent, scale-out SQL database"
arch=('x86_64')
url="https://www.cockroachlabs.com/"
license=('BSD' 'MIT' 'custom:BSL' 'custom:CCL' 'custom:LevelDB' 'custom:OFL' 'custom:PostgreSQL')
depends=('glibc')
source=("https://binaries.cockroachdb.com/cockroach-v${pkgver}.linux-amd64.tgz"
        "https://raw.githubusercontent.com/cockroachdb/cockroach/v${pkgver}/LICENSE"
        "https://raw.githubusercontent.com/cockroachdb/cockroach/v${pkgver}/licenses/BSD-biogo.txt"
        "https://raw.githubusercontent.com/cockroachdb/cockroach/v${pkgver}/licenses/BSD-golang.txt"
        "https://raw.githubusercontent.com/cockroachdb/cockroach/v${pkgver}/licenses/BSD-grpc.txt"
        "https://raw.githubusercontent.com/cockroachdb/cockroach/v${pkgver}/licenses/BSD-vitess.txt"
        "https://raw.githubusercontent.com/cockroachdb/cockroach/v${pkgver}/licenses/BSL.txt"
        "https://raw.githubusercontent.com/cockroachdb/cockroach/v${pkgver}/licenses/CCL.txt"
        "https://raw.githubusercontent.com/cockroachdb/cockroach/v${pkgver}/licenses/LevelDB.txt"
        "https://raw.githubusercontent.com/cockroachdb/cockroach/v${pkgver}/licenses/MIT-gofrs.txt"
        "https://raw.githubusercontent.com/cockroachdb/cockroach/v${pkgver}/licenses/OFL-inconsolata.txt"
        "https://raw.githubusercontent.com/cockroachdb/cockroach/v${pkgver}/licenses/OFL-lato.txt"
        "https://raw.githubusercontent.com/cockroachdb/cockroach/v${pkgver}/licenses/PostgreSQL.txt"
        cockroach.service
        cockroach.default
        cockroach.sysusers
        cockroach.tmpfiles)
sha256sums=('21046d8e448533db125fd62cccf890a4bf9b75f384f6b0afcca126930b2a6e2a'
            '8a2fba9d26592ff3538f44c96d1b894ef44649058b4d04f3fda49518a9c4ae11'
            'b3ef077aa9a0d4b697722de993fa83959f10910ae600de90bcdcdd49fafce371'
            '2d36597f7117c38b006835ae7f537487207d8ec407aa9d9980794b2030cbc067'
            'af1c246b8eb8b2d2ee3f1471247569d7f35cefff40e9b967d563622bb04c1e69'
            '23681c6986fb33d57957660543f6e9dcbbcf6d2ae2f9fa2dbdb5efec5aa0d95f'
            'aee63ff7287ef00a38e33db06c5a27e38443c23941c1266febe67804dd57697e'
            '2cd6aceddb7240c6ef395f7d92e26de4da63f7700504f6ce47e2aab4e39a4122'
            'b568f1f37a5a1d37a3e981e7c8b7fc4856ca33b2ca0a45bc8e847aaaf7afe485'
            '6932de4a7e8c7877f4d83b6e174d3331f229b1aba4c4490590c8894d0ddf914e'
            '38dabe8206e881aa2fd82d4bc58f09447499894e063678135084614fe3e9bfcb'
            '14b8609fd8281cb961730de7d3b2964dcc6e0e395e759b1422e52e39a0fdc6b2'
            'b34067e89373e1a47367b454862f43061ad1680542b39b6d95ed29c354473e15'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP')

build() {
    # generate shell completion
    "${srcdir}/cockroach-v${pkgver}.linux-amd64/cockroach" \
        gen autocomplete bash --out "${srcdir}/cockroach.bash"
    "${srcdir}/cockroach-v${pkgver}.linux-amd64/cockroach" \
        gen autocomplete zsh --out "${srcdir}/cockroach.zsh"

    # generate man pages
    "${srcdir}/cockroach-v${pkgver}.linux-amd64/cockroach" \
        gen man --path "${srcdir}/man"
}

package() {

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
  install -Dm644 "${srcdir}/LICENSE"        "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
  install -Dm644 "${srcdir}/BSD-biogo.txt"  "${pkgdir}/usr/share/licenses/${pkgname}/BSD-biogo.txt"
  install -Dm644 "${srcdir}/BSD-golang.txt" "${pkgdir}/usr/share/licenses/${pkgname}/BSD-golang.txt"
  install -Dm644 "${srcdir}/BSD-grpc.txt"   "${pkgdir}/usr/share/licenses/${pkgname}/BSD-grpc.txt"
  install -Dm644 "${srcdir}/BSD-vitess.txt" "${pkgdir}/usr/share/licenses/${pkgname}/BSD-vitess.txt"
  install -Dm644 "${srcdir}/BSD-vitess.txt" "${pkgdir}/usr/share/licenses/${pkgname}/LevelDB.txt"
  install -Dm644 "${srcdir}/CCL.txt"        "${pkgdir}/usr/share/licenses/${pkgname}/CCL.txt"
  install -Dm644 "${srcdir}/PostgreSQL.txt" "${pkgdir}/usr/share/licenses/${pkgname}/PostgreSQL.txt"
}
