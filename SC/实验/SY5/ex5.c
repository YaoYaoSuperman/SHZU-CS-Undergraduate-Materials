#include<reg52.h>
#include<intrins.h>
void delay(unsigned int d){
 while(--d>0);}
 void main(){
 unsigned char i,sel;
   while(1)
   {
   sel =0xfe;
   for(i=0;i<=8;i++){
   P1=sel;
   delay(50000);
   sel = _crol_(sel,1);
   }
   }
   }