from setuptools import setup, find_packages

setup(
    name="estat-python-adapter",
    version="0.1.0",
    description="e-Statのデータを取得するための非公式Pythonライブラリ",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Zaiwa-linus",
    url="https://github.com/Zaiwa-linus/estat_python_adapter",
    packages=find_packages(),
    install_requires=[
        "requests",
        "pandas",
    ],
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
) 