import logging
import subprocess
import shutil
from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction

logger = logging.getLogger(__name__)

class GnomeSettings(Extension):
  def __init__(self):
    logger.info('Loading Gnome Settings Extension')
    super(GnomeSettings, self).__init__()
    self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())

class KeywordQueryEventListener(EventListener):
  def on_event(self, event, extension):
    keyword = event.get_keyword()

    # Find the keyword id using the keyword (since the keyword can be changed by users)
    for setting, kw in extension.preferences.items():
      if kw == keyword:
        subprocess.Popen(['gnome-control-center', setting])
        return HideWindowAction()

if not shutil.which('gnome-control-center'):
  logger.error('gnome-control-center not found')
elif __name__ == '__main__':
  GnomeSettings().run()
