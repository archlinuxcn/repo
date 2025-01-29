# Maintainer: Josef Vybíhal <josef.vybihal@gmail.com>
# Contributor: Polarian <polarian@polarian.dev>
# Contributor: Benjamin Denhartog <ben@sudoforge.com>
# Contributor: Mansour Behabadi <mansour@oxplot.com>
# Contributor: Troy Engel <troyengel+arch@gmail.com>
# Contributor: Geoff Hill <geoff@geoffhill.org>
# Contributor: Sebastien Bariteau <numkem@numkem.org>
# Contributor: Justin Dray <justin@dray.be>

# Release Notes: https://cloud.google.com/sdk/docs/release-notes

#  shellcheck disable=SC2034
# Cloud Storage Bucket: https://console.cloud.google.com/storage/browser/cloud-sdk-release/for_packagers/linux
# deb pool: 
#  - https://packages.cloud.google.com/apt/dists/cloud-sdk/main/binary-amd64/Packages
#  - https://packages.cloud.google.com/apt/pool/google-cloud-cli_455.0.0-0_all_568366af2c266f73f44b302536eb2b7e143d67d783aaf0f89452dbd8ca805410.deb
_extractedName="google-cloud-sdk"
pkgname="google-cloud-cli"
pkgver=508.0.0
pkgrel=1
pkgdesc="A set of command-line tools for the Google Cloud Platform. Includes gcloud (with beta and alpha commands), gsutil, and bq."
url="https://cloud.google.com/cli/"
license=('Apache-2.0')
arch=('x86_64')
depends=('python')

optdepends=(
  "python-crcmod: [gsutil] verify the integrity of GCS object contents"
)
options=('!strip' 'staticlibs' !zipman)

_use_pyupgrade=0

if [ $_use_pyupgrade -eq 1 ]; then
  makedepends=('pyupgrade')
fi


# TODO:
#  - cleanup of package content
#  - maybe use .deb as source? (already compressed manpages)
#  - aarch64 as separate source
#  - packages for components
source=(
  "$pkgname-$pkgver.orig.tar.gz::https://dl.google.com/dl/cloudsdk/release/downloads/for_packagers/linux/${pkgname}_${pkgver}.orig_amd64.tar.gz"
  "google-cloud-cli.sh"
  "0003-add-compdef-to-zsh-completion.patch"
)
# Conflict the old package name to force migration
conflicts=('google-cloud-sdk')
provides=('google-cloud-sdk')
replaces=('google-cloud-sdk')
sha256sums=('e0a923d5114cc650ec069cef686c0e8503bacdeb577a2e24abe9083be9aa451e'
            '5d9ca924675b24fc1ed044cf52f9f218e72ddc12703770271b0417a4a3c3a15d'
            'c19dbe916e6fd18d9b17b3309ee60c5d389035c5520822d2c14c045d8b853924')

prepare() {
  cd "${_extractedName}"

  for f in "${source[@]}"; do
    [[ "$f" =~ \.patch$ ]] && \
    ( \
      patch -p1 -i "${srcdir}/${f}" > /dev/null 2>&1 ||\
      ( \
        echo "failed to apply patch: $(basename ${f})" && \
        exit 1 \
      ) \
    )
  done

  if [ $_use_pyupgrade -eq 1 ]; then
    echo "Running pyupgrade, it will take some time..."
    find . -name "*.py" -type f -exec pyupgrade {} + >/dev/null
  fi
}

package() {
  mkdir "${pkgdir}/opt"
  cp -r "${_extractedName}" "${pkgdir}/opt/$pkgname"

  # The Google code uses a _TraceAction() method which spams the screen even
  # in "quiet" mode, we're throwing away output on purpose to keep it clean
  #  ref: lib/googlecloudsdk/core/platforms_install.py
  "${pkgdir}/opt/${pkgname}/install.sh" \
    --quiet \
    --usage-reporting false \
    --path-update false \
    --bash-completion false \
    > /dev/null

  find $pkgdir -name '__pycache__' -type d -exec rm -rf {} +

  install -D -m 0755 "${srcdir}/${source[1]}" \
    "${pkgdir}/etc/profile.d/google-cloud-cli.sh"

  install -d -m 0755 \
    "${pkgdir}/etc/bash_completion.d" \
    "${pkgdir}/usr/share/zsh/site-functions" \

  ln -rsT "${pkgdir}/opt/${pkgname}/completion.bash.inc" \
    "${pkgdir}/etc/bash_completion.d/google-cloud-cli"

  for cmd in gcloud gsutil bq; do
    ln -rsT "${pkgdir}/opt/${pkgname}/completion.zsh.inc" \
      "${pkgdir}/usr/share/zsh/site-functions/_${cmd}"
  done

  mkdir -p "${pkgdir}/usr/share"
  mv -f "${pkgdir}/opt/${pkgname}/help/man" "${pkgdir}/usr/share/"
}
