

def addElement(T,e):
    if T == [""] :
        T.append(list(e))
    else :
        for i in T[1] : 
            if e == i :
                break
        if e != i :
            T[1].append(e)       
    return T


import unittest

class NumberTreeTestCase(unittest.TestCase):
    def setUp(self) :
        self.a = 5
        self.emptyT = [""]
        
    def test1(self):
        self.assertListEqual(self.emptyT,[""])

    def test_addOneElement(self) :
        self.assertListEqual(addElement(self.emptyT,"9"),["",["9"]])

    def test_diffElement(self) :
        for j in ["5","6","5"] :
            self.emptyT = addElement(self.emptyT,j)
        self.assertListEqual(self.emptyT,["",["5","6"]])

    def test_addThreeDigit(self) :
        self.assertListEqual(addElement(self.emptyT,"914"),["",["9",["1",["4"]]]])


        
if __name__ == '__main__' :
    unittest.main()
    
