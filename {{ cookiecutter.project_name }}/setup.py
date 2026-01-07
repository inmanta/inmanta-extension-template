from setuptools import setup, find_packages

requires = [
    "inmanta-core>=7.2.0.dev",
]

namespace_packages = ["inmanta_ext.{{ cookiecutter.extension_name }}"]

setup(
    version="{{ cookiecutter.extension_version }}",
    python_requires=">={{ cookiecutter.minimum_python_version }}",  # also update classifiers
    # Meta data
    name="{{ cookiecutter.project_name }}",
    description="{{ cookiecutter.project_description }}",
    author="{{ cookiecutter.author }}",
    author_email="{{ cookiecutter.author_email }}",
    url="{{ cookiecutter.git_repo_url }}",
    license="{{ cookiecutter.license }}",
    project_urls={
        "Bug Tracker": "{{ cookiecutter.git_repo_url }}/issues",
    },
    # Packaging
    package_dir={"": "src"},
    packages= namespace_packages + find_packages("src"),
    package_data={"": []},
    include_package_data=True,
    install_requires=requires,
    entry_points={
    },
    extras_require={
        "dev": [
            "inmanta-core[pytest-inmanta-extensions]",
            "inmanta-dev-dependencies[pytest,async,extension]",
            "bumpversion",
        ],
    },
)
