from pathlib import Path
import tkinter as tk
import sys

class Notepad(tk.Tk):

    def __init__(self) -> None:
        super().__init__()
        self.title("Notepad")
        self.geometry("800x500")
        self.menubar = tk.Menu()
        self.file_menu = tk.Menu(tearoff=False)
        self.file_menu.add_command(label="New", command=self.new)
        self.file_menu.add_command(label="Open", command=self.open)
        self.file_menu.add_command(label="Save", command=self.save)
        self.file_menu.add_command(
            label="Save As...",
            command=self.save_as
        )
        self.menubar.add_cascade(menu=self.file_menu, label="File")
        self.config(menu=self.menubar)
        # Main widget to edit a text file.
        self.text = tk.Text()
        self.text.pack(expand=True, fill=tk.BOTH)
        # The `current_file` attribute contains the path of the
        # file that is being edited or `None` if the file has
        # not been saved yet.
        self.current_file: Optional[Path] = None
        # File types that will show in the open and save
        # file dialogs.
        self.filetypes: tuple[tuple[str, str], ...] = (
            ("Text Files", "*.txt"),
            ("All Files", "*.*")
        )
        # Replace Tk's default behaviour to the event that
        # closes the window so we can save the file before
        # exiting the program.
        self.protocol("WM_DELETE_WINDOW", self.close)

    def close(self) -> None:
        if not self.can_continue():
            return
        # Destroy the window.
        self.destroy()

    def set_current_file(self, current_file: Path) -> None:
        self.current_file = current_file
        self.title(self.current_file.name + " - Notepad")

    def can_continue(self) -> bool:
        if self.text.edit_modified():
            result = messagebox.askyesnocancel(
                title="Unsaved Changes",
                message="Do you want to save changes?"
            )
            cancel = result is None
            save_before = result is True
            if cancel:
                return False
            elif save_before:
                self.save()
            return True
        # If there were no editions, continue without saving.
        return True

    def new(self) -> None:
        if not self.can_continue():
            return
        # Delete the previous text.
        self.text.delete("1.0", tk.END)
        self.current_file = None
        self.title("Notepad")

    def open(self) -> None:
        filename = filedialog.askopenfilename(filetypes=self.filetypes)
        if not filename or not self.can_continue():
            return
        # Remove previous text and load the new one.
        self.text.delete("1.0", tk.END)
        file = Path(filename)
        self.text.insert("1.0", file.read_text("utf8"))
        # Reset text state when a new file is opened.
        self.text.edit_modified(False)
        self.set_current_file(file)

    def save_current_file(self) -> None:
        if self.current_file is None:
            return
        self.current_file.write_text(self.text.get("1.0", tk.END), "utf8")

    def save(self) -> None:
        if self.current_file is None:
            self.save_as()
            return
        self.save_current_file()

    def save_as(self) -> None:
        filename = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=self.filetypes
        )
        # Do nothing if the user closed or cancelled the dialog.
        if not filename:
            return
        self.set_current_file(Path(filename))
        self.save_current_file()



if __name__ == "__main__":
    print('in "if __'
          'name__ == __main__()')
    args = sys.argv[1:]
    Notepad()
