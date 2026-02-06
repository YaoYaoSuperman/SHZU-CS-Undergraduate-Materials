#include <string>
#include <iostream>
#include "time.h"
#include <stdlib.h> 
using namespace std;
unsigned char msg[8] ={ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h' };//明文
unsigned int C_uint[10];
unsigned int Dec[10];
unsigned int PP = 7;//两个素数
unsigned int QQ = 17;
 
//判断p是否为素数
//在产生密钥函数中调用
bool JudgePrimeNum(unsigned int num)
{
    unsigned int devider=2;
    for(;devider<int(num/2);devider++)
    {
       if(num%devider==0)
           return false;
    }
    return true;
}
 
//产生2到t-1的随机数e
//在产生密钥函数中调用
unsigned int RandomlyGenerateE(unsigned int t)
{
    unsigned int e=0;
    srand((int)time(0));//设置随机数种子，在rand之前调用一次即可
    e=2+rand()%(t-3);
    return(e);//随机数
}
//求最大公因素
void Gcd(unsigned int BigNum,unsigned int SmallNum,unsigned int &MaxGcd )
{
    int tmp=0;
   while(BigNum%SmallNum)
   {
       tmp=SmallNum;
       SmallNum=BigNum%SmallNum; 
       BigNum=tmp;
   }
   MaxGcd=SmallNum;
}
//判断最大公约数数是否是1，是1的话两个数就互质
//在产生密钥函数中调用
bool JudgeGcd_1(unsigned int BigNum,unsigned int SmallNum)
{
    unsigned int M=0;
    Gcd( BigNum,SmallNum,M);
    if(M==1)
        return true;
    else
        return false;
}
 
//　3*7 = 21; 21 % 20 = 1 ; 所以3,7 互为 20 的 模逆.
//　9*3 = 27; 27 % 26 = 1 ; 所以9,3 互为 26 的 模逆. 
//==利用加的模等于模的加求e*d = 1 mod model 中的d
//在产生密钥函数中调用
int Moni(unsigned int e, unsigned int model, unsigned int* d)
{
    unsigned int i;
    unsigned int over = e;
    for (i = 1; i<model;)
    {
        over = over % model;
        if (over == 1)
        {
            *d = i;
            return 1;
        }
        else
        {
            if (over + e <= model)
            {
                do
                {
                    i++;
                    over += e;
                } while (over + e <= model);
            }
            else
            {
                i++;
                over += e;
            }
        }
    }
    return 0;
}
//产生密钥函数  其中p q互异至数  ，公钥P{e,n)，私钥S{d,n}
//在主函数调用
void ProduceKey(unsigned int p,unsigned int q,unsigned int &e,unsigned int &d,unsigned int &n)
{
    unsigned int t=0;
    while(!JudgePrimeNum(p))
    {
        cout<<"p不是质数，请重新输入p:";
        cin>>p;
    }
    while(!JudgePrimeNum(q))
    {
        cout<<"q不是质数，请重新输入q:";
        cin>>q;
    } 
    //  随机选择一个2<e<t ,使得gcd(t,e)=1 
   n=p*q;
   t=(p-1)*(q-1);
   e=RandomlyGenerateE(t);
   while(!JudgeGcd_1(t,e))
   {
     e=RandomlyGenerateE(t);
   }
   //计算d,使得e*d=1 mod t
    Moni(e,t,&d);
}
unsigned int Modular_Ex(unsigned int e1,int b,const unsigned int m)
{
    unsigned int i;
    unsigned int tmp=b;
     for(i=0;i<e1;i++)
      {
        b=b%m;
        b=b*tmp;
      }
     return  b/tmp;
}
//二进制转换
int BianaryTransform(int num, int bin_num[])
{
    int i = 0, mod = 0;
    //转换为二进制，逆向暂存temp[]数组中
    while(num != 0)
    {
        mod = num%2;
        bin_num[i] = mod;
        num = num/2;
        i++;
    }
    //返回二进制数的位数
    return i;
}
//反复平方求幂
unsigned int Modular_Exonentiation(unsigned int a, int b, int n)
{
    int c = 0, bin_num[1000];
    long long d = 1;
    int k = BianaryTransform(b, bin_num)-1;
 
    for(int i = k; i >= 0; i--)
    {
        c = 2*c;
        d = (d*d)%n;
        if(bin_num[i] == 1)
        {
            c = c + 1;
            d = (d*a)%n;
        }
    }
    return d;
}
//RSA加密
//在主函数调用a*a%n =((a%n)*a)%n
void RSA_Encrytion(unsigned int e1,const unsigned int n1)
{
    unsigned int i;
    unsigned int tmp;
    int j;
    for(j=0;j<sizeof(msg);j++)
    {
        C_uint[j]=Modular_Exonentiation(msg[j],e1,n1);
   }
 
}
//RSA解密
void RSA_Decrytion(unsigned int d2,const unsigned int n2)
{
    unsigned int i;
    unsigned int tmp;
    int j;
    for(j=0;j<sizeof(msg);j++)
    {
 
        Dec[j]=Modular_Exonentiation(C_uint[j],d2,n2);
 
 
    }
}
void RunRSA()
{
   unsigned int e=0;
   unsigned int d=0;
   unsigned int n=0;//n=p*q
   ProduceKey(PP,QQ,e,d,n);
   cout<<"e:"<<e<<endl;
   cout<<"d:"<<d<<endl;
   RSA_Encrytion( e, n);//加密
   RSA_Decrytion( d,n);//解密
}
int main()
{
    RunRSA();
    cout<<sizeof(unsigned int)<<endl;
    cout<<"原明文："<<msg<<endl;
     cout<<"密文：";
    for(int i=0;i<sizeof(msg);i++)
    {
      cout<<char(C_uint[i]);
    }
    cout<<endl;
     cout<<"解密得到的明文：";
    for(int i=0;i<sizeof(msg);i++)
    { 
       cout<<char(Dec[i]);
    }
    cout<<endl;
    system("pause"); 
    return 0;
}
