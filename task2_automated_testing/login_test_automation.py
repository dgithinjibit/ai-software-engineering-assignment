# task2_automated_testing/login_test_automation.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import time

class LoginTestAutomation:
    def __init__(self, driver_path=None):
        """Initialize the test automation suite"""
        self.driver = webdriver.Chrome()  # Requires chromedriver
        self.wait = WebDriverWait(self.driver, 10)
        self.results = []
    
    def setup_test_page(self):
        """Create a simple login page for testing"""
        html_content = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Login Test Page</title>
        </head>
        <body>
            <div id="login-form">
                <h2>Login</h2>
                <input type="text" id="username" placeholder="Username">
                <input type="password" id="password" placeholder="Password">
                <button onclick="login()">Login</button>
                <div id="message"></div>
            </div>
            
            <script>
                const validUsers = {
                    "admin": "admin123",
                    "user": "password123"
                };
                
                function login() {
                    const username = document.getElementById("username").value;
                    const password = document.getElementById("password").value;
                    const message = document.getElementById("message");
                    
                    if (validUsers[username] && validUsers[username] === password) {
                        message.textContent = "Login successful!";
                        message.style.color = "green";
                    } else {
                        message.textContent = "Invalid credentials!";
                        message.style.color = "red";
                    }
                }
            </script>
        </body>
        </html>
        """
        
        self.driver.get("data:text/html," + html_content)
    
    def run_test_case(self, username, password, expected_success, test_name):
        """Run a single test case"""
        result = {
            "test_name": test_name,
            "username": username,
            "password": password,
            "expected": "success" if expected_success else "failure"
        }
        
        try:
            # Clear fields
            username_field = self.wait.until(EC.presence_of_element_located((By.ID, "username")))
            password_field = self.driver.find_element(By.ID, "password")
            username_field.clear()
            password_field.clear()
            
            # Enter credentials
            username_field.send_keys(username)
            password_field.send_keys(password)
            
            # Click login
            self.driver.find_element(By.TAG_NAME, "button").click()
            
            # Wait for response
            time.sleep(1)
            message = self.driver.find_element(By.ID, "message").text.lower()
            
            # Determine actual result
            actual_success = "successful" in message
            result["actual"] = "success" if actual_success else "failure"
            result["passed"] = actual_success == expected_success
            result["message"] = message
            
        except Exception as e:
            result["error"] = str(e)
            result["passed"] = False
        
        self.results.append(result)
        return result
    
    def run_all_tests(self):
        """Run all test cases"""
        # Valid credentials
        self.run_test_case("admin", "admin123", True, "Valid Credentials - Admin")
        self.run_test_case("user", "password123", True, "Valid Credentials - User")
        
        # Invalid credentials
        self.run_test_case("admin", "wrongpass", False, "Invalid Password")
        self.run_test_case("invaliduser", "admin123", False, "Invalid Username")
        self.run_test_case("", "", False, "Empty Credentials")
        
        return self.results
    
    def save_results(self, filename="test_results.json"):
        """Save test results to JSON file"""
        with open(filename, 'w') as f:
            json.dump(self.results, f, indent=2)
    
    def close(self):
        """Close the browser"""
        self.driver.quit()

# Example usage
if __name__ == "__main__":
    test_suite = LoginTestAutomation()
    try:
        test_suite.setup_test_page()
        results = test_suite.run_all_tests()
        test_suite.save_results()
        
        # Print summary
        passed = sum(1 for r in results if r["passed"])
        total = len(results)
        print(f"Test Summary: {passed}/{total} passed")
        
    finally:
        test_suite.close()
