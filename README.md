# ulauncher-gnome-settings

[Ulauncher](https://ulauncher.io) extension for accessing Gnome settings directly as if they were apps.

This extension is using experimental techniques to make Ulauncher keywords look and behave like apps. This comes with a couple of minor caveats but as of writing this, it works fine.

## How it works (primarily for extension developers)

Ulauncher's extension API is intended for keywords and arguments, not simple application shortcuts (at least not yet). In order to avoid the extra step of a keyword + argument, each Gnome Control Center panel is added as a keyword. Keywords are primarily meant to be typed, not searched. To avoid this, the keyword is the same as the full name shown in search (unless you override the settings). Ulauncher doesn't allow spaces in keywords, so instead another blank utf-8 character is used (which also can't be typed with a keyboard). As a result the keyword completion will show the application name briefly before closing ulauncher and opening the panel. This doesn't look too strange so you may not even think about it, but Ulauncher doesn't do this for apps.

Ulauncher sorts keywords above apps, and only shows a limited amount of results. This extension needed to add 24 keywords, most of them containing the word "Settings". This would make it impossible to find the ordinary "Settings" or other settings apps. In order to avoid this, a similar workaround as above was used: The "e" in settings is actually a Ukrainian "Ye" letter. It looks identical with my font (compare "e" vs "е"). Ulauncher's search will still match the letter E, but sort it after full matches.

## Alternatives

### ulauncher-gnome-control-center
[ulauncher-gnome-control-center](https://github.com/noam09/ulauncher-gnome-control-center) is very well written extension with internal logic for caching and sorting settings based on your use. It uses a "normal" ulauncher keyword however, so it has the extra step this extension was designed to avoid.

### Create or modify desktop entries
Ulauncher's app index is built from [desktop entries](https://specifications.freedesktop.org/desktop-entry-spec/desktop-entry-spec-latest.html).
gnome-control-center creates these, but specify that they shouldn't turn up in launchers and application menus. You can override this:

```sh
# Ulauncher will look for .desktop-files in ~/.local/share/
UAPP_DIR=~/.local/share/ulauncher-apps
# Assure user home dir for desktop entries
mkdir -p $UAPP_DIR
# Copy disabled gnome-control-center desktop entries to user home dir
cp -f /usr/share/applications/gnome-*-panel.desktop $UAPP_DIR
# Enable them (or more strictly disable "NoDisplay")
sed -i '/NoDisplay=true/s/^/#/' $UAPP_DIR/gnome-*-panel.desktop
```

Note that your new desktop entries could be read by other applications.

### Modify Ulauncher (not recommended)
You can change [Ulauncher's filter](https://github.com/Ulauncher/Ulauncher/blob/3c39799b119abf485fba07f8c80b4f79526e5fca/ulauncher/util/desktop/reader.py#L40) to override `app.get_nodisplay()` if `app.get_executable() == 'gnome-control-center'`.

Note that local modifications will be removed when you upgrade ulauncher.

## Credits
* noam09 for [the original extension](https://github.com/noam09/ulauncher-gnome-control-center) (this one started off as [an attempted PR](https://github.com/noam09/ulauncher-gnome-control-center/issues/2)).
* The icon is from the [Numix project](https://github.com/numixproject).
