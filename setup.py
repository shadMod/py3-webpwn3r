import setuptools

__version__ = "0.0.5"

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="py3-webpwn3r",
    version=__version__,
    author="shadMod",
    author_email="support@shadmod.it",
    description="Web Applications Security Scanner",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[
        "WebPwn3r",
    ],
    url="https://github.com/shadMod/py3-webpwn3r/",
    download_url=f"https://github.com/shadMod/py3-webpwn3r/archive/refs/tags/{__version__}.tar.gz",
    project_urls={
        "GitHub": "https://github.com/shadMod/py3-webpwn3r/",
        "Bug Tracker": "https://github.com/shadMod/py3-webpwn3r/issues/",
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    packages=["py3_webpwn3r", "py3_webpwn3r.core"],
    python_requires=">=3.10",
)
