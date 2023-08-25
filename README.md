# Virtual Assistant Application

The Virtual Assistant application is a Python program built using the Tkinter library for creating a graphical user interface and various other libraries to provide different functionalities. The application acts as a voice-controlled virtual assistant that can perform tasks based on voice commands and button clicks.

## Functionalities

The Virtual Assistant offers the following functionalities:

1. **Greeting**: The assistant greets the user based on the time of day (morning, afternoon, evening).

2. **Date and Time**: Retrieves and displays the current date and time when the user clicks the "Date and Time" button.

3. **Open Website**: Opens a user-specified website in the default web browser.

4. **Open Documents**: Opens the default file explorer to a specified directory.

5. **Weather Forecast**: Displays the weather forecast for a user-specified city using information retrieved from a weather API.

6. **Wikipedia Search**: Allows the user to search for and read summaries of topics using the Wikipedia API.

7. **Voice Command**: Records and processes voice commands from the user, triggering the corresponding functionalities.

8. **Exit**: Closes the application when the user clicks the "Close" button or issues a "bye" command.

## Libraries Used

The application utilizes the following Python libraries:

- **tkinter**: For creating the graphical user interface.
- **time, datetime**: For handling time-related operations.
- **os, sys, subprocess**: For interacting with the operating system and file management.
- **webbrowser**: For opening websites in the default web browser.
- **speech_recognition**: For speech recognition to capture user voice commands.
- **requests**: For making HTTP requests to retrieve weather and Wikipedia information.
- **wikipedia**: For accessing Wikipedia content.
- **pyttsx3**: For text-to-speech functionality.

## Usage

1. Install the required libraries using `pip`:

   ```
   pip install tkinter speech_recognition requests wikipedia pyttsx3
   ```

2. Run the `main.py` file using a Python interpreter.

3. The application's graphical interface will open, displaying various buttons for different functionalities.

4. Clicking the buttons will execute the respective tasks. For the "Voice Command" button, the assistant will listen for your voice command and respond accordingly.

## Additional Information

- The application uses images (`assistant.png` and `record.png`) for buttons and aesthetics. Ensure these image files are in the same directory as the script.
- The assistant recognizes specific keywords in voice commands to trigger functionalities. Refer to the code comments for a list of recognized keywords.
- The weather information is retrieved from the [wttr.in](http://wttr.in) website using HTTP requests.
- The Wikipedia summaries are fetched using the `wikipedia` library.

