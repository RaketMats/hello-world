from xml.dom import minidom
import pickle

# The purpose of this application is to simulate the Scaled Agile Framework
# The main information sources are a 'Program backlog' and a 'Release train'
# The backlog can be filled with 'Features' which are going through the stages defining, elaborating, implementing and testing
# Accordingly the 'Release train' is filled with assumed release content, from the definitions, and it is becoming more and more
# explicit until testing is finally done and the exact content of the release is made. 
# The simulation has then run a full circle and continues from definition
# 
# Test of inheritance. This is the base class        
class cCustomer:

    m_strName = ''

    def __init__(self, a_strName):
        self.m_strName = a_strName
        print 'Constructing cCustomer', self.m_strName
     
    def sayHi(self):
        print 'This is a customer named: ', self.m_strName

# This is the class that holds all data
class cSession:

    m_strSessionName = ''
    m_guid = 0
    m_strCustomers = [] # To be able to pickle this list of objects, it must be used in the constructor, see below

    def __init__(self, a_strName):
        self.m_strSessionName = a_strName
        self.m_strCustomers = [] # This seemingly unecessary initialisation is needed to pickle the object list.
                                 # If not present, the pickle will not contain objects in the list

    def addCustomer(self, a_strName):
        self.m_strCustomers.append(cCustomer(a_strName))
        #self.m_strCustomers.append(a_strName)
        self.m_guid = self.m_guid+1

    def showAll(self):
        print 'Session name: ', self.m_strSessionName
        print 'Current guid is: ', self.m_guid
        for oView in self.m_strCustomers:
            oView.sayHi()
#        print self.m_strCustomers

# Test of inheritance. This is the base class        
class cPoints:

    m_strID = ''
    m_nBalance = 0

    def __init__(self, a_strID, a_strValue):
        self.m_strID = a_strID # This is an object variable, i.e. does not keep value between instances of cPoints
        self.m_nBalance = int(a_strValue)
        #print 'Constructing cPerson', self.m_strName

    def credit(amount):
        m_nBalance = m_Balance-amount
        
    def sayHi(self):
        print 'Point: ', self.m_strID, ' Value: ', self.m_nBalance

# Test of inheritance, this is a derived class
class cPoints2(cPoints):

    m_strOwner = ''

    def __init__(self, a_strID, a_strValue, a_strOwner):
        cPoints.__init__(self, a_strID, a_strValue)
        self.m_strOwner = a_strOwner
        #print 'Constructing cPoints2', self.m_strOwner

    def sayHi(self):
        print 'Owner: ', self.m_strOwner, ' ID: ', self.m_strID, ' Balance: ', self.m_nBalance

# the main routine    
if __name__ == '__main__':

    #p1 = cPoints2('Ascom', '1234')
    #p1.sayHi()
    b1 = True

    oAll = cSession('Testing') 
        
    print 'available commands: add, cred, view, quit, load, save, info'
    while (b1):
        cmd = raw_input('yes, what do you want? ')
        
        if (cmd == 'add'):
            name = raw_input('enter customer name: ')
            oAll.addCustomer(name)

        elif (cmd == 'cred'):
            strID = raw_input('enter id: ')
            print strID
            strAmount = raw_input('enter amount: ')
#            for oCred in p2:
#                if oCred.m_strID == strID:
#                    oCred.m_nAmount = oCred.m_nAmount-int(strAmount)
#                    oCred.sayHi()
                    
        elif (cmd == 'view'):
            oAll.showAll()

        elif (cmd == 'save'):
            pickle_file = file("savestate.pickle", "w")
            pickle.dump(oAll, pickle_file)
            del pickle_file
            
        elif (cmd == 'load'):
            pickle_file = file("savestate.pickle")
            oAll = pickle.load(pickle_file)

        elif (cmd == 'info'):
            print 'Pickle version is: ', pickle.format_version
            
        elif (cmd == 'quit'):
            print 'Bye, bye!'
            b1 = False

        else:
            print 'Dont understand!'
