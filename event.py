class Event:
    def __init__(self, name):
        self.name = name
        self.entries = []
        self.results = []

    def add_entry(self, swimmer):
        self.entries.append(swimmer)

    def clear_entries(self):
        self.entries = []

    def set_results(self, results):
        self.results = results

    def __repr__(self):
        return f"Event({self.name}, entries={len(self.entries)})"
