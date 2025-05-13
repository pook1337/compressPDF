import fitz  # PyMuPDF

def compress_pdf(input_path, output_path, image_quality=50):
    """
    Compress PDF by downsampling images to reduce file size.
    
    :param input_path: Path to input PDF file
    :param output_path: Path to save compressed PDF
    :param image_quality: Quality percentage for images (1-100)
    """
    doc = fitz.open(input_path)
    for page in doc:
        images = page.get_images(full=True)
        for img_index, img in enumerate(images):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            # Replace image with compressed version
            # PyMuPDF can compress images by re-inserting them with lower quality
            pix = fitz.Pixmap(fitz.csRGB, fitz.open("png", image_bytes))
            new_image = pix.tobytes("jpeg", quality=image_quality)
            doc.update_image(xref, new_image)
    doc.save(output_path, deflate=True)
    print(f"Compressed PDF saved to {output_path}")

if __name__ == "__main__":
    compress_pdf("input.pdf", "output_compressed.pdf", image_quality=40)
