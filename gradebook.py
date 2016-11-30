import pickle
from pandas import *
import numpy as np
import matplotlib.pyplot as plt

g9 = {'Grade' : Series(['B+', 'B+', 'B+', 'B+', 'A-', 'A-', 'A', 'A'],
                      index=['Honors Chemistry', 'Honors Geometry and Trigonometry', 'Honors Latin II', 'Digital Media Arts I',
                             'Health and Wellness I', 'English 9', 'World History 1: Rise of Civilization',
                             'World History 2: 1610 to 1919']), 'Credit' : Series([1,1,1,.5,1,.5,.5,.5], index=['Honors Chemistry', 'Honors Geometry and Trigonometry', 'Honors Latin II', 'Digital Media Arts I',
                             'Health and Wellness I', 'English 9', 'World History 1: Rise of Civilization',
                             'World History 2: 1610 to 1919'])}
g9df = DataFrame(g9)


g10 = {'Grade' : Series(['A', 'A+', 'A', 'A-', 'B+', 'A+', 'B+', 'B+', 'A-'],
                      index=['AP Computer Science Principles', 'Honors History: Rise of the Dictators', 'Honors Biology', 'Honors Latin III',
                             'Honors PreCalculus', 'Comparitive World Religion', 'English 10',
                             'Health & Wellness II 10th', "World History 3: 1919 to Present"]), 'Credit' : Series([1,.5,1,1,1,.5,1,.5,.5], index=['AP Computer Science Principles', 'Honors History: Rise of the Dictators', 'Honors Biology', 'Honors Latin III',
                             'Honors PreCalculus', 'Comparitive World Religion', 'English 10',
                             'Health & Wellness II 10th', "World History 3: 1919 to Present"])}
g10df = DataFrame(g10)


g11 = {'Grade' : Series(['','','','','','','','',''] ,
                        index=['AP Calculus AB', 'AP Economics: Micro', 'AP Economics: Macro', 'Honors Physics', 'Honors US History Survey',
                               'Honors Latin IV', 'Honors Technology and Literature', 'Engineering and Robotics', 'Fiction Workshop']), 'Credit' : Series([1,.5,.5,1,1,1,.5,.5,.5], index = ['AP Calculus AB', 'AP Economics: Micro','AP Economics: Macro', 'Honors Physics', 'Honors US History Survey',
                               'Honors Latin IV', 'Honors Technology and Literature', 'Engineering and Robotics', 'Fiction Workshop'])}
g11df = DataFrame(g11)


g12 = {'Grade' : Series(['','',''] , index=['Class 1', 'Class 2', 'Class 3']), 'Credit' : Series([1,1,1], index=['Class 1', 'Class 2', 'Class 3'])}
g12df = DataFrame(g12)


#First is GPA, second is minimum (decimal) percentage of the grade
legend = {'GPA' : Series([4.3,4.0,3.7,3.3,3.0,2.7,2.3,2.0,1.7,0,0,0,0.0], index=['A+','A','A-','B+','B','B-','C+','C','C-','D+','D','D-','F']), 'Lowest Decimal Percentage Grade' :
    Series([.98,.93,.9,.87,.83,.8,.77,.73,.7,0,0,0,.0], index=['A+','A','A-','B+','B','B-','C+','C','C-','D+','D','D-','F'])}
legenddf = DataFrame(legend)
