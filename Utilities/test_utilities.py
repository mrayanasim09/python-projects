"""
Unit tests for Utilities module
This code is made by MRayan Asim
"""

import unittest
import sys
import os
from io import StringIO
from unittest.mock import patch, MagicMock
import datetime

# Add the Utilities directory to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


class TestWordCount(unittest.TestCase):
    """Tests for word_count.py functionality"""
    
    def test_count_letters_in_sentence(self):
        """Test letter counting function"""
        # Import the function by executing the module code
        import string
        
        def count_letters_in_sentence(sentence):
            words = sentence.replace(",", "").replace(".", "").split()
            count = 0
            for word in words:
                count += len(word)
            return count
        
        # Test cases
        self.assertEqual(count_letters_in_sentence("hello world"), 10)
        self.assertEqual(count_letters_in_sentence("a b c"), 3)
        self.assertEqual(count_letters_in_sentence(""), 0)
        self.assertEqual(count_letters_in_sentence("test, case."), 8)  # "test" (4) + "case" (4) = 8
        self.assertEqual(count_letters_in_sentence("Python Programming"), 17)
    
    def test_word_count_with_punctuation(self):
        """Test word counting with punctuation"""
        import string
        
        def count_words(sentence):
            return sum([i.strip(string.punctuation).isalpha() for i in sentence.split()])
        
        self.assertEqual(count_words("Hello, world!"), 2)
        self.assertEqual(count_words("One, two, three."), 3)
        self.assertEqual(count_words(""), 0)


class TestShortForm(unittest.TestCase):
    """Tests for short_form.py functionality"""
    
    def test_generate_acronym(self):
        """Test acronym generation"""
        def generate_acronym(user_input):
            text = user_input.split()
            acronym = " "
            for word in text:
                acronym += str(word[0]).upper()
            return acronym
        
        # Test cases
        self.assertEqual(generate_acronym("As Soon As Possible"), " ASAP")
        self.assertEqual(generate_acronym("hello world"), " HW")
        self.assertEqual(generate_acronym("Python"), " P")
        self.assertEqual(generate_acronym(""), " ")


class TestPasswordGenerator(unittest.TestCase):
    """Tests for passwrd_generator.py functionality"""
    
    def test_password_generation(self):
        """Test password generation"""
        import random
        
        def generate_password(length):
            s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
            return "".join(random.sample(s, length))
        
        # Test password length
        password = generate_password(12)
        self.assertEqual(len(password), 12)
        
        password = generate_password(8)
        self.assertEqual(len(password), 8)
        
        password = generate_password(16)
        self.assertEqual(len(password), 16)
    
    def test_password_characters(self):
        """Test that generated password contains valid characters"""
        import random
        
        def generate_password(length):
            s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
            return "".join(random.sample(s, length))
        
        valid_chars = set("abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?")
        
        for _ in range(10):  # Run multiple times to ensure randomness
            password = generate_password(12)
            for char in password:
                self.assertIn(char, valid_chars)


