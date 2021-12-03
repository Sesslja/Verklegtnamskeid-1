
class TextCompleter:
    def __init__(self, options) -> None:
        self.options = options

    def complete(self, text, state):
        response = None

        if state == 0:
            # This is the first time for this text,
            # so build a match list.
            if text:
                self.matches = [
                    s
                    for s in self.options
                    if s and s.startswith(text)
                ]
            else:
                self.matches = self.options[:]

        # Return the state'th item from the match list,
        # if we have that many.
        try:
            response = self.matches[state]
        except IndexError:
            response = None
        
        return response