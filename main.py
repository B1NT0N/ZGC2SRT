import datetime 
import sys


def convert():
    #open file
    filename = sys.argv[-1]
    with open(filename, 'r') as infile:
        lines = infile.readlines()
        star_time = True
        first = True

        #get time and phrase
        for index , line in enumerate(lines):
            text = line.split(":")
            
            hours = text[0]
            minutes = text[1]
            seconds = text[2][:2]
            
            if len(text) > 4:
                for i in range(len(text)-4):
                    phrase = text[3]+text[3+i]
            else:
                phrase = text[3][1:]
            
            if star_time == False:
                if first == True:
                    with open("output.txt", 'w+') as outfile:
                        outfile.write(f"{index}\n")
                        outfile.write(f"{next_hours}:{next_minutes}:{next_seconds},000 --> {hours}:{minutes}:{seconds},000\n")
                        outfile.write(f"{next_phrase}\n")
                        first = False 
                else :
                    
                        with open("output.txt", 'a') as outfile:
                            outfile.write(f"{index}\n")
                            outfile.write(f"{next_hours}:{next_minutes}:{next_seconds},000 --> {hours}:{minutes}:{seconds},000\n")
                            outfile.write(f"{next_phrase}\n")
                    
            next_text = text
            next_hours = hours
            next_minutes = minutes
            next_seconds = seconds
            next_phrase = phrase

            #checking for potencial error
            
            star_time = False
            
                
                
            
            
            
            
            
if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print("\n")
        print("Help: main.py <filename.txt> \n")
        sys.exit(-1)
    convert()