//birthday paradox
#include<iostream>
#include<stdlib.h>
using namespace std;
int main(){
//theoretical way to calculate probablity
	int noOfPeople,i,bdays[365]={0},j,flag,count;
	float probability,p;
         
	cout<<"enter number of people\n";
	cin>>noOfPeople;
	float x=1;
	for(i=0;i<noOfPeople;i++){
		x *= (365 - i)/365.0;
		
	}
	probability = (1 - x);
	cout<<"Probability = "<<probability<<endl;	


//practical way to calculate probablity
count=0;
for(j = 0; j < 1000; j++)
{
flag=0;
for(i = 0; i < 365; i++)
bdays[i] = 0; 
for(i = 0; i < noOfPeople; i++)
bdays[rand()%365] += 1; 
for(i = 0; i < 365; i++)
{ 
if(bdays[i] >= 2) 
flag=1; 
}
if(flag==1)
count++;
}


p=(float)count/1000;


cout<<"the number of sets out of 1000 which have clashing bdays "<<count;

cout<<"\nthe generated probability is "<<p;

return 0;	
}

