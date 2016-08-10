from setuptools import setup

setup(
    name='pip-module-scanner',
    packages=['pip_module_scanner'],
    version='0.2',
    description='Scans your Python project for all installed third party pip libraries and generates a requirements.txt based output',
    author='Luke Paris (Paradoxis)',
    author_email='luke@paradoxis.nl',
    url='https://github.com/Paradoxis/Python-Third-Party-Module-Scanner',
    download_url='https://github.com/Paradoxis/Python-Third-Party-Module-Scanner/tarball/0.1',
    keywords=['scanning', 'requirements.txt', 'requirements'],
    classifiers=[],
    scripts=['pip-module-scanner'],
   entry_points = {
        'console_scripts': ['pip-module-scanner=pip_module_scanner.main:main'],
   }
)
