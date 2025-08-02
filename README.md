
# AI-Powered Caption Generator

This project is a multi-modal AI application that generates descriptive captions for images. It leverages state-of-the-art machine learning models for image understanding and natural language generation, providing a seamless user experience through a Streamlit web interface.

## Features

- **Image-to-Text Captioning**: Upload an image and receive a contextually relevant caption.
- **Voice-to-Text Input**: Use your voice to provide context or instructions for caption generation.
- **Customizable Prompts**: Fine-tune caption generation with custom text prompts.
- **Modular Architecture**: Built with a clean, modular structure for easy extension and maintenance.
- **Interactive Web UI**: A user-friendly interface built with Streamlit.

## Getting Started

### Prerequisites

- Python 3.8+
- `uv` for package and environment management.

  To install `uv`, run the following command in your terminal:
  ```bash
  curl -LsSf https://astral.sh/uv/install.sh | sh
  ```

  If installing from PyPI, we recommend installing uv into an isolated environment, e.g., with pipx:
  ```bash
  pipx install uv
  ```

  However, pip can also be used:
  ```bash
  pip install uv
  ```

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/caption-generator.git
   cd caption-generator
   ```

2. **Create and activate a virtual environment using uv:**
   ```bash
   uv venv
   source .venv/bin/activate
   ```

3. **Install dependencies using uv:**
   ```bash
   uv pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   - Create a `.env` file in the root directory.
   - Add your Mistral API key:
     ```
     MISTRAL_API_KEY="your-mistral-api-key"
     ```

### Running the Application

To start the Streamlit server, run:
```bash
streamlit run main.py
```
The application will be accessible at `http://localhost:8501`.

## Project Structure

```
/caption-generator/
├── main.py              # Streamlit app
├── modules/
│   ├── voice_input.py   # Voice to text
│   ├── image_caption.py # Image to caption
│   ├── prompt_builder.py
│   └── langgraph_runner.py
├── assets/
│   └── sample_images/
├── .env
└── requirements.txt
```

- **`main.py`**: The entry point for the Streamlit application.
- **`modules/`**: Contains the core logic for different functionalities.
  - **`image_caption.py`**: Handles image captioning using the BLIP model.
  - **`voice_input.py`**: Manages voice-to-text conversion.
  - **`prompt_builder.py`**: Constructs prompts for the language model.
  - **`langgraph_runner.py`**: Executes the LangGraph pipeline for response generation.
- **`assets/`**: Stores static files, such as sample images.
- **`.env`**: Holds environment variables (e.g., API keys).
- **`requirements.txt`**: Lists the Python dependencies for the project.

## Troubleshooting

- **`TypeError: the JSON object must be str, bytes or bytearray, not NoneType`**:
  - This error may occur if the Hugging Face cache is corrupted. Clear it by running:
    ```bash
    rm -rf ~/.cache/huggingface/transformers
    ```
- **`NameError: name 'MISTRAL_API_KEY' is not defined`**:
  - Ensure your `.env` file is correctly set up and the variable name matches the one used in the code.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.
