from docx2txt import process
import os

def convert_docx_to_md(input_file_name):
    # Create a directory for images
    image_dir = os.path.join(os.getcwd(), "images")
    os.makedirs(image_dir, exist_ok=True)

    # Extract text and write images in the image directory
    text = process(input_file_name, image_dir)

    # Identify the images and replace placeholders with Markdown image syntax
    for filename in os.listdir(image_dir):
        if filename.endswith(".jpg") or filename.endswith(".png"):  # You can add more extensions if needed
            image_path = os.path.join("images", filename)
            image_tag = f"![{filename}]({image_path})"
            text = text.replace(filename, image_tag)

    # Save the result to a markdown file
    with open('guide2.md', 'w') as f:
        f.write(text)

    print(f"Conversion to Markdown completed. Images are saved in {image_dir}.")

# Call the conversion function with the Word document path
convert_docx_to_md("b.docx")
