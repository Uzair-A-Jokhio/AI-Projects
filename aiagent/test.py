from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

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
    print(get_file_content(working_dir, "main.py"))
    print(get_file_content(working_dir, "pkg/not_happeing.py"))
    print(get_file_content(working_dir, "/bin/cat"))
    
main()