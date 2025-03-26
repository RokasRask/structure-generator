# Project Structure Generator

A simple and flexible Python tool to generate project structures from YAML configuration files. This tool allows you to quickly create consistent directory and file structures for your projects without the tedious manual work.

## Features

- Generate entire project structures from a single YAML file
- Create empty files and directories in one command
- Skip asset files (images, fonts, etc.) automatically
- Include default content for common files like package.json, README.md
- Replace variables in template files (project name, year, etc.)
- Support for multiple project templates

## Requirements

- Python 3.6 or higher
- PyYAML package

## Installation

1. Make sure you have Python installed on your system.

2. Install the PyYAML package:

   ```bash
   pip install pyyaml
   ```

3. Download the project files:
   - `generate_project.py` - The main script
   - `project_template.yaml` - The template file

4. Make the script executable (Linux/Mac):

   ```bash
   chmod +x generate_project.py
   ```

## Basic Usage

### Generate a project using the default template

```bash
python generate_project.py
```

This will create a new project using the default `project_template.yaml` file in the current directory.

### Generate a project with a custom name

```bash
python generate_project.py -n "My Awesome Project"
```

### Generate a project in a specific directory

```bash
python generate_project.py -o my-project-folder
```

### Use a custom template file

```bash
python generate_project.py custom_template.yaml
```

### Combine options

```bash
python generate_project.py custom_template.yaml -n "Custom Project" -o custom-output
```

## Command Line Options

| Option | Short | Description |
|--------|-------|-------------|
| `--name` | `-n` | Set the project name (overrides the name in YAML file) |
| `--output` | `-o` | Specify the output directory |
| `yaml_file` | - | Path to YAML template file (default: project_template.yaml) |

## Creating Custom Templates

The YAML template file has the following structure:

```yaml
project_info:
  name: "PROJECT_NAME"
  description: "Description of your project"
  author: "Your Name"
  version: "1.0.0"

directories:
  - public
  - src/components
  - src/pages
  # Add more directories as needed

files:
  - package.json
  - src/index.js
  - src/App.js
  # Add more files as needed

skip_extensions:
  - ".png"
  - ".jpg"
  # Add more extensions to skip

file_contents:
  "package.json": |
    {
      "name": "PROJECT_NAME",
      "version": "1.0.0"
    }
  # Add more file contents
```

### Template Variables

You can use the following variables in your file contents:

- `PROJECT_NAME` - Replaced with the project name
- `CURRENT_YEAR` - Replaced with the current year

### Creating Multiple Templates

You can create different templates for different types of projects:

1. Copy the `project_template.yaml` file
2. Rename it to something like `react-template.yaml` or `node-api-template.yaml`
3. Customize the directories, files, and content to match the project type
4. Use the template with the generator:

```bash
python generate_project.py react-template.yaml -n "My React App"
```

## Example Use Cases

### Creating a React Project

```bash
python generate_project.py react-template.yaml -n "My React App"
```

### Creating a Node.js API

```bash
python generate_project.py node-api-template.yaml -n "My API" -o api-project
```

### Creating a Static Website

```bash
python generate_project.py static-site-template.yaml -n "My Website"
```

## Troubleshooting

### Error: "No module named 'yaml'"

You need to install the PyYAML package:

```bash
pip install pyyaml
```

### Error: "Configuration file not found"

Make sure the YAML template file exists in the specified path.

### Files Not Being Created

Check if the file extensions are listed in the `skip_extensions` section of your template.

## License

This project is open source and available under the MIT License.

## Contributing

Feel free to fork this project and make improvements or customize it for your own needs.