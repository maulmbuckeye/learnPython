import unittest
import sys

class nTree(object) :

    def __init__(self):
        self.tree = []

    def show(self) :
        return self.tree


    def set(self,l) :
        self.tree = l

    def str_(self,result) : 
    
        print ("result=", result)
        if self.show() == [] :
            return ""
        else : 
            for i in self.show() :
                result.append(i[0])
            return result

    def str(self) :
        result = []
        return self.str_(result)
                



class nTreeTests(unittest.TestCase) :
    
    def setUp(self) :
        self.nt = nTree()
        self.list1 = [ "1", []]
        self.list2 = [ "2", []]
        self.list12 = [self.list1,self.list2]
        self.list34 = ["3", ["4", []]  ]

    def testEmpty(self):
        self.assertListEqual(self.nt.show(),[])

    def testEmptyStr(self) :
        self.assertEqual(self.nt.str(), "")

    def testList12Str(self) :
        self.nt.set(self.list12)
        print(self.nt.show())
        self.assertListEqual(self.nt.str(),["1","2"])

    def testList34Str(self) :
        self.nt.set(self.list34)
        print(self.nt.show())
        self.assertListEqual(self.nt.str(),["34"])



    def xtestAdd1SingleDigt(self):
        self.nt.add("9")
        self.assertListEqual(self.nt.show(),[ ["9",[]]])

    def xtestAdd3SingleDigits(self):
        self.nt.add("9")
        self.nt.add("0")
        self.nt.add("9")
        self.assertListEqual(self.nt.show(),[["9",[]],["0",[]]])
        
    def xtestTwoDigit(self):
        self.nt.add("12")
        self.assertListEqual(self.nt.show(), self.list12)

    def xtestThreeDigits(self) : 
        self.nt.add("123")
        self.assertListEqual(self.nt.show(), self.list123)
        
    def xtestStrEmpty(self) :
        self.assertEqual(self.nt.str(),"")

    def xtestStr1SingleDigits(self) :
        self.nt.add("1")
        self.assertEqual(self.nt.str(),"1")

    def xtestStr1ThreeDigits(self) :
        self.nt.add("123")
        self.assertEqual(self.nt.str(),"123")
        
        

        

if __name__ == "__main__" :
    unittest.main()

    
