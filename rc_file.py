import os

# Define the directory containing the icons
icon_dir = "ico"
rc_filename = "Folder11Icons.rc"

# Ensure the directory exists
if not os.path.isdir(icon_dir):
    print(f"Error: Directory '{icon_dir}' not found.")
    exit(1)

# Open the .rc file for writing
with open(rc_filename, "w", encoding="utf-8") as rc_file:
    rc_file.write("// Resource script for Folder11 icons\n")
    rc_file.write("// Auto-generated\n\n")
    
    # Enumerate all .ico files in the directory
    for index, icon in enumerate(sorted(os.listdir(icon_dir)), start=1):
        if icon.lower().endswith(".ico"):
            icon_path = os.path.join(icon_dir, icon)
            resource_id = f"IDI_ICON{index}"
            rc_file.write(f"{resource_id} ICON \"{icon_path}\"\n")

print(f"Resource script '{rc_filename}' generated successfully.")
