
def import_or_install(package):
    try:
        __import__(package)
    except ImportError:
        import pip
        pip.main(['install', package])


import_or_install('pandas')
import_or_install('numpy')

