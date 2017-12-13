from setuptools import setup

def readme():
	with open('README.rst') as f:
		return f.read()

setup(name='tubafcdpy',
      version='0.2.5',
      description='TU Bergakademie Freiberg Corporate Design functions and colors for python/matplotlib',
      long_description=readme(),
      author='Sven Jachalke',
      author_email='sven.jachalke@gmail.com',
	  url='ssh://git@sj-home.ddns.net:/home/git/tubafcd.git',
      license='CC',
      packages=['tubafcdpy'],
	install_requires=[
	  	'matplotlib',
	  ],
	include_package_data=True,
      zip_safe=False)