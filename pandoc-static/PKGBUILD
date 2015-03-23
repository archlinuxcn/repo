# Maintainer: Nicolas Reynolds <fauno@kiwwwi.com.ar>
# Contributor: Luke Shumaker <lukeshu@sbcglobal.net>
# Based on haskell-pandoc

pkgname=pandoc-static
_pkgname=pandoc
pkgver=1.13.2
pkgrel=1
pkgdesc='Conversion between markup formats (no Haskell libraries)'
url='http://johnmacfarlane.net/pandoc/'
license=('GPL')

replaces=('pandoc')
provides=('pandoc')

arch=('i686' 'x86_64')
depends=('icu>=54' 'icu<55' 'gmp' 'libffi' 'zlib')
makedepends=('ghc' 'sh' 'cabal-install' 'alex' 'happy')
optdepends=('texlive-most: for PDF creation')
options=(strip !makeflags !distcc !emptydirs)
source=(https://repo.parabola.nu/other/${pkgname}/${pkgname}-${pkgver}.tar.xz)
md5sums=('dd2667b233b5f97b2841ae09895c2ac2')

declare -gA _flags
_flags[pandoc]='https make-pandoc-man-pages'
_flags[pandoc_citeproc]='small_base bibutils hexpat unicode_collation'

_packages=(hs-bibutils network hexpat text text-icu hsb2hs
  http-client-0.3.8.2
  http-client-tls http-types
  pandoc-${pkgver} pandoc-citeproc)
mkdepends=('ghc' 'cabal-install')
mksource() (
  set -o pipefail
  # building haddock requires an utf8 lang, if you use anything else you
  # have to enable an utf8 locale and run locale-gen
  test "${LANG#*.}" != "utf8" && export LANG="en_US.utf8"
  export HOME="$srcdir"

  mkdir $pkgname-$pkgver
  cd    $pkgname-$pkgver

  cabal update
  cabal fetch "${_packages[@]}"

  # Get the build order
  cabal install --dry-run \
     --flags="embed_data_files ${_flags[*]}" \
    "${_packages[@]}" > BUILDORDER

  # Place all of the downloaded sources in the target directory
  for file in ../.cabal/packages/*/*/*/*.tar.?z; do
    bsdtar xf "$file"
  done
)

prepare() {
  # EC is unfree and makes Parabola TeXLive cry
  # besides, it's unneeded
  find "${srcdir}/${pkgname}-${pkgver}/${_pkgname}-${pkgver}" \
    -name default.latex \
    -exec sed "/fontenc/d" -i {} \;
}

build() (
  cd "${srcdir}/${pkgname}-${pkgver}"
  mkdir -p ../build

  # building haddock requires an utf8 lang, if you use anything else you
  # have to enable an utf8 locale and run locale-gen
  test "${LANG#*.}" != "utf8" && export LANG="en_US.utf8"
  export HOME="${srcdir}"
  export PATH="${srcdir}/build/usr/bin:${PATH}"

  while read hkpkg; do
    if [ -d "$srcdir"/build/usr/share/doc/*/"$hkpkg" ]; then
      msg2 'Skipping %s' "$hkpkg"
      continue
    fi

    msg2 'Building %s' "$hkpkg"
    pushd "$hkpkg" >/dev/null
    case "$hkpkg" in
      $_pkgname-$pkgver)
        # Don' bother trying to set --libdir= outside of $pkgdir,
        # libdir is a relative (to prefix) path, never absolute.
        cabal configure -v \
          --flags="embed_data_files ${_flags[pandoc]}" \
          --prefix=/usr
        cabal build
        cabal register --inplace
        ;;
      pandoc-citeproc-*)
        cabal configure -v \
          --flags="embed_data_files ${_flags[pandoc_citeproc]}" \
          --prefix=/usr
        cabal build
        ;;
      *)
        cabal install --prefix="${srcdir}"/build/usr --flags="embed_data_files"
        ;;
    esac
    popd >/dev/null
  done < <(sed -rn 's/(\S*[0-9]+).*/\1/p' BUILDORDER)
)

package() {
  cd "${srcdir}/${pkgname}-${pkgver}"

  msg2 "Installing pandoc..."
  cd ${_pkgname}-${pkgver}
  cabal copy --destdir="${pkgdir}/"
  install -Dm644 {,"$pkgdir"/usr/share/}man/man1/pandoc.1
  install -Dm644 {,"$pkgdir"/usr/share/}man/man5/pandoc_markdown.5

  msg2 "Installing pandoc-citeproc..."
  cd ../pandoc-citeproc-*
  cabal copy --destdir="${pkgdir}/"

  msg2 "Installing extra executables..."
  cp -av "${srcdir}"/build/usr/bin/* "${pkgdir}"/usr/bin/

  msg2 "Removing library files..."
  rm -rfv "$pkgdir"/usr/lib

  msg2 "Installing licenses..."
  install -d                                 "${pkgdir}"/usr/share/licenses/${pkgname}
  cp -rv "${srcdir}"/build/usr/share/doc/*/* "${pkgdir}"/usr/share/licenses/${pkgname}
  mv -v        "${pkgdir}"/usr/share/doc/*/* "${pkgdir}"/usr/share/licenses/${pkgname}
}
md5sums=('6c763fae16e10400874b15d7b084ad82')
