import os
import cv2
import matplotlib.pyplot as plt

def get_char_for_number(number):
    char_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ. '  
    if 1 <= number <= len(char_list):
        return char_list[number - 1]  
    return None

def create_image_dictionary(folder_path):
    image_dict = {}
    for filename in os.listdir(folder_path):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            try:
                number = int(os.path.splitext(filename)[0]) 
                char = get_char_for_number(number)
                if char:
                    img_path = os.path.join(folder_path, filename)
                    img = cv2.imread(img_path)
                    if img is not None:
                        image_dict[char] = img
                    else:
                        print(f"Failed to load image: {filename}")
            except ValueError:
                print(f"Filename is not a valid number: {filename}")
    return image_dict

def display_name_images(image_dict, name):
    images_to_display = [image_dict[char] for char in name.upper() if char in image_dict]
    
    if not images_to_display:
        print("No images found for the given name.")
        return
    
    fig, axes = plt.subplots(1, len(images_to_display), figsize=(15, 5))
    if len(images_to_display) == 1:
        axes = [axes]  
    for ax, img in zip(axes, images_to_display):
        ax.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        ax.axis('off')
    plt.show()

if __name__ == "__main__":
    folder_path = input("Enter the Alphabet folder path: ")
    if not os.path.isdir(folder_path):
        print("Invalid folder path. Please make sure the path is correct.")
    else:
        image_dict = create_image_dictionary(folder_path)
        name = input("Enter name: ")
        display_name_images(image_dict, name)

