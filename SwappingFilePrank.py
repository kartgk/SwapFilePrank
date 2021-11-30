def SwapFileData():
    Real = input('Enter the original file name: ')
    Fake = input('Enter the duplicate file name: ')
    original= open(Real,'r')
    duplicate = open(Fake,'r')
    originalDocument = original.readlines()
    duplicateDocument = duplicate.readlines()
    original2 = open(Real,'w')
    duplicate2 = open(Fake, 'w')
    original2.writelines(duplicateDocument)
    duplicate2.writelines(originalDocument)

SwapFileData()
