import pickle

g9 = {'Honors Chemistry': ['B+',1], 'Honors Geometry and Trigonometry': ['B+',1],
      'Honors Latin II': ['B+',1], 'Digital Media Arts I': ['B+',.5], 'English 9': ['A-',1],
      'Health and Wellness I': ['A',.5], 'World History 1: Rise of Civilization': ['A',.5],
      'World History 2: 1610 to 1919': ['A-',.5]}

g10 = {'AP Computer Science Principles': ['A',1],
       'Honors History: Rise of the Dictators': ['A+',.5],
       'Biology':['A',1], 'Honors Latin III': ['A-',1], 'Honors PreCalculus': ['B+',1],
       "Comparitive World Religion": ['A+',.5],"English 10": ['B+',1],
       "Health & Wellness II 10th": ['B+',.5], "World History 3: 1919 to Present": ["A-",.5]}

g11 = {'AP Calculus AB': ['',1], 'AP Economics: Micro': ['',.5], 'AP Economics: Macro': ['',.5],
       'Honors Physics': ['',1], 'Honors US History Survey': ['',1], 'Honors Latin IV': ['',1],
       'Honors Technology and Literature': ['',1], 'Engineering and Robotics': ['',1],
       'Fiction Workshop': ['',1]}

g12 = {}

#First is GPA, second is minimum (decimal) percentage of the grade
legend = {"A+":[4.3,.98], "A":[4.0,.93], "A-":[3.7,.9], "B+":[3.3,.87], "B": [3.0,.83],
          "B-": [2.7,.8], "C+": [2.3,.77], "C":[2.0,.73], "C-":[1.7,.7], "D+":[], "D":[],
          "D-":[], "F":[0,0]}

menuchoice = input('Would you like to:\n1.Get Quick Report\n2. Do Something Else\n')


if menuchoice == 1:
    print 'Transcipt:\n'
    print '9th Grade:\n'
    for key in g9:
        print key + ": " + str(g9[key][0])
    print '\n10th Grade:\n'
    for key in g10:
        print key + ": " + str(g10[key][0])
    print '\n11th Grade:\n'
    for key in g11:
        print key + ": " + str(g11[key][0])
    print '\n12th Grade:\n'
    for key in g12:
        print key + ": " + str(g12[key][0])

    g9unweightedgpa = []
    g10unweightedgpa = []
    g11unweightedgpa = []
    g12unweightedgpa = []

    for key in g9:
        if g9[key] > 0:
            key1 = g9[key][0]
            g9unweightedgpa.append(legend[key1][0])
            g9unweightedgpa = sum(g9unweightedgpa) / len(g9unweightedgpa)
        else:
            pass
    for key in g10:
        if g10[key] > 0:
            key1 = g10[key][0]
            g10unweightedgpa.append(legend[key1][0])
            g10unweightedgpa = sum(g10unweightedgpa) / len(g10unweightedgpa)
        else:
            pass
    for key in g11:
        if g11[key] > 0:
            key1 = g11[key][0]
            g11unweightedgpa.append(legend[key1][0])
            g11unweightedgpa = sum(g11unweightedgpa) / len(g11unweightedgpa)
        else:
            pass
    for key in g12:
        if g12[key] > 0:
            key1 = g12[key][0]
            g12unweightedgpa.append(legend[key1][0])
            g12unweightedgpa = sum(g12unweightedgpa) / len(g12unweightedgpa)
        else:
            pass

    g9unweightedgpa = sum(g9unweightedgpa) / len(g9unweightedgpa)
    unweightedgpa = g9unweightedgpa + g10unweightedgpa + g10unweightedgpa + g11unweightedgpa

    print '\n\nGPA:\n'
    print 'Unweighted GPA: ' + unweighted
    print '\nWeighted GPA: ' + weighted

else:
    pass
