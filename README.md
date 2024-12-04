```markdown
# VRV Security Log Analyzer

## Overview
The **VRV Security Log Analyzer** is a Python script designed to process web server log files, analyze request patterns, and identify potential security issues such as suspicious activity, brute force attempts, and frequently accessed endpoints.

---

## Features
- **Request Count per IP Address**: Counts the number of requests made by each IP address.
- **Most Frequently Accessed Endpoint**: Identifies the most accessed endpoint.
- **Suspicious Activity Detection**: Flags IPs with repeated failed login attempts (`401` status code).

---

## Input Format
The script processes log files with entries in the following format:

```
<IP Address> - - [<Date>] "<HTTP Method> <Endpoint> <HTTP Version>" <Status Code> <Size> "<Additional Info>"
```

### Example Log Entries
```
192.168.1.1 - - [03/Dec/2024:10:12:34 +0000] "GET /home HTTP/1.1" 200 512
203.0.113.5 - - [03/Dec/2024:10:12:35 +0000] "POST /login HTTP/1.1" 401 128 "Invalid credentials"
10.0.0.2 - - [03/Dec/2024:10:12:36 +0000] "GET /about HTTP/1.1" 200 256
```

---

## Installation

1. **Clone the Repository**
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. **Set Up Python Environment**  
   Ensure you have Python 3.x installed on your system.

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows, use `env\Scripts\activate`
   pip install -r requirements.txt
   ```

3. **Run the Script**
   ```bash
   python VRV_Security.py
   ```

---

## Output

### Sample Output
```plaintext
IP Address Request Counts:
203.0.113.5 8
198.51.100.23 8
192.168.1.1 7
10.0.0.2 6
192.168.1.100 5

Most Frequently Accessed Endpoint:
/login (Accessed 13 times)

Suspicious Activity Detected:
- IP Address: 203.0.113.5 (Repeated failed login attempts)
- IP Address: 192.168.1.100 (Repeated failed login attempts)
```

---

## Contributing
Feel free to contribute to this project by creating a pull request or submitting an issue.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

## Author
**Shreyas Patil**  
For questions or suggestions, feel free to reach out at:  
📧 [shreyaspatil554@gmail.com](mailto:shreyaspatil554@gmail.com)  
📞 +91 9657451214
```
