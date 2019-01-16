# Maintainer: Fredy García <frealgagu at gmail dot com>
# Contributor: Youngbin Han <sukso96100@gmail.com>
# Contributor: blainester <theblainestory@gmail.com>
# Contributor: mar77i <mar77i at protonmail dot ch>

pkgname=micro
pkgver=1.4.1
pkgrel=2
pkgdesc="A modern and intuitive terminal-based text editor"
arch=("armv6h" "armv7h" "i686" "x86_64")
url="https://github.com/zyedidia/${pkgname}"
license=("MIT")
depends=("glibc")
makedepends=("git" "go")
optdepends=('xclip: Required for copying/pasting text')
source=("${pkgname}-${pkgver}::git+https://github.com/zyedidia/${pkgname}.git#tag=v1.4.1"
        "semver::git+https://github.com/blang/semver"
        "go-humanize::git+https://github.com/dustin/go-humanize"
        "errors::git+https://github.com/go-errors/errors"
        "go-isatty::git+https://github.com/mattn/go-isatty"
        "go-runewidth::git+https://github.com/mattn/go-runewidth"
        "go-homedir::git+https://github.com/mitchellh/go-homedir"
        "go-diff::git+https://github.com/sergi/go-diff"
        "gopher-lua::git+https://github.com/yuin/gopher-lua"
        "net::git+https://go.googlesource.com/net"
        "clipboard::git+https://github.com/zyedidia/clipboard"
        "glob::git+https://github.com/zyedidia/glob"
        "tcell::git+https://github.com/zyedidia/tcell"
        "encoding::git+https://github.com/gdamore/encoding"
        "text::git+https://go.googlesource.com/text"
        "go-colorful::git+https://github.com/lucasb-eyer/go-colorful"
        "gopher-luar::git+https://github.com/layeh/gopher-luar"
        "yaml.v2::git+https://gopkg.in/yaml.v2"
        "poller::git+https://github.com/zyedidia/poller"
        "json5::git+https://github.com/flynn/json5"
        "terminal::git+https://github.com/zyedidia/terminal"
        "pty::git+https://github.com/zyedidia/pty"
        "goconvey::git+https://github.com/smartystreets/goconvey"
        "gls::git+https://github.com/jtolds/gls"
        "assertions::git+https://github.com/smartystreets/assertions")
sha256sums=("SKIP" "SKIP" "SKIP" "SKIP" "SKIP"
            "SKIP" "SKIP" "SKIP" "SKIP" "SKIP"
            "SKIP" "SKIP" "SKIP" "SKIP" "SKIP"
            "SKIP" "SKIP" "SKIP" "SKIP" "SKIP"
            "SKIP" "SKIP" "SKIP" "SKIP" "SKIP")

prepare() {
  cd "${srcdir}/${pkgname}-${pkgver}"

  git submodule init
  git config "submodule.cmd/${pkgname}/vendor/github.com/blang/semver.url" "${srcdir}/semver"
  git config "submodule.cmd/${pkgname}/vendor/github.com/dustin/go-humanize.url" "${srcdir}/go-humanize"
  git config "submodule.cmd/${pkgname}/vendor/github.com/go-errors/errors.url" "${srcdir}/errors"
  git config "submodule.cmd/${pkgname}/vendor/github.com/mattn/go-isatty.url" "${srcdir}/go-isatty"
  git config "submodule.cmd/${pkgname}/vendor/github.com/mattn/go-runewidth.url" "${srcdir}/go-runewidth"
  git config "submodule.cmd/${pkgname}/vendor/github.com/mitchellh/go-homedir.url" "${srcdir}/go-homedir"
  git config "submodule.cmd/${pkgname}/vendor/github.com/sergi/go-diff.url" "${srcdir}/go-diff"
  git config "submodule.cmd/${pkgname}/vendor/github.com/yuin/gopher-lua.url" "${srcdir}/gopher-lua"
  git config "submodule.cmd/${pkgname}/vendor/golang.org/x/net.url" "${srcdir}/net"
  git config "submodule.cmd/${pkgname}/vendor/github.com/zyedidia/clipboard.url" "${srcdir}/clipboard"
  git config "submodule.cmd/${pkgname}/vendor/github.com/zyedidia/glob.url" "${srcdir}/glob"
  git config "submodule.cmd/${pkgname}/vendor/github.com/zyedidia/tcell.url" "${srcdir}/tcell"
  git config "submodule.cmd/${pkgname}/vendor/github.com/gdamore/encoding.url" "${srcdir}/encoding"
  git config "submodule.cmd/${pkgname}/vendor/golang.org/x/text.url" "${srcdir}/text"
  git config "submodule.cmd/${pkgname}/vendor/github.com/lucasb-eyer/go-colorful.url" "${srcdir}/go-colorful"
  git config "submodule.cmd/${pkgname}/vendor/layeh.com/gopher-luar.url" "${srcdir}/gopher-luar"
  git config "submodule.cmd/${pkgname}/vendor/gopkg.in/yaml.v2.url" "${srcdir}/yaml.v2"
  git config "submodule.cmd/${pkgname}/vendor/github.com/zyedidia/poller.url" "${srcdir}/poller"
  git config "submodule.cmd/${pkgname}/vendor/github.com/flynn/json5.url" "${srcdir}/json5"
  git config "submodule.cmd/${pkgname}/vendor/github.com/zyedidia/terminal.url" "${srcdir}/terminal"
  git config "submodule.cmd/${pkgname}/vendor/github.com/zyedidia/pty.url" "${srcdir}/pty"
  git config "submodule.cmd/${pkgname}/vendor/github.com/smartystreets/goconvey.url" "${srcdir}/goconvey"
  git config "submodule.cmd/${pkgname}/vendor/github.com/jtolds/gls.url" "${srcdir}/gls"
  git config "submodule.cmd/${pkgname}/vendor/github.com/smartystreets/assertions.url" "${srcdir}/assertions"
  
  git submodule update --init
}

build() {
  cd "${srcdir}/${pkgname}-${pkgver}"

  echo "Linking to repository path..."
  mkdir -p "${srcdir}/src/github.com/zyedidia"
  ln -s "${srcdir}/${pkgname}-${pkgver}" "${srcdir}/src/github.com/zyedidia/${pkgname}"
  cd "${srcdir}/src/github.com/zyedidia/${pkgname}"
  
  GOPATH="${srcdir}" PATH="${PATH}:${GOPATH}/bin" make build-quick
  
  echo "Removing link..."
  rm -rf "${srcdir}/src"
}

package() {
  install -Dm755 "${srcdir}/${pkgname}-${pkgver}/${pkgname}" "${pkgdir}/usr/bin/${pkgname}"
  install -Dm644 "${srcdir}/${pkgname}-${pkgver}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
  for _file in ${srcdir}/${pkgname}-${pkgver}/*.md
  do
    install -Dm644 "${_file}" "${pkgdir}/usr/share/doc/${pkgname}/$(basename ${_file})"
  done
}
