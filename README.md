# ulauncher-gnome-settings

[Ulauncher](https://ulauncher.io) extension for accessing Gnome settings (Gnome Control Center panels) directly as if they were apps.


![](settings-animation.gif)


This extension is using experimental techniques to make Ulauncher keywords look and behave like apps. This comes with a couple of minor caveats but as of writing this, it works fine.

## How it works (primarily for extension developers)

Ulauncher's extension API is intended for adding keywords with arguments, like "`decode` \&amp;" or "`npm` lodash". Extensions registers these keywords in their manifests. Keywords have the properties `name` and `default_value`. The `name` is searchable. For example, the extension "Process Killer" (if you have it) will show up in the result list if you type "proc.." or "ki..". If you press enter or alt + number it will convert your input to "kill ". "kill" is the `default_value` and the space character after is needed to triggers the extension.

Since this behavior is not needed or wanted for apps, this extension uses a `default_value` that looks like the `name` but with an untypable blank character instead of space.

1. Converting your search input to `default_value` + space can't be disabled, but converting it to the same name as displayed in the search result list at least makes some sense and looks a lot less hacky. This requires the `default_value` to be the same as the `name`, but since space is used to separate the keyword and argument(s), using the actual space character in keywords doesn't work.
2. Launching an application by typing the `default_value` followed by a space is not how applications behave in Ulauncher, and is unwanted and unintuitive (for applications). Making the keywords untypable prevents this.

As a result, the keyword's name (usually the settings panel name followed by " Settings") will show (followed by a space character) briefly before closing Ulauncher and opening the panel. This doesn't look too strange, so you may not even think about it (see the gif).

Additionally, a similar "hack" is used to control the order of the search results. The "e" in "Settings" is actually a Ukrainian "Ye" letter. It looks identical with my font (compare "e" vs "е"). This was needed because Ulauncher normally shows keywords above apps, and only shows a limited amount of results. This extension adds 20 keywords containing the word "Settings". This would make it impossible to find the ordinary "Settings" application or anything else by typing in "settings". Ulauncher's search is rather forgiving so the slight mismatch won't have a big impact on the results, but will affect the sort order. The highligting doesn't seem to distinguish between "e" or "е" so that works too.

Users can override keywords in Ulauncher's preferences (hence the "default" in `default_value`). If you do this, this extension will not work as intended, but you may want to delete keywords completely if you don't want a specific panel to appear in search.

## Alternatives

### ulauncher-gnome-control-center
[ulauncher-gnome-control-center](https://github.com/noam09/ulauncher-gnome-control-center) is very well written extension with internal logic for caching and sorting settings based on your use. It uses a "normal" ulauncher keyword however, so it has the extra step this extension was designed to avoid.

### Create or modify desktop entries
Ulauncher's app index is built from [desktop entries](https://specifications.freedesktop.org/desktop-entry-spec/desktop-entry-spec-latest.html).
gnome-control-center creates these, but specify that they shouldn't display in application menus and launchers. You can override this:

```sh
# Ulauncher will look for .desktop-files in ~/.local/share/
UAPP_DIR=~/.local/share/applications
# Assure user home dir for desktop entries
mkdir -p $UAPP_DIR
# Copy disabled gnome-control-center desktop entries to user home dir
cp -f /usr/share/applications/gnome-*-panel.desktop $UAPP_DIR
# Enable them (or more strictly disable "NoDisplay")
sed -i '/NoDisplay=true/s/^/#/' $UAPP_DIR/gnome-*-panel.desktop
```

Note that this will likely cause duplicate entries to appear for other launcher apps which makes exceptions for these, such as Gnome's "Show All Applications" (Super+A).

### Modify Ulauncher (not recommended)
You can change [Ulauncher's filter](https://github.com/Ulauncher/Ulauncher/blob/3c39799b119abf485fba07f8c80b4f79526e5fca/ulauncher/util/desktop/reader.py#L40) to override `app.get_nodisplay()` if `app.get_executable() == 'gnome-control-center'`.

Note that local modifications will be removed when you upgrade ulauncher.

## Credits
* noam09 for [the original extension](https://github.com/noam09/ulauncher-gnome-control-center) (this extension started off as [a suggestion](https://github.com/noam09/ulauncher-gnome-control-center/issues/2)).
* The icon is from the [Numix project](https://github.com/numixproject).
