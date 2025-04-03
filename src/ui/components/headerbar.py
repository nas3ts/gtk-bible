import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk

class SearchHeaderBar(Gtk.HeaderBar):
    def __init__(self):
        super().__init__()
        self.set_show_title_buttons(True)

        # Create the search entry
        self.search_entry = Gtk.Entry()
        self.search_entry.set_placeholder_text("Search...")
        
        # Connect the search entry signal to the search function
        self.search_entry.connect("activate", self.on_search_activate)

        # Add the search entry to the header bar
        self.pack_start(self.search_entry)

    def on_search_activate(self, entry):
        search_text = entry.get_text()
        # Perform search logic with the search text
        print(f"Searching for: {search_text}")

