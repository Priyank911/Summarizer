# Text Summarizer

*Text Summarizer Interface*

## Overview

This project is a simple text summarizer built using the Hugging Face Transformers library and Gradio. It allows users to input a block of text and receive a concise summary. The application is hosted using Gradio, making it easy to use with an interactive web interface.

## Features

- **Text Summarization:** Enter a block of text, and the model generates a summary.
- **User-friendly Interface:** Built with Gradio for an easy-to-use and interactive UI.
- **Customizable:** You can tweak the summarization model or parameters according to your needs.

## Demo

You can view a live demo of the project [here](http://127.0.0.1:5000/get_summary). (If hosted online, replace with the actual URL.)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/Summarizer.git
   cd Summarizer
   ```

2. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   python app.py
   ```

## Usage

1. Run the application by executing the `app.py` script.
2. Open the provided link in your browser to access the Gradio interface.
3. Enter the text you want to summarize and click on "Summarize" to get the output.

## Methods

### Method 1: Using a Pre-trained Transformer Model

![Method 1](https://github.com/Priyank911/Summarizer/blob/main/gradio.png)  
*Pre-trained Transformer Method*

This method utilizes a pre-trained transformer model from Hugging Face to generate summaries. It's quick to set up and provides good results for general use cases.

### Method 2: Fine-tuning a Transformer Model

![Method 2](https://github.com/Priyank911/Summarizer/blob/main/WithoutFrameWork.png)  
*Fine-tuning Transformer Method*

In this method, the summarizer is fine-tuned on specific datasets to improve its performance on domain-specific texts. This approach might require more computational resources and time but can yield better results for specialized tasks.

## Contributing

If you'd like to contribute to this project, please fork the repository and submit a pull request.

## Acknowledgments

- Thanks to Hugging Face for providing the pre-trained models.
- Thanks to Gradio for the user-friendly interface framework.

---
