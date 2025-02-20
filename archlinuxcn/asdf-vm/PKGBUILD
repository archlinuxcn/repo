# Maintainer: Alec Mev <alec@mev.earth>
# Maintainer: Raphael Nestler <raphael.nestler@gmail.com>

_pkgname=asdf
pkgname=asdf-vm
pkgver=0.16.3
pkgrel=1
pkgdesc='Extendable version manager with support for Ruby, Node.js, Elixir, Erlang & more'
arch=('x86_64' 'aarch64')
url='https://asdf-vm.com'
license=('MIT')
makedepends=('go')
depends=(
  'curl'
  'git'
)
optdepends=(
  'autoconf'
  'automake'
  'bash-completion: For completions to work in Bash'
  'libffi'
  'libtool'
  'libxslt'
  'libyaml'
  'ncurses'
  'openssl'
  'readline'
  'unixodbc'
  'unzip: Needed by some plugins, like Elixir'
)
install=asdf-vm.install
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/asdf-vm/asdf/archive/v${pkgver}.tar.gz")
sha256sums=('987402cff487219de1591abfc6923ebd8f79f596c991a36fc6542e6c330af722')

build() {
  cd "${_pkgname}-${pkgver}"
  export CGO_CPPFLAGS="${CPPFLAGS}"
  export CGO_CFLAGS="${CFLAGS}"
  export CGO_CXXFLAGS="${CXXFLAGS}"
  export CGO_LDFLAGS="${LDFLAGS}"
  export GOFLAGS="-buildmode=pie -trimpath -ldflags=-linkmode=external -mod=readonly -modcacherw"
  go build -ldflags="-s -X main.version=${pkgver}-arch" -o build/ ./cmd/asdf
}

package() {
  cd "${_pkgname}-${pkgver}"

  install -Dm755  build/asdf "$pkgdir"/usr/bin/$_pkgname

  local usrshare="${pkgdir}/usr/share"

  local docdir="${usrshare}/doc/${pkgname}"
  mkdir -p "${docdir}"
  cp help.txt "${docdir}"

  # https://aur.archlinux.org/packages/asdf-vm#comment-886293
  find . \
    -path ./.github \
    -prune \
    -o \
    -name '*.md' \
    -exec cp --parents '{}' "${docdir}" \;

  install -Dm644 -t "${usrshare}/licenses/${pkgname}/" LICENSE

  install -Dm644 internal/completions/asdf.bash "${usrshare}/bash-completion/completions/asdf"
  install -Dm644 internal/completions/asdf.fish "${usrshare}/fish/vendor_completions.d/asdf.fish"
  install -Dm644 internal/completions/asdf.zsh     "${usrshare}/zsh/site-functions/_asdf"
}
