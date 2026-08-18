# This code is made by MRayan Asim
# Packages needed:
#   pip install pyqt5 pyqtwebengine

import sys

from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QAction, QApplication, QLineEdit, QMainWindow, QToolBar

DEFAULT_HOME = "https://duckduckgo.com"


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl(DEFAULT_HOME))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # navbar
        navbar = QToolBar()
        self.addToolBar(navbar)

        back_btn = QAction("Back", self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        forward_btn = QAction("Forward", self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        reload_btn = QAction("Reload", self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        home_btn = QAction("Home", self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)
        self.browser.loadFinished.connect(self._on_load_finished)

    def navigate_home(self) -> None:
        self.browser.setUrl(QUrl(DEFAULT_HOME))

    def navigate_to_url(self) -> None:
        url = self.url_bar.text().strip()
        if not url.startswith(("http://", "https://")):
            url = "https://" + url
        self.browser.setUrl(QUrl(url))

    def update_url(self, q: QUrl) -> None:
        self.url_bar.setText(q.toString())

    def _on_load_finished(self, ok: bool) -> None:
        if not ok:
            self.statusBar().showMessage(f"Failed to load: {self.browser.url().toString()}", 5000)


app = QApplication(sys.argv)
QApplication.setApplicationName("Python Projects Browser")
window = MainWindow()
app.exec_()
