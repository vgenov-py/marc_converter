a = ("001",
"007",



"015",
"008",
"008",
"041",
"041",
"041",
"041",
"007",
"008",


"017",
"020",
"024",
"028",
"040",
"080",
"084",
"100",
"700",
"110",
"710",
"111",

"130",
"240",
"243",
"245",
"246",
"740",
"250",
"260",
"264",
"260",
"264",
"300",
"300",
"300",
"300",
"336",
"337",
"338",
"347",
"344",
"382",
"508",
"511",
"518",
"505",
"440",
"490",
"500",


"510",


"520",
"521",

"530",
"533",
"538",
"540",
"546",
"561","586", "593", "594", "595", "596","597",
"600",
"610",

"630",
"650",
"651",
"653",
"655",
"856"

)


a = list(set(a))
for t in sorted(a):
    print(f't_{t},')
