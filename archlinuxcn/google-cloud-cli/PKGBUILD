# Maintainer: Josef Vybíhal <josef.vybihal@gmail.com>
# Contributor: Polarian <polarian@polarian.dev>
# Contributor: Benjamin Denhartog <ben@sudoforge.com>
# Contributor: Mansour Behabadi <mansour@oxplot.com>
# Contributor: Troy Engel <troyengel+arch@gmail.com>
# Contributor: Geoff Hill <geoff@geoffhill.org>
# Contributor: Sebastien Bariteau <numkem@numkem.org>
# Contributor: Justin Dray <justin@dray.be>

#  shellcheck disable=SC2034

# Release Notes: https://cloud.google.com/sdk/docs/release-notes
# Cloud Storage Bucket: https://console.cloud.google.com/storage/browser/cloud-sdk-release/for_packagers/linux
# deb pool: 
#  - https://packages.cloud.google.com/apt/dists/cloud-sdk/main/binary-amd64/Packages
#  - https://packages.cloud.google.com/apt/pool/cloud-sdk/google-cloud-cli_516.0.0-0_amd64_e19fae4ce840c378a624e2cbdba2aa87.deb

_extractedName="google-cloud-sdk"
pkgname="google-cloud-cli"
pkgver=520.0.0
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

# Python 3.13 is not officialy supported yet, force use of bundled 3.12
export _force_budled_python=true

# TODO:
#  - packages for components
source=(
  "$pkgname-$pkgver.orig.tar.gz::https://dl.google.com/dl/cloudsdk/release/downloads/for_packagers/linux/${pkgname}_${pkgver}.orig_amd64.tar.gz"
  "$pkgname.sh"
  "$pkgname.install"
  "0003-add-compdef-to-zsh-completion.patch"
)

install=$pkgname.install

# Conflict the old package name to force migration
conflicts=('google-cloud-sdk')
provides=('google-cloud-sdk')
replaces=('google-cloud-sdk')

sha256sums=('8e467fe2a022e7ca2a54ce00368a6a7e7ad96f48b0a2724b48a869162a0ce400'
            '6e88b535c020b0f28c986fdb66918f8c07e4d337e813b77ec2068068f03457f8'
            'fdba342aecce102b85fd96f21205d7ee2f8043b4bb56cabf363375785e3d423c'
            'c19dbe916e6fd18d9b17b3309ee60c5d389035c5520822d2c14c045d8b853924')

backup=(etc/profile.d/google-cloud-cli.sh)

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
}

package() {
  _install_path="${pkgdir}/opt/${pkgname}"
  _bundled_py_bin="${_install_path:${#pkgdir}}/platform/bundledpythonunix/bin/python3"

  mkdir "${pkgdir}/opt"
  cp -r "${_extractedName}" "${_install_path}"

  # The Google code uses a _TraceAction() method which spams the screen even
  # in "quiet" mode, we're throwing away output on purpose to keep it clean
  #  ref: lib/googlecloudsdk/core/platforms_install.py
  "${_install_path}/install.sh" \
    --quiet \
    --usage-reporting false \
    --path-update false \
    --bash-completion false \
    > /dev/null 2>&1

  find $pkgdir -name '__pycache__' -type d -exec rm -rf {} +

  install -D -m 0755 "${srcdir}/${source[1]}" \
    "${pkgdir}/etc/profile.d/google-cloud-cli.sh"

  if [ "$_force_budled_python" = true ]; then
    { echo "export CLOUDSDK_PYTHON=${_bundled_py_bin}"
      echo "export CLOUDSDK_GSUTIL_PYTHON=${_bundled_py_bin}"
      echo "export CLOUDSDK_BQ_PYTHON=${_bundled_py_bin}"
    } >> "${pkgdir}/etc/profile.d/google-cloud-cli.sh"
  fi

  install -d -m 0755 \
    "${pkgdir}/etc/bash_completion.d" \
    "${pkgdir}/usr/share/zsh/site-functions" \

  ln -rsT "${_install_path}/completion.bash.inc" \
    "${pkgdir}/etc/bash_completion.d/google-cloud-cli"

  for cmd in gcloud gsutil bq; do
    ln -rsT "${_install_path}/completion.zsh.inc" \
      "${pkgdir}/usr/share/zsh/site-functions/_${cmd}"
  done

  mkdir -p "${pkgdir}/usr/bin"
  for bin in gcloud \
             gcloud-crc32c \
             gsutil \
             docker-credential-gcloud \
             git-credential-gcloud.sh \
             bq; do
    ln -rsT "${_install_path}/bin/${bin}" \
      "${pkgdir}/usr/bin/${bin}"
  done

  mkdir -p "${pkgdir}/usr/share"
  mv -f "${pkgdir}/opt/${pkgname}/help/man" "${pkgdir}/usr/share/"
}
