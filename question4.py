import cv2
import numpy as np

def keep_color(image_path, color_to_keep, output_path):
    # Load the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Create a mask for the color to keep
    lower = np.array(color_to_keep[0], dtype="uint8")
    upper = np.array(color_to_keep[1], dtype="uint8")
    mask = cv2.inRange(image, lower, upper)

    # Use the mask to keep the color and grayscale the rest
    result = cv2.bitwise_and(image, image, mask=mask)

    # Convert the grayscale part to grayscale image
    non_matching = cv2.cvtColor(cv2.bitwise_and(image, image, mask=cv2.bitwise_not(mask)), cv2.COLOR_BGR2GRAY)
    non_matching = cv2.cvtColor(non_matching, cv2.COLOR_GRAY2BGR)

    # Combine the kept color and the grayscale part
    final_result = cv2.add(result, non_matching)

    # Save the final result
    cv2.imwrite(output_path, final_result)

if __name__ == "__main__":
    # Process "mushroom.jpg" to preserve red
    mushroom_image_path = "./Assignment1/mushroom.jpg"
    mushroom_output_path = "./Assignment1/mushroom_output.jpg"
    red_color_to_keep = ([0, 0, 50], [100, 100, 255])  # Adjusted red color range

    keep_color(mushroom_image_path, red_color_to_keep, mushroom_output_path)
    print(f"Processed {mushroom_image_path}. Result saved as '{mushroom_output_path}'.")

    # Process "tree.jpg" to preserve green
    tree_image_path = "./Assignment1/tree.jpg"
    tree_output_path = "./Assignment1/tree_output.jpg"
    green_color_to_keep = ([0, 0, 5], [100, 255, 100])  # Green color range

    keep_color(tree_image_path, green_color_to_keep, tree_output_path)
    print(f"Processed {tree_image_path}. Result saved as '{tree_output_path}'.")
