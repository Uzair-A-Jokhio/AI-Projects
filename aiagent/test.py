from functions.get_files_info import get_files_info

def main():
    working_dir = "calculator"
    root_content = get_files_info(working_dir)
    print(root_content)
    pkg_content = get_files_info(working_dir, "pkg")
    print(pkg_content)
    pkg_content = get_files_info(working_dir, "/bin")
    print(pkg_content)
    pkg_content = get_files_info(working_dir, "../")
    print(pkg_content)

main()