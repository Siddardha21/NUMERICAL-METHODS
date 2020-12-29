
#include<iostream>
#include<cmath>

using namespace std;

int main() {
    int i,j,m,n,l;
    float x[10],a[10][10],b[10],c[10];
    cout<<"\nEnter the value of n : \n";
    cin>>n;
    cout<<"\nEnter the number of iterations : \n";
    cin>>l;
    cout<<"\nEnter the right hand side constants : \n";
    for(i=0;i<n;i++) {
        cin>>b[i];
    }
    cout<<"\nEnter the coefficients row wise : \n";
    for(i=0;i<n;i++) {
        x[i]=0;
        for(j=0;j<n;j++) {
            cin>>a[i][j];
        }
    }
    m=1;
    line:
    for(i=0;i<n;i++) {
        c[i]=b[i];
        for(j=0;j<n;j++) {
            if(i!=j) {
                c[i]=c[i]-a[i][j]*x[j];
            }
        }
    }
    for(i=0;i<n;i++) {
        x[i]=c[i]/a[i][i];
    }
    m++;
    if(m<=l) {
        goto line;
    }
    else {
        cout<<"\nThe Solution is : \n";
        for(i=0;i<n;i++) {
            cout<<"\nx("<<i<<") = "<<x[i]<<"\n";
        }
    }
}

