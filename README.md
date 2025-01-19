# Image Steganography Tool

This Python-based application provides a user-friendly graphical interface for hiding secret text messages within images (steganography). It enables you to encode a message into an image and later decode it to retrieve the hidden message.

## Features

- **Hide Secret Messages**: Encode your text messages into PNG or JPG images.
- **Retrieve Messages**: Decode messages embedded within images.
- **Simple GUI**: User-friendly interface built with `tkinter`.
- **Image Preview**: Displays the selected image for easy interaction.
- **Image Resizing**: Automatically adjusts images to fit the display area.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/samuelhany-cpu/Steganography.git
   cd Steganography
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python Data_Hider_3.py
   ```

## Dependencies

- Python 3.7+
- `tkinter` (built-in with Python)
- `Pillow` (Python Imaging Library)
  ```bash
  pip install pillow
  ```

## How to Use

1. **Open an Image**: Click on the "Open Image" button to load an image file (PNG or JPG).
2. **Hide a Message**:
   - Type the message into the "Encoded Text" box.
   - Click "Hide Data" to encode the message into the selected image.
3. **Save the Image**: Use the "Save Image" button to save the modified image (`hidden.png`).
4. **Retrieve a Message**:
   - Open an image with hidden data.
   - Click "Show Data" to reveal the hidden message in the "Decoded Text" box.
5. **Clear All**: Reset the interface to start fresh.

## Screenshots

_Add relevant screenshots of the application interface here._

## Folder Structure

```
image-steganography-tool/
├── Data_Hider_3.py        # Main application script
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

## License

This project is licensed under the MIT License. See `LICENSE` for more details.

## Acknowledgments

- The application uses basic steganography principles and `Pillow` for image manipulation.
- Special thanks to the open-source community for providing inspiration and tools!
