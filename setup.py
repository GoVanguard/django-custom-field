from setuptools import setup, find_packages

setup(
    name = "django-custom-field",
    version = "2.9",
    author = "David Burke",
    author_email = "wward@warddevelopment.com",
    description = ("End user custom fields for Django including contrib.admin support"),
    license = "MIT",
    keywords = "django admin",
    url = "http://github.com/willseward/django-custom-field",
    packages=find_packages(),
    include_package_data=True,
    install_requires = ['django'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        'Environment :: Web Environment',
        'Framework :: Django',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.8',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        "License :: OSI Approved :: MIT License",
    ],
)
