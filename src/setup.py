from setuptools import setup
import setup_translate

pkg = 'Extensions.ardmediathek'
setup(name='enigma2-plugin-extensions-ardmediathek',
       version='3.0',
       description='Zugriff auf die ARD-Mediathek',
       package_dir={pkg: 'ardmediathek'},
       packages=[pkg],
       package_data={pkg: ['images/*.png', '*.png', '*.xml', 'locale/*/LC_MESSAGES/*.mo', 'logo.png', 'maintainer.info', 'keymap.xml', 'skin_FHD.xml', 'skin_HD.xml', 'img/*.png']},
       cmdclass=setup_translate.cmdclass,  # for translation
      )
