#include <iostream>
#include <algorithm>

using namespace std;
#define max(x,y)  ((x)>(y)?(x):(y)) //don't need add ';'
#define min(x, y)  ((x) < (y) ? (x) : (y))

void MaxMin(int a[], int low, int high, int &maxe,int &maxe1, int &mine, int &mine1){ //
	//首先是递归出口(问题规模缩小到1 or NULL)
	if(low == high){ //当只有一个元素时
		maxe = mine = a[low];
		maxe1 = mine1 = a[low];
	}
	else if(low == high - 1){	//只有两个元素时，只有1个最大最小
		maxe = max(a[low], a[high]);
		maxe1 = min(a[low], a[high]);
		mine = min(a[low], a[high]);
		mine1 = max(a[low], a[high]);
	}
	else{
		int mid = (low + high) / 2;
//		cout << mid << endl;
		int lmaxe, lmine, lmaxe1, lmine1;
		MaxMin(a, low, mid , lmaxe, lmaxe1, lmine, lmine1);
		int rmaxe, rmine, rmaxe1, rmine1;
		MaxMin(a, mid + 1, high, rmaxe, rmaxe1, rmine, rmine1);
		//回溯的时候 要进行比较！！(递归回溯)
		
		//求数组最大的两个数
		maxe = max(lmaxe, rmaxe); 
		if(min(lmaxe, rmaxe) > max(lmaxe1, rmaxe1)) //两个最大在同一边
			maxe1 = min(lmaxe, rmaxe);
		else  //不在同一边
			maxe1 = max(lmaxe1, rmaxe1); //catious about detail !
		
		//求数组最小的两个数
		mine = min(lmine, rmine);
		if(max(lmine, rmine) < min(lmine1, rmine1)) //注意多参数的利用！
			mine1 = max(lmine, rmine);
		else
			mine1 = min(lmine1, rmine1);	
	}
//	cout << "first:" <<maxe << "ååå "<< mine<<endl;
//	cout << maxe1 << " "<< mine1<<endl;
}

int Sum(int a[], int low, int high){
	//二叉遍历 数组即可～
	int mid;
	int sum = 0;
	if(low == high){ //分治到只有一个元素
		return a[low];
    }
	else if(low < high){
		mid = (low + high) / 2;
		return Sum(a, low, mid) + Sum(a, mid + 1, high);
	}
	return 0;
}

int main(int argc, char *argv[]) {
	int a[] = {5, 4, 2, 8, 1, 9}; //0 - 5
//	int min1 , max1, min2, max2 ;
//	MaxMin(a, 0, 5, max1, max2, min1, min2);
//	
//	cout << "Max1:" << max1 <<" "<< "Min1:" << min1<<endl;
//	cout << "Max2:" << max2 <<" "<< "Min2:" << min2<<endl;
	cout << Sum(a, 0, 5);
}
