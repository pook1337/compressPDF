
# compressPDF

A simple Python tool to compress PDF files by reducing image quality and optimizing the PDF structure. This project helps reduce PDF file sizes while maintaining reasonable quality, making it easier to share and store PDFs efficiently.

---

## Features

- Compress single PDF files by downsampling images  
- Optimize PDF structure to reduce file size  
- Easy-to-use Python script  
- Cross-platform (Windows, macOS, Linux)  

---

## Requirements

- Python 3.6+  
- [`PyMuPDF`](https://pypi.org/project/PyMuPDF/) (also known as `fitz`) for PDF manipulation  

---

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/pook1337/compressPDF.git
   cd compressPDF
   ```

2. Install dependencies:

   ```
   pip install PyMuPDF
   ```

---

## Usage

Run the compression script `cp.py` with your input PDF file and specify the output file name:

```
python cp.py input.pdf output_compressed.pdf
```

### Example

```
python cp.py example.pdf example_compressed.pdf
```

This will create a compressed version of `example.pdf` named `example_compressed.pdf`.

---

## How it works

- The script opens the PDF file and iterates through its pages.  
- Images inside the PDF are downsampled to reduce their quality and size.  
- The optimized PDF is saved as a new file.

---

## Notes

- Compression quality can be adjusted in the script (if implemented).  
- The tool focuses on image-heavy PDFs for best compression results.  
- Keep backups of your original PDFs before compression.  

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contributing

Contributions and suggestions are welcome! Feel free to open issues or submit pull requests.

