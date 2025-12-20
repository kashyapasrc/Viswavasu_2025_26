import os

# Dictionary: old filename -> new filename
rename_map = {
    "page3.pdf": "_చైత్రము_.pdf",
    "page4.pdf": "_వైశాఖము_.pdf",
    "page5.pdf": "_జ్యేష్ఠము_.pdf",

    "page6.pdf": "_ఆషాఢము_.pdf",
    "page7.pdf": "_శ్రావణము_.pdf",
    "page8.pdf": "_భాద్రపదము_.pdf",

    "page9.pdf": "_ఆశ్వీయుజము_.pdf",
    "page10.pdf": "_కార్తికము_.pdf",
    "page11.pdf": "_మార్గశిరము_.pdf",

    "page12.pdf": "_పుష్యము_.pdf",
    "page13.pdf": "_మాఘము_.pdf",
    "page14.pdf": "_ఫాల్గుణము_.pdf"
}

folder_path = "./pdfs/2025_2026/"

for old_name, new_name in rename_map.items():
    old_path = os.path.join(folder_path, old_name)
    new_path = os.path.join(folder_path, new_name)

    if os.path.exists(old_path):
        os.rename(old_path, new_path)
        print(f"Renamed: {old_name} → {new_name}")
    else:
        print(f"File not found: {old_name}")
