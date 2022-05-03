# Information hiding
class Solution():
    __privatcounter = 0

    def sum(self):
        self.__privatcounter += 1
        print(self.__privatcounter)


sol1 = Solution()
sol1.sum()
sol1.sum()

# Die Klassenvariabel kann nicht einfach so ausgegeben und veraendert werden, da diese verseckt ist!
#print(sol1.__privatcounter)

# Um die Klassenvariabel auszugeben, muss man diese so ansprechen.
print(sol1._Solution__privatcounter)