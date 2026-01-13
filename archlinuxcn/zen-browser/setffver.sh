source ./PKGBUILD || {
  echo "Failed to source PKGBUILD"
  exit 1
}

_firefox_version=$(
  curl -fsSL "https://raw.githubusercontent.com/zen-browser/desktop/refs/tags/${_zen_version}/surfer.json" |
    jq -er '.version.version'
) || {
  echo "Failed to fetch or parse surfer.json for tag ${_zen_version}"
  exit 1
}

sed -i "s/^_firefox_version=.*/_firefox_version=${_firefox_version}/" PKGBUILD ||
  {
    echo "Failed to update _firefox_version in PKGBUILD"
    exit 1
  }
