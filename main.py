from ota_update.ota import OTAUpdater


def download_and_install_update_if_available():
     o = OTAUpdater('https://github.com/jfmthor/WS32') 
     o.download_and_install_update_if_available('Boyz', '27854112Ca')


def start():
     print("Nada que actualizarpor ahora")

def boot():
     download_and_install_update_if_available()
     start()

boot()
