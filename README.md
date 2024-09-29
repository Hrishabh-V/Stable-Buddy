# Stable Buddy: A Custom Stable Diffusion GUI Application

Welcome to **Stable Buddy**, a custom desktop application designed to make it easy for users to generate images using the **Stable Diffusion** model from a simple interface. This project integrates **CustomTkinter** for an aesthetic dark-themed UI, with support for CUDA-enabled devices for fast image generation using **Stable Diffusion**. The application is powered by **Hugging Face's Diffusers Library** and **Stable Diffusion v1-4**, making use of efficient memory optimization techniques for GPUs with limited VRAM.

## Key Accomplishments

- **CustomTkinter GUI**: Implemented a sleek, responsive dark-themed interface using CustomTkinter for an easy-to-use experience.
- **Stable Diffusion Integration**: Leveraged the Stable Diffusion model via Hugging Face's Diffusers library to generate high-quality images based on text prompts.
- **Memory Optimization**: Used `autocast` for memory efficiency, enabling the app to run on systems with only 4GB of GPU VRAM by casting the model to FP16 precision.
- **CUDA Support**: Detects CUDA availability and utilizes GPU for faster image generation.
- **Image Display and Download**: Generated images are displayed in the GUI and can be downloaded with the click of a button.

## How It Works

### 1. **Text-to-Image Generation**
   The user provides a text prompt in the UI. This prompt is passed to the **Stable Diffusion pipeline** to generate a unique image based on the text description. The generated image is displayed in the application.

### 2. **Memory Efficient Image Generation**
   To optimize performance, the application uses `autocast` in conjunction with FP16 precision, allowing it to run on GPUs with limited memory while maintaining high-quality output.

### 3. **Downloading the Generated Image**
   Once an image is generated, users can save it locally by clicking the **Download** button. The image is stored in a dedicated `data/` folder within the project directory.

## Project Architecture

This project is organized into the following key components:

- **UI Components**: The interface is built using **CustomTkinter**, a modern Tkinter wrapper for dark-themed GUIs.
- **Image Generation**: The text prompt is passed to the **Stable Diffusion v1-4** pipeline from Hugging Face's Diffusers library. The pipeline is optimized using the FP16 precision model to reduce memory usage and increase generation speed. 
If you want you can configure it for "CPU" by using float32
- **Environment Variables**: The app uses an `AUTH_TOKEN` from Hugging Face, which is securely stored in a `.env` file and loaded using `dotenv`.

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Hrishabh-V/Stable-Buddy.git
cd stable-buddy
```

### 2. Set Up Environment Variables
Create a `.env` file in the root directory of the project and add your Hugging Face API token:

```
AUTH_TOKEN=your_huggingface_auth_token
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

The key libraries include:

- `customtkinter`
- `diffusers`
- `Pillow`
- `torch`
- `python-dotenv`

### 4. Run the Application
```bash
python app.py
```

## Metrics and Results

The application was tested on systems with both CPU and GPU, with the following performance results:

- **GPU (4GB VRAM, CUDA enabled)**:
   - Image generation time: 10-15 seconds per image.
   - Memory usage: ~3.5 GB (FP16 precision).
  
- **CPU**:
   - Image generation time: 5-15 minutes per image.
   - Memory usage: ~6-7 GB.

On CUDA-enabled GPUs with 4GB VRAM, the application successfully generates high-quality images without exceeding memory limits, thanks to FP16 optimization.

## Understanding Stable Diffusion

**Stable Diffusion** is a type of latent diffusion model designed to generate high-quality images from text prompts. It uses a **Transformer** architecture in combination with a **latent space** representation, allowing it to learn the underlying structure of images and generate them from text inputs. Stable Diffusion is part of the generative AI revolution, known for producing photorealistic images or art pieces based on detailed descriptions.

Key characteristics of Stable Diffusion include:

- **Text-based generation**: Converts natural language descriptions into images.
- **Scalability**: Can work with large datasets and produce diverse outputs.
- **Efficiency**: With model optimizations like FP16, it can run on consumer-grade GPUs.

## Future Enhancements

- **Advanced Customization**: Add sliders for controlling different aspects like guidance scale, number of inference steps, and seed.
- **Batch Generation**: Enable users to generate multiple images from a list of prompts.
- **Advanced Previews**: Implement a real-time preview of intermediate steps during image generation.

## Conclusion

**Stable Buddy** provides an easy-to-use interface for generating images using one of the most advanced AI models available. With memory-efficient optimizations, it runs on consumer GPUs, making it accessible to a wider audience.

Feel free to explore and extend the project. Contributions are welcome!

## License

This project is licensed under the MIT License.

---

If you encounter any issues or have suggestions for improvements, feel free to open an issue or contribute to the repository!
