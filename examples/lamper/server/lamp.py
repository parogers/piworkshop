# lamp.py

class Lamp(object):
    state = False

    def set_on(self, on):
        if (on):
            print "LAMP IS ON"
        else:
            print "LAMP IS OFF"
        self.state = on
        # Update GPIO pin
        # ...
