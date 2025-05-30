import os

# Folders and file types to skip
EXCLUDE_DIRS = {'__pycache__', '.git', '.vscode', 'venv', 'env', 'Lib', 'Scripts', 'dist', 'build'}
EXCLUDE_EXTENSIONS = {'.pyc', '.pyo', '.log'}

def print_directory_tree(start_path, indent='', max_files=10):
    try:
        items = sorted(
            [item for item in os.listdir(start_path) if not item.startswith('.')]
        )
    except PermissionError:
        print(f"{indent}🚫 Permission Denied: {start_path}")
        return

    folders = [item for item in items if os.path.isdir(os.path.join(start_path, item)) and item not in EXCLUDE_DIRS]
    files = [
        item for item in items
        if os.path.isfile(os.path.join(start_path, item)) and
        not os.path.splitext(item)[1] in EXCLUDE_EXTENSIONS
    ]

    for folder in folders:
        print(f"{indent}📁 {folder}")
        print_directory_tree(os.path.join(start_path, folder), indent + '    ', max_files)

    files_to_show = files[:max_files]
    for file in files_to_show:
        print(f"{indent}📄 {file}")
    
    if len(files) > max_files:
        print(f"{indent}...and {len(files) - max_files} more files")

# Set your main project folder path here
project_path = r"D:\Vehical type detection and speed estimation"

print(f"\n🟢 Project structure for: {project_path}\n")
print_directory_tree(project_path, max_files=10)
