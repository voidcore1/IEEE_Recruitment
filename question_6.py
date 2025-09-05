import pprint
cutoff_list = [
    ("Pilani", "Chemical", 224),
    ("Pilani", "Electrical & Electronics", 286),
    ("Pilani", "Mechanical", 254),
    ("Pilani", "Computer Science", 327),
    ("Pilani", "Electronics & Instrumentation", 279),
    ("Pilani", "Electronics & Communication", 306),
    ("Pilani", "Mathematics and Computing", 309),
    ("Pilani", "M.Sc. Biological Sciences", 213),
    ("Pilani", "M.Sc. Chemistry", 213),
    ("Pilani", "M.Sc. Economics", 270),
    ("Pilani", "M.Sc. Mathematics", 236),
    ("Pilani", "M.Sc. Physics", 235),
    ("Goa", "Chemical", 239),
    ("Goa", "Electrical&Electronics", 278),
    ("Goa", "Mechanical", 254),
    ("Goa", "Computer Science", 301),
    ("Goa", "Electronics&Instrumentation", 270),
    ("Goa", "Electronics&Communication", 287),
    ("Goa", "Mathematics and Computing", 295),
    ("Goa", "M.Sc. Biological Sciences", 234),
    ("Goa", "M.Sc. Chemistry", 236),
    ("Goa", "M.Sc. Economics", 263),
    ("Goa", "M.Sc. Mathematics", 249),
    ("Goa", "M.Sc. Physics", 248),
    ("Hyderabad", "Chemical", 238),
    ("Hyderabad", "Civil", 235),
    ("Hyderabad", "Electrical & Electronics", 275),
    ("Hyderabad", "Mechanical", 251),
    ("Hyderabad", "Computer Science", 298),
    ("Hyderabad", "Electronics & Instrumentation", 270),
    ("Hyderabad", "Electronics & Communication", 284),
    ("Hyderabad", "Mathematics and Computing", 293),
    ("Hyderabad", "B. Pharm", 161),
    ("Hyderabad", "M.Sc. Biological Sciences", 234),
    ("Hyderabad", "M.Sc. Chemistry", 235),
    ("Hyderabad", "M.Sc. Economics", 261),
    ("Hyderabad", "M.Sc. Mathematics", 247),
    ("Hyderabad", "M.Sc. Physics", 245),
]

cutoff_dit = {}

for campus, branch, cutoff in cutoff_list:
    if campus not in cutoff_dit:
        cutoff_dit[campus] = {}
    cutoff_dit[campus][branch] = cutoff

pprint.pprint(cutoff_dit)