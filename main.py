import logging
import subprocess
import distutils.spawn
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
    subprocess.Popen(['gnome-control-center', event.get_keyword_id()])
    return HideWindowAction()

if not distutils.spawn.find_executable('gnome-control-center'):
  logger.error('gnome-control-center not found')
elif __name__ == '__main__':
  GnomeSettings().run()
