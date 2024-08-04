import java.sql.Date;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Scanner;

public class Main {
    private static Scanner scanner = new Scanner(System.in);
    private static EmployeeManager manager = new EmployeeManager();

    public static void main(String[] args) {
        while (true) {
            System.out.println(" ");
            System.out.println("1. Add Employee");
            System.out.println("2. Update Employee");
            System.out.println("3. Delete Employee");
            System.out.println("4. Search Employee");
            System.out.println("5. Update Salaries");
            System.out.println("6. View Full-Time Employee Info");
            System.out.println("7. View Total Pay by Job Title");
            System.out.println("8. View Total Pay by Division");
            System.out.println("9. Exit");
            System.out.println(" ");

            int choice = scanner.nextInt();
            scanner.nextLine(); // Consume newline

            try {
                switch (choice) {
                    case 1:
                        addEmployee();
                        break;
                    case 2:
                        updateEmployee();
                        break;
                    case 3:
                        deleteEmployee();
                        break;
                    case 4:
                        searchEmployee();
                        break;
                    case 5:
                        updateSalaries();
                        break;
                    case 6:
                        viewFullTimeEmployeeInfo();
                        break;
                    case 7:
                        viewTotalPayByJobTitle();
                        break;
                    case 8:
                        viewTotalPayByDivision();
                        break;
                    case 9:
                        System.out.println("Exiting...");
                        return;
                    default:
                        System.out.println("Invalid option. Please try again.");
                }
            } catch (SQLException | ParseException e) {
                e.printStackTrace();
            }
        }
    }

    private static void addEmployee() throws SQLException, ParseException {
        System.out.print("Enter Name: ");
        String name = scanner.nextLine();
        System.out.print("Enter SSN: ");
        String ssn = scanner.nextLine();
        System.out.print("Enter Job Title: ");
        String jobTitle = scanner.nextLine();
        System.out.print("Enter Salary: ");
        double salary = scanner.nextDouble();
        scanner.nextLine(); // Consume newline
        System.out.print("Enter Hire Date (yyyy-MM-dd): ");
        String hireDateStr = scanner.nextLine();
        Date hireDate = parseDate(hireDateStr);

        manager.addEmployee(name, ssn, jobTitle, salary, hireDate);
        System.out.println("Employee added successfully.");
    }

    private static void updateEmployee() throws SQLException, ParseException {
        System.out.print("Enter Employee ID: ");
        int empId = scanner.nextInt();
        scanner.nextLine(); // Consume newline
        System.out.print("Enter Name: ");
        String name = scanner.nextLine();
        System.out.print("Enter SSN: ");
        String ssn = scanner.nextLine();
        System.out.print("Enter Job Title: ");
        String jobTitle = scanner.nextLine();
        System.out.print("Enter Salary: ");
        double salary = scanner.nextDouble();
        scanner.nextLine(); // Consume newline
        System.out.print("Enter Hire Date (yyyy-MM-dd): ");
        String hireDateStr = scanner.nextLine();
        Date hireDate = parseDate(hireDateStr);

        manager.updateEmployee(empId, name, ssn, jobTitle, salary, hireDate);
        System.out.println("Employee updated successfully.");
    }

    private static void deleteEmployee() throws SQLException {
        System.out.print("Enter Employee ID: ");
        int empId = scanner.nextInt();
        scanner.nextLine(); // Consume newline

        manager.deleteEmployee(empId);
        System.out.println("Employee deleted successfully.");
    }

    private static void searchEmployee() throws SQLException {
        System.out.print("Enter Name (or leave blank): ");
        String name = scanner.nextLine();
        System.out.print("Enter SSN (or leave blank): ");
        String ssn = scanner.nextLine();
        System.out.print("Enter Employee ID (or leave blank): ");
        String empIdStr = scanner.nextLine();
        int empId = empIdStr.isEmpty() ? -1 : Integer.parseInt(empIdStr);

        ResultSet rs = manager.searchEmployee(name, ssn, empId);
        while (rs.next()) {
            System.out.println("ID: " + rs.getInt("emp_id"));
            System.out.println("Name: " + rs.getString("name"));
            System.out.println("SSN: " + rs.getString("ssn"));
            System.out.println("Job Title: " + rs.getString("job_title"));
            System.out.println("Salary: " + rs.getDouble("salary"));
            System.out.println("Hire Date: " + rs.getDate("hire_date"));
            System.out.println("-----");
        }
    }

    private static void updateSalaries() throws SQLException {
        System.out.print("Enter Salary Percentage Increase (e.g., 3.2 for 3.2%): ");
        double percentage = scanner.nextDouble();
        System.out.print("Enter Minimum Salary: ");
        double minSalary = scanner.nextDouble();
        System.out.print("Enter Maximum Salary: ");
        double maxSalary = scanner.nextDouble();
        scanner.nextLine(); // Consume newline

        manager.updateSalaries(percentage, minSalary, maxSalary);
        System.out.println("Salaries updated successfully.");
    }

    private static void viewFullTimeEmployeeInfo() throws SQLException {
        ResultSet rs = manager.getFullTimeEmployeeInfo();
        while (rs.next()) {
            System.out.println("ID: " + rs.getInt("emp_id"));
            System.out.println("Name: " + rs.getString("name"));
            System.out.println("SSN: " + rs.getString("ssn"));
            System.out.println("Job Title: " + rs.getString("job_title"));
            System.out.println("Salary: " + rs.getDouble("salary"));
            System.out.println("Hire Date: " + rs.getDate("hire_date"));
            System.out.println("-----");
        }
    }

    private static void viewTotalPayByJobTitle() throws SQLException {
        System.out.print("Enter Month (1-12): ");
        int month = scanner.nextInt();
        System.out.print("Enter Year (yyyy): ");
        int year = scanner.nextInt();
        scanner.nextLine(); // Consume newline

        ResultSet rs = manager.getTotalPayByJobTitle(month, year);
        while (rs.next()) {
            System.out.println("Job Title: " + rs.getString("job_title"));
            System.out.println("Total Pay: " + rs.getDouble("total_pay"));
            System.out.println("-----");
        }
    }

    private static void viewTotalPayByDivision() throws SQLException {
        System.out.print("Enter Month (1-12): ");
        int month = scanner.nextInt();
        System.out.print("Enter Year (yyyy): ");
        int year = scanner.nextInt();
        scanner.nextLine(); // Consume newline

        ResultSet rs = manager.getTotalPayByDivision(month, year);
        while (rs.next()) {
            System.out.println("Division: " + rs.getString("division"));
            System.out.println("Total Pay: " + rs.getDouble("total_pay"));
            System.out.println("-----");
        }
    }

    private static Date parseDate(String dateStr) throws ParseException {
        SimpleDateFormat format = new SimpleDateFormat("yyyy-MM-dd");
        java.util.Date parsedDate = format.parse(dateStr);
        return new Date(parsedDate.getTime());
    }
}
