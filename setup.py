from setuptools import setup

def readme():
	with open('README.rst') as f:
		return f.read()

setup(name='tubafcdpy',
      version='0.2.4',
      description='TU Bergakademie Freiberg Corporate Desing functions for python',
      long_description=readme(),
      author='Sven Jachalke',
      author_email='sven.jachalke@physik.tu-freiberg.de',
	  url='ssh://git@sj-home.ddns.net:/home/git/tubafcd.git',
      license='CC',
      packages=['tubafcdpy'],
	  install_requires=[
	  	'matplotlib',
	  ],
	  include_package_data=True,
      zip_safe=False)