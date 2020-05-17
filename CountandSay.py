class Solution:
    def countAndSay(self, n):
        firstValue = "1"
        if(n > 1):
            return self.createcall(self.countAndSay(n-1))
        else:
            return firstValue



    
    def createcall(self,prev):
        output = ""
        count = 1
        for i in range(len(prev)):
            if(i==len(prev)-1):
                output = output + str(count)
                output = output + prev[i]
                return output
            if(prev[i]==prev[i+1]):
                count = count + 1
            else:
                output = output + str(count)
                output = output + prev[i]
                count = 1