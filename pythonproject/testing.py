import os
path="G:\\3. MUSIC"
song_list=os.listdir(path)

song_name=input("Enter the name of the song you want to play:")

n=1
bl=[]
for i in song_list:
    if song_name.upper() in i.upper():
        print(n,i)
        bl.append(i)
        n=n+1

if len(bl)==1:
    index=song_list.index(bl[0])
    os.startfile(os.path.join(path,song_list[index]))
elif len(bl)>1:
    print("\nThere are multiple options for the name",song_name)
    print("From the above songs which one do you want to play")
    ch=int(input("Enter the number corresponding to your choice:"))
    print("\n")
    song=bl[ch-1]

    for i in song_list:
        if song in i:
            index=song_list.index(i)
            os.startfile(os.path.join(path,song_list[index]))
