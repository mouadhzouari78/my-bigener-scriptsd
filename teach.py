import platform
from pathlib import Path


def find_image_on_pc(filename):
    # 1. Automatically detect the correct Root Directory for your OS
    if platform.system() == "Windows":
        root = Path("C:/")  # Change to "D:/" etc. if your image is on another drive
    else:
        root = Path("/")  # macOS and Linux root

    print(f"Searching entire PC starting from {root}... This may take a minute.")

    target_name = filename.lower()

    # 2. Use rglob to search everything, but handle permissions safely
    # We use a generator expression to catch permission errors line-by-line
    try:
        for path in root.rglob("*"):
            try:
                # Check if it's a file and matches our target name (case-insensitive)
                if path.is_file() and path.name.lower() == target_name:
                    return path.resolve()
            except (PermissionError, FileNotFoundError):
                # Skip folders that Python isn't allowed to look inside
                continue
    except Exception as e:
        print(f"An error occurred: {e}")

    return None


# --- How to use it ---
image_name = "image.png"
found_path = find_image_on_pc(image_name)

if found_path:
    print(f"\n🎉 Success! Image found at:\n{found_path}")
else:
    print(f"\n❌ Could not find an image named '{image_name}' anywhere on this drive.")
