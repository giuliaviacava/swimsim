class Event:
    # Initializes event using name of event, creates empty list of swimmers entered into event, crates empty list for results of event
    def __init__(self, name):
        self.name = name
        self.entries = []
        self.results = []

    # Add a swimmer to the list of entries for this event
    def add_entry(self, swimmer):
        self.entries.append(swimmer)

    # Remove all swimmers from the event
    def clear_entries(self):
        self.entries = []

    # Store the final results for the event
    def set_results(self, results):
        self.results = results

    # Return a string showing the event name and number of swimmers entered
    def __str__(self):
        return f"Event({self.name}, entries={len(self.entries)})"
