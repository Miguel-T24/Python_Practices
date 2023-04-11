# 14. Write a python program to sor a given dictionary key


color_dict = {'red':'#FF0000',
          'green':'#008000',
          'black':'#000000',
          'white':'#FFFFFF'}

for key in sorted(color_dict):
    print("{} : {}".format(key, color_dict[key]))
    
