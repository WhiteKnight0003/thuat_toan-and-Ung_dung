#include<bits/stdc++.h>
using namespace std;

int main(){
	ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
	int n,m,k;
	cin>>n>>m>>k;
	int a[m+5]={};
	while(n--){
		int l,r;
		cin>>l>>r;
		a[l]++; // đánh dấu bắt đầu của đoạn quét
		a[r]--; //  đánh dấu kết thúc của đoạn quét
	}
	int res = a[0] >=k; // res = 0 nếu (a[0] >= sai) , =1 nếu ngược lại
        for(int i=1;i<m;i++){
		a[i]+=a[i-1]; //tính tổng cộng dồn
		res += a[i]>=k; //tăng res lên 1 nếu a[i] >= k
	}
	cout<<res;
}