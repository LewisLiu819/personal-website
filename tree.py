import os

def generate_tree(folder_path, prefix=""):
    lines = []
    items = os.listdir(folder_path)
    for index, item in enumerate(items):
        is_last = index == len(items) - 1
        lines.append(f"{prefix}{'└── ' if is_last else '├── '}{item}")
        item_path = os.path.join(folder_path, item)
        if os.path.isdir(item_path):
            new_prefix = f"{prefix}{'    ' if is_last else '│   '}"
            lines.extend(generate_tree(item_path, new_prefix))
    return lines

folder_path = r"C:\Users\Windows11\OneDrive\Desktop\Personal Website\personal-website"
output_file = r"C:\Users\Windows11\OneDrive\Desktop\output.txt"

with open(output_file, 'w', encoding='utf-8') as f:
    f.write("\n".join(generate_tree(folder_path)))
