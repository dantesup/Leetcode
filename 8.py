class Solution:
    def pre_handle(self,str):
        if str[0] in '+-' and str[1].isdecimal():
            end=1
            for i in str[2:]:
                if i.isdecimal():
                    end+=1
                else:
                    break
            return end+1
        elif str[0].isdecimal():
            end=0
            for i in str[1:]:
                if i.isdecimal():
                    end+=1
                else:
                    break
            return end+1


    def myAtoi(self,str):
        str=str.strip()
        if len(str)<=0:
            return 0
        s=Solution()
        if(str[0] in '+-'):
            if len(str)>1 and str[1].isdecimal():
                if int(str[0:s.pre_handle(str)]) < -2 ** 31:
                    return -2 ** 31
                elif int(str[0:s.pre_handle(str)])>2147483647:
                    return 2147483647
                else:
                    return int(str[0:s.pre_handle(str)])
            else:
                return 0
        elif str[0].isdecimal():
            if int(str[0:s.pre_handle(str)])<-2**31:
                return -2**31
            elif int(str[0:s.pre_handle(str)]) > 2147483647:
                return 2147483647
            else:
                return int(str[0:s.pre_handle(str)])
        elif str[0].isdecimal()==0:
            return 0


if __name__=="__main__":
    s=Solution()
    print(s.myAtoi("      -42"))


