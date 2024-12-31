import subprocess

from flathub import install_flathub_programs, remove_flathub_programs
from repo import install_programs, remove_programs
from snap import install_snap_programs, remove_snap_programs
from ps_download import  ps_download
from ps_install import ps_install

def read_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        programs = [line.split() for line in lines]
    return programs

files = ['repo.txt', 'flathub.txt', 'snap.txt']
all_programs = read_file(files[0])
all_flathub_programs = read_file(files[1])
all_snap_programs = read_file(files[2])

'''if __name__ == '__main__':
    while True:
        print('1. Install programs')
        print('2. Remove programs')
        print('3. Install flathub programs')
        print('4. Remove flathub programs')
        print('5. Install snap programs')
        print('6. Remove snap programs')
        print('7. Downlad Pioneer Station')
        print('8. Install Pioneer Station')
        print('9. Install Flatpak')
        print('10. Return Alt+Shift')
        print('11. Exit')
        choice = input('Enter your choice:')
        if choice == '1':
            install_programs(all_programs)
        elif choice == '2':
            remove_programs(all_programs)
        elif choice == '3':
            install_flathub_programs(all_flathub_programs)
        elif choice == '4':
            remove_flathub_programs(all_flathub_programs)
        elif choice == '5':
            install_snap_programs(all_snap_programs)
        elif choice == '6':
            remove_snap_programs(all_snap_programs)
        elif choice == '7':
            ps_download()
        elif choice == '8':
            ps_install()
        elif choice == '9':
            subprocess.run(
                "/run/media/roman/Files/Python/autoinstall-ubuntu-programs-pyqt/install_flathub.sh",
                 shell= True
            )
        elif choice == '10':
            subprocess.run(
                "/run/media/roman/Files/Python/autoinstall-ubuntu-programs-pyqt/alt-shift.sh",
                shell= True
            )
        elif choice == '11':
            break
        else:
            print('Invalid choice')'''
