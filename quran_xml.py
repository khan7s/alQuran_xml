import xml.etree.ElementTree as et

tree = et.parse("/home/surkhab-khan/Drive Linux/Verse/quran_xml/quranChapter.xml")
root = tree.getroot()

surah = root.find("Chapters")
juzz = root.find("juzs")

# for val in surah.findall("sura"):
#     chapter = val.attrib.get("tname")
#     print(chapter)

# it will get you surah names which have Sajdah ayat
# for val in surah.findall("sura"):
#     if val.attrib.get("sajda_index") != "NA":
#         # print(val.attrib.get("tname"),val.attrib.get("sajda_aya"))
#         idx = int(val.attrib.get("index")) - 1

#         # Print all attributes and their values
#         sura = surah[idx]
#         for attr, val in sura.attrib.items():
#             print(f"{attr}: {val}")
#         print()

# get sajdah details in chapters
# with open("sajdah_chapterlist.txt", "w") as f:
#     for val in surah.findall("sura"):
#         if val.attrib.get("sajda_index") != "NA":
#             # print(val.attrib.get("tname"),val.attrib.get("sajda_aya"))
#             idx = int(val.attrib.get("index")) - 1

#             # Print all attributes and their values
#             sura = surah[idx]
#             for attr, val in sura.attrib.items():
#                 # line = 
#                 f.write(f"{attr}: {val}"+ "\n")
#             f.write("\n")

# get chapters by order of revelation
res = [(int(val.get("order")),val.get("tname"),val.get("ename"),val.get("index")) for val in surah.findall("sura")]
res.sort(key=lambda x:x[0])
# # print(res)
# with open("chapterByOrder.txt","w") as f:
#     f.write(f"OrderId\tchapter Name\tEng Name\tChapter Number")
#     f.write("\n")
#     for t,tname,ename,id in res:
#         line = f"Order:\t{t}\t{tname}\t{ename}\t(chapter:{id})"
#         f.write(line+"\n")

# check if any chapter have same index and order:
print("chapters with same number as revelation sequence:")
for ls in res:
    if ls[0] == int(ls[3]):
        print(ls[0],"\t",ls[1],"\t",ls[3])


# get Juzz start chapter:verse 
for val in juzz.findall("juz"):
    print(f"Juz {val.attrib.get("index")} start from verse {val.attrib.get("aya")} of chapter {val.attrib.get("sura")}\n")

# export to txt file
# with open("juz.txt","w") as f:
#     f.write("Juz detail - start from chapter:verse (surah:ayat)\n\n")
#     for val in juzz.findall("juz"):
#         line = f"Juz {val.attrib.get("index")} start from verse {val.attrib.get("aya")} of chapter {val.attrib.get("sura")}\n"
#         f.write(line)

print("exit")