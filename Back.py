

            const filePromises = files.map(file => {
                if (file.endsWith('.mp4') || file.endsWith('.avi') || file.endsWith('.mov')) {
                    const inputPath = path.join(videosDir, file);
                    const outputPath = path.join(audiosDir, `${path.basename(file, path.extname(file))}.mp3`);

                    return new Promise((resolve, reject) => {
                        ffmpeg(inputPath)
                            .outputOptions('-vn', '-ab', '128k', '-ar', '44100')
                            .toFormat('mp3')
                            .save(outputPath)
                            .on('error', (err) => reject(`Error converting file: ${err}`))
                            .on('end', () => {
                                result.push(outputPath);
                                resolve(result);
                            });
                    });
                }
                return Promise.resolve();
            });

            Promise.all(filePromises).then(() => resolve(result));
        });
    });

    const convertedAudios: string[] = await promises;

    if (convertedAudios.length === 0) throw new Error(`В этой директории нет видеофайлов: ${videosDir}`);

    return convertedAudios;
}

for a1 in printable:
    for a2 in printable:
        for a3 in printable:
            for a4 in printable:
                print(a1+a2+a3)
                num = 5
print(type(num))

stroka = "A"
print(type(stroka))
print(4 == 4)
print(type(4 == 4))

string = "Helo World!"
print("Length of string -", len(string))

string ="Hello world"
string_2 = "- Hello to youl"

string_sum = string + string_2
big_str = string * 3
print("string_sum -",string_sum)
print("big_str -", big_str)

string ="Hello world"
string_list = string.split()
print(string_list)

string_1 = "I am string and I KILL YOU"
print("upper -",string_1.upper())
print("title -", string_1.title())
print("capitalize -",string_1.capitalize())
print("lower -",string_1.lower())
print(string_1.startswith("I am"))
print(string_1.endswith("printed"))
#num = 12
#string_num = "Age 12"
#print(string_num)
string_1 = "Axmed"
string_2 = "12"
string_num = "4"
print(string_1.isalpha())
print(string_2.isdigit())
print(string_num.isalnum())
string = "PYTHON AAAA kRIMINAL xAKER"
print(string[0:40])

list = []
name = "Ayaz"
list.append(3)
list.append("r")
list.append(name)
print(list)
list.remove("r")
print(list)
list.insert(2, "HI")
print(len(list))
list.pop(2)
print(list)
list_1 = [1,2,3]
list_2 = [4,5,6]
list_3 = list_1 + list_2
print(list_3)
list_1.sort()
print(max(list_1))
print(min(list_1))
print(sum(list_1))
list_2.sort()
print(max(list_2))
print(min(list_2))
print(sum(list_2))
age2 = int(input("your age:"))
name3 = input("your name:")
print(age