#include<fstream.h>
#include<conio.h>
#include<stdio.h>
#include<string.h>
#include<ctype.h>
struct date
{
	int day;
	int month;
	int year;
}dob, doj;
class employee
{
	protected:
		int empno;
		char name[50];
		char sex[10];
		char desig[50];
		double  bsal;
		int phone, mob;
		char address[30];
   	public:
   		void empinput()
    		{
    			cout<<"Enter the name of the employee: "; gets(name);
        		cout<<"Enter the employee number: "; cin>>empno;
        		cout<<"Enter the gender: "; cin>>sex;
        		cout<<"Enter the designation: "; cin>>desig;
        		cout<<endl<<endl;
        		cout<<"Enter the date of birth";
        		cout<<"\nDate: "; cin>>dob.day;
        		cout<<"Month: "; cin>>dob.month;
        		cout<<"Year: "; cin>>dob.year;
        		cout<<endl;
        		cout<<"Enter the date of joining\n";
        		cout<<"Date: "; cin>>doj.day;
        		cout<<"Month: "; cin>>doj.month;
        		cout<<"Year: "; cin>>doj.year;
        		cout<<endl<<endl;
        		cout<<"Enter your basic salary: "; cin>>bsal;
        		cout<<"Enter the phone number: "; cin>>phone;
        		cout<<"Enter the mobile number: "; cin>>mob;
        		cout<<"Enter the email address: "; gets(address);
			}
      	int retempno() { return empno; }
      	char *retname() { return name; }
      	char *retsex() { return sex; }
      	char *retdesig() { return desig; }
      	double retbsal() { return bsal; }
      	int retphone() { return phone; }
      	int retmob() { return mob; }
      	char *retadd() { return address; }
      	date retdob() { return dob;}
      	date retdoj() { return doj;}
      	void udes(char *des) { strcpy(desig, des); }
      	void ubsal(double bs) { bsal=bs; }
      	void uphone(int ph) { phone=ph; }
      	void umob(int long mobile) { mob=mobile; }
      	void uad(char *addr) { strcpy(address, addr); }
};
class monthlypay: public employee
{
	float DA, HRA, con, ded, gross, mbsal,net, dw;
	public:
		void salary()
		{
			         char month[20];
         int td;
         cout<<"Month ? ";gets(month);
         if(strcmpi(month,"january")==0)
         td=31;
         else
         if(strcmpi(month,"february")==0)
         td=28;
         else
         if(strcmpi(month,"march")==0)
         td=31;
         else
         if(strcmpi(month,"april")==0)
         td=30;
         else
         if(strcmpi(month,"may")==0)
         td=31;
         else
         if(strcmpi(month,"june")==0)
         td=30;
         else
         if(strcmpi(month,"july")==0)
         td=31;
         else
         if(strcmpi(month,"august")==0)
         td=31;
         else
         if(strcmpi(month,"september")==0)
         td=30;
         else
         if(strcmpi(month,"october")==0)
         td=31;
         else
         if(strcmpi(month,"november")==0)
         td=30;
         else
         if(strcmpi(month,"december")==0)
         td=31;
			cout<<"Input number of days worked: "; cin>>dw;
			cout<<"Input deduction: "; cin>>ded;
			mbsal=bsal*dw/td;
			DA=0.55*mbsal;
			HRA=0.35*mbsal;
			con=0.15*mbsal;
			gross=mbsal+DA+HRA+con;
			net=gross-ded;
		}
		void empsearchdisp()
		{
			cout<<"------------------------------------------";
			cout<<"               Employee Details";
			cout<<"------------------------------------------";
			cout<<"Employee number: "<<empno<<endl;
			cout<<"Employee name: "<<name<<endl;
			cout<<"Sex: "<<sex<<endl;
			cout<<"Designation: "<<desig<<endl;
			cout<<"Date of birth: "<<dob.day<<"/"<<dob.month<<"/"<<dob.year<<endl;
			cout<<"Date of birth: "<<doj.day<<"/"<<doj.month<<"/"<<doj.year<<endl;
			cout<<"Phone number: "<<phone<<endl;
			cout<<"Mobile number: "<<mob<<endl;
			cout<<"Address: "<<address<<endl;
			cout<<"Basic Salary: "<<bsal<<endl;
			cout<<"Dearness Allowance: "<<DA<<endl;
			cout<<"House Rest Allowance: "<<HRA<<endl;
			cout<<"Conveyance: "<<con<<endl;
			cout<<"Gross: "<<gross<<endl;
		}
		void salstatement()
		{
			//cout<<"Salary statement for the month of: "<<month<<endl; //check
			printf("%4i %-20s %-15s %6.0f %6.0f %5.0f %5.0f\n", empno, name, desig, mbsal, gross, ded, net);
		}
		void salslip()
		{
			//cout<<"Salary slip for the month of: "<<month<<endl; //check
			printf("Employee code: %4i Employee name: %-20s\n", empno, name);
			cout<<"----------------------------------------------------------------\n";
 			cout<<"------------\n";
 			printf("Basic : %8.0f Deductions: %8.0f\n", mbsal, ded);
 			printf("DA : %8.0f\n", DA);
 			printf("HRA : %8.0f\n", HRA);
			printf("Conveyance : %8.0f\n", con);
 			cout<<"----------------------------------------------------------------\n";
 			cout<<"------------\n";

 			printf("Gross Salary : %8.0f Net Salary: %8.0f\n", gross, net);
 			cout<<"----------------------------------------------------------------\n";
 			cout<<"------------\n\n\n\n";
		}
};
void addrec()
{
   ofstream fout("EMPLOYEE.DAT", ios::binary|ios::app);
   monthlypay a;
   int n;
   clrscr();
   cout<<"Number of records? "; cin>>n;
   for (int k=0; k<n; k++)
   {
      cout<<"Record #"<<(k+1)<<endl;
      a.empinput();
      a.salary();
      fout.write((char*)&a, sizeof(a));
      cout<<endl<<endl;
   }
   fout.close();
   cout<<endl<<endl<<"Press any key.."<<endl;
   getch();
}
void readrec1()
{
	ifstream fin("EMPLOYEE.DAT", ios::binary);
   monthlypay a;
	while (fin.read((char*)&a, sizeof(a)))
    {
     clrscr();
     a.empsearchdisp();
     cout<<"\n\nPress any key to continue ...";
	  getch();
    }
    fin.close();
}
void readrec2()
{
	ifstream fin("EMPLOYEE.DAT", ios::binary);
   monthlypay a;
   clrscr();
   cout<<"----------------------------------------------------------------------";
   cout<<"----------------------------\n";
   cout<<"CODE NAME                      SEX DESIGNATION                      ";
   cout<<"BASIC      GROSS      NET\n";
   cout<<"----------------------------------------------------------------------";
   cout<<"----------------------------\n";
   while (fin.read((char*)&a, sizeof(a)))
   a.salstatement();
   fin.close();
	cout<<"\nPress any key to return...";
	getch();
}
void readrec3()
{
ifstream fin("EMPLOYEE.DAT", ios::binary);
     monthlypay a;
     clrscr();
	while (fin.read((char*)&a, sizeof(a)))
		a.salslip();
     fin.close();
	cout<<"\nPress any key to return...";
	getch();
}
void searchname()
{
	ifstream fin("EMPLOYEE.DAT", ios::binary);
	monthlypay a;
	int found=0;
	char name[21];
	cout<<"Name: "; gets(name);
	while (fin.read((char*)&a, sizeof(a)))
	if (strcmpi(name, a.retname())==0)
	{
   	a.empsearchdisp();
		found=1;
      break;
	}
	if (found==0)
		cout<<name<<" not found in the file\n";
	fin.close();
     cout<<endl<<endl<<"Press any key."<<endl;
	getch();
}
void searchcode()
{
	ifstream fin("EMPLOYEE.DAT", ios::binary);
	monthlypay a;
	int found=0, empno;
	clrscr();
	cout<<"Employee number: "; cin>>empno;
	while (fin.read((char*)&a, sizeof(a)))
		if (empno==a.retempno())
		{
			a.empsearchdisp();
			found=1;
         break;
		}
	if (found==0)
		cout<<empno<<" not found in the file\n";
	fin.close();
     	cout<<endl<<endl<<"Press any key."<<endl;
	getch();
}
void modphone()
{
	fstream f("EMPLOYEE.DAT", ios::binary|ios::out|ios::in);
	monthlypay a;
	int found=0, empno;
	clrscr();
	cout<<"Employee number: "; cin>>empno;
	while (f.read((char*)&a, sizeof(a)))
      if (empno==a.retempno())
      {
         a.empsearchdisp();
         int phone;
         cout<<"Input new Phone number: "; cin>>phone;
         a.uphone(phone);
         f.seekg(-sizeof(a), ios::cur);
         f.write((char*)&a, sizeof(a));
         cout<<"Record updated! \n";
         found=1;
         break;
      }
	if (found==0)
		cout<<empno<<" Not found in the file\n";
	f.close();
     	cout<<endl<<endl<<"Press any key."<<endl;
	getch();
}
void modmob()
{
   fstream f("EMPLOYEE.DAT", ios::binary|ios::in|ios::out);
   monthlypay a;
   int found=0, empno;
   clrscr();
   cout<<"Employee number: ";cin>>empno;
   while(f.read((char*)&a, sizeof(a)))
      if(empno==a.retempno())
      {
         a.empsearchdisp();
         int mob;
         cout<<"Input new mobile number: ";cin>>mob;
         a.umob(mob);
         f.seekg(-sizeof(a), ios::cur);
         f.write((char*)&a, sizeof(a));
         cout<<"Record updated! \n";
         found=1;
         break;
      }
  	 if(found==0)
		cout<<empno<<": Not found in file! \n";
 	f.close();
      	cout<<endl<<endl<<"Press any key."<<endl;
	 getch();
}
void moddesig()
{
	fstream f("EMPLOYEE.DAT", ios::binary|ios::out|ios::in);
	monthlypay a;
	int found=0, empno;
	clrscr();
	cout<<"Employee number: "; cin>>empno;
	while (f.read((char*)&a, sizeof(a)))
	if (empno==a.retempno())
	{
		a.empsearchdisp();
		char desig[21];
		cout<<"Input new Designation: "; gets(desig);
          	a.udes(desig);
		f.seekg(-sizeof(a), ios::cur);
		f.write((char*)&a, sizeof(a));
		cout<<"Record updated.\n";
		found=1;
      break;
	}
	if (found==0)
		cout<<empno<<" not found in the file\n";
	f.close();
	cout<<endl<<endl<<"Press any key."<<endl;
	getch();
}
void modbsal()
{
	fstream f("EMPLOYEE.DAT", ios::binary|ios::out|ios::in);
	monthlypay a;
	int found=0, empno;
	clrscr();
	cout<<"Employee number: "; cin>>empno;
	while (f.read((char*)&a, sizeof(a)))
	if (empno==a.retempno())
	{
		a.empsearchdisp();
		double bsal;
		cout<<"Input new Basic salary: "; cin>>bsal;
		a.ubsal(bsal);
		f.seekg(-sizeof(a), ios::cur);
		f.write((char*)&a, sizeof(a));
		cout<<"Record updated! \n";
		found=1;
      break;
	}
	if (found==0)
		cout<<empno<<": not found in the file!\n";
	f.close();
     	cout<<endl<<endl<<"Press any key."<<endl;
	getch();
}
void modaddress()
{
	fstream f("EMPLOYEE.DAT", ios::binary|ios::out|ios::in);
	monthlypay a;
	int found=0, empno;
	clrscr();
	cout<<"Employee number: "; cin>>empno;
	while (f.read((char*)&a, sizeof(a)))
      if (empno==a.retempno())
      {
         a.empsearchdisp();
         char addr[90];
         cout<<"Input new email address: "; gets(addr);
         a.uad(addr);
         f.seekg(-sizeof(a), ios::cur);
         f.write((char*)&a, sizeof(a));
         cout<<"Record updated! \n";
         found=1;
         break;
      }
	if(found==0)
   		cout<<empno<<": Not found in file! \n";
	f.close();
     	cout<<endl<<endl<<"Press any key."<<endl;
	getch();
}
void displaymenu()
{
int ch;
   do
   {
      clrscr();
      cout<<"Display Menu\n";
      cout<<"1. Display employee basic details"<<endl;
      cout<<"2. Display salary statement"<<endl;
      cout<<"3. Display salary slip"<<endl;
      cout<<"0. Return back"<<endl;
      cout<<endl<<"Input choice? ";cin>>ch;
      switch(ch)
      {
      	case 1: readrec1(); break;
        case 2: readrec2(); break;
        case 3: readrec3(); break;
      }
   }
   while(ch);
}
void modmenu()
{
	int ch;
   do
   {
   	clrscr();
	cout<<"Modify Menu\n";
      	cout<<"1. Modify Designation"<<endl;
      	cout<<"2. Modify Basic salary"<<endl;
      	cout<<"3. Modify Phone Number"<<endl;
      	cout<<"4. Modify Mobile number"<<endl;
      	cout<<"5. Modify Email ID"<<endl;
      	cout<<"0. Return Back"<<endl;
      	cout<<endl<<"Input choice? ";cin>>ch;
      	switch(ch)
      	{
		case 1: moddesig(); break;
          	case 2: modbsal(); break;
          	case 3: modphone(); break;
          	case 4: modmob(); break;
          	case 5: modaddress(); break;
      }
   }
   while(ch);
}
void searchmenu()
{
	int ch;
   do
   {
      clrscr();
      cout<<"Search Menu\n";
      cout<<"1. Employee Name"<<endl;
      cout<<"2. Employee Code"<<endl;
      cout<<"0. Return Back"<<endl;
      cout<<endl<<"Input choice? ";cin>>ch;
      switch(ch)
      {
      	case 1: searchname(); break;
        case 2: searchcode(); break;
      }
   }
   while(ch);
}
void main()
{
	int ch;
   do
   {
   	 clrscr();
      cout<<"Main Menu\n";
      cout<<"1. Add Records"<<endl;
      cout<<"2. Display Records"<<endl;
      cout<<"3. Edit Records"<<endl;
      cout<<"4. Search Records"<<endl;
      cout<<"0. Exit Program"<<endl;
      cout<<endl<<"Input choice? ";cin>>ch;
      switch(ch)
      {
      	  case 1: addrec(); break;
          case 2: displaymenu(); break;
          case 3: modmenu(); break;
          case 4: searchmenu(); break;
      }
   }
   while(ch);
}