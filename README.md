# NumTextAlchemy

**NumTextAlchemy** is a Python library that allows for the conversion of extremely large numbers (up to \(10^{212}\)) into their text representation and back to integer format. Unlike most other libraries, **NumTextAlchemy** supports arbitrary-precision numbers, enabling it to handle conversions of both very large integers and their textual counterparts with ease.

## Features

- Convert integers up to \(10^{212}\) to their textual representation.
- Convert the textual representation back to integer format.
- No external libraries are required—it's a pure Python implementation.
- Efficient handling of arbitrary-precision integers.
- Works with numbers far beyond traditional integer limits.

## Installation
Using PIP:
```bash
pip install NumTextAlchemy
```


Clone the repository:

```bash
git clone https://github.com/Srinath-N-Gudi/NumTextAlchemy.git
```

## Usage
### Example 1: Converting Large Numbers to Text
```python
from NumTextAlchemy import num2text

number = "94891894789189789496964897"

number_text = num2text(number)

print(number_text) # The above number in text-format
```

### Example 2: Converting Large Text to Numbers

```python
from NumTextAlchemy import text2num

text = 'one hundred twenty-three octodecillion four hundred fifty-six septendecillion seven hundred eighty-nine sexdecillion twelve quindecillion three hundred forty-five quattuordecillion six hundred seventy-eight tredecillion nine hundred one duodecillion two hundred thirty-four undecillion five hundred sixty-seven decillion eight hundred ninety nonillion one hundred twenty-three octillion four hundred fifty-six septillion seven hundred eighty-nine sextillion twelve quintillion three hundred forty-five quadrillion six hundred seventy-eight trillion nine hundred one billion two hundred thirty-four million five hundred sixty-seven thousand eight hundred ninety'

number_text = text2num(number)

print(number_text) # 123456789012345678901234567890123456789012345678901234567890
```

## How It Works

### Number to Text Conversion
The library implements an algorithm that takes large numbers and breaks them down into manageable parts for conversion into readable English text. This allows you to convert numbers far beyond normal integer limits into a human-readable format, even numbers with hundreds of digits.

### Text to Number Conversion
**NumTextAlchemy** also supports converting textual representations of numbers back into their integer format. This is done using a custom parser to handle large-scale text-based number input, allowing for seamless back-and-forth conversions.

## Why NumTextAlchemy?

Most number-to-text conversion libraries are limited by the size of the numbers they can handle, often restricted to standard integer ranges. **NumTextAlchemy** breaks these barriers by supporting numbers as large as \(10^{212}\) and beyond, making it ideal for applications that require arbitrary-precision arithmetic.

## Use Cases

- **Scientific Computation**: Represent extremely large numbers in text for easier interpretation in papers or output.
- **Data Serialization**: Convert large integers into text for storage and easily parse them back into numbers.
- **Educational Tools**: Use the library for teaching or working with large numbers in a textual format.

## Contribution

Contributions are welcome! If you'd like to improve the library, feel free to open a pull request or submit an issue.

1. Fork the repository.
2. Create your feature branch:
3. Commit your changes:
4. Push to the branch:
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
