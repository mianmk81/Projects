import java.sql.*;
import java.util.Date;

public class EmployeeManager {
    private Connection connection;

    public EmployeeManager() {
        try {
            connection = DBConnection.getConnection();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public void addEmployee(String name, String ssn, String jobTitle, double salary, Date hireDate) throws SQLException {
        String query = "INSERT INTO employees (name, ssn, job_title, salary, hire_date) VALUES (?, ?, ?, ?, ?)";
        try (PreparedStatement stmt = connection.prepareStatement(query)) {
            stmt.setString(1, name);
            stmt.setString(2, ssn);
            stmt.setString(3, jobTitle);
            stmt.setDouble(4, salary);
            stmt.setDate(5, new java.sql.Date(hireDate.getTime()));
            stmt.executeUpdate();
        }
    }

    public void updateEmployee(int empId, String name, String ssn, String jobTitle, double salary, Date hireDate) throws SQLException {
        String query = "UPDATE employees SET name = ?, ssn = ?, job_title = ?, salary = ?, hire_date = ? WHERE emp_id = ?";
        try (PreparedStatement stmt = connection.prepareStatement(query)) {
            stmt.setString(1, name);
            stmt.setString(2, ssn);
            stmt.setString(3, jobTitle);
            stmt.setDouble(4, salary);
            stmt.setDate(5, new java.sql.Date(hireDate.getTime()));
            stmt.setInt(6, empId);
            stmt.executeUpdate();
        }
    }

    public void deleteEmployee(int empId) throws SQLException {
        String query = "DELETE FROM employees WHERE emp_id = ?";
        try (PreparedStatement stmt = connection.prepareStatement(query)) {
            stmt.setInt(1, empId);
            stmt.executeUpdate();
        }
    }

    public ResultSet searchEmployee(String name, String ssn, int empId) throws SQLException {
        String query = "SELECT * FROM employees WHERE name = ? OR ssn = ? OR emp_id = ?";
        PreparedStatement stmt = connection.prepareStatement(query);
        stmt.setString(1, name);
        stmt.setString(2, ssn);
        stmt.setInt(3, empId);
        return stmt.executeQuery();
    }

    public void updateSalaries(double percentage, double minSalary, double maxSalary) throws SQLException {
        String query = "UPDATE employees SET salary = salary * ? WHERE salary BETWEEN ? AND ?";
        try (PreparedStatement stmt = connection.prepareStatement(query)) {
            stmt.setDouble(1, 1 + percentage / 100);
            stmt.setDouble(2, minSalary);
            stmt.setDouble(3, maxSalary);
            stmt.executeUpdate();
        }
    }

    public ResultSet getFullTimeEmployeeInfo() throws SQLException {
        String query = "SELECT * FROM employees";
        Statement stmt = connection.createStatement();
        return stmt.executeQuery(query);
    }

    public ResultSet getTotalPayByJobTitle(int month, int year) throws SQLException {
        String query = "SELECT job_title, SUM(salary) AS total_pay FROM employees WHERE MONTH(hire_date) = ? AND YEAR(hire_date) = ? GROUP BY job_title";
        PreparedStatement stmt = connection.prepareStatement(query);
        stmt.setInt(1, month);
        stmt.setInt(2, year);
        return stmt.executeQuery();
    }

    public ResultSet getTotalPayByDivision(int month, int year) throws SQLException {
        String query = "SELECT division, SUM(salary) AS total_pay FROM employees WHERE MONTH(hire_date) = ? AND YEAR(hire_date) = ? GROUP BY division";
        PreparedStatement stmt = connection.prepareStatement(query);
        stmt.setInt(1, month);
        stmt.setInt(2, year);
        return stmt.executeQuery();
    }
}
