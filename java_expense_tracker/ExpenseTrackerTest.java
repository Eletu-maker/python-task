import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;


public class ExpenseTrackerTest{

	@Test
	public void dateExpense(){
		ExpenseTracker myET = new ExpenseTracker();
		assertEquals("2024-02-24",myET.dateExpenses());
}



	@Test
	public void descriptionExpense(){
	ExpenseTracker myET = new ExpenseTracker();
	assertEquals("lunch",myET.descriptionExpenses());
}
	@Test
	public void amountExpense(){
	ExpenseTracker myET = new ExpenseTracker();
	assertEquals(200,myET.amountExpenses());
}
	@Test
	public void getOptions(){
	ExpenseTracker myET = new ExpenseTracker();
	assertEquals(1,myET.getOption());
	assertEquals(3,myET.getOption());
}

}