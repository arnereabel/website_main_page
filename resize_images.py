#!/usr/bin/env python3
"""
Image Resizer Script
Resizes JPG and PNG images while maintaining aspect ratio
"""

from PIL import Image
import os

def resize_image(input_path, output_path, max_width=750, quality=85):
    """
    Resize an image while maintaining aspect ratio

    Args:
        input_path: Path to input image
        output_path: Path to save resized image
        max_width: Maximum width in pixels (default: 750)
        quality: JPEG quality (1-100, default: 85)
    """
    try:
        # Open the image
        with Image.open(input_path) as img:
            # Get original dimensions
            original_width, original_height = img.size
            print(f"Original size: {original_width}x{original_height}")

            # Calculate new dimensions maintaining aspect ratio based on width
            ratio = max_width / original_width
            new_width = max_width
            new_height = int(original_height * ratio)

            print(f"New size: {new_width}x{new_height}")

            # Resize the image
            resized_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

            # Save with appropriate format
            if input_path.lower().endswith('.jpg') or input_path.lower().endswith('.jpeg'):
                resized_img.save(output_path, 'JPEG', quality=quality, optimize=True)
            elif input_path.lower().endswith('.png'):
                # For PNG, use optimize=True to reduce file size
                resized_img.save(output_path, 'PNG', optimize=True)
            else:
                resized_img.save(output_path)

            print(f"Saved: {output_path}")

    except Exception as e:
        print(f"Error processing {input_path}: {e}")

def main():
    # Images to resize - all with width > 750
    images = [
        "static/images/filling_120mm_PA.jpg",
        "static/images/filling_120mm_PA_complete.jpg",
        "static/images/filling_120mm_PA_layer_2.jpg",
        "static/images/filling_120mm_PA_layer_6.jpg",
        "static/images/filling_120mm_PE.jpg",
        "static/images/filling_120mm_PE_layer_5.jpg",
        "static/images/slp_setup_jig_setup.jpg",
        "static/images/tky1_complete_ready_for_transport.jpg",
        "static/images/tky1_detail_front_root_opening.jpg",
        "static/images/tky1_detail_side_root_opening.jpg",
        "static/images/tky1_one_side_complete.jpg",
        "static/images/tky1_one_side_complete_2.jpg",
        "static/images/tky1_one_side_filling_backside.jpg",
        "static/images/weldsupport_jig_setup.jpg",
        "static/images/weldsupport_root_opening2.jpg",
        "static/images/welsupport_welded_inside.jpg",
    ]

    # Resize settings
    max_width = 750  # Fixed width for all images
    quality = 90    # JPEG quality (1-100)

    for image_path in images:
        if os.path.exists(image_path):
            # Create output path (overwrite original)
            output_path = image_path

            print(f"\nProcessing: {image_path}")
            resize_image(image_path, output_path, max_width, quality)
        else:
            print(f"File not found: {image_path}")

if __name__ == "__main__":
    main()
