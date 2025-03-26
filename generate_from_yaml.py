#!/usr/bin/env python3
"""
Generate project structure from YAML configuration file.
Much simpler than parsing markdown!
"""

import os
import sys
import yaml

def create_structure_from_yaml(yaml_file, root_dir="gameforge-js"):
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
    for file_path in config.get('files', []):
        # Skip files with extensions in the skip_assets list
        if any(file_path.endswith(ext.replace('*', '')) for ext in config.get('skip_assets', [])):
            print(f"Skipping asset file: {file_path}")
            continue
            
        full_path = os.path.join(root_dir, file_path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        
        # Create empty file
        open(full_path, 'a').close()
        print(f"Created file: {file_path}")
    
    print(f"\nProject structure created successfully at: {root_dir}")

if __name__ == "__main__":
    yaml_file = "structure.yaml"
    if len(sys.argv) > 1:
        yaml_file = sys.argv[1]
    
    create_structure_from_yaml(yaml_file)