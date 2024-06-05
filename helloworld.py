import threading
import tkinter as tk

class HelloWorldPrinter:
    def __init__(self):
        self.message = "Hello World"
    
    def double_letters(self, message):
        return ''.join([char * 2 for char in message])
    
    def print_message(self):
        doubled_message = self.double_letters(self.message)
        print(doubled_message)

class HelloWorldThread(threading.Thread):
    def __init__(self, printer):
        threading.Thread.__init__(self)
        self.printer = printer

    def run(self):
        self.printer.print_message()

class HelloWorldGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Hello World Printer")
        self.label = tk.Label(self.root, text="Click the button to print 'Hello World'")
        self.label.pack(pady=10)
        self.button = tk.Button(self.root, text="Print Hello World", command=self.print_hello_world)
        self.button.pack(pady=5)

    def print_hello_world(self):
        printer = HelloWorldPrinter()
        thread = HelloWorldThread(printer)
        thread.start()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    gui = HelloWorldGUI()
    gui.run()

