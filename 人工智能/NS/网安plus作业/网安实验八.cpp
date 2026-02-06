#include<iostream>
#include<math.h>
#include<time.h>
#include<stdlib.h>
using namespace std;
int mod(int a,int b){
	int ans;
	while(a<0){
		a=a+b; 
	}
	ans=a%b;
	return ans;
}
int tongyu(int a,int m,int n){//???? 
	long long int temp=a%n,ans;
	if(m==1){
		ans=temp;
	}
	else if(m>=2){
		ans=mod((temp*tongyu(a,m-1,n)),n);
	}
	return ans;
}
int f_mod(int k,int p){
	int ans;
	for(int i=1;;i++){
		ans=mod(i*k-1,p);
		if(ans==0){
			return i;
			break;
		}
	}
}
 
int gcd(int k,int p){
	int temp;
	if(k<p){
		temp=k;
		k=p;
		p=temp;
	}
	while(p!=0){
		temp=p;
		p=mod(k,p);
		k=temp;
	}
	return k;
}
int suiji(int p){
	int k,k1,p1;
	k=2+rand()%(1000);
	k=5;
	k1=k;
	p1=p;
	if(gcd(k1,p1)==1){
		return k;
	}
	else{
		suiji(p);
	}
}
int main(){
	int p,g,x,y,m,k,r,s,v1,v2,temp1,temp2,flag;
	cout<<"??????p:";
	cin>>p;
	cout<<"??????g:";
	cin>>g;
	cout<<"???????x(1ÑÑ"<<p-2<<"):";
	cin>>x;
	cout<<"?????m:";
	cin>>m;
	y=tongyu(g,x,p);
	k=suiji(p-1);
	r=tongyu(g,k,p);
	temp1=f_mod(k,p-1);
	s=mod((mod(m-x*r,p-1)*mod(temp1,p-1)),p-1);
	temp1=tongyu(y,r,p);
	temp2=tongyu(r,s,p);
	v1=mod((mod(temp1,p)*mod(temp2,p)),p);
	v2=tongyu(g,m,p); 
	flag=mod(v1-v2,p);
	if(flag==0){
		cout<<"????";
	}
	else{
		cout<<"??";
	}
}
