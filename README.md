# Grayscale-Image-Processor

A versatile Python script that converts color images to grayscale, with options for handling transparency, including non-image files, and outputting to a directory or a zip archive.

## Features

- **Grayscale Conversion:** Converts color images to grayscale, preserving the original image's transparency if present.
- **Flexible Output:** Choose to save processed images to a directory structure that mirrors the input directory or directly to a zip archive.
- **Non-Image File Handling:** Option to include non-image files in the output, making it easy to maintain the integrity of the original directory's content.
- **Customizable Output:** Control whether to write to an output folder or skip it in favor of a zip file, and whether to create a zip archive at all.

## Usage

1. **Set Up Your Environment:**
   Ensure you have Python installed on your system and the necessary libraries (OpenCV for image processing).

2. **Prepare Your Images:**
   Place the images you want to process in the 'input' directory. The script accepts popular image formats such as PNG, JPG, JPEG, BMP, TIF, and TIFF.

3. **Configure the Script:**
   - `input_dir`: The directory containing your images.
   - `output_dir`: The desired output directory for processed images.
   - `zip_filename`: The name of the zip archive, if you choose to create one.
   - `output_folder`: Set to `True` to write processed images to the output directory, `False` to skip.
   - `create_zip`: Set to `True` to create a zip archive of the output.
   - `include_non_images`: Set to `True` to include non-image files in the output.

4. **Run the Script:**
   Execute the script with Python. Processed images will be saved according to your configuration, either in the output directory, a zip archive, or both.

## Requirements

- Python 3.x
- OpenCV library (`cv2` module)

To install OpenCV, run:

```bash
pip install opencv-python
