#include<iostream>
using namespace std;

int main(){
    int arr[5]={9,6,2,4,1};
    for(int i=0;i<5-1;i++){
        for(int j=0;j<5-i-1;j++){
            if(arr[j]>arr[j+1]){
                int temp=arr[j];
                arr[j]=arr[j+1];
                arr[j+1]=temp;
            }
        }
    }
    cout<<"sorted array is: "<<endl;
    for(auto i:arr){
        cout<<i;
    }
    return 0;
}