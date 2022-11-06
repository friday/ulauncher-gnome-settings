import logging
import subprocess
import shutil
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction
from ulauncher.api import Extension

logger = logging.getLogger(__name__)

class GnomeSettings(Extension):
    def on_launch(self, trigger_id):
        subprocess.Popen(['gnome-control-center', trigger_id])
        return HideWindowAction()

if not shutil.which('gnome-control-center'):
    logger.error('gnome-control-center not found')
elif __name__ == '__main__':
    GnomeSettings().run()
