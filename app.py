#imports
import customtkinter as ctk
from PIL import Image, ImageTk
import torch
from torch import autocast
from diffusers import StableDiffusionPipeline
import os
from dotenv import load_dotenv

# Load the environment variables from .env
load_dotenv()

class StableBuddyApp:
    def __init__(self, master):
        self.master = master
        self.master.geometry("532x632")
        self.master.title("Stable Buddy")
        ctk.set_appearance_mode("dark")
        
        self.generated_image = None  # store generated image
        
        # Check if the data directory exists
        if not os.path.exists('data'):
            os.makedirs('data')
        
        # UI Setup
        self.setup_ui()
        
        # Load Pipeline model
        self.setup_pipeline()

    def setup_ui(self):
        """Set up the UI components like entries, buttons, labels."""
        # Prompt Entry
        self.prompt = ctk.CTkEntry(master=self.master, height=40, width=512, text_color='black', fg_color='white')
        self.prompt.place(x=10, y=10)
        
        # Label to display image
        self.lmain = ctk.CTkLabel(master=self.master, height=512, width=512)
        self.lmain.place(x=10, y=110)
        
        # Generate Button
        self.trigger = ctk.CTkButton(master=self.master, height=40, width=120, text_color='white', fg_color='purple', command=self.generate)
        self.trigger.configure(text='Generate')
        self.trigger.place(x=150, y=60)
        
        # Download Button
        self.download_button = ctk.CTkButton(master=self.master, height=40, width=120, text_color='white', fg_color='blue', command=self.download)
        self.download_button.configure(text='Download')
        self.download_button.place(x=280, y=60)
        
    def setup_pipeline(self):
        """Set up the Stable Diffusion pipeline."""
        model_id = "CompVis/stable-diffusion-v1-4"
        device = "cuda" if torch.cuda.is_available() else "cpu"
        
        # Get the auth_token from the environment variable
        auth_token = os.getenv("AUTH_TOKEN")
        
        if not auth_token:
            raise ValueError("AUTH_TOKEN environment variable is not set.")
        
        # Use float16 and fp16 so that stable diffusion can work on 4GB VRAM
        self.pipe = StableDiffusionPipeline.from_pretrained(
            model_id, revision='fp16', torch_dtype=torch.float16, use_auth_token=auth_token
        )
        self.pipe.to(device)

    def generate(self):
        """Generate an image based on the prompt."""
        self.lmain.configure(image='', text='Generating...')  # Show a temporary text
        
        try:
            # prompt text
            prompt_text = self.prompt.get()
            
            # autocast improve memory efficiency
            with autocast("cuda"):
                image = self.pipe(prompt_text, guidance_scale=8.5).images[0]
            
            # Save the generated image
            self.generated_image = image
            image.save('data/generated_image.png')
            
            # Tkinter display
            img = ImageTk.PhotoImage(image)
            self.lmain.configure(image=img, text='')
            self.lmain.image = img  # Keep a reference to avoid garbage collection
            
        except Exception as e:
            print(f"An error occurred: {e}")
            self.lmain.configure(text="Error generating image")

    def download(self):
        """Save the generated image."""
        if self.generated_image is not None:
            self.generated_image.save('data/generated_image.png') 
            self.lmain.configure(text="Image downloaded!")
        else:
            self.lmain.configure(text="No image to download!")


if __name__ == "__main__":
    app = ctk.CTk()  
    stable_buddy_app = StableBuddyApp(app)  # Instantiate the StableBuddyApp 
    app.mainloop()
