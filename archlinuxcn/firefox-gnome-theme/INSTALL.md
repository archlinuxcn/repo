## Manual installation from a system installed package

1. Go to `about:support` in Firefox.

2. Application Basics > Profile Directory > Open Directory.

3. Open directory in a terminal.

4. Create a `chrome` directory if it doesn't exist:

   ```sh
   mkdir chrome
   cd chrome
   ```

5. create a symlink to the actual theme location:

   ```sh
   ln -s /usr/lib/firefox-gnome-theme firefox-gnome-theme
   ```

6. Create single-line user CSS files if non-existent or empty (at least one line is needed for `sed`):

   ```sh
   [[ -s userChrome.css ]] || echo >> userChrome.css
   [[ -s userContent.css ]] || echo >> userContent.css
   ```

7. Import this theme at the beginning of the CSS files (all `@import`s must come before any existing `@namespace` declarations):

   ```sh
   sed -i '1s/^/@import "firefox-gnome-theme\/userChrome.css";\n/' userChrome.css
   sed -i '1s/^/@import "firefox-gnome-theme\/userContent.css";\n/' userContent.css
   ```

8. Symlink preferences file:

   ```sh
   cd .. # Go back to the profile directory
   ln -fs chrome/firefox-gnome-theme/configuration/user.js user.js
   ```

9. Restart Firefox.

10. Open Firefox customization panel and move the new tab button to headerbar.

Done. See README.md for more details.
