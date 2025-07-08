from tkinter import *
from googletrans import Translator

def translate_text():
    try:
        user_input = text_input.get("1.0", END).strip()
        src = src_lang.get().strip()
        dest = dest_lang.get().strip()

        if not user_input or not src or not dest:
            result_output.delete("1.0", END)
            result_output.insert(END, "Please fill all fields.")
            return

        translator = Translator()
        translated = translator.translate(user_input, src=src, dest=dest)
        
        result_output.delete("1.0", END)
        result_output.insert(END, translated.text)

    except Exception as e:
        result_output.delete("1.0", END)
        result_output.insert(END, f"Error: {e}")

root = Tk()
root.title("Language Translator")
root.geometry("500x350")
root.configure(bg='lightblue')

Label(root, text="Enter Text", bg='lightblue', font=('Arial', 12)).pack()
text_input = Text(root, height=4)
text_input.pack()

Label(root, text="From Language Code (e.g., 'en')", bg='lightblue').pack()
src_lang = Entry(root)
src_lang.pack()

Label(root, text="To Language Code (e.g., 'fr')", bg='lightblue').pack()
dest_lang = Entry(root)
dest_lang.pack()

Button(root, text="Translate", command=translate_text, bg='skyblue').pack(pady=10)

Label(root, text="Translated Text", bg='lightblue', font=('Arial', 12)).pack()
result_output = Text(root, height=4)
result_output.pack()

root.mainloop()
 