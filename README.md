# ulauncher-gnome-settings

[Ulauncher](https://ulauncher.io) extension for accessing Gnome settings directly as if they were apps.

This extension is using an experimental way to make Ulauncher keywords behave like apps. This works, but comes with a couple of caveats. If you want to avoid that and is fine with using a wrapper keyword, then [ulauncher-gnome-control-center](https://github.com/noam09/ulauncher-gnome-control-center) is recommended instead.

## Caveats

* While opening, the user input will be replaced with the setting name for a very brief moment before the setting is opened. This looks quite intentional and snappy. You may not even notice it, but Ulauncher doesn't do this for apps. These are actually extension keywords. Keywords can't contain spaces, so these are using a similar looking blank character.
* Ulauncher sorts keywords above apps, and only shows 9 results. This extension needed to add 25 keywords, almost all contains the word "Settings". This would make it impossible to find the ordinary "Settings" or other settings apps. In order to avoid this, a similar workaround as above was used: The "e" in settings is actually a Ukrainian "Ye" letter. It looks identical at least with my font (let me know if this is not the case for you), and due to Ulaunchers fault tolerant search it will still match the letter E.

The icon is from the [Numix project](https://github.com/numixproject).
