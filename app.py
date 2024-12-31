from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton

from flathub import install_flathub_programs, remove_flathub_programs
from repo import install_programs, remove_programs
from snap import install_snap_programs, remove_snap_programs
from ps_download import  ps_download
from ps_install import ps_install


app = QApplication([])
window = QWidget()
layout = QVBoxLayout()
install_repo_button = QPushButton("Install programs")
remove_repo_button = QPushButton("Remove programs")
install_flathub_button = QPushButton("Install Flathub programs")
remove_flathub_button = QPushButton("Remove Flathub programs")
install_snap_button = QPushButton("Install Snap programs")
remove_snap_button = QPushButton("Remove Snap programs")
download_ps_button = QPushButton("Download Pioneer Station")
install_ps_button = QPushButton("Install Pioneer Station")
install_flatpak_button = QPushButton("Install Flatpak")
return_alt_shift_bbutton = QPushButton("Return to Alt+Shift")
exit_button = QPushButton("Exit")

window.setLayout(layout)

layout.addWidget(install_repo_button)
layout.addWidget(remove_repo_button)
layout.addWidget(install_flathub_button)
layout.addWidget(remove_flathub_button)
layout.addWidget(install_snap_button)
layout.addWidget(remove_snap_button)
layout.addWidget(download_ps_button)
layout.addWidget(install_ps_button)
layout.addWidget(install_flatpak_button)
layout.addWidget(return_alt_shift_bbutton)
layout.addWidget(exit_button)

install_repo_button.clicked.connect(lambda: print("Install programs"))
remove_repo_button.clicked.connect(lambda: print("Remove programs"))
install_flathub_button.clicked.connect(lambda: print("Install Flathub programs"))
remove_flathub_button.clicked.connect(lambda: print("Remove Flathub programs"))
install_snap_button.clicked.connect(lambda: print("Install Snap programs"))
remove_snap_button.clicked.connect(lambda: print("Remove Snap programs"))
download_ps_button.clicked.connect(lambda: print("Download Pioneer Station"))
install_ps_button.clicked.connect(lambda: print("Install Pioneer Station"))
install_flatpak_button.clicked.connect(lambda: print("Install Flatpak"))
return_alt_shift_bbutton.clicked.connect(lambda: print("Return to Alt+Shift"))
exit_button.clicked.connect(lambda: print("Exit"))


window.resize(500, 500)
window.setWindowTitle("Autoinstall Ubuntu Programs")

window.show()
app.exec_()