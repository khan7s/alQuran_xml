import xml.etree.ElementTree as et

tree = et.parse("./quranChapter.xml")
root = tree.getroot()

# for val in root.findall("sura"):
#     chapter = val.attrib.get("tname")
#     print(chapter)

# it will get you surah names which have Sajdah ayat
# for val in root.findall("sura"):
#     if val.attrib.get("sajda_index") != "NA":
#         # print(val.attrib.get("tname"),val.attrib.get("sajda_aya"))
#         idx = int(val.attrib.get("index")) - 1

#         # Print all attributes and their values
#         sura = root[idx]
#         for attr, val in sura.attrib.items():
#             print(f"{attr}: {val}")
#         print()

# get sajdah details in chapters
# with open("sajdah_chapterlist.txt", "w") as f:
#     for val in root.findall("sura"):
#         if val.attrib.get("sajda_index") != "NA":
#             # print(val.attrib.get("tname"),val.attrib.get("sajda_aya"))
#             idx = int(val.attrib.get("index")) - 1

#             # Print all attributes and their values
#             sura = root[idx]
#             for attr, val in sura.attrib.items():
#                 # line = 
#                 f.write(f"{attr}: {val}"+ "\n")
#             f.write("\n")

# get chapters by order of revelation
res = [(int(val.get("order")),val.get("tname"),val.get("ename"),val.get("index")) for val in root.findall("sura")]
res.sort(key=lambda x:x[0])
# print(res)
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

print("exit")