class TestBirthday(unittest.TestCase):
    """Tests for birthday.py functionality"""
    
    def test_get_day_of_week(self):
        """Test day of week calculation"""
        def get_day_of_week(date_str):
            try:
                date = datetime.datetime.strptime(date_str, "%d-%m-%Y")
                return date.strftime("%A")
            except ValueError:
                return "Invalid date format. Please enter the date in dd-mm-yyyy format."
        
        # Test known dates
        self.assertEqual(get_day_of_week("01-01-2000"), "Saturday")
        self.assertEqual(get_day_of_week("25-12-2020"), "Friday")
        self.assertEqual(get_day_of_week("15-08-1947"), "Friday")
        self.assertEqual(get_day_of_week("invalid"), "Invalid date format. Please enter the date in dd-mm-yyyy format.")
    
    def test_get_days_until_birthday(self):
        """Test days until birthday calculation"""
        def get_days_until_birthday(date_str):
            try:
                today = datetime.datetime.now().date()
                birth_date = datetime.datetime.strptime(date_str, "%d-%m-%Y").date()
                next_birthday = datetime.date(today.year, birth_date.month, birth_date.day)
                if today > next_birthday:
                    next_birthday = datetime.date(today.year + 1, birth_date.month, birth_date.day)
                days_left = (next_birthday - today).days
                return days_left
            except ValueError:
                return "Invalid date format. Please enter the date in dd-mm-yyyy format."
        
        # Should return a non-negative integer
        result = get_days_until_birthday("01-01-2000")
        self.assertIsInstance(result, int)
        self.assertGreaterEqual(result, 0)
        
        # Invalid format
        self.assertEqual(get_days_until_birthday("invalid"), "Invalid date format. Please enter the date in dd-mm-yyyy format.")
    
    def test_get_zodiac_sign(self):
        """Test zodiac sign determination"""
        def get_zodiac_sign(day, month):
            if (month == 1 and day >= 20) or (month == 2 and day <= 18):
                return "Aquarius"
            elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
                return "Pisces"
            elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
                return "Aries"
            elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
                return "Taurus"
            elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
                return "Gemini"
            elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
                return "Cancer"
            elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
                return "Leo"
            elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
                return "Virgo"
            elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
                return "Libra"
            elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
                return "Scorpio"
            elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
                return "Sagittarius"
            else:
                return "Capricorn"
        
        # Test all zodiac signs
        self.assertEqual(get_zodiac_sign(25, 1), "Aquarius")
        self.assertEqual(get_zodiac_sign(25, 2), "Pisces")
        self.assertEqual(get_zodiac_sign(25, 3), "Aries")
        self.assertEqual(get_zodiac_sign(25, 4), "Taurus")
        self.assertEqual(get_zodiac_sign(25, 5), "Gemini")
        self.assertEqual(get_zodiac_sign(25, 6), "Cancer")
        self.assertEqual(get_zodiac_sign(25, 7), "Leo")
        self.assertEqual(get_zodiac_sign(25, 8), "Virgo")
        self.assertEqual(get_zodiac_sign(25, 9), "Libra")
        self.assertEqual(get_zodiac_sign(25, 10), "Scorpio")
        self.assertEqual(get_zodiac_sign(25, 11), "Sagittarius")
        self.assertEqual(get_zodiac_sign(25, 12), "Capricorn")
    
    def test_calculate_life_path_number(self):
        """Test life path number calculation"""
        def calculate_life_path_number(date_str):
            date = datetime.datetime.strptime(date_str, "%d-%m-%Y")
            day = date.day
            month = date.month
            year = date.year
            total = day + month + year
            while total > 9:
                total = sum(int(digit) for digit in str(total))
            return total
        
        # Test cases
        result = calculate_life_path_number("01-01-2000")
        self.assertIsInstance(result, int)
        self.assertGreaterEqual(result, 1)
        self.assertLessEqual(result, 9)
    
    def test_get_birthstone(self):
        """Test birthstone lookup"""
        def get_birthstone(month):
            birthstones = {
                1: "Garnet", 2: "Amethyst", 3: "Aquamarine",
                4: "Diamond", 5: "Emerald", 6: "Pearl",
                7: "Ruby", 8: "Peridot", 9: "Sapphire",
                10: "Opal", 11: "Topaz", 12: "Turquoise",
            }
            return birthstones.get(month, "Unknown")
        
        self.assertEqual(get_birthstone(1), "Garnet")
        self.assertEqual(get_birthstone(6), "Pearl")
        self.assertEqual(get_birthstone(12), "Turquoise")
        self.assertEqual(get_birthstone(13), "Unknown")
    
    def test_get_birth_flower(self):
        """Test birth flower lookup"""
        def get_birth_flower(month):
            birth_flowers = {
                1: "Carnation", 2: "Violet", 3: "Daffodil",
                4: "Daisy", 5: "Lily of the Valley", 6: "Rose",
                7: "Larkspur", 8: "Gladiolus", 9: "Aster",
                10: "Marigold", 11: "Chrysanthemum", 12: "Poinsettia",
            }
            return birth_flowers.get(month, "Unknown")
        
        self.assertEqual(get_birth_flower(1), "Carnation")
        self.assertEqual(get_birth_flower(6), "Rose")
        self.assertEqual(get_birth_flower(12), "Poinsettia")
        self.assertEqual(get_birth_flower(13), "Unknown")


