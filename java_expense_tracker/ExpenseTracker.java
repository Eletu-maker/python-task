import java.util.Scanner;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.time.format.DateTimeParseException;
import java.util.ArrayList;
import java.util.InputMismatchException;
public class ExpenseTracker{
	public static void main(String []args){
	Scanner entries = new Scanner(System.in);
	
	ArrayList<ArrayList<Object>> expenseAdded = new ArrayList<>();
	
	int option =0;
	int added =0;
	boolean validInput = false;
	double total =0;
	
	
	
	
	System.out.println("Welcome to semicolon Expense Tracker App");
	System.out.println("`````````````````````````````````````````");
do{ 

System.out.println("""
1. Add an expense
2. View all expense
3. calculate total expenses
4. Exist
""");

	option= getOption();
            			


	
switch (option){
	case 1:
	added++;
	ArrayList<Object> expense = new ArrayList<>();
	String date= dateExpenses();

		expense.add(date);










	String description= descriptionExpenses();





	
	expense.add(description);
	




	Double Amount = amountExpenses();



	
	expense.add(Amount);
	total +=Amount;




	System.out.println("expense added ");
	expenseAdded.add(expense);
	System.out.println();
	break;
	case 2:
	if(total==0){
	System.out.println("no expenses added yet");
} else{
	System.out.println("Date           Description            amount");
	for(int count=0; count <added;count++){
	System.out.println(expenseAdded.get(count).get(0)+"         "+expenseAdded.get(count).get(1)+"       "+expenseAdded.get(count).get(2));
}
}
	System.out.println();
	break;
	case 3:
	if(total==0){
	System.out.println("no expenses added yet");
}else{
	System.out.println("The total expenese are: "+ total);
}
	System.out.println();
	break;
	case 4:
	System.out.println("bye");
}



}while(option >0 && option <4);













}



public static String dateExpenses(){
Scanner entries = new Scanner(System.in);
System.out.print("Enter the date(YYYY-MM-DD): ");
	String Date ="";
	
	while(true){
	try{
	Date = entries.nextLine();
	LocalDate date = LocalDate.parse(Date, DateTimeFormatter.ofPattern("yyyy-MM-dd"));
	
	return Date;
}      catch (DateTimeParseException e){
	System.out.println("Unacceptable value: please enter a valid number.");
	System.out.print("Enter the date(YYYY-MM-DD): ");
}

}
	
}

public static String descriptionExpenses(){
Scanner entries = new Scanner(System.in);
System.out.print("Enter the description: ");
	String Description = entries.nextLine();
	return Description;
}

public static double amountExpenses(){
Scanner entries = new Scanner(System.in);
double amount =0;

while(true){
	try{
	System.out.print("Enter amount: ");
	amount = entries.nextDouble();
	while (amount <0){
	System.out.println("invalid input(no negative number)");
	System.out.print("Enter amount: ");
	amount = entries.nextDouble();
}	if(amount >0){
	return amount;
}
	}catch (InputMismatchException e){
	System.out.println("Unacceptable value: please enter a valid number.");
	entries.next();
}
}
	
	
}

public static int getOption(){
Scanner entries = new Scanner(System.in);

int option =0;
	while(true){
 try{
 System.out.print("Enter your choice: ");
option = entries.nextInt();
while( option <= 0 || option > 4 ){
 System.out.println("Unacceptable value: please enter option number.");
System.out.print("Enter your choice: ");
 option = entries.nextInt();
} 
return option;

} catch (InputMismatchException e) {
System.out.println("Unacceptable value: please enter a valid number.");
entries.next();
 }


}
}


}

