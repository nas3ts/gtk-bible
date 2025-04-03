import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk
# from ui.components.headerbar import SearchHeaderBar

class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, application):
        super().__init__(application=application)
        self.set_default_size(800, 600)
        self.set_title("")  # Set the window title here

        # #  Create the custom header bar
        # header_bar = SearchHeaderBar()

        # # Set the header bar as the window's title bar
        # self.set_titlebar(header_bar)

def on_activate(application):
    window = MainWindow(application)
    window.present()

def main():
    app = Gtk.Application(application_id="com.nas3ts.bibleapp")
    app.connect('activate', on_activate)
    app.run()

if __name__ == "__main__":
    main()

