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
            if text[0][0] != "0":
                pass
            else:
                hours = text[0]
                minutes = text[1]
                seconds = text[2][:2]
                phrase = text[3]
                if len(text) > 4:
                    for i in range(len(text)-4):
                        phrase = phrase+text[4+i]
                else:
                    phrase = text[3][1:]
                    
                if star_time == False:
                    if first == True:
                        with open(f"{filename}.srt", 'w+') as outfile:
                            outfile.write(f"{index}\n")
                            outfile.write(f"{next_hours}:{next_minutes}:{next_seconds},000 --> {hours}:{minutes}:{seconds},500\n")
                            outfile.write(f"{next_phrase}\n")
                            first = False 
                    else :
                        
                            with open(f"{filename}.srt", 'a') as outfile:
                                outfile.write(f"{index}\n")
                                outfile.write(f"{next_hours}:{next_minutes}:{next_seconds},500 --> {hours}:{minutes}:{seconds},500\n")
                                outfile.write(f"{next_phrase}\n")
                
                if star_time == False and index == len(lines) -1:
                        with open(f"{filename}.srt", 'a') as outfile:
                                outfile.write(f"{index+1}\n")
                                outfile.write(f"{hours}:{minutes}:{seconds},500 --> {hours}:{minutes}:{str(int(seconds)+2)},500\n")
                                outfile.write(f"{phrase}\n")
                
                next_text = text
                next_hours = hours
                next_minutes = minutes
                next_seconds = seconds
                next_phrase = phrase
                
                star_time = False
            

if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print("\n")
        print("Help: main.py <filename.txt> \n")
        sys.exit(-1)
    convert()