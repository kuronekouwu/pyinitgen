"""Install packages as defined in this file into the Python environment."""
import setuptools

setuptools.setup(
	name="pyinitgen",
	version='0.0.1',
	author="M-307",
	author_email="me@m307.dev",
	description="A python __init__ generator",
	packages=setuptools.find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	python_requires=">=3.6",
	include_package_data=True
)