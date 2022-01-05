import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="grafana-dashboard-templater",
    version="1.0.0",
    author="Pascal Zimmermann",
    author_email="info@theiotstudio.com",
    description="A Grafana dashboard templater",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ZPascal/grafana_dashboard_templater",
    project_urls={
        "Bug Tracker": "https://github.com/ZPascal/grafana_dashboard_templater/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=["jinja2"],
    python_requires=">=3.6",
)
