#!/usr/bin/env python3
"""
Generate project structure from YAML configuration file.
Enhanced version with file content support and project variables.
"""

import os
import sys
import yaml
import argparse
from datetime import datetime

def create_structure_from_yaml(yaml_file, output_dir=None, project_name=None):
    """Create project structure from YAML configuration."""
    try:
        with open(yaml_file, 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)
    except FileNotFoundError:
        print(f"Error: Configuration file '{yaml_file}' not found.")
        sys.exit(1)
    except yaml.YAMLError as e:
        print(f"Error parsing YAML file: {e}")
        sys.exit(1)
    
    # Get project info
    project_info = config.get('project_info', {})
    if not project_name:
        project_name = project_info.get('name', 'project')
    
    # Determine root directory
    if not output_dir:
        root_dir = project_name.lower().replace(' ', '-')
    else:
        root_dir = output_dir
    
    print(f"Generating project: {project_name}")
    print(f"Output directory: {root_dir}")
    
    # Create root directory
    os.makedirs(root_dir, exist_ok=True)
    print(f"Created root directory: {root_dir}")
    
    # Create directories
    print("\nCreating directories...")
    for directory in config.get('directories', []):
        path = os.path.join(root_dir, directory)
        os.makedirs(path, exist_ok=True)
        print(f"Created directory: {directory}")
    
    # Create files
    print("\nCreating files...")
    file_contents = config.get('file_contents', {})
    
    for file_path in config.get('files', []):
        # Skip files with extensions in the skip_extensions list
        if any(file_path.endswith(ext) for ext in config.get('skip_extensions', [])):
            print(f"Skipping asset file: {file_path}")
            continue
        
        full_path = os.path.join(root_dir, file_path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        
        # Create file with content if available, otherwise create empty file
        with open(full_path, 'w', encoding='utf-8') as f:
            if file_path in file_contents:
                content = file_contents[file_path]
                # Replace project variables
                content = content.replace('PROJECT_NAME', project_name)
                content = content.replace('CURRENT_YEAR', str(datetime.now().year))
                f.write(content)
                print(f"Created file with content: {file_path}")
            else:
                print(f"Created empty file: {file_path}")
    
    print(f"\nProject structure created successfully at: {root_dir}")
    print(f"You can now start working on your {project_name} project!")

def main():
    parser = argparse.ArgumentParser(description='Generate project structure from YAML configuration.')
    parser.add_argument('yaml_file', nargs='?', default='project_template.yaml', 
                        help='Path to YAML configuration file (default: project_template.yaml)')
    parser.add_argument('-o', '--output', help='Output directory name')
    parser.add_argument('-n', '--name', help='Project name (overrides the name in YAML file)')
    
    args = parser.parse_args()
    
    create_structure_from_yaml(args.yaml_file, args.output, args.name)

if __name__ == "__main__":
    main()