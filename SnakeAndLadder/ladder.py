class Ladder:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __eq__(self, other):
        return self.start == other.end and self.start == other.end

    def get_start(self):
        return self.start

    def get_end(self):
        return self.end
