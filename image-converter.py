import customtkinter as ctk
from tkinter import filedialog, messagebox
from PIL import Image
import os

try:
    from pillow_heif import register_heif_opener
    register_heif_opener()
except ImportError:
    pass

try:
    import rawpy
except ImportError:
    pass

try:
    from svglib.svglib import svg2rlg
    from reportlab.graphics import renderPM
except ImportError:
    pass


# Configurações de aparência
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Conversor de Imagens")
        self.geometry("500x380")
        self.resizable(False, False)

        # Fundo principal
        self.main_frame = ctk.CTkFrame(self, corner_radius=15)
        self.main_frame.pack(pady=20, padx=20, fill="both", expand=True)

        # Título
        self.label = ctk.CTkLabel(self.main_frame, text="📸 Conversor Universal para JPEG", font=ctk.CTkFont(family="Roboto", size=22, weight="bold"))
        self.label.pack(pady=(30, 10))

        self.subtitle = ctk.CTkLabel(self.main_frame, text="Converta HEIC, RAW, WEBP, SVG e mais", font=ctk.CTkFont(family="Roboto", size=13), text_color="gray")
        self.subtitle.pack(pady=(0, 25))

        # Botão de seleção
        self.select_btn = ctk.CTkButton(self.main_frame, text="📂 Selecionar Imagens", 
                                        font=ctk.CTkFont(size=15, weight="bold"),
                                        height=40, corner_radius=8,
                                        command=self.open_file)
        self.select_btn.pack(pady=10)

        # Botão de processamento
        self.process_btn = ctk.CTkButton(self.main_frame, text="⚡ Converter e Salvar", 
                                          font=ctk.CTkFont(size=15, weight="bold"),
                                          height=45, corner_radius=8,
                                          fg_color="#2EA043", hover_color="#237632",
                                          command=self.process)
        self.process_btn.pack(pady=20)

        self.image_paths = []

    def open_file(self):
        supported_types = [
            ("Todas as Imagens Suportadas", "*.jpg *.png *.jpeg *.webp *.heif *.heic *.raw *.cr2 *.nef *.orf *.sr2 *.dng *.arw *.tiff *.tif *.svg"),
            ("JPEG / PNG / WEBP", "*.jpg *.png *.jpeg *.webp"),
            ("HEIF / HEIC", "*.heif *.heic"),
            ("RAW", "*.raw *.cr2 *.nef *.orf *.sr2 *.dng *.arw"),
            ("TIFF", "*.tiff *.tif"),
            ("SVG", "*.svg")
        ]
        self.image_paths = filedialog.askopenfilenames(filetypes=supported_types)
        if self.image_paths:
            if len(self.image_paths) == 1:
                self.select_btn.configure(text=os.path.basename(self.image_paths[0]), fg_color="gray")
            else:
                self.select_btn.configure(text=f"{len(self.image_paths)} imagens selecionadas", fg_color="gray")

    def process(self):
        if not self.image_paths:
            messagebox.showwarning("Erro", "Selecione pelo menos uma imagem primeiro!")
            return

        try:
            if len(self.image_paths) == 1:
                # Se for apenas uma imagem, deixamos a pessoa escolher onde salvar e com qual nome
                original_name = os.path.splitext(os.path.basename(self.image_paths[0]))[0]
                suggested_name = f"{original_name}_convertida.jpg"
                output_path = filedialog.asksaveasfilename(
                    initialfile=suggested_name,
                    defaultextension=".jpg", 
                    filetypes=[("JPEG", "*.jpg"), ("JPEG", "*.jpeg")]
                )
                
                if output_path:
                    ext = os.path.splitext(self.image_paths[0])[1].lower()
                    img = None
                    if ext == '.svg':
                        drawing = svg2rlg(self.image_paths[0])
                        img = renderPM.drawToPIL(drawing)
                    elif ext in ['.cr2', '.nef', '.dng', '.raw', '.orf', '.arw', '.sr2']:
                        with rawpy.imread(self.image_paths[0]) as raw:
                            rgb = raw.postprocess()
                            img = Image.fromarray(rgb)
                    else:
                        img = Image.open(self.image_paths[0])

                    if img:
                        with img:
                            if img.mode in ("RGBA", "P"):
                                img = img.convert("RGB")
                            img.save(output_path, "JPEG", optimize=True, quality=100)
                    messagebox.showinfo("Sucesso", "Imagem convertida e salva com sucesso!")
            
            else:
                # Se for mais de uma, perguntamos em qual pasta a pessoa quer armazenar
                output_folder = filedialog.askdirectory(title="Selecione a pasta para salvar as imagens")
                
                if output_folder:
                    for path in self.image_paths:
                        original_name = os.path.splitext(os.path.basename(path))[0]
                        suggested_name = f"{original_name}_convertida.jpg"
                        output_path = os.path.join(output_folder, suggested_name)
                        
                        ext = os.path.splitext(path)[1].lower()
                        img = None
                        if ext == '.svg':
                            drawing = svg2rlg(path)
                            img = renderPM.drawToPIL(drawing)
                        elif ext in ['.cr2', '.nef', '.dng', '.raw', '.orf', '.arw', '.sr2']:
                            with rawpy.imread(path) as raw:
                                rgb = raw.postprocess()
                                img = Image.fromarray(rgb)
                        else:
                            img = Image.open(path)

                        if img:
                            with img:
                                if img.mode in ("RGBA", "P"):
                                    img = img.convert("RGB")
                                img.save(output_path, "JPEG", optimize=True, quality=100)
                            
                    messagebox.showinfo("Sucesso", f"{len(self.image_paths)} imagens convertidas e salvas com sucesso!")

        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    app = App()
    app.mainloop()