# # import cv2

# # import matplotlib.pyplot as plt 

# # image = cv2.imread("C:/Users/sahil/Downloads/DoggyBhai.jpeg")# read the iamge 

# # resizing= cv2.resize(image,(400,400)) #resize the image with the in the dimensions in width and the height

# # plt.imshow(resizing)#To show the image which is the resized

# # plt.show()#using of the plt library of the plt and the show....


# # import cv2

# # # Load the image
# # image = cv2.imread("C:/Users/sahil/Downloads/DoggyBhai.jpeg")

# # # Resize the image to 50% of its original size
# # resized_image = cv2.resize(image, None, fx=0.5, fy=0.5)

# # # Resize the image to a specific size
# # resized_image_2 = cv2.resize(image, (640, 480))

# # # Resize the image using a specific interpolation method
# # resized_image_3 = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

# # # Display the resized images
# # cv2.imshow('Resized Image 1', resized_image)
# # cv2.imshow('Resized Image 2', resized_image_2)
# # cv2.imshow('Resized Image 3', resized_image_3)
# # cv2.waitKey(0)
# # cv2.destroyAllWindows()

# import cv2



    
    
# image = cv2.imread("C:/Users/sahil/Downloads/DoggyBhai.jpeg")

    
    
# if image is None:
#     print("Image not found")
#     exit()
        
#     def regularresizer():
#         try:
            
#             width=int(input("Enter the new Width: "))
#             height= int(input("Enter thr new height: "))
#             regular_resized=cv2.resize(image,(width,height))
#             cv2.imshow("Regular Resized Image",regular_resized)
#             print("Image Reized SUCESSFULLY")
#             cv2.waitKey(0)
#             cv2.destroyAllWindows()
#         except Exception as e:
#             print(f"Error during resizing: {e}")
        
#     def masalaresize():
#         try:
            
#             scale_percent=int(input("Enter Percentage to be resized: "))
#             original_height,original_width = image.shape[:2]
            
#             height= int(original_height*scale_percent/100)
#             width= int(original_width*scale_percent/100)
            
#             print("What Type of the image resizing do u want?")
#             print("Press 1 for Shrinking Image ")
#             print("Press 2 for Image Zooming with Image ")
#             print("Press 3 for Image Zooming with Quality ")
#             print("Press 4 for Image Fast resize in any Direction ")
            
#             response=int(input("Enter ur Response: "))
#             if response==1:
#                 resized_Shrinking_image = cv2.resize(image, (width,height), interpolation=cv2.INTER_AREA)
#                 cv2.imshow('Shrinked Resized Image', resized_Shrinking_image)
#                 print("Image Reized SUCESSFULLY")
                
#                 cv2.waitKey(0)
#                 cv2.destroyAllWindows()
            
#             elif response==2:
#                 resized_Shrinking_image = cv2.resize(image, (width,height), interpolation=cv2.INTER_LINEAR)
#                 cv2.imshow('Resized Zoom Image', resized_Shrinking_image)
#                 print("Image Reized SUCESSFULLY")
#                 cv2.waitKey(0)
#                 cv2.destroyAllWindows()
#             elif response==3:
#                 resized_Shrinking_image = cv2.resize(image, (width,height), interpolation=cv2.INTER_LANCZOS4)
#                 cv2.imshow('Resized Quality Image', resized_Shrinking_image)
#                 print("Image Reized SUCESSFULLY")
#                 cv2.waitKey(0)
#                 cv2.destroyAllWindows()
#             elif response==4:
#                 resized_Shrinking_image = cv2.resize(image, (width,height), interpolation=cv2.INTER_NEAREST)
#                 cv2.imshow('Fast Resized Image', resized_Shrinking_image)
#                 print("Image Reized SUCESSFULLY")
#                 cv2.waitKey(0)
#                 cv2.destroyAllWindows()
#         except Exception as e:
#             print(f"Error during masala resize: {e}")   
                
# print("Masala Finished")
    

                


    
# while True:
    
#     print("Press 1 to RESIZE with Regular Dimension: ")
#     print("Press 2 to RESIZE with the Masala Percent: ")
#     print("Press 0 to exit:")
#     check=int(input("Enter ur Response: "))
#     if check==1:
#         regularresizer()
#     elif check==2:
#         masalaresize()
#     elif check==0:
#         break

import cv2

image = cv2.imread("C:/Users/sahil/Downloads/DoggyBhai.jpeg")

if image is None:
    print("Image not found")
    exit()

def regularresizer():
    try:
        width = int(input("Enter the new Width: "))
        height = int(input("Enter thr new height: "))
        regular_resized = cv2.resize(image, (width, height))
        cv2.imshow("Regular Resized Image", regular_resized)
        #cv2.imwrite('newdoggyBhai.jpg',regular_resized) these will be using to save image that hass being created but make sure u remove cv2.destroyallwindows() as these will be deleting ur file that has been created or newly modified image
        
        print("Image Resized SUCCESSFULLY")
        cv2.waitKey(7000)
        cv2.destroyAllWindows()
    except Exception as e:
        print(f"Error during resizing: {e}")

def masalaresize():
    try:
        scale_percent = int(input("Enter Percentage to be resized: "))
        original_height, original_width = image.shape[:2]

        height = int(original_height * scale_percent / 100)
        width = int(original_width * scale_percent / 100)

        print("What Type of the image resizing do u want?")
        print("Press 1 for Shrinking Image ")
        print("Press 2 for Image Zooming with Image ")
        print("Press 3 for Image Zooming with Quality ")
        print("Press 4 for Image Fast resize in any Direction ")

        response = int(input("Enter ur Response: "))
        if response == 1:
            resized_Shrinking_image = cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)
            cv2.imshow('Shrinked Resized Image', resized_Shrinking_image)
            print("Image Resized SUCCESSFULLY")
            cv2.waitKey(7000)
            cv2.destroyAllWindows()

        elif response == 2:
            resized_Shrinking_image = cv2.resize(image, (width, height), interpolation=cv2.INTER_LINEAR)
            cv2.imshow('Resized Zoom Image', resized_Shrinking_image)
            print("Image Resized SUCCESSFULLY")
            cv2.waitKey(7000)
            cv2.destroyAllWindows()
        elif response == 3:
            resized_Shrinking_image = cv2.resize(image, (width, height), interpolation=cv2.INTER_LANCZOS4)
            cv2.imshow('Resized Quality Image', resized_Shrinking_image)
            print("Image Resized SUCCESSFULLY")
            cv2.waitKey(7000)
            cv2.destroyAllWindows()
        elif response == 4:
            resized_Shrinking_image = cv2.resize(image, (width, height), interpolation=cv2.INTER_NEAREST)
            cv2.imshow('Fast Resized Image', resized_Shrinking_image)
            print("Image Resized SUCCESSFULLY")
            cv2.waitKey(7000)
            cv2.destroyAllWindows()
    except Exception as e:
        print(f"Error during masala resize: {e}")

print("Masala Finished")

while True:
    print("Press 1 to RESIZE with Regular Dimension: ")
    print("Press 2 to RESIZE with the Masala Percent: ")
    print("Press 0 to exit:")
    check = int(input("Enter ur Response: "))
    if check == 1:
        regularresizer()
    elif check == 2:
        masalaresize()
    elif check == 0:
        print("Exited SUCESSFULLY")
        break
