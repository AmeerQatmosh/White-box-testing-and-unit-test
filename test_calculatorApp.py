import unittest
from unittest import mock
from unittest.mock import patch
from calculatorApp import *
import calculatorApp

from asyncio.windows_events import NULL
from ast import Add
from decimal import DivisionUndefined



class TestCalculate(unittest.TestCase):
    def setUp(self):
        print("Setup .. ")
       ## self.patcher1 = patch('calculatorApp.add', return_value = 5)
       ## self.MockClass1 = self.patcher1.start()
       ## self.addCleanup(self.patcher1.stop)

    ## def test_AddPass(self):
    ##    self.assertEqual(add(6,3), 9)# will execute the add
    ##    self.assertEqual(calculate('1',6,3), 5) # will call the mock

    ## def test_AddInvalid(self):
    ##    self.assertNotEqual(calculate('1',9,3), 9)

    ## def test_DividByZerrorEx1(self):
    ##    with self.assertRaises(ValueError):
    ##         calculate('4','3','w')
    
    ##OR

    ## def test_DividByZerrorEx2(self):
    ##    self.assertRaises(ValueError, calculate, '4','3','w') 

    ## def test_DividByZerrorRegex(self):
    ##    with self.assertRaisesRegex(ValueError, "input is not a number!"):
    ##         calculate('4','3','w')

    
    ## def test_AddPassWithMockEx1(self):
    ##    with mock.patch('calculatorApp.add', return_value = 6):
    ##        result = calculate('1',2,4)
    ##    self.assertEqual(result, 6)

    ##@mock.patch('calculatorApp.add', return_value = 4)
    ##def test_AddPassWithMockEx2(self, mock_check):
    ##    result = calculate('1',3,2)
    ##    self.assertEqual(result, 4)


    ## def test_AddPassWithMocEx3(self):
    ##    assert calculatorApp.add is self.MockClass1
    ##    self.assertEqual(calculate('1',2,6), 5)

###########################################        check_user_input Test Cases     ###########################################

    def testCase_1_check_user_input(self):
        self.assertEqual(ValueError,check_user_input(""))   

    def testCase_2_check_user_input(self):
        self.assertEqual(check_user_input("15"), 15)

    def testCase_3_check_user_input(self):
        self.assertEqual(check_user_input("3.7"), 3.7)

    def testCase_4_check_user_input(self):
        self.assertEqual(ValueError,check_user_input("string"))    

###########################################        Add Test Cases     ###########################################
  
    def testCase_1_Add(self):
        self.assertEqual(add(9,3),12)

###########################################       Subtract Test Cases     ###########################################

    def testCase_1_Subtract(self):
        self.assertEqual(subtract(9,3),6)   

###########################################       Multiply Test Cases     ###########################################

    def testCase_1_Multiply(self):
        self.assertEqual(multiply(9,3),27)  

###########################################       Divide Test Cases     ###########################################

 
    def testCase_1_Divide(self):
        self.assertEqual(divide(9,3),3)   

    def testCase_2_Divide(self):
        self.assertRaises(ZeroDivisionError, divide(9,0))    

    def testCase_3_Divide(self):
        self.assertEqual(divide(0,3),0)    
       

###########################################        Calculate Test Cases     ###########################################\

    def testCase_1_Calculate (self):
        self.assertRaises(ValueError, calculate('1', 0, 7))

    def testCase_2_Calculate (self):
        self.assertRaises(Exception, calculate('7', 7, 8))

    def testCase_3_Calculate (self):
        with mock.patch('calculatorApp.add', return_value = 10):
         result = calculate('1',8,2)
        self.assertEqual(result, 10)    

    def testCase_4_Calculate (self):
        with mock.patch('calculatorApp.subtract', return_value = 6):
         result = calculate('2',8,2)
        self.assertEqual(result, 6) 

    def testCase_5_Calculate (self):
        with mock.patch('calculatorApp.multiply', return_value = 16):
         result = calculate('3',8,2)
        self.assertEqual(result,16) 

    def testCase_6_Calculate (self):
        with mock.patch('calculatorApp.divide', return_value = 4):
         result = calculate('4',8,2)
        self.assertEqual(result, 4) 

    def testCase_7_Calculate (self):
         self.assertRaises(ZeroDivisionError,calculate('4', 8, '0')) 

       
###########################################       IsExit Test Cases     ###########################################

    def testCase_1_IsExit(self):
        self.assertEqual(isExit("no"),True)   

    def testCase_2_IsExit(self):
        self.assertEqual(isExit("yes"),False)     

    def testCase_3_IsExit(self):
        self.assertRaises(ValueError, isExit ("else"))    



    def tearDown(self):
        print("tearDown .. ")
        #self.patcher1.stop()#or add this and remove self.addCleanup(self.patcher1.stop) in startup but this is not recommened!


## class TestCalculateWithoutMock(unittest.TestCase):
##    def test_AddPass(self):
##        self.assertEqual(add(6,3), 9)
##        self.assertEqual(calculate('1',6,3), 9)

if __name__ == '__main__':
	unittest.main()
