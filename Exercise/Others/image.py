from PIL import Image 
  
def main(): 
    try: 
        #Relative Path 
        img = Image.open("data.png")  
          
        #Angle given 
        img = img.rotate(180)  
          
        #Saved in the same relative location 
        img.save("rotated_picture.png") 
    except IOError: 
        pass
  
if __name__ == "__main__": 
    main()