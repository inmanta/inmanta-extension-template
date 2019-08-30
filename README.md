# Inmanta extension template

A cookiecutter template to create a new Inmanta extension.

# Install dependencies

```bash
pip install cookiecutter
```

# Usage

```bash
cookiecutter https://github.com/inmanta/inmanta-extension-template.git
```

This command will prompt for the template parameters.

### Parameters

| Template parameters    | Default value                                            | Description                                                        |
|------------------------|----------------------------------------------------------|--------------------------------------------------------------------|
| project_name           | project                                                  | The name of the root directory of the new Inmanta extension.       |
| project_description    |                                                          | A description of the new Inmanta extension.                        |
| author                 | Inmanta                                                  | The author to be mentioned in the setup.py file                    |
| author_email           | code@inmanta.com                                         | The e-mail address of the author.                                  |
| license                | ASL 2.0                                                  | The License of this new Inmanta extension.                         |
| copyright              | ${year} Inmanta                                          | The owner of the copyright of the extension.                       |
| git_repo_url           | https://github.com/inmanta/{{cookiecutter.project_name}} | The URL to the Git repository where this extension will be stored. |
| minimum_python_version | 3.6                                                      | The minimum Python version required to run this extension.         |
| extension_name         | extension_name                                           | The name of the Inmanta extension.                                 |
| extension_version      | 1.0                                                      | The version of this extension.                                     |
| slice_name             | slice_name                                               | The name of the first server slice of this extension.              |
| slice_class_name       | SliceName                                                | The name of the class implementing the first server slice.         |
| slice_package_name     | slices                                                   | The Python package that will host the first server slice.          |