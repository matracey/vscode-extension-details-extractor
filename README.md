# VSCode Extension Details Extractor

This is a Python script that extracts the short description of one or more Visual Studio Code extensions.

## Introduction

If you're a Visual Studio Code user, you might be interested in learning more about the extensions that are available for the editor. This script makes it easy to extract the short description of one or more extensions, which can be useful for a variety of purposes.

## How it works

The script uses the `requests` and `beautifulsoup4` libraries to scrape the marketplace page for each extension and extract the short description. It then prints the short description to the console.

## Installation

To install `vscode-extension-details-extractor`, you can use `pip`:

```shell
pip install vscode-extension-details-extractor
```

## Usage

To use the script without installing from `pip`, you'll need to have Python 3.x installed, as well as the `requests` and `beautifulsoup4` libraries. Here's how to get started:

1. Clone this repository or download the `vscode_extension_details_extractor.py` file.
2. Install the required libraries by running `pip install -r requirements.txt`.
3. Run the script using the following command:

```shell
python vscode_extension_details_extractor.py EXTENSION_ID [EXTENSION_ID ...]
```

Replace `<extension_id>` with the ID of the extension you want to extract the short description for. You can specify multiple extension IDs separated by spaces.

## Examples

Here are some examples of how the script can be used:

- Extract the short description of the `ms-python.python` extension:

    ```shell
    python vscode_extension_details_extractor.py ms-python.python
    ```

- Extract the short description of the `ms-python.python` and `ms-vscode.cpptools` extensions:

    ```shell
    python vscode_extension_details_extractor.py ms-python.python ms-vscode.cpptools
    ```

## Contributing

If you find a bug or have a feature request, please [open an issue](https://github.com/matracey/vscode-extension-details-extractor/issues/new).

If you want to contribute to the project, please follow the [contributing guidelines](CONTRIBUTING.md).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Additional Files

This repository also includes the following files:

### GitHub

- [`.github/ISSUE_TEMPLATE.md`](./.github/ISSUE_TEMPLATE.md): A template for creating new issues on GitHub.
- [`.github/PULL_REQUEST_TEMPLATE.md`](./.github/PULL_REQUEST_TEMPLATE.md): A template for creating new pull requests on GitHub.
- [`.github/workflows/python-ci.yml`](./.github/workflows/python-ci.yml): A GitHub Actions workflow for running automated tests on the code.

### Sphinx

- [`conf.py`](./conf.py): A configuration file for Sphinx, a documentation generator.
- [`index.rst`](./index.rst): The main documentation file for the project.
- [`make.bat`](./make.bat): A batch file for building the documentation using Sphinx on Windows.
- [`Makefile`](./Makefile): A makefile for building the documentation using Sphinx on Unix-based systems.

### Python Packaging

- [`requirements.txt`](./requirements.txt): A file that specifies the required Python packages and their versions.
- [`setup.py`](./setup.py): A file for packaging the script as a Python package.

### Visual Studio Code

- [`.editorconfig`](./.editorconfig): A configuration file for defining and maintaining consistent coding styles between different editors and IDEs.
- [`.gitignore`](./.gitignore): A file that specifies which files and directories should be ignored by Git.
- [`vscode_extension_details_extractor.py`](./vscode_extension_details_extractor.py): The main Python script for extracting extension details.
- [`.vscode/launch.json`](./.vscode/launch.json): A configuration file for launching the script in Visual Studio Code.
- [`.vscode/settings.json`](./.vscode/settings.json): A configuration file for Visual Studio Code settings.

## Limitations

The script relies on web scraping, which can be fragile and may break if the marketplace page for an extension changes. Additionally, the script only extracts the short description of an extension, so if you need more detailed information, you'll need to look elsewhere.

## Related resources

Here are some related resources that you might find useful:

- [Visual Studio Code Marketplace](https://marketplace.visualstudio.com/): The official marketplace for Visual Studio Code extensions.
- [VSCode Extension API](https://code.visualstudio.com/api): The official documentation for the Visual Studio Code extension API.
