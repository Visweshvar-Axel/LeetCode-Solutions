
class Solution:
    def defangIPaddr(self, address: str) -> str:
        ##own
        res = ""
        for c in address:
            if(c == '.'):
                res += "[.]"
            else: 
                res+=c
        return res
        ##fun
        # return address.replace(".","[.]")
        ##fun
        # res = address.split(".")
        # return "[.]".join(res)
