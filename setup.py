from setuptools import setup

def readme():
	with open('README.rst') as f:
		return f.read()

setup(name='tubafcd',
      version='0.2.1',
      description='TU Bergakademie Freiberg Corporate Desing functions',
      long_description=readme(),
      author='Sven Jachalke',
      author_email='sven.jachalke@physik.tu-freiberg.de',
	  url='ssh://git@sj-home.ddns.net:/home/git/tubafcd.git',
      license='CC',
      packages=['tubafcd'],
	  install_requires=[
	  	'matplotlib',
	  ],
	  include_package_data=True,
      zip_safe=False)