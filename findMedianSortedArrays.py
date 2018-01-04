class Solution(object):
    def findMedianSortedArrays(self,nums1,nums2):
            L1=len(nums1)
            L2=len(nums2)
            L=L1+L2
            out=[]
            if L1!=0 and L2 !=0:
                out=self.kAndkPlusOne(nums1,nums2,int(L/2)-1)
            elif L2 !=0:
                out.append(nums2[int(L/2)-1])
                out.append(nums2[int(L/2)])
            elif L1 !=0:
                out.append(nums1[int(L/2)-1])
                out.append(nums1[int(L/2)])
            else:
                return 0
            if L%2==0:
                #print(out)
               # print(L)
                return (out[0]+out[1])/2.0
            else:
                #print(out)
               # print(L)
                return out[1]   
    def kAndkPlusOne(self,a,b,k):
        #find the kth and kth+1 largest value in the merged list formed from a and b
        #a and b are sorted lists
        # Do this O(log(N+M)) time
        La=len(a) #number of a values under consideration.  this will decrease as we approach a solution
        Lb=len(b) #number of a values under consideration.  this will decrease as we approach a solution
        st_a=0   #starting index of a    this will increase as we elminate possible answers
        st_b=0   #starting index of b.   this will increase as we elminate possible answers
        out=[-1,-1]
        TotalL=La+Lb 
        if k>La+Lb-1:
            raise Exception('k is too large')
        if k==La+Lb-1:  #then we know it is the largest element
            out=max(a[La-1],b[Lb-1])
            return out
        if k==0:  #then it is the smallest
            out[0]=min(a[st_a],b[st_b])
            if La==1 and a[st_a]<=b[st_b]: #a picked
                out[1]=b[st_b]
            elif La==1 and a[st_a]>b[st_b]: # b picked
                if Lb>1:
                    out[1]=min(a[st_a],b[st_b+1])
                else:
                    out[1]=a[st_a]
            elif Lb==1 and a[st_a]>b[st_b]: # b picked
                    out[1]=a[st_a]
            elif Lb==1 and a[st_a]<=b[st_b]:  #a picked
                if La>1:
                    out[1]=min(a[st_a+1],b[st_b])
                else:
                    out[1]=b[st_b]
            else:               
                out[1]=min(min(max(a[st_a],b[st_b]),a[st_a+1]),b[st_b+1])
            return out
        it=0
       
        while La>0 and Lb>0:
            #print('hi')
            it+=1
            midA=max(int(La/2)-1,0)+(st_a)
            midB=max(int(Lb/2)-1,0)+(st_b)
            T=(midA+midB)
            LaOld=La
            LbOld=Lb
            #print(T)
            #print(midA)
            #print(midB)
            #print(st_a+st_b)
            #print(st_a)
            #print(st_b)
            #print(a[st_a])
            #print(b[st_b])

            #print(st_a)
            #print(st_b)
            print((La,Lb))
            if k==st_a+st_b:  #then everything less than index k has been removed
                #we know k is the smallest element
                out[0]=min(a[st_a],b[st_b])
                if La>1 and Lb>1:
                    out[1]=min(min(max(a[st_a],b[st_b]),a[st_a+1]),b[st_b+1])
                    return out
                elif La>1:
                    out[1]=min(max(a[st_a],b[st_b]),a[st_a+1])
                    return out
                elif Lb>1:
                    out[1]=min(max(a[st_a],b[st_b]),b[st_b+1])
                    return out
                else:
                    out[1]=max(a[st_a],b[st_b])
                    return out
#            if La==1:
#                if k>midB:  #then we can remove from front of b
#                    st_b_new=max(st_b,midB-2)
#                    if st_b_new==(midB-2):
#                        Lb=Lb-(midB-2-st_b)
#                        st_b=st_b_new
#                else:  #then we remove from back
#                    Lb=min(Lb,midB+2-(st_b))
#            elif Lb==1:
#                if k>midA:  #then we can remove from front of a
#                    st_a_new=max(st_a,midA-2)
#                    if st_a_new==(midA-2):
#                        La=La-(midA-2-st_a)
#                        st_a=st_a_new
#                else:  #then we remove from back
#                    La=min(La,midA+2-(st_a))
            if T>=k:  #then we can remove some elements at the end of list from consideration
                if a[midA]>b[midB]:
                    La=min(La,midA+1-(st_a))
                else:
                    Lb=min(Lb,midB+1-(st_b))
            else:   # we can remove elements from start of list
                if a[midA]<b[midB]:
                    La=La-(midA-st_a)
                    st_a=midA
                else:
                    Lb=Lb-(midB-st_b)
                    st_b=midB
            
            if Lb>La:
                kPrime=k-st_a-st_b
                stNew=max(0,kPrime-La)
                Lnew=kPrime+2-stNew
                st_bOld=st_b
                st_b=stNew+st_bOld
                Lb=min(Lb-(st_b-st_bOld),Lnew)
            if La>Lb:
                kPrime=k-st_a-st_b
                stNew=max(0,kPrime-Lb)
                Lnew=kPrime+2-stNew
                st_aOld=st_a
                st_a=stNew+st_aOld
                La=min(La-(st_a-st_aOld),Lnew)
            if k>st_a+st_b and La>0 and Lb>0 and (LaOld==La) and (LbOld==Lb): #then we know the smallest value can be eliminated
                if a[st_a]>b[st_b]:
                    st_b=st_b+1
                    Lb=Lb-1
                else:
                    st_a=st_a+1
                    La=La-1   
        if La==0:
            nRemoveA=st_a   #number of elements removed from front of listA
            out[0]=b[k-nRemoveA]
            out[1]=b[k-nRemoveA+1]
            return out
        if Lb==0:
            nRemoveB=st_b   #number of elements removed from front of listA
            out[0]=a[k-nRemoveB]
            out[1]=a[k-nRemoveB+1]
            return out
import numpy as np
A=Solution()
s1=np.random.randint(low=1,high=20000)
s2=np.random.randint(low=1,high=20000)
a=np.random.randint(low=22000,high=81887,size=(s1,))
b=np.random.randint(low=0,high=21511,size=(s2,))
a.sort()
b.sort()
#a=np.array([2,2,2,2,2,2,2,2,2,2,2,2,2,2])
#b=np.array([2,2])

c=np.r_[a,b]
a=list(a)
b=list(b)
c.sort()

print(A.findMedianSortedArrays(a,b))
print(np.median(c))

q=np.random.randint(low=0,high=len(c))
print(A.kAndkPlusOne(a,b,q))
print(c[q:q+2])