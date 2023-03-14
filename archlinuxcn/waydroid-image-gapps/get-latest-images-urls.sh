#!/bin/zsh
curl 'https://sourceforge.net/projects/waydroid/rss?path=/images' -o file-list.rss
echo "Latest x86_64 GAPPS:"
grep link file-list.rss | grep -- 'GAPPS-waydroid_x86_64-system.zip' | sed 's/<[^>]*>//g' | sed -E 's/\/download//' | sed -E 's/\s+//g' | head -1 | grep --color -E '[0-9]{8}'
echo "Latest x86_64 vendor:"
grep link file-list.rss | grep -- 'MAINLINE-waydroid_x86_64-vendor.zip' | sed 's/<[^>]*>//g' | sed -E 's/\/download//' | sed -E 's/\s+//g' | head -1 | grep --color -E '[0-9]{8}'
echo

echo "Latest x86 GAPPS:"
grep link file-list.rss | grep -- 'GAPPS-waydroid_x86-system.zip' | sed 's/<[^>]*>//g' | sed -E 's/\/download//' | sed -E 's/\s+//g' | head -1 | grep --color -E '[0-9]{8}'
echo "Latest x86 vendor:"
grep link file-list.rss | grep -- 'MAINLINE-waydroid_x86-vendor.zip' | sed 's/<[^>]*>//g' | sed -E 's/\/download//' | sed -E 's/\s+//g' | head -1 | grep --color -E '[0-9]{8}'
echo

echo "Latest arm64 GAPPS:"
grep link file-list.rss | grep -- 'GAPPS-waydroid_arm64-system.zip' | sed 's/<[^>]*>//g' | sed -E 's/\/download//' | sed -E 's/\s+//g' | head -1 | grep --color -E '[0-9]{8}'
echo "Latest arm64 vendor:"
grep link file-list.rss | grep -- 'MAINLINE-waydroid_arm64-vendor.zip' | sed 's/<[^>]*>//g' | sed -E 's/\/download//' | sed -E 's/\s+//g' | head -1 | grep --color -E '[0-9]{8}'
echo

echo "Latest arm GAPPS:"
grep link file-list.rss | grep -- 'GAPPS-waydroid_arm-system.zip' | sed 's/<[^>]*>//g' | sed -E 's/\/download//' | sed -E 's/\s+//g' | head -1 | grep --color -E '[0-9]{8}'
echo "Latest arm vendor:"
grep link file-list.rss | grep -- 'MAINLINE-waydroid_arm-vendor.zip' | sed 's/<[^>]*>//g' | sed -E 's/\/download//' | sed -E 's/\s+//g' | head -1 | grep --color -E '[0-9]{8}'

#cleanup
#rm file-list.rss

# perhaps fix in future so we change date in PKGBUILD and then do
# updpkgsums (util found in pacman-contrib so the checksums is updated)
