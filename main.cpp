#include<iostream>
#include<cstring>
#include<string.h>
#include<stdio.h>

using namespace std;
typedef struct task
{
    char task_name[50][30];
    char min[50][3],hour[50][4],date[50][2],month[50][2],year[50][2];
    struct task *next;
}*node;
class reg
{
    int que;
char name[20],username[15],password[15],gmail[30],phone[10],ans[20];
public:
 int task_num=0;
void add_details();
void incr_task();
friend void forgot();
friend int login();
friend int search(char user1[15]);
friend int search1(char u1[15],char p1[15]);
friend void add_task(node x);
};

const int size = 50;
static reg s[size];

static int  n=1;
static node first[50];
void reg:: incr_task()
{
     int *p;
     p=&task_num;
     ++*p;
}
void add_task(node x,int n1)
{
  int k;
k=s[n1].task_num;

cout<<"\n Enter the task ";
cin>>x->task_name[k];
cout<<"\n Enter the date";

cin>>x->date[k];
cout<<"\n Enter the month";
cin>>x->month[k];
cout<<"\n Enter the year";
cin>>x->year[k];
cout<<"\n Enter the hour";
cin>>x->hour[k];
cout<<"\n Enter the min";
cin>>x->min[k];
}


void create_task(int n1,int tnum)
{
  node a;


  if(first[n1]==nullptr)
  {
     first[n1] = new (struct task);
     add_task(first[n1],n1);

     first[n1]->next=nullptr;
     s[n1].incr_task();

  }
  else
  {
    a=first[n1];
    while(a->next!=nullptr)
    {
      a=a->next;
    }
    while(tnum>0)
    {
      a->next= new(struct task);
      a=a->next;
      add_task(a,n1);
      s[n1].incr_task();
      --tnum;
    }
  }
}
void show_task(int n)
{
    cout<<"\n Your tasks are";
    cout<<"\n task name \t date/month/year \t hour:min";
     node a;
    int i=0;
    a=first[n];
    while(a!=nullptr)
    {
        cout<<"\n"<<a->task_name[i]<<"\t"<<a->date[i]<<"/"<<a->month[i]<<"/"<<a->year[i]<<"\t"<<a->hour[i]<<":"<<a->min[i];
        a=a->next;
        ++i;

    }
}
void delete_task(int n)
{
     int num;
    cout<<"\n Enter the task number you want to delete";
    cin>>num;

    node a,b;
    a=first[n];
     if(num==1 && s[n].task_num==1)
      {
         delete a;

      }
     if(num ==1 && s[n].task_num!=1)
      {
         b=a;
         a=a->next;
         delete b;
         first[n]=a;


     }
   else
   {
    while(num>1)
    {
       b=a;
       a=a->next;

     }
    b->next=a->next;
    delete a;
   }
}
int  search(char user1[15])
{
int i,count=0;
for(i=0;i<n;i++)
 {
     if(strcmp(user1,s[i].username)==0)
      {

          ++count;
         return 0;
      }
  }
  if(count==0)
  {
     return -1;
   }
count=0;
return 0;
}
void reg::add_details()
{
int ret,x;
++n;
char user1[15];
cout<<"\n Enter your name";
cin>>name;
cout<<"\n Enter your gmail";
cin>>gmail;
cout<<"\n Enter your phone number";
cin>>phone;
do
{

cout<<"\n Enter your username (maximum character 15)";
cin>>user1;
ret=search(user1);
if(ret==0)
{
  cout<<"\n please choose other username.someone has already taken it";
}
else
{
     strcpy(username,user1);
}

}while(ret==0);
cout<<"\n Enter your password (maximum character 15)";
cin>>password;
cout<<"\n which security question do you want to keep (maximum character 15)? \nPress 1 : What is the name of your first school?\n Press 2 : What is the name of your pet?";
do
{

cin>>x;
switch(x)
{
  case 1 : cin>>ans;
            que=x;
           break;
  case 2 :cin>>ans;
             que=x;
          break;
  default: cout<<"\n Oops!! Wrong input given \n please try again";


}
}while(x!=1 && x!=2);

}

void forgot()
{
char g1[30],p1[10];
    char a1[20];
int i=0,count=0;
 cout<<"\n Enter your gmail";
cin>>g1;
cout<<"\n Enter your phone number";
cin>>p1;
for(i=0;i<n;i++)
 {
     if(strcmp(g1,s[i].gmail)==0 && strcmp(p1,s[i].phone)==0)
      {
          if(s[i].que == 1)
          {
               cout<<"\n  What is the name of your first school?";
               cin>>a1;
          }
          else
          {
                cout<<"\n  What is the name of your pet?";
               cin>>a1;
          }

     if(strcmp(a1,s[i].ans)==0)
     {
            cout<<"\n Your username and password are";
            cout<<s[i].username<<"\t"<<s[i].password;
     }
     else
     {
            cout<<"\n You had given wrong answer";
     }
     ++count;
    }

  }

  if(count==0)
  {
     cout<<"Your entered gmail and phone number didn't matched";
   }
count=0;
}
int search1(char u1[15],char p1[15])
{
int i,count=0;
for(i=0;i<n;i++)
{

if(strcmp(u1,s[i].username)==0 && strcmp(p1,s[i].password)==0)
  {

       ++count;
        return i;
  }
}
  if(count==0)
  {
        return -1;
  }
  return 0;
}
int  login()
{
int ret;
char u1[15],p1[15];
do
{

cout<<"\n Enter your Username";
cin>>u1;
cout<<"\n Enter your password";
cin>>p1;
ret = search1(u1,p1);
if(ret!=-1 )
{
    return ret;
}
else
{
  cout<<"\n PLease try again";
}
}while(ret!=1);
return 0;
}
void task_selection(int n1)
{
  int x,tnum;
  char ans1;

do
{
    cout<<"\n Press 1 : To add task  \n Press 2 : To read task \n Press  3 : To delete task";
  cin>>x;
switch(x)
{
   case 1 :cout<<"\n Enter the number of task you want to add";
                 cin>>tnum;

           if(tnum>1 && s[n1].task_num==0)
           {
              create_task(n1,1);
              create_task(n1,tnum-1);
           }
           else
           {
               create_task(n1,tnum);
           }
           break;
     case 2 :show_task(n1);
             break;
     case 3 :delete_task(n1);
             break;
    default :cout<<"\n Wrong input given";
  }
cout<<"Do you want to continue(y/n)?";
cin>>ans1;
}while(ans1=='y');
}
int main()
{

char ans1;
int x,ret;

do
{
cout<<"\n Press 1 : To register \n Press 2 : To login \n Press 3 : forgot username/password \n Enter your choice";
cin>>x;
switch(x)
{
   case 1 : s[n].add_details();

            break;
   case 2 : ret=login();
            if(ret!=-1)
            {
                task_selection(ret);

            }


            break;
   case 3 :forgot();
             break;
  default :cout<<"\n Wrong input given!!";

}
cout<<"Do you want to continue(y/n)?";
cin>>ans1;
}while(ans1=='y');

}



