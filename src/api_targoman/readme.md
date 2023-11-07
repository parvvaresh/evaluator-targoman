# Targoman Translation API Client

This Python script is a client for the Targoman Translation API provided by `targoman.ir`. It allows you to translate text from one language to another using the Targoman translation service.

## Usage

1. Make sure you have the `requests` library installed. You can install it using `pip`:

   ```
   pip install requests
   ```

2. Define your Targoman API URL. The script uses the following URL by default: `https://targoman.ir/API`. You can modify the `URL` variable in the script to use a different URL if needed.

3. You can use the `translate` function to translate text. Here's an example of how to use it:

   ```python
   translation = translate("سلام", fromLang="fa", toLang="en")
   print(translation)
   ```

   - The `word` parameter is the text you want to translate.
   - The `fromLang` parameter is the source language code (e.g., "fa" for Farsi).
   - The `toLang` parameter is the target language code (e.g., "en" for English).
   
4. The `Translate` function is a simplified wrapper around the `translate` function. You can use it like this:

   ```python
   translation = Translate("سلام", fromLang="fa", toLang="en")
   print(translation)
   ```

   The `Translate` function handles the language direction and returns the translated text directly.

## API Request

The `translate` function sends a POST request to the Targoman API with a JSON payload. The response is parsed to extract the translation result.

## Sample Output

The response from the `translate` function is a JSON object that contains the translation result. The translated text can be accessed as follows:

```python
result = translate("سلام", fromLang="fa", toLang="en")
translation = result["result"]["tr"]["base"][0][1]
print(translation)
```