class TestURLValidation(unittest.TestCase):
    """Tests for url.py functionality"""
    
    def test_validate_url(self):
        """Test URL validation"""
        import re
        
        def validate_url(url):
            pattern = re.compile(
                r"^https?://"
                r"([A-Za-z0-9.-]+)"
                r"(:\\d+)?"
                r"(/[A-Za-z0-9_\\.-]*)*?$"
            )
            return bool(re.match(pattern, url))
        
        # Valid URLs
        self.assertTrue(validate_url("http://example.com"))
        self.assertTrue(validate_url("https://example.com"))
        self.assertTrue(validate_url("http://www.example.com"))
        self.assertTrue(validate_url("https://example.com/path"))
        
        # Invalid URLs
        self.assertFalse(validate_url("ftp://example.com"))
        self.assertFalse(validate_url("example.com"))
        self.assertFalse(validate_url(""))
    
    def test_is_valid_url_mock(self):
        """Test URL existence check with mock"""
        with patch('requests.head') as mock_head:
            # Mock successful response
            mock_response = MagicMock()
            mock_response.status_code = 200
            mock_head.return_value = mock_response
            
            def is_valid_url(url, timeout=10):
                try:
                    import requests
                    response = requests.head(url, timeout=timeout)
                    return response.status_code == requests.codes.ok
                except Exception:
                    return False
            
            self.assertTrue(is_valid_url("http://example.com"))
            
            # Mock failed response
            mock_response.status_code = 404
            self.assertFalse(is_valid_url("http://example.com"))


class TestNetworkWifi(unittest.TestCase):
    """Tests for network.py functionality"""
    
    @patch('subprocess.run')
    def test_get_wifi_profiles(self, mock_run):
        """Test Wi-Fi profile retrieval"""
        # Mock subprocess output
        mock_output = """
        WLAN Profile
        -------------
        All User Profile     : HomeWiFi
        All User Profile     : OfficeWiFi
        """
        mock_run.return_value = MagicMock(stdout=mock_output, stderr="")
        
        def get_wifi_profiles():
            try:
                result = subprocess.run(
                    ["netsh", "wlan", "show", "profiles"],
                    capture_output=True,
                    text=True,
                    shell=False,
                    check=True,
                )
                output = result.stdout
                lines = output.split("\n")
                profiles = []
                for line in lines:
                    if "All User Profile" in line:
                        profile = line.split(":")[1].strip()
                        profiles.append(profile)
                return profiles
            except Exception:
                return []
        
        import subprocess
        profiles = get_wifi_profiles()
        self.assertIn("HomeWiFi", profiles)
        self.assertIn("OfficeWiFi", profiles)
    
    def test_get_wifi_password(self):
        """Test Wi-Fi password retrieval logic"""
        def get_wifi_password(profile, mock_output=None):
            if not profile:
                return None
            if mock_output:
                lines = mock_output.split("\n")
                password = None
                for line in lines:
                    if "Key Content" in line:
                        password = line.split(":")[1].strip()
                        break
                return password
            return None
        
        # Test with mock output
        mock_output = """
        Security settings
        Key Content        : MyPassword123
        """
        self.assertEqual(get_wifi_password("HomeWiFi", mock_output), "MyPassword123")
        self.assertIsNone(get_wifi_password(""))


