import cv2
import os
import shutil
import zipfile

def convert_to_grayscale_with_alpha(image):
    if image.shape[2] == 4:
        bgr, alpha = image[:, :, :3], image[:, :, 3]
        grayscale = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)
        return cv2.merge([grayscale, grayscale, grayscale, alpha])
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def process_image(file_path, output_path=None, zipf=None, arcname=None, include_non_images=True):
    is_image = file_path.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tif', '.tiff'))
    if is_image:
        original_image = cv2.imread(file_path, cv2.IMREAD_UNCHANGED)
        grayscale_image = convert_to_grayscale_with_alpha(original_image)
        if zipf and arcname:
            _, img_bytes = cv2.imencode(os.path.splitext(file_path)[1], grayscale_image)
            zipf.writestr(arcname, img_bytes)
        elif output_path:
            cv2.imwrite(output_path, grayscale_image)
    elif include_non_images:
        if zipf and arcname:
            zipf.write(file_path, arcname)
        elif output_path:
            shutil.copy(file_path, output_path)

input_dir = 'input' # Control input folder name
output_dir = 'output' # Control output folder name
zip_filename = 'default.zip' # Control ZIP output name
output_folder = True  # Control writing to the output folder
create_zip = False  # Control whether to create a zip file
include_non_images = False  # Control whether to include non-image files

if not output_folder and create_zip:
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(input_dir):
            for filename in files:
                file_path = os.path.join(root, filename)
                arcname = os.path.join(os.path.relpath(root, input_dir), filename)
                process_image(file_path, zipf=zipf, arcname=arcname, include_non_images=include_non_images)
    print(f"Created zip archive: {zip_filename}")
else:
    if output_folder:
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        for root, _, files in os.walk(input_dir):
            for filename in files:
                file_path = os.path.join(root, filename)
                output_folder_path = os.path.join(output_dir, os.path.relpath(root, input_dir))
                if not os.path.exists(output_folder_path):
                    os.makedirs(output_folder_path)
                output_file_path = os.path.join(output_folder_path, filename)
                process_image(file_path, output_path=output_file_path, include_non_images=include_non_images)

    if create_zip:
        with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, _, files in os.walk(output_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    zipf.write(file_path, os.path.relpath(file_path, output_dir))
        print(f"Created zip archive: {zip_filename}")
