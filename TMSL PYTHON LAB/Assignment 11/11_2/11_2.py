import cv2
import matplotlib.pyplot as plt

def display_histogram(image_path):
    # Read the image in grayscale
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    if image is None:
        print(f"Error: Unable to read the image at '{image_path}'.")
        return

    # Calculate the histogram
    hist = cv2.calcHist([image], [0], None, [256], [0, 256])

    # Perform histogram equalization
    equalized_image = cv2.equalizeHist(image)

    # Calculate the equalized histogram
    equalized_hist = cv2.calcHist([equalized_image], [0], None, [256], [0, 256])

    # Display the original image and histogram
    plt.subplot(2, 2, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Original Image')
    plt.axis('off')

    plt.subplot(2, 2, 2)
    plt.plot(hist, color='black')
    plt.title('Original Histogram')
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')

    # Display the equalized image and histogram
    plt.subplot(2, 2, 3)
    plt.imshow(equalized_image, cmap='gray')
    plt.title('Equalized Image')
    plt.axis('off')

    plt.subplot(2, 2, 4)
    plt.plot(equalized_hist, color='black')
    plt.title('Equalized Histogram')
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')

    # Show the plots
    plt.show()

if __name__ == "__main__":
    # Replace 'your_image_path.jpg' with the path to your grayscale image
    image_path = 'your_image_path.jpg'
    display_histogram(image_path)