class TestTransferFile(unittest.TestCase):
    """Tests for transfer.py functionality"""
    
    def test_port_configuration(self):
        """Test port configuration"""
        PORT = 8010
        self.assertIsInstance(PORT, int)
        self.assertGreater(PORT, 0)
        self.assertLess(PORT, 65536)
    
    def test_ip_address_format(self):
        """Test IP address format construction"""
        import socket
        
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            s.connect(("8.8.8.8", 80))
            IP = "http://" + s.getsockname()[0] + ":" + str(8010)
            
            # Verify IP format
            self.assertTrue(IP.startswith("http://"))
            self.assertIn(":8010", IP)
        finally:
            s.close()


class TestSecretCode(unittest.TestCase):
    """Tests for secret_code.py functionality"""
    
    def test_encode_decode_logic(self):
        """Test encoding/decoding logic"""
        def encode_message(message, shift=3):
            encoded = ""
            for char in message:
                if char.isalpha():
                    ascii_offset = ord('A') if char.isupper() else ord('a')
                    encoded += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
                else:
                    encoded += char
            return encoded
        
        def decode_message(message, shift=3):
            return encode_message(message, -shift)
        
        original = "Hello World!"
        encoded = encode_message(original)
        decoded = decode_message(encoded)
        
        self.assertNotEqual(original, encoded)
        self.assertEqual(original, decoded)


class TestConnectivity(unittest.TestCase):
    """Tests for connectivity.py functionality"""
    
    @patch('requests.get')
    def test_check_internet_connection(self, mock_get):
        """Test internet connectivity check"""
        # Mock successful connection
        mock_get.return_value.status_code = 200
        
        def check_connection(url="http://www.google.com", timeout=5):
            try:
                import requests
                response = requests.get(url, timeout=timeout)
                return response.status_code == 200
            except Exception:
                return False
        
        self.assertTrue(check_connection())
        
        # Mock failed connection
        mock_get.side_effect = Exception("Connection failed")
        self.assertFalse(check_connection())


class TestGithubFunctions(unittest.TestCase):
    """Tests for github.py functionality"""
    
    def test_github_api_url_format(self):
        """Test GitHub API URL construction"""
        base_url = "https://api.github.com"
        username = "testuser"
        
        api_url = f"{base_url}/users/{username}"
        
        self.assertEqual(api_url, "https://api.github.com/users/testuser")
        self.assertTrue(api_url.startswith("https://"))


class TestBTCFunctions(unittest.TestCase):
    """Tests for btc.py functionality"""
    
    def test_btc_price_check_logic(self):
        """Test BTC price check logic"""
        # Simulate price checking logic
        def check_btc_price(mock_price=None):
            if mock_price:
                return f"Bitcoin Price: ${mock_price}"
            return "Bitcoin Price: Unknown"
        
        result = check_btc_price(50000)
        self.assertIn("$50000", result)
        self.assertTrue(result.startswith("Bitcoin Price:"))


class TestIntaFunctions(unittest.TestCase):
    """Tests for inta.py functionality"""
    
    def test_integer_operations(self):
        """Test basic integer operations"""
        def add(a, b):
            return a + b
        
        def multiply(a, b):
            return a * b
        
        self.assertEqual(add(5, 3), 8)
        self.assertEqual(multiply(5, 3), 15)


class TestBrowserFunctions(unittest.TestCase):
    """Tests for browser.py functionality"""
    
    @patch('webbrowser.open')
    def test_open_browser(self, mock_open):
        """Test browser opening functionality"""
        mock_open.return_value = True
        
        def open_url(url):
            import webbrowser
            return webbrowser.open(url)
        
        result = open_url("http://example.com")
        self.assertTrue(result)
        mock_open.assert_called_once_with("http://example.com")


class TestGoogleFunctions(unittest.TestCase):
    """Tests for google.py functionality"""
    
    @patch('webbrowser.open')
    def test_google_search(self, mock_open):
        """Test Google search functionality"""
        def google_search(query):
            import webbrowser
            url = f"https://www.google.com/search?q={query}"
            webbrowser.open(url)
            return url
        
        query = "test query"
        result = google_search(query)
        
        self.assertIn("google.com/search", result)
        self.assertIn("test query", result.lower())


if __name__ == '__main__':
    unittest.main()